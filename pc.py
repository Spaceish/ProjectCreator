import os
import sys

def create_starting_file(name: str) -> None:
    f = open(f'{name}/hei.txt', 'w')
    f.write('heii')
    f.close()

def create(name: str) -> None:
    os.system(f"mkdir {name} && cd {name} && code .")
    create_starting_file(name)
    print("Heii dani proiectul tau >", name, "s-a creat lol. :>")
    sys.exit(1405)

if __name__ == "__main__":
    print("Hei dan, ProjectCreatorV2, By 0xSpaceDot#8745")
    create(sys.argv[1])