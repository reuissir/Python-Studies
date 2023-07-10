# regular expressions

import re

email = input("What's your email? ").strip()

# re.search(pattern, string, flags=0)
# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? or 1 repetition
# {m} m repetitions
# {m, n} m-n repetitions

#if re.search(r"^[^@]+@[^@]+\.com$", email):
    #print("valid")

# r --> indicates raw string
# ^ matches the start of the string
# ? matches the end of the string
# [] set of characters
# [^] complementing the set - cannot match any given character
# \w - represents word character...as well as numbers and the underscore
# \W - not a word character
# A|B either A or B
# (...) a group
# ? 0 or 1 repetition

## first half(left)
# r --> allows search to recognize raw string \
# ^ start of the input
# /w + at least one or more word character(a-zA-Z0-9_)
# @ add sign in the middle

## second half
# at least one(+) of any word character plus a period (optional through ?)
# at least one(+) of any word character plus a period (\.)
# any one of the strings within the group (| --> or)
# $ end of the input

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|net|org|kr)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# re.match
# re.fullmatch
