# Small Task Automator

A single Python script that automates three small, genuinely repetitive jobs from one menu:
moving photos out of a cluttered folder, pulling email addresses out of a text file, and
saving the title of a webpage to a log.

Written with the Python standard library plus `requests`. No frameworks, no classes — plain
functions, so every line can be explained line by line.

## The three tasks

**1. Move all `.jpg` files into a new folder** — walks through a folder you choose, moves every
`.jpg` / `.jpeg` file into a destination folder (created automatically), and leaves documents,
music and sub-folders untouched. If an image of the same name already exists at the destination,
the incoming file becomes `photo_1.jpg` instead of overwriting anything.
Concepts: `os.listdir`, `os.path`, `os.makedirs`, `shutil.move`.

**2. Extract email addresses from a `.txt` file** — reads the file, finds every address with a
regular expression, lowercases them, drops duplicates while keeping the original order, and
writes the clean list to `<filename>_emails.txt`. It reports how many matches were found and how
many duplicates were removed.
Concepts: `re.findall`, sets for de-duplication, reading and writing text files.

**3. Scrape a webpage title and save it** — downloads a page, pulls the text out of its
`<title>` tag, tidies the whitespace, and *appends* a timestamped line to `titles_log.txt`, so
running it every day builds a history instead of erasing the last result.
Concepts: `requests.get`, HTTP status handling, `re.search` with `DOTALL`, appending to files.

## Running it

```
pip install requests          # needed only for task 3
python automation_tasks.py
```

Then pick 1, 2 or 3 from the menu. Pressing Enter at a prompt accepts the suggested default
(the `jpg_files` sub-folder for task 1, `https://www.python.org` for task 3).

A `sample_data` folder is included so the script can be tried immediately:
`sample_data/messy_folder` holds three real JPEGs mixed with a `.txt` and a `.pdf`, and
`sample_data/contacts.txt` contains addresses with deliberate duplicates and near-misses.

## Sample run

```
===== Small Task Automator =====
1. Move all .jpg files into a new folder
2. Extract email addresses from a .txt file
3. Scrape a webpage title and save it
0. Exit
Choose an option (0-3) : 2

--- Task 2: Extract email addresses from a .txt file ---
Text file to read : sample_data/contacts.txt

Total matches found : 6
Unique addresses    : 4
Duplicates removed  : 2
Saved to            : sample_data/contacts_emails.txt
```

## How it handles mistakes

Bad input re-prompts instead of crashing, which is the part that took the most care:

- a folder path that does not exist, or that points at a file, is rejected and asked again
- a missing `.txt` file, or a file with the wrong extension, is asked again
- a text file with no addresses in it saves nothing and says so
- a dead link, a 404 or a page with no `<title>` prints a readable message and returns to the menu
- if `requests` is not installed, tasks 1 and 2 still work; only task 3 reports the missing package

## Testing notes

All three tasks were run end to end. Task 1 was checked against a folder mixing `.jpg`, `.JPG`,
`.jpeg`, `.txt`, `.pdf`, `.mp3` and a sub-folder, including a deliberate filename clash — both
files survived, one renamed. Task 2 was checked against duplicates in different cases and a line
containing an `@` that is not an address. Task 3 was verified against a local test server, which
also covered the 404, unreachable-host and missing-`<title>` paths.

## Possible next steps

Sort images into sub-folders by the date the photo was taken, validate extracted addresses against
a mail server, and run task 3 on a schedule so the title log fills in by itself.
