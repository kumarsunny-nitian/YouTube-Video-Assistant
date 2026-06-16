const sidebar = document.createElement("div");

sidebar.id = "yt-ai-sidebar";

sidebar.innerHTML = `
    <h2>Video Chat</h2>

    <textarea
        id="yt-question"
        rows="4"
        placeholder="Ask about this video..."
    ></textarea>

    <button id="yt-ask-btn">
        Ask
    </button>

    <div id="yt-answer"></div>
`;

document.body.appendChild(sidebar);

document
.getElementById("yt-ask-btn")
.addEventListener("click", async () => {

    const question =
        document.getElementById(
            "yt-question"
        ).value;

    const answerDiv =
        document.getElementById(
            "yt-answer"
        );

    answerDiv.innerHTML =
        "Thinking...";

    try {

        const response =
            await fetch(
                "http://127.0.0.1:8000/ask",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                        "application/json"
                    },

                    body: JSON.stringify({
                        video_url:
                            window.location.href,

                        question
                    })
                }
            );

        const data =
            await response.json();

        answerDiv.innerHTML =
            data.answer;

    } catch(error) {

        answerDiv.innerHTML =
            error.message;
    }
});