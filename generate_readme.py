import os

with open("README.md", "a") as readme:
    readme.write("## Preview\n\n")
    readme.write('<div style="display: flex; flex-wrap: wrap; gap: 8px;">\n')
    for entry in os.listdir("images"):
        readme.write(f'\t<img src="images/{entry}">\n')
    readme.write('</div>')
