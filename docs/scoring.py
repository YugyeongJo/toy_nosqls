# list_answer = [a,b,c,d,e] ------------응시자 답변
#list_quiz의 정답 dict와 answer가 같으면
#점수 합산.

import database

뭐시기뭐시기 = database.function  # list quiz값 받아오기

list_quiz = ["question : ", "choice : ", "answer : ", "score : " ]

list_answer = [D,D,D,D,D]



sum = 0

for number in range(len[list_quiz]) :
    if list_answer == list_quiz[number]["answer"] :
        sum = sum + list_quiz[number]["score"]


    print("응사자별 채점결과:")
    print("{}:{}".format(인풋받은입력값,점수합한값.))
    print("과목 평균 점수: {}".format(평균값 구하는 식))














# 각 문항 정답 [1, 2, 3, 4, 1]


# 응시자별 채점 결과:
#   홍길동: 95점
#   이순신: 85점
#   ...
# 과목 평균 점수: 90점
