sdict = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

reg = ""

for i in range (2) : 
    a = input()
    reg = reg + str(sdict[a])
    
b = input()
print (int(reg) * (10 ** sdict[b]))