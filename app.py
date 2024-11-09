from flask import Flask, render_template, request
from chat import chat  # Import the chatbot function

app = Flask(__name__)

# Store chat history in memory
chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = chat(user_input)
        chat_history.append({"role": "user", "message": user_input})
        chat_history.append({"role": "bot", "message": bot_response})
    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, render_template, request
# from chat import chat  # Import the chatbot function

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def home():
#     response = ""
#     if request.method == "POST":
#         user_input = request.form["user_input"]
#         response = chat(user_input)
#     return render_template("index.html", response=response)

# if __name__ == "__main__":
#     app.run(debug=True)
