import { useState } from "react";
import axios from "axios";

function ChatPage() {

 const [message, setMessage] = useState("");
 const [messages, setMessages] = useState([]);

 const sendMessage = async () => {

  const res = await axios.post("http://localhost:8000/chat", {
    message: message
  });

  setMessages([
   ...messages,
   { user: message, bot: res.data.response }
  ]);

  setMessage("");
 };

 return (
  <div>

   <h2>AI Chatbot</h2>

   {messages.map((m, i) => (
    <div key={i}>
      <p><b>You:</b> {m.user}</p>
      <p><b>Bot:</b> {m.bot}</p>
    </div>
   ))}

   <input
    value={message}
    onChange={(e)=>setMessage(e.target.value)}
   />

   <button onClick={sendMessage}>Send</button>

  </div>
 );
}

export default ChatPage;