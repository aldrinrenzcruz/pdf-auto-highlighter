import os
import fitz

errors_file = os.path.abspath("_list.txt")

with open(errors_file, "r", encoding='utf-8') as f:
    errors = f.read().splitlines()

doc = fitz.open("input.pdf")

for page in doc:
    for text in errors:
        text_instances = page.search_for(text.lower())
        for inst in text_instances:
            highlight = page.add_highlight_annot(inst)
            highlight.update()

doc.save("output.pdf", garbage=4, deflate=True, clean=True)
