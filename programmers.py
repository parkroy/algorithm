def solution(s):
    if len(s)==4 or len(s)==6:
        for i in s:
            if i.isalpha():
                return False
            else:
                return True
    else:
        return False

    #1. 완주하지 못한 선수
def solution(participant, completion):
    for i in participant:
        if i not in completion:
            return answer


    #2. 수포자


    #3. K번째 수
def solution(array, commands):
    answer = []
    for i in commands:
        temp = array[i[0]-1:i[1]]
        temp.sort()
        answer.append(temp[i[2]-1])
    return answer


    #4. 체육복

def solution(n, lost, reserve):
    ax=0
    for i in lost:
        if i+1 in reserve:
            ax=ax+1
        if i-1 in reserve:
            ax=ax+1
    for j in reserve:
        if j+1 and j-1 in lost:
            ax=ax-1
        answer=ax+n-len(lost)
    return answer
