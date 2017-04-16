import random


def main():
    # Shapes
    egg = " ..... \n"
    egg += "........ \n"
    egg += "..........\n"
    egg += "........\n"
    egg += " ......\n"
    egg += "  ...\n"
    egg += "Happy Easter, egg goes here"
    bunny = "Happy Easter, bunny goes here"
    chick = "Happy Easter, chick goes here"
    shapes = [egg, bunny, chick]

    # Choose shape
    shape = random.choice(shapes)

    # Write to file
    with open('easter0.txt', 'w') as f:
        f.write(shape)


if __name__ == '__main__':
    main()
