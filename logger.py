# logger.py

import datetime

def log_query(question, classification, legal_count, coding_count):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # generate log entry format
    log_entry = f"{timestamp} | Q: {question} | Result: {classification} | Legal: {legal_count} | Coding: {coding_count}\n"

    # append to log file
    with open("query_log.txt", "a") as file:
        file.write(log_entry)

    print(f"Logged to query.txt")