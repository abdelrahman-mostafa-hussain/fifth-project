import random

def randomNumTemplate():
    return random.choice(range(1,5))

def openAndReadStoryFile():
    file= open(f"template-{randomNumTemplate()}.txt")
    return file.read()

def main():
    content=openAndReadStoryFile()
    noun=input("enter the noun: ")
    name=input("enter the name: ")
    verb=input("enter the verb: ")
    adjective=input("enter the adjective: ")

    if noun!=None:
        content=content.replace("[noun]",f"{noun}")
    if name!=None:
        content=content.replace("[name]",f"{name}")
    if verb!=None:
        content=content.replace("[verb]",f"{verb}")
    if adjective!=None:
        content=content.replace("[adjective]",f"{adjective}") 

    print(content)   

if __name__=="__main__":
    main()