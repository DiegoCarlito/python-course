import re

url = input("URL: ").strip()

# re.sub(pattern, repl, string, count=0, flags=0)
# re.split(pattern, string, maxsplit=0, flag=0)
# re.findall(pattern, string, flags=0)
if matches := re.search(r"^https?://(?:www\.)?github\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))