# 등차수열, 등비수열의 일반항 n 대입기

mode = int(input("등차수열은 1, 등비수열은 2를 입력하세요. : "))

def arithmetic() :
    coefficient = float(input("계수 (공차) 입력 : "))
    leading_component_arithmetic = float(input("등차수열의 첫째 항 입력 : "))
    
    while True :
        n = int(input("n 입력 : "))
        outvalue = coefficient * n + (leading_component_arithmetic - coefficient)
        print ("출력 값 : ", outvalue)
    
def geometric() :
    ratio = float(input("공비 입력 : "))
    leading_component_geometric = float(input("등비수열의 첫째 항 입력 : "))
    
    while True :
        n = int(input("n 입력 : "))
        outvalue = leading_component_geometric * (ratio)**(n-1)
        print ("출력 값 : ", outvalue)
    
if mode == 1 :
    arithmetic()
    
elif mode == 2 :
    geometric()
    
else :
    print ("ERROR : 프로그램을 종료합니다.")
    quit()
