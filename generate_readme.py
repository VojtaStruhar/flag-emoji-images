import os

with open("README.md", "a") as readme:
    readme.write("\n\n## Preview\n\n")
    readme.write('<div style="display: flex; flex-wrap: wrap; gap: 4px;">\n')
    for entry in sorted(os.listdir("images")):
        alt = entry.split(".")[0]
        readme.write(f'\t<img src="images/{entry}" alt="{alt}">\n')
    readme.write('</div>')
