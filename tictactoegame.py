def fun(s):
    if(d[1]=='  X  '):
        print("Player_1 won the game ")
        exit
    else:
        print("Player_2 won the game ")
        exit
l='---------------'
d={1:'      ',2:'      ',3:'      ',4:'      ',5:'      ',6:'      ',7:'      ',8:'      ',9:'      '}
p1='  X  '
p2='  O  '
j=0
while(j<=7):
    print(l)
    print(d[1],'|',d[2],'|',d[3])
    print(l)
    print(d[4],'|',d[5],'|',d[6])
    print(l)
    print(d[7],'|',d[8],'|',d[9])
    print(l)
    print(' Player_1 : X  Player_2 : O ')
    if(j%2==0):
        s=int(input("Player_1 select the box in which u want to occupy"))
        if(d[s]=='  O  '):
            print('you have choosen wrong box start again')
            exit
        else:
            d[s]='  X  '
            print('occupied successfully')
    else:
        s=int(input("Player_2 select the box in which u want to occupy"))
        if(d[s]=='  X  '):
            print('you have choosen wrong box start again')
            exit
        else:
            d[s]='  O  '
            print('occupied successfully')
    if(j>=4):
        if(d[1]+d[2]+d[3]=='  X    X    X  ' or d[1]+d[2]+d[3]=='  O    O    O  '):
            fun(d[1])
        elif(d[1]+d[4]+d[7]=='  X    X    X  ' or d[1]+d[4]+d[7]=='  O    O    O  '):
            fun(d[1])
        elif(d[1]+d[5]+d[9]=='  X    X    X  ' or d[1]+d[5]+d[9]=='  O    O    O  '):
            fun(d[1])
        elif(d[2]+d[5]+d[8]=='  X    X    X  ' or d[2]+d[5]+d[8]=='  O    O    O  '):
            fun(d[2])
        elif(d[3]+d[6]+d[9]=='  X    X    X  ' or d[3]+d[6]+d[9]=='  O    O    O  '):
            fun(d[3])
        elif(d[4]+d[5]+d[6]=='  X    X    X  ' or d[4]+d[5]+d[6]=='  O    O    O  '):
            fun(d[4])
        elif(d[3]+d[5]+d[7]=='  X    X    X  ' or d[3]+d[5]+d[7]=='  O    O    O  '):
            fun(d[5])
        elif(d[7]+d[8]+d[9]=='  X    X    X  ' or d[7]+d[8]+d[9]=='  O    O    O  '):
            fun(d[7])
        else:
            pass
    j+=1
print(l)
print(d[1],'|',d[2],'|',d[3])
print(l)
print(d[4],'|',d[5],'|',d[6])
print(l)
print(d[7],'|',d[8],'|',d[9])
print(l)
print(' Player_1 : X  Player_2 : O ')
