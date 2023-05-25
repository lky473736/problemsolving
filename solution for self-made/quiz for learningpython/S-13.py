file = open("/Users/alphastation/Desktop/컴퓨터공학전공/repository/problemsolving/words.txt", "r")

file.seek(0)
words = file.readlines()
print (words)
file.close()

starting_point = int(input("6자 이상인 단어를 출력하려면 0을 입력하세요: "))

if starting_point == 0:
    for word in words:
        if len(word.strip()) >= 6:
            print(word)