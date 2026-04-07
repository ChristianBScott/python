"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
Christian Scott
"""

import datetime


bug_info_dict = {}
while True:
    entry = input("Enter log to report a bug (or 'quit' to stop): ")
    if entry.lower() == "quit":
        break
    elif entry == "log":
        bug_info_str = input(
            f"Enter file name, description, and priority separated by commas.\n"
        )
        bug_info_dict = [item.strip() for item in bug_info_str.split(",")]
        current_time = datetime.datetime.now()
        timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open("bug_log.txt", "a") as file:
            file.write(f"--- {timestamp_str} ---\n")
            for bugs in bug_info_dict:
                file.write(f" - {bugs}\n")

            file.write("\n")

    else:
        print("Invalid input. Please try again.\n")
