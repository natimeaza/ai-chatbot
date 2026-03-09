// API service for chatbot interactions

const API_BASE_URL = 'http://localhost:3000'; // Replace with your backend URL

export const sendMessage = async (message) => {
  try {
    const response = await fetch(`${API_BASE_URL}/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error sending message:', error);
    return { error: 'Failed to send message' };
  }
};