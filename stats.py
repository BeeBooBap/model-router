
# stats.py
def analyse_performance():
    """Show statistics about classificaiton patterns"""

    try:
        with open("query_log.txt", "r") as file:
            lines = file.readlines()

        if not lines:
                print("No queries to analyse yet!")
                return
        
        legal_count = 0
        coding_count = 0
        general_count = 0
        total_queries = len(lines)

        for line in lines:
            if "LEGAL question" in line:
                legal_count += 1
            elif "CODING question" in line:
                coding_count += 1
            else:
                general_count += 1
        
        print(f"\n--- Classification Statistics ---")
        print(f"Total queries analysed: {total_queries}")
        print(f"Legal questions: {legal_count} ({legal_count/total_queries*100:.1f}%)")
        print(f"Coding questions: {coding_count} ({coding_count/total_queries*100:.1f}%)")
        print(f"General/Mixed: {general_count} ({general_count/total_queries*100:.1f}%)")

        # Check for corrections
        try:
            with open("corrections.txt", "r") as corrections_file:
                corrections = corrections_file.read()
                correction_count = corrections.count("CORRECTION:")
                print(f"Manual corrections made: {correction_count}")
                if correction_count > 0:
                    accuracy = ((total_queries - correction_count) / total_queries) * 100
                    print(f"Estimated accuracy: {accuracy:.1f}%")
        except FileNotFoundError:
            print("No corrections file found - accuracy unknown")
    
    except FileNotFoundError:
        print("No query log found. Ask me some questions first!")

def show_keyword_coverage():
    """Show which keywords are actually being used"""

    from keywords import LEGAL_KEYWORDS, CODING_KEYWORDS

    try:
        with open("query_log.txt", "r") as file:
            all_text = file.read().lower()
            
        print(f"\n--- Keyword Usage ---")
        
        used_legal = []
        unused_legal = []
        for word in LEGAL_KEYWORDS:
            if word in all_text:
                used_legal.append(word)
            else:
                unused_legal.append(word)
        
        used_coding = []
        unused_coding = []
        for word in CODING_KEYWORDS:
            if word in all_text:
                used_coding.append(word)
            else:
                unused_coding.append(word)
        
        print(f"Legal keywords being used: {len(used_legal)}/{len(LEGAL_KEYWORDS)}")
        print(f"Coding keywords being used: {len(used_coding)}/{len(CODING_KEYWORDS)}")

        if unused_legal:
            print(f"Unused legal keywords: {', '.join(unused_legal[:5])}...")
        if unused_coding:
            print(f"Unused coding keywords: {', '.join(unused_coding[:5])}...")
        
    except FileNotFoundError:
        print("No query log found.")