import json
import os
import random

with open("data.json", "r") as f:
    spaces = f.read()
data = json.loads(spaces)

spaces = []

for space in data:
    spaces.append(space)

while True:
    print("[1] - Create new space")
    print("[2] - Insert data into space")
    print("[3] - List spaces")
    print("[4] - Shuffle JSON")
    print("[5] - Save")
    choice = int(input("> "))
    os.system("cls")
    match choice:
        case 1:
            spaceName = str(input("Name: "))
            spaceDescription = str(input("Description: "))
            space = dict()
            space["id"] = 0
            space["name"] = spaceName
            space["description"] = spaceDescription
            space["media"] = []
            spaces.append(space)
        
        case 2:
            print("[*] - Insert the corresponding number")
            for i, space in enumerate(spaces):
                print(f"-{i}- {space['name']}")
            spaceChoice = int(input("> "))
            mediaList = spaces[spaceChoice]["media"]
            
            print(f"[*] - Selected space: {spaces[spaceChoice]['name']}")
            mediaInput = input("Media URL's (separated by space): ")
            mediaUrls = mediaInput.split()

            mediaList.extend(mediaUrls)
            spaces[spaceChoice]["media"] = mediaList

        case 3:
            for i, space in enumerate(spaces):
                print(f"-{i}- {space['name']}")

        case 4:
            random.shuffle(spaces)
            print("[*] - Shuffled")

        case 5:
            with open("data.json", "w", encoding="utf-8") as output:
                json.dump(spaces, output, ensure_ascii=False, indent=4)
            break
            
