"""
This python script accepts the user queries and sends them to the deepseek-r1-distill-llama-70b model 
hosted on GroqCloud, recieves and displays responses.

"""

import requests
import os
from dotenv import load_dotenv
import logging
# Loading the environment variables from .env
load_dotenv()

# Retrieving the API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Setting up basic logging to be able to track questions and responses
logging.basicConfig(
    filename="assistant.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class CustomerSupportAssistant:
    """
    A customer support assistant that interacts with the GroqCloud API
    to provide responses to user queries.
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "deepseek-r1-distill-llama-70b"

    def ask_question(self, user_input):
        """
        Sends a user query to the GroqCloud API and returns the assistant's response.

        Args:
            user_input (str): The question or message from the user.

        Returns:
            str: The assistant's response.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
    "model": self.model,
    "messages": [
        {
            "role": "system",
            "content": (
                "You are a professional, polite, and concise customer support assistant. "
                "NEVER show internal thoughts, step-by-step reasoning, or use tags like <think>."
                "Always answer customer questions clearly, starting directly with your response. "
                "Avoid thinking out loud, reasoning step-by-step, or using tags like <think>. "
                "Respond in a calm, helpful, and customer-service tone. Be empathetic and proactive in resolving issues."
            )
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
}


        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            assistant_reply = data["choices"][0]["message"]["content"]
            if "<think>" in assistant_reply:
              start = assistant_reply.find("<think>")
              end = assistant_reply.find("</think>")
              if end != -1:
               assistant_reply = assistant_reply[end + len("</think>"):].strip()


            # Log the interaction
            logging.info(f"User: {user_input}")
            logging.info(f"Assistant: {assistant_reply}")

            return assistant_reply

        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            return "Sorry, I couldn't reach the support system right now. Please try again later."
        

def main():
    """
    The main function that initializes the assistant and starts the user interaction loop.
    """
    assistant = CustomerSupportAssistant(api_key=GROQ_API_KEY)

    print("👋 Hello! I’m your Customer Support Assistant.")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_query = input("You: ").strip()

        if user_query.lower() in ["exit", "quit"]:
            print("Assistant: Thank you for chatting with us. Goodbye!")
            break

        if not user_query:
            print("Assistant: Please enter a valid message.")
            continue

        response = assistant.ask_question(user_query)
        print(f"Assistant: {response}\n")


if __name__ == "__main__":
    main()
