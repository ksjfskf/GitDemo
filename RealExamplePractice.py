name1 = "True"
name2 = "Love"

matchChar = 0

def calculate_love_score(name_one,name_two):
    global matchChar
    for i in name1:
        for j in name_one:
            if i == j:
                matchChar = matchChar + 1
                print(f"yes match with character {matchChar}!!")
    for i in name1:
        for j in name_two:
            if i == j:
                matchChar = matchChar + 1
                print(f"yes match with character {matchChar}!!")
    for k in name2:
        for l in name_one:
            if k == l:
                matchChar = matchChar + 1
                print(f"yes match with character {matchChar}!!")
    for k in name2:
        for l in name_two:
            if k == l:
                matchChar = matchChar + 1
                print(f"yes match with character {matchChar}!!")
calculate_love_score(name_one="Abhishek",name_two="Khanaj")

