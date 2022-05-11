a=0
for i in range(1,101,1):
    k=1/(i+1)
    a+=k
print(a)

#로그 조화급수
import math
b=0
for j in range(1,101,1):
    b+=j
    c=math.log(j+1)
print(c)


print("오차율은", (c-a)/a )

