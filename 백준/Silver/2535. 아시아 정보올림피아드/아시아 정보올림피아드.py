import sys

N = int(input())

country = []
student = []
score = []

win_country = []
winner = []

for i in range (N) :
    com1, com2, com3 = sys.stdin.readline().split()
    country.append(int(com1))
    student.append(int(com2))
    score.append(int(com3))
    
# gold 
gold_medal = score.index(max(score))
win_country.append (country[gold_medal])
winner.append ((country[gold_medal], student[gold_medal]))

country.pop(gold_medal)
student.pop(gold_medal)
score.pop(gold_medal)

# silver
silver_medal = score.index(max(score))
win_country.append (country[silver_medal])
winner.append ((country[silver_medal], student[silver_medal]))

country.pop(silver_medal)
student.pop(silver_medal)
score.pop(silver_medal)

# bronze
if win_country[0] == win_country[1] :
    for i in range (N - 2) :
        bronze_medal = score.index(max(score))
        
        if country[bronze_medal] in win_country : 
            country.pop(bronze_medal)
            student.pop(bronze_medal)
            score.pop(bronze_medal)
        
        else : 
            win_country.append (country[bronze_medal])
            winner.append ((country[bronze_medal], student[bronze_medal]))
            
            break
    
else :
    bronze_medal = score.index(max(score))
    win_country.append (country[bronze_medal])
    winner.append ((country[bronze_medal], student[bronze_medal]))
    
for i in winner :
    for j in i : 
        print (j, end = ' ')
        
    print()
    