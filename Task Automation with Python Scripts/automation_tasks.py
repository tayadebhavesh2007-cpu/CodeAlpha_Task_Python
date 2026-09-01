"""
automation_tasks.py
-------------------
A small menu-driven program that automates three repetitive, real-life jobs:

    1. Move all .jpg files from a folder into a new folder      (os, shutil)
    2. Extract all email addresses from a .txt file             (re)
    3. Scrape the <title> of a fixed webpage and save it        (requests, re)

Key concepts used: os, shutil, re, requests, file handling.

Author : Bhavesh Tayade
Run it : python automation_tasks.py
"""

import os
import re
import shutil
from datetime import datetime

# requests is not part of the standard library, so it may not be installed.
# We import it here but only actually need it for Task 3, so the other two
# tasks keep working even if the package is missing.
try:
    import requests
except ImportError:
    requests = None

# Extensions treated as JPEG images (compared in lower case).
JPG_EXTENSIONS = (".jpg", ".jpeg")

# Regular expression for a normal email address:
#   one or more allowed characters, then @, then a domain, then a .tld
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

# Regular expression for the text inside the <title> ... </title> tag.
TITLE_PATTERN = r"<title[^>]*>(.*?)</title>"

# The "fixed webpage" used by Task 3 when the user just presses Enter.
DEFAULT_URL = "https://www.python.org"

def ask_for_folder(message):
    """Keep asking until the user types the path of a folder that exists."""
    while True:
        path = input(message).strip().strip('"')
        if path == "":
            print("   Please type a folder path.\n")
        elif not os.path.exists(path):
            print("   That path does not exist. Try again.\n")
        elif not os.path.isdir(path):
            print("   That is a file, not a folder. Try again.\n")
        else:
            return path


def ask_for_file(message, must_end_with=None):
    """Keep asking until the user types the path of a file that exists."""
    while True:
        path = input(message).strip().strip('"')
        if path == "":
            print("   Please type a file path.\n")
        elif not os.path.isfile(path):
            print("   No such file. Check the name and try again.\n")
        elif must_end_with and not path.lower().endswith(must_end_with):
            print("   The file must end with " + must_end_with + ". Try again.\n")
        else:
            return path


def make_unique_path(folder, filename):
    """
    Build a file path inside 'folder' that does not overwrite anything.

    If photo.jpg already exists there, this returns photo_1.jpg,
    then photo_2.jpg, and so on. This is why nothing gets lost.
    """
    target = os.path.join(folder, filename)
    if not os.path.exists(target):
        return target

    name, extension = os.path.splitext(filename)
    counter = 1
    while os.path.exists(target):
        target = os.path.join(folder, name + "_" + str(counter) + extension)
        counter += 1
    return target


def move_jpg_files():
    """
    TASK 1 -- os + shutil
    Look at every item in a folder and move the .jpg / .jpeg files
    into a separate folder, so photos stop sitting mixed with documents.
    """
    print("\n--- Task 1: Move .jpg files into a new folder ---")

    source = ask_for_folder("Folder to clean up : ")

    # Pressing Enter accepts the suggested destination.
    suggested = os.path.join(source, "jpg_files")
    typed = input("New folder for images [" + suggested + "] : ").strip().strip('"')
    destination = typed if typed else suggested

    # exist_ok=True means "do not crash if the folder is already there".
    os.makedirs(destination, exist_ok=True)

    moved = 0
    skipped = 0

    for filename in sorted(os.listdir(source)):
        full_path = os.path.join(source, filename)

        # Folders are ignored -- we only move files.
        if not os.path.isfile(full_path):
            continue

        if not filename.lower().endswith(JPG_EXTENSIONS):
            skipped += 1
            continue

        new_path = make_unique_path(destination, filename)
        shutil.move(full_path, new_path)
        moved += 1
        print("   moved   : " + filename + " -> " + os.path.basename(new_path))

    print("\nDone. Moved " + str(moved) + " image file(s).")
    print("Left alone : " + str(skipped) + " non-image file(s).")
    if moved:
        print("Images are now in : " + destination)


