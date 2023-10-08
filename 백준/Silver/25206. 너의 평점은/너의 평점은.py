credit = []
grade = [] # credit's compo -> grade's compo (일대일 대응)

scoredict = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

score = []

for k in range (20) :
    stuff = input()
    
    if stuff[-1] != 'P' and stuff[-1] != 'F' :
        credit.append (float(stuff[-6 : -3]))
        grade.append (stuff[-2 : ])
        
    else :
        credit.append (float(stuff[-5 : -2]))
        grade.append (stuff[-1])
        
P_count = 0
P_credit = 0

for j in range (20) :
    if grade[j] != 'P' : 
        score.append (scoredict[grade[j]] * credit[j])
        
    else :
        P_credit += credit[j]

# https://blockdmask.tistory.com/534

finalscore = sum(score) / (sum(credit) - P_credit)
print("{:.6f}".format(finalscore))