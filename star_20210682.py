# ##피라미드 만들기
n=int(input("n >"))
for i in range(n) :
    for j in range(n-1-i) :
        print(end=' ')
    for j in range(2*i+1):
        print("*", end='')
    for j in range(n-1-i):
        print(end=' ')

    print()  #못함 93번쨰에 계쏙 반복