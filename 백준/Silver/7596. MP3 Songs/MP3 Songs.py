'''
수는 자신의 MP3 플레이어를 사랑하지만 셔플 모드가 곡을 무작위로 재생하는 것을 싫어합니다. 수는 순서와 패턴을 좋아하기 때문에 MP3 플레이어에 있는 곡을 곡 이름의 알파벳 순서로 재생하길 원합니다. 이 문제에서는 수를 돕기 위해 곡을 알파벳 순서로 정렬해야 합니다.
'''

import sys

caset = 1

while True :
    num_song = int(sys.stdin.readline())
    
    if num_song == 0 :
        break
    
    else :
        lst_song = []
        
        for i in range (num_song) :
            lst_song.append (sys.stdin.readline().rstrip())
        
        lst_song.sort()
        
        print (caset)
        
        for song in lst_song :
            print (song)
    
    caset += 1 