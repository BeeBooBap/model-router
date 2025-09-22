
# menu.py
from keywords import LEGAL_KEYWORDS, CODING_KEYWORDS
from logger import log_query

def classify_query(text):
    text_lower = text.lower()

    # assess input against keywords by summing identified keywords
    legal_matches = sum(1 for word in LEGAL_KEYWORDS if word in text_lower)
    coding_matches = sum(1 for word in CODING_KEYWORDS if word in text_lower)

    if legal_matches > coding_matches:
        result = "LEGAL question"
    elif coding_matches > legal_matches:
        result = "CODING question"
    else:
        result = "GENERAL/MIXED question"

    log_query(text, result, legal_matches, coding_matches)

    return result, legal_matches, coding_matches

def view_log():
    try:
        with open("query_log.txt", "r") as file:
            lines = file.readlines()
            if lines:
                print("\n--- Recent Queries ---")
                # Show last 10 entries
                for line in lines[-10:]:
                    print(line.strip())
            else:
                print("No queries logged yet!")
    except FileNotFoundError:
        print("No log file found. Ask some questions first!")

def main_menu():
    while True:
        print("\n=== Query Classifier ===")
        print("1. Ask a question")
        print ("2. View recent queries")
        print ("3. Report wrong classification")
        print("4. View corrections")
        print("5. Quit")

        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            question = input("\nAsk me a question: ")
            result, legal_count, coding_count = classify_query(question)
            print(f"\nResult: {result}")
            print(f"Legal matches: {legal_count}, Coding matches: {coding_count}")
        
        elif choice == "2":
            view_log()

        elif choice == "3":
            from improver import manual_correction
            manual_correction()
        
        elif choice == "4":
            from improver import view_corrections
            view_corrections()
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Please enter 1-5")

if __name__ == "__main__":
    main_menu()