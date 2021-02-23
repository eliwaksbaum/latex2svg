import requests
import toml
from pathlib import Path

imgs:list
config:dict

def parseTex(lines:list):
    new_lines = []
    for i, line in enumerate(lines):
        if line == "\n":
            continue

        inline = False
        if (line[0] == "$" and line[1] != "$"):
            inline = True
        line = line.replace("$", "")
        line = line.replace("\n", "")
        line = line.replace(" ", "&space;")
        line = line.replace("+", "&plus;")
        new_lines.append((line, inline))
    return new_lines

def addColor(lines:list, color:str):
    colortag = "{\color[RGB]{" + color + "}"
    return ["""\inline""" + colortag + line[0] + "}" if(line[1]) else colortag + line[0] + "}" for line in lines]




if Path("config.toml").exists():
    with open("config.toml", "r") as loadconfig:
        config = toml.load(loadconfig)
    if config == {}:
        config = {"colors": ["0, 0, 0"], "outputs": [""]}
else:
    config = {"colors": ["0, 0, 0"], "outputs": [""]}

with open("tex.txt", "r") as tex:
    imgs = tex.readlines()

imgs = parseTex(imgs) #returns a list of tuples, [0] is the parsed text, [1] is an inline boolean
for i, color in enumerate(config["colors"]):
    coloredimgs = addColor(imgs, color)
    output = "output" / Path(config["outputs"][i])
    if (not output.exists()):
        output.mkdir()
    for j, tex in enumerate(coloredimgs):
        link = "https://latex.codecogs.com/svg.latex?" + tex
        print(link)
        r = requests.get(link)
        with open(output / ("latex" + str(j) + ".svg"), "wb") as svg:
            svg.write(r.content)
