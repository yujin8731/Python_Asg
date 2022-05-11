def solution(mat):

    sum=0
    mat_ret=[]
    for i in range(len(mat[0])):  #디버그찍기
        for j in range(len(mat)):
            sum+=mat[j][i]  #ji의 경우에는 10,20,30이 됨
        mat_ret.append(sum)
        sum=0
    return mat_ret

answer1=solution([[1,2],[4,5],[6,7]])
print(answer1)
