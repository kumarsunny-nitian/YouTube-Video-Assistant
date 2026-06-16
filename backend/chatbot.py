import re

from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import (
    HuggingFaceEmbeddings,
    HuggingFaceEndpoint,
    ChatHuggingFace
)

from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda
)
from langchain_core.output_parsers import StrOutputParser


# -------------------------------
# Load embedding model once
# -------------------------------

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -------------------------------
# Load LLM once
# -------------------------------

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
    
)

model = ChatHuggingFace(llm=llm)

# -------------------------------
# Prompt
# -------------------------------

prompt = PromptTemplate(
    template="""
You are a helpful assistant.

Answer only from the provided transcript.

If the transcript does not contain the answer,
say "I couldn't find that information in the video."

Transcript:
{context}

Question:
{question}
""",
    input_variables=["context", "question"]
)


# -------------------------------
# Extract video id
# -------------------------------

def extract_video_id(video_url):

    patterns = [
        r"v=([^&]+)",
        r"youtu\.be/([^?]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, video_url)

        if match:
            return match.group(1)

    raise ValueError("Invalid YouTube URL")


# -------------------------------
# Format docs
# -------------------------------

def format_docs(retrieved_docs):

    return "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )


# -------------------------------
# Main function
# -------------------------------

def ask_question(video_url, question):

    try:

        # Extract ID
        video_id = extract_video_id(video_url)

        # Get transcript
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.fetch(video_id, languages=["en"])


        
        transcript = " ".join(
                        chunk.text
                        for chunk in transcript_list
                    )
        

        # Split transcript
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )

        chunks = splitter.create_documents(
            [transcript]
        )

        # Create FAISS vector store
        vector_store = FAISS.from_documents(
            chunks,
            embedding
        )

        retriever = vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 4}
        )

        # RAG chain
        parallel_chain = RunnableParallel(
            {
                "context":
                    retriever
                    | RunnableLambda(format_docs),

                "question":
                    RunnablePassthrough()
            }
        )

        parser = StrOutputParser()

        chain = (
            parallel_chain
            | prompt
            | model
            | parser
        )

        answer = chain.invoke(question)

        return answer

    except Exception as e:

        return f"Error: {str(e)}"