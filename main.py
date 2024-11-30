import glob
import os

import numpy as np
from PIL import Image


def print_image_in_console(image_path: str, width: int):
    image = Image.open(image_path)
    image = image.resize((width, int(image.height * width / image.width)))
    image_array = np.array(image)
    output = ""
    for row in image_array:
        for pixel in row:
            r, g, b = pixel[:3]
            output += f"\033[48;2;{r};{g};{b}m  "
        output += "\033[0m\n"
    return output


def main():
    image_files = glob.glob(os.path.join("assets", "frame", "*.png"))
    with open("dist/main.js", "w") as f:
        f.write("#!/usr/bin/env node\n")
        f.write("(async () => {\n")
        for image_file in image_files:
            f.write("if(process.stdout.columns>179){\n")
            f.write(f"console.log(`{print_image_in_console(image_file, 90)}`);\n")
            f.write("}else if(process.stdout.columns>119){\n")
            f.write(f"console.log(`{print_image_in_console(image_file, 60)}`);\n")
            f.write("}else{\n")
            f.write(f"console.log(`{print_image_in_console(image_file, 30)}`);\n")
            f.write("}\n")
            f.write("await new Promise((resolve) => setTimeout(resolve, 100));\n")
            f.write("console.clear();\n")
        f.write("})();\n")


if __name__ == "__main__":
    main()
