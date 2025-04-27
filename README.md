# Customer Support Assistant 

This is a Python-based intelligent **Customer Support Assistant** powered by the `deepseek-r1-distill-llama-70b` model via the [GroqCloud API](https://console.groq.com).

##  Setup Instructions 📦

1. **Clone the repository**
 ```bash
 git clone https://github.com/DataEpicOrg/your-repo-name.git
 cd your-repo-name
   ```

2. **Create and Activate Virtual Environment**
```   
 python -m venv venv
```
```
 .\venv\Scripts\activate  # For Windows
```
```
 source venv/bin/activate #For Mac/Linux
```

4. **Install Dependencies**
```
pip install -r requirements.txt
```

6. ***Create a .env file***
In the project root directory, add your Groq API key in a file named .env:
GROQ_API_KEY=your_groq_api_key_here

## How to run Customer Assistant ##

Run the following command in your terminal:
```
python assistant.py
```
Then start chatting by typing your queries. Type exit, quit, or bye to end the session.

## Example Usage ##
You: I want to return a faulty product.
Assistant: I'm sorry to hear that! Please provide your order ID so I can assist you with the return process.

You: What are your store hours?
Assistant: Our store is open Monday to Saturday, from 9 AM to 6 PM. Let me know if you need help with anything else.

## Current Limitations: ##

- The assistant does not remember previous interactions.

- Interaction with assistant is purely command-line based.

-  Basic logging and error handling only.

## Ideas for Future Enhancements: ##

- Add context-awareness and session memory.

- Build a web-based or mobile-friendly interface.

-  Connect to a real database or ticketing system (e.g., for tracking complaints).

- Add unit tests for better code coverage and stability.

## Acknowledgement: ##

This project was developed as part of the Data Epic Mentorship Program (2025 Cohort).
