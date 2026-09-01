# Simple Rule-Based Chatbot (Python)

A beginner-level command-line chatbot that replies to the user from a fixed set
of rules. There is no machine learning involved — every reply is chosen by an
`if-elif-else` chain, which makes the whole decision process easy to read and
explain.

Built with Python's standard library only. No installation or dependencies.

## How to run

```bash
python chatbot.py
```

## Sample conversation

```
=============================================
            SIMPLE CHATBOT
=============================================
Hi, I am PyBot. Type something and I will reply.
Try: hello / how are you / your name / help / bye
---------------------------------------------
You: Hello!
PyBot: Hi!
You: How are you?
PyBot: I'm fine, thanks!
You: your name
PyBot: My name is PyBot. I am a rule-based chatbot.
You: blah blah
PyBot: Sorry, I did not understand that. Type 'help' to see examples.
You: bye
PyBot: Goodbye!
---------------------------------------------
Chat ended. You sent 5 message(s).
```

## Rules the bot knows

| User types | Bot replies |
|---|---|
| hi, hello, hey, hii | Hi! |
| good morning / afternoon / evening | Good day to you too! |
| how are you | I'm fine, thanks! |
| your name, who are you | My name is PyBot... |
| help, what can you do | list of supported messages |
| thanks, thank you | You're welcome! |
| what is python | short definition |
| bye, goodbye, exit, quit | Goodbye! (and the loop ends) |
| anything else | fallback "I did not understand" reply |

## Key concepts used

- **Functions** — the program is split into small functions with one job each:
  `show_welcome()`, `clean_input()`, `is_exit_word()`, `get_reply()`, `chat()`.
- **if-elif-else** — `get_reply()` checks the rules from top to bottom and the
  first match wins; the `else` block handles unknown input.
- **Loop** — a `while True` loop keeps the conversation going and `break` ends
  it when the user says goodbye.
- **Input / output** — `input()` reads each message, `print()` shows the reply.

## Design notes

- **Input cleaning:** `clean_input()` lowercases the text and strips `! . , ?`
  so that `"Hello!!"`, `"hello"` and `"HELLO"` all match the same rule.
- **Empty input** is handled separately instead of falling into the fallback,
  so the bot says something sensible if the user just presses Enter.
- **`Ctrl+C` / end of input** is caught in `main()` so the program says
  "Goodbye!" instead of printing a traceback.
- **Exit words live in one function** (`is_exit_word`) because they are needed
  in two places — the reply logic and the loop's stop condition.

## Limitations (honest)

The bot matches whole messages, not keywords, so `"hello there friend"` falls
through to the fallback reply. It has no memory of earlier messages and no
understanding of meaning — it is pattern matching, not AI.

## Possible next steps

1. Match on **keywords inside** the sentence instead of the whole sentence.
2. Move the rules into a **dictionary** so replies can be added without
   touching the if-elif chain.
3. Pick randomly from several replies per rule using the `random` module, so
   the bot feels less repetitive.
4. Load the rules from a **JSON or CSV file** so non-programmers can edit them.
5. Only after that: try an actual intent classifier (e.g. scikit-learn) to see
   the real difference between rule-based and learned responses.
