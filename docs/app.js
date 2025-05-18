document.getElementById("submitButton").addEventListener("click", async () => {
  const questionInput = document.getElementById("questionInput");
  const responseBox = document.getElementById("responseBox");
  const historyContainer = document.getElementById("historyContainer");

  const question = questionInput.value.trim();
  if (!question) return;

  // Display the question in the history
  const questionElement = document.createElement("div");
  questionElement.className = "history-item question";
  questionElement.textContent = `Q: ${question}`;
  historyContainer.prepend(questionElement);

  // Send the question to the API
  try {
    const response = await fetch("http://127.0.0.1:8000/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question }),
    });

    if (response.ok) {
      const data = await response.json();
      console.log(data);

      // Clear previous response
      responseBox.innerHTML = "";

      // Process and display the answer
      const answerElement = document.createElement("div");
      answerElement.className = "history-item answer";
      answerElement.innerHTML = formatResponse(data.answer);
      historyContainer.prepend(answerElement);

      // Also display it in the main response box
      responseBox.innerHTML = answerElement.innerHTML;
    } else {
      responseBox.innerHTML = `<p style="color: red;">Failed to get a response from the server.</p>`;
    }
  } catch (error) {
    console.error(error);
    responseBox.innerHTML = `<p style="color: red;">An error occurred while connecting to the server.</p>`;
  }
  
  questionInput.value = "";
});

/**
 * Formats the raw response from the AI assistant.
 */
function formatResponse(rawResponse) {
  if (!rawResponse) return "<p>No data received.</p>";

  // Remove Markdown-style list items and format neatly
  const formattedResponse = rawResponse
    .replace(/### Local results from pro-analytics-01:/g, "<h3>Local results from pro-analytics-01:</h3>")
    .replace(/- \[ \]/g, "<li>")
    .replace(/\n/g, "")
    .replace(/\*\*/g, "")
    .replace(/<\/li>\s*<li>/g, "</li><li>");

  // Create unordered list where needed
  return `<ul>${formattedResponse}</ul>`;
}
