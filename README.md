# Latex2Svg
A quick and easy way to get embeddable, scalable images from Latex equations.

Basically it just downloads the svg files that CodeCogs so graciously supplies so you can store them locally.

## tex.text
Your Latex goes here. Surround with $ for inline and with $$ for display.

## Config.toml
If you want to set the color, or want multiple copies in different colors,
list the colors in RGB format and the names of their associated output directories like below.
```
colors = ["32, 32, 32", "235, 235, 235"]
outputs = ["light", "dark"]
```
The default is one copy in black, so if that's all you need feel free to delete this file.
