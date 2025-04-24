document.getElementById("submitButton").addEventListener("click", async () => {
    const question = document.getElementById("questionInput").value;
    if (!question.trim()) return;
  
    const responseBox = document.getElementById("responseBox");
    responseBox.innerText = "Thinking...";

    const BACKEND_URL = "http://127.0.0.1:8000/query";

  
    try {
      const res = await fetch(BACKEND_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ question })
      });
  
      if (!res.ok) throw new Error("Network response was not ok");
      const data = await res.json();
      responseBox.innerText = data.answer;
      console.log("Answer:", data.answer);
    } catch (err) {
      responseBox.innerText = "Error: " + err.message;
      console.error("Error:", err);
    }
  });
  