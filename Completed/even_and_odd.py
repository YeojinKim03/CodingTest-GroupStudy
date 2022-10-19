#https://school.programmers.co.kr/learn/courses/30/lessons/12937
#내 풀이
def solution(num):
    if num%2==0:
        answer='Even'
    else:
        answer='Odd'
    return answer

#다른 사람 풀이
def evenOrOdd(num):
    if (num%2): #num%2가 1이 된다는 것은 홀수라는 뜻
        return "Odd"
    else:
        return "Even"