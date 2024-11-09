import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="\"You are a seasoned psychologist with a warm, approachable style. You speak to users in a relaxed and humorous way, using light jokes or playful metaphors when appropriate to help them feel at ease. Your goal is to provide insightful advice on psychology topics, covering emotions, behavior, and mental health. Be supportive, engaging, and use friendly language—aim to make users feel comfortable and understood. Adjust your humor to be gentle, never making light of serious issues but adding warmth and personality to your responses.\"",
)

history = []

def chat(user_input):
    chat_session = model.start_chat(history=history)
    response = chat_session.send_message(user_input)
    model_response = response.text
    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})
    return model_response



# import os
# import google.generativeai as genai
# from dotenv import load_dotenv
# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # Create the model
# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 40,
#   "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
# }

# model = genai.GenerativeModel(
#   model_name="gemini-1.5-pro",
#   generation_config=generation_config,
#   system_instruction="\"You are a seasoned psychologist with a warm, approachable style. You speak to users in a relaxed and humorous way, using light jokes or playful metaphors when appropriate to help them feel at ease. Your goal is to provide insightful advice on psychology topics, covering emotions, behavior, and mental health. Be supportive, engaging, and use friendly language—aim to make users feel comfortable and understood. Adjust your humor to be gentle, never making light of serious issues but adding warmth and personality to your responses.\"",
# )

# history = []

# print("Friendly Psychologist: Hi! How can I help you today?")

# while True:
#     user_input = input("You: ")

#     chat_session = model.start_chat(
#     history= history,
#     )

#     response = chat_session.send_message(user_input)

#     model_response = response.text
#     print(f'Friendly Psychologist: {model_response}')
#     print()

#     history.append({"role": "user", "parts": [user_input]})
#     history.append({"role": "model", "parts": [model_response]})