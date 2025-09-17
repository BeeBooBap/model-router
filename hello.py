# hello.py

# basic classifier
def classify_query(text):
    if "legal" in text.lower() or "contract" in text.lower():
        return "This looks like a legal question."
    elif "code" in text.lower() or "python" in text.lower():
        return "This looks like a coding question."
    else:
        return "I'm not sure what type of question this is."

# test
question = input("Ask me a question: ")
result = classify_query(question)
print(result)