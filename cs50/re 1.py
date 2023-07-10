import re

url = input("URL: ").strip()

# search user's URL for given regular expression
# group('()') + make it optional('?')
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
    print(f"Username:", matches.group(1))