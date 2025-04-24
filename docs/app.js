document.getElementById("submitButton").addEventListener("click", async () => {
  try {
    const questionInput = document.getElementById("questionInput");
    const responseBox = document.getElementById("responseBox");
    const question = questionInput.value.trim();

    if (!question) {
      responseBox.innerText = "Please enter a question.";
      return;
    }

    responseBox.innerText = "Thinking...";
    console.log("Sending question:", question);

    const BACKEND_URL = "http://127.0.0.1:8000/query";
    console.log("About to fetch from:", BACKEND_URL);

    const res = await fetch(BACKEND_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ question })
    });

    console.log("Fetch status:", res.status);

    if (!res.ok) throw new Error(`Network response was not ok (status ${res.status})`);

    const data = await res.json();
    console.log("Received data:", data);

    if (data.answer) {
      responseBox.innerText = data.answer;
      console.log("Displayed answer.");
    } else {
      responseBox.innerText = "No answer returned.";
      console.warn("Empty response content.");
    }
  } catch (err) {
    console.error("Top-level error:", err);
    const responseBox = document.getElementById("responseBox");
    responseBox.innerText = "Error: " + err.message;
    alert("An error occurred: " + err.message);
  }
});
