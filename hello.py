# hello.py
from keywords import LEGAL_KEYWORDS, CODING_KEYWORDS
from logger import log_query

# basic classifier
def classify_query(text):

    # convert input text to lowercase for parsing
    text_lower = text.lower()

    # assess input against keywords by summing identified keywords
    legal_matches = sum(1 for word in LEGAL_KEYWORDS if word in text_lower)
    coding_matches = sum(1 for word in CODING_KEYWORDS if word in text_lower)

    print(f"Legal matches: {legal_matches}")
    print(f"Coding matches: {coding_matches}")

    # generate result based on keyword match
    if legal_matches > coding_matches:
        result = "This looks like a legal question."
    elif coding_matches > legal_matches:
        result = "This looks like a coding question."
    else:
        result = "I'm not sure what type of question this is."
    
    # log this query
    log_query(text, result, legal_matches, coding_matches)

    return result

# test
question = input("Ask me a question: ")
result = classify_query(question)
print(result)