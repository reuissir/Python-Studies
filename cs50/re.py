# reformat user's input
import re

name = input("What's your name? ").strip()

# parantheses () allows python to group certain values
if matches := re.search(r"^(.+), *(.+)$", name)
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

