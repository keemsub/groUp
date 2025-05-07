document.getElementById("send-btn").addEventListener("click", sendMessage);

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value;
  if (!message) return;

  appendMessage("user", message);
  input.value = "";

  const res = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: message })
  });

  const data = await res.json();
  appendMessage("bot", data.answer);
}

function appendMessage(role, text) {
  const div = document.createElement("div");
  div.className = "message " + role;
  div.textContent = (role === "user" ? "👤 " : "🤖 ") + text;
  document.getElementById("chat-box").appendChild(div);
  document.getElementById("chat-box").scrollTop = 9999;
}

function handleFileUpload() {
  const fileInput = document.getElementById("file-upload");
  const file = fileInput.files[0];
  if (file) {
    appendMessage("user", `📎 ${file.name} 첨부됨`);
    // 실제 업로드는 서버와 연동 필요
  }
}
