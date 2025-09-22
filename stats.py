
# stats.py
def show_original_performance():
    """Show statistics about initial classificaiton patterns"""

    try:
        with open("query_log.txt", "r") as file:
            lines = file.readlines()
            
        if not lines:
            print("No queries to analyze yet!")
            return
            
        total_queries = len(lines)
        
        # Count corrections made
        correction_count = 0
        try:
            with open("corrections.txt", "r") as corrections_file:
                corrections = corrections_file.read()
                correction_count = corrections.count("CORRECTION:")
        except FileNotFoundError:
            correction_count = 0
        
        print(f"\n--- Original Classifier Performance ---")
        print(f"Total queries: {total_queries}")
        print(f"Questions classified correctly: {total_queries - correction_count}")
        print(f"Questions that needed correction: {correction_count}")
        
        if total_queries > 0:
            accuracy = ((total_queries - correction_count) / total_queries) * 100
            print(f"Initial accuracy: {accuracy:.1f}%")
            
        if correction_count > 0:
            print("\nYour classifier needs improvement on these types of questions!")
        else:
            print("\nNo corrections needed yet - classifier is doing well!")
            
    except FileNotFoundError:
        print("No query log found. Ask some questions first!")

def show_corrected_distribution():
    """Show the true distribution of question types after corrections"""
    try:
        with open("query_log.txt", "r") as file:
            lines = file.readlines()
            
        if not lines:
            print("No queries to analyze yet!")
            return
        
        # Start with original counts
        legal_count = 0
        coding_count = 0  
        general_count = 0
        
        # Count original classifications
        for line in lines:
            if "LEGAL question" in line:
                legal_count += 1
            elif "CODING question" in line:
                coding_count += 1
            else:
                general_count += 1
        
        print(f"\n--- True Data Distribution (After Corrections) ---")

        # Track net changes
        try:
            with open("corrections.txt", "r") as corrections_file:
                content = corrections_file.read()

                # Parse corrections to find what was changed
                corrections = content.split("---")

                legal_net_change = 0
                coding_net_change = 0
                general_net_change = 0
                
                for correction in corrections:
                    if "CORRECTION:" in correction and "should be" in correction:
                        lines_in_correction = correction.strip().split("\n")
                        for line in lines_in_correction:
                            if line.startswith("CORRECTION:"):
                                # Example: "CORRECTION: 'some question' should be LEGAL"
                                if "should be LEGAL" in line:
                                    legal_net_change += 1
                                    # This question was moved TO legal, so it came FROM somewhere else
                                    # We need to subtract 1 from wherever it came from
                                    general_net_change -= 1  # Most corrections come from general
                                    
                                elif "should be CODING" in line:
                                    coding_net_change += 1
                                    general_net_change -= 1  # Assume it came from general
                                    
                                elif "should be GENERAL" in line:
                                    general_net_change += 1
                                    # This is rare, but could come from legal or coding
                
                # Calculate final counts
                final_legal = legal_count + legal_net_change
                final_coding = coding_count + coding_net_change  
                final_general = general_count + general_net_change

                print(f"Legal questions: ~{legal_count} (+ {legal_net_change} corrections)")
                print(f"Coding questions: ~{coding_count} (+ {coding_net_change} corrections)")  
                print(f"General questions: ~{general_count} (+ {general_net_change} corrections)")
        
        except FileNotFoundError:
            print(f"\n--- Current Data Distribution ---")
            total = legal_count + coding_count + general_count
            print(f"Legal questions: {legal_count} ({legal_count/total*100:.1f}%)")
            print(f"Coding questions: {coding_count} ({coding_count/total*100:.1f}%)")
            print(f"General questions: {general_count} ({general_count/total*100:.1f}%)")
            
    except FileNotFoundError:
        print("No query log found.")

def analyse_performance():
    """Show both performance metrics"""
    show_original_performance()
    show_corrected_distribution()

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