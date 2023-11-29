import random

def randomNumTemplate():
    return random.choice(range(1,5))

def openAndReadStoryFile():
    file = open(f"template-{randomNumTemplate}.txt")
    return file.read()

def main():
    print("this is story generator")

if __name__=="__main__":
    main()