
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def library_chatbot(message):
    message = message.lower().strip()

    if message in ["hi", "hello", "hey"]:
        return "Hello! Welcome to the Library Enquiry Chatbot. How can I help you?"

    elif "timing" in message or "opening hours" in message:
        return "The library is open from 9:00 AM to 5:00 PM on working days."

    elif "book" in message and ("available" in message or "availability" in message):
        return "Please provide the book title or ask the librarian to check availability."

    elif "issue" in message or "borrow" in message:
        return "You can borrow books using your valid library membership card."

    elif "return" in message:
        return "Please return borrowed books to the library counter before the due date."

    elif "fine" in message or "late" in message:
        return "A late return may incur a fine. Please check the library's current fine rules."

    elif "membership" in message or "member" in message:
        return "Visit the library counter with your student ID to ask about membership."

    elif "location" in message or "where is" in message:
        return "The library is located on the college campus. Please check with the office for directions."

    elif "computer" in message or "internet" in message:
        return "Please ask the librarian about computer and internet facilities."

    elif "thank" in message:
        return "You're welcome! Happy reading!"

    elif "bye" in message or "goodbye" in message:
        return "Thank you for visiting the Library Chatbot. Goodbye!"

    else:
        return "Sorry, I didn't understand. You can ask about timings, books, issuing, returns, fines, or membership."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    reply = library_chatbot(message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
