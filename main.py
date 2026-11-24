"""Entry for make.fun: The Long Roast: Lawmakers and the File They Cannot Convert.

Writes the single entry sentence to /output/entry.txt (UTF-8, 1-320 chars).
Deterministic, stdlib only, no network.

The sentence is the whole entry: one satirical roast, exactly as written below.
"""

import os

ENTRY = "They can draft a 400-page law on artificial intelligence before breakfast, but ask them to turn a Word document into a PDF and suddenly the hearing needs a recess, a consultant, and a teenager."

# The bounty gate allows 1-320 characters; refuse to write anything outside it.
# len() counts Unicode code points, which is what the gate counts as
# characters, so this check matches the sealed scorer exactly.
if not 1 <= len(ENTRY) <= 320:
    raise SystemExit(f"entry is {len(ENTRY)} characters, outside the 1-320 gate")

OUTPUT_PATH = "/output/entry.txt"

os.makedirs("/output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(ENTRY)

# Read back and confirm the file holds exactly the entry sentence: what the
# grader reads must be what was intended, byte for byte.
with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
    written = f.read()
if written != ENTRY:
    raise SystemExit("entry.txt does not match the entry sentence after writing")
