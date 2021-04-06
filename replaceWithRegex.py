# replaceWithRegex.py
import re

text = "Today is 10/29/2019. Deadline is 11-15-2019"
print(text)
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\1-\2-\3", text))
print(re.sub(r"(\d+)-(\d+)-(\d+)", r"\1/\2/\3", text))
