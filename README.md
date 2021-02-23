# Latex2Svg
A quick and easy way to get embeddable, scalable images from Latex equations

## Config.toml
If you want to set the color, or want multiple copies in different colors,
list the colors in RGB format and the names of their associated output directories like below.
```
colors = ["32, 32, 32", "235, 235, 235"]
outputs = ["light", "dark"]
```
The default is one copy in black, so if that's all you need feel free to delete this file.