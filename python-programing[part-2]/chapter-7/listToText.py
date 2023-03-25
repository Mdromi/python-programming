# python3 chapter-7/listToText.py

import re

with open("chapter-7/list.html", "r") as f:
    html = f.read()

pattern = r'<li>\s*(\w+)\s*<ol>([\s\S]*?)<\/ol>\s*<\/li>'
matches = re.findall(pattern, html)

print(matches)

for country, players_html in matches:
    player_names = re.findall(r'<li>([\w\s]+)<\/li>', players_html)
    player_names_str = ', '.join(player_names)
    print(f"{country} - {player_names_str}")