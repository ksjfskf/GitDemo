name1 = 'abhishet'
t = 0
r = 0
u = 0
e = 0
get_lenght = 0
def calculate_love_score(name_one):
    global t, r, u, e
    for i in name_one:
        if i in name1:
            if i == "t":
                t = t + 1
                print(f"{i} occures {t} times")
            elif i == "r":
                r = r +  1
                print(f"{i} occures {r}")
            elif i == "u":
                u = u + 1
                print(f"{i} occures {u}")
            elif i == "e":
                e = e + 1
                print(f"{i} occures {e} times")
        else:
            print(f"{i} not occures")
calculate_love_score(name_one="true")