def extract_emails():
    """
    TASK 2 -- re
    Read a .txt file, find every email address inside it with a regular
    expression, remove duplicates, and save the clean list to a new file.
    """
    print("\n--- Task 2: Extract email addresses from a .txt file ---")

    source = ask_for_file("Text file to read : ", must_end_with=".txt")

    # errors="ignore" stops the program from crashing on odd characters.
    with open(source, "r", encoding="utf-8", errors="ignore") as text_file:
        content = text_file.read()

    found = re.findall(EMAIL_PATTERN, content)

    # Remove duplicates but keep the original order.
    # Emails are compared in lower case so Abc@x.com == abc@x.com.
    unique_emails = []
    seen = set()
    for email in found:
        cleaned = email.lower()
        if cleaned not in seen:
            seen.add(cleaned)
            unique_emails.append(cleaned)

    if not unique_emails:
        print("\nNo email addresses found in that file. Nothing was saved.")
        return

    # Save next to the input file, e.g. contacts.txt -> contacts_emails.txt
    name_without_extension = os.path.splitext(source)[0]
    output_path = name_without_extension + "_emails.txt"

    with open(output_path, "w", encoding="utf-8") as output_file:
        for email in unique_emails:
            output_file.write(email + "\n")

    print("\nTotal matches found : " + str(len(found)))
    print("Unique addresses    : " + str(len(unique_emails)))
    print("Duplicates removed  : " + str(len(found) - len(unique_emails)))
    print("Saved to            : " + output_path)


def scrape_page_title():
    """
    TASK 3 -- requests + re
    Download one fixed webpage and pull out the text inside its <title> tag,
    then append that title to a log file with the date and time.
    """
    print("\n--- Task 3: Scrape a webpage title and save it ---")

    if requests is None:
        print("The 'requests' package is not installed, so this task cannot run.")
        print("Install it once with :  pip install requests")
        return

    typed = input("Website address [" + DEFAULT_URL + "] : ").strip()
    url = typed if typed else DEFAULT_URL

    # Some sites reject requests that do not look like a browser.
    headers = {"User-Agent": "Mozilla/5.0 (simple python learning script)"}

    print("Fetching " + url + " ...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()          # turns 404 / 500 into an error
    except requests.exceptions.RequestException as error:
        print("Could not download the page: " + str(error))
        return

    # re.DOTALL lets '.' match newlines, in case the title spans two lines.
    match = re.search(TITLE_PATTERN, response.text, re.IGNORECASE | re.DOTALL)
    if match is None:
        print("The page loaded but it has no <title> tag.")
        return

    title = match.group(1)
    title = re.sub(r"\s+", " ", title).strip()      # squeeze extra whitespace
    for code, character in [("&amp;", "&"), ("&#39;", "'"), ("&quot;", '"')]:
        title = title.replace(code, character)

    # The log lives beside this script, not wherever the terminal happens to be.
    script_folder = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(script_folder, "titles_log.txt")
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # "a" = append, so every run adds a line instead of erasing the old ones.
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(stamp + " | " + title + " | " + url + "\n")

    print("\nPage title : " + title)
    print("Saved to   : " + log_path)


def show_menu():
    """Print the list of available tasks."""
    print("\n===== Small Task Automator =====")
    print("1. Move all .jpg files into a new folder")
    print("2. Extract email addresses from a .txt file")
    print("3. Scrape a webpage title and save it")
    print("0. Exit")


def main():
    """Show the menu again and again until the user chooses 0."""
    while True:
        show_menu()
        choice = input("Choose an option (0-3) : ").strip()

        if choice == "1":
            move_jpg_files()
        elif choice == "2":
            extract_emails()
        elif choice == "3":
            scrape_page_title()
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 0, 1, 2 or 3.")


# This block runs only when the file is executed directly,
# not when it is imported by another Python file.
if __name__ == "__main__":
    main()
