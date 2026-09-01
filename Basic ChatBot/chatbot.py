"""
Simple Rule-Based Chatbot
-------------------------
A beginner-level chatbot that replies to the user using a fixed set of rules.
There is no machine learning here: every reply is decided by an if-elif chain.

Concepts used: functions, if-elif-else, while loop, input / output (print).
Only Python's standard library is used.

Author: Bhavesh Tayade
"""

BOT_NAME = "PyBot"


def show_welcome():
    """Print the banner and a short help note when the chatbot starts."""
    print("=" * 45)
    print(" " * 12 + "SIMPLE CHATBOT")
    print("=" * 45)
    print("Hi, I am " + BOT_NAME + ". Type something and I will reply.")
    print("Try: hello / how are you / your name / help / bye")
    print("-" * 45)


def clean_input(text):
    """
    Make the user's text easy to compare.

    Steps: remove extra spaces, convert to lowercase, and drop simple
    punctuation so that "Hello!!" and "hello" are treated as the same input.
    """
    text = text.strip().lower()
    for mark in ["!", ".", ",", "?"]:
        text = text.replace(mark, "")
    return text


def is_exit_word(text):
    """Return True if the cleaned text is one of the goodbye words."""
    return text in ["bye", "goodbye", "exit", "quit", "see you"]


def get_reply(user_text):
    """
    Decide the bot's reply for one user message.

    This is the heart of the program. The rules are checked from top to
    bottom with if-elif, and the first matching rule wins. If nothing
    matches, the else block gives a default reply.
    """
    text = clean_input(user_text)

    if text == "":
        reply = "You did not type anything. Please say something."

    elif text in ["hi", "hello", "hey", "hii", "hello there"]:
        reply = "Hi!"

    elif text in ["good morning", "good afternoon", "good evening"]:
        reply = "Good day to you too!"

    elif text in ["how are you", "how r u", "how are you doing"]:
        reply = "I'm fine, thanks!"

    elif text in ["what is your name", "your name", "who are you"]:
        reply = "My name is " + BOT_NAME + ". I am a rule-based chatbot."

    elif text in ["what can you do", "help"]:
        reply = "I reply to fixed messages like hello, how are you, and bye."

    elif text in ["thanks", "thank you", "thanks a lot"]:
        reply = "You're welcome!"

    elif text in ["what is python", "python"]:
        reply = "Python is a simple, high-level programming language."

    elif is_exit_word(text):
        reply = "Goodbye!"

    else:
        reply = "Sorry, I did not understand that. Type 'help' to see examples."

    return reply


def chat():
    """
    Run the conversation loop.

    The loop keeps asking for input until the user types a goodbye word.
    Each round: read input -> get reply -> print reply.
    """
    show_welcome()
    message_count = 0

    while True:
        # input() waits for the user to type a line and press Enter.
        user_text = input("You: ")
        message_count = message_count + 1

        reply = get_reply(user_text)
        print(BOT_NAME + ": " + reply)

        # break stops the while loop, which ends the chat.
        if is_exit_word(clean_input(user_text)):
            break

    print("-" * 45)
    print("Chat ended. You sent " + str(message_count) + " message(s).")


def main():
    """Start the chatbot and handle Ctrl+C so the program exits cleanly."""
    try:
        chat()
    except (KeyboardInterrupt, EOFError):
        print()
        print(BOT_NAME + ": Goodbye!")


# This runs main() only when the file is executed directly.
if __name__ == "__main__":
    main()
