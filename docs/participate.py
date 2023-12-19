# [Naming Rule]

# list_quiz - 문항, 선택지, 점수, 정답모음
# dict_quizlist - 문항 1개

# list_username - 응시자 이름 list_answer - 응시자의 답변

# list_userscore - 응시자별 채점 결과

# 문제 유형을 입력하세요 (4지 선다형): 4지 선다형
# 문항 수를 입력하세요 (5문항): 5
import database

types_quiz = input("문제 유형을 입력하세요 (4지 선다형): ")
num_quiz = input("문항 수를 입력하세요 (5문항): ")
str_username = input("응시자의 이름을 입력하세요: ")
num_user_answer = input("답: ")
str_add_user = input("다음 응시자가 있나요?(계속: c, 종료: x): ")

dic_user = {}
dic_user['name'] = str_username
dic_user['user_answer'] = num_user_answer

list_user_answer = []

 def find_quiz_list():
        quiz = quiz_list.find({},{"question":1,"choice":1,"answer":1,"score":1})
        list_quiz = []
        for i in quiz:
            dic_quiz = {}
            dic_quiz["question"] = i["question"]
            pass
            dic_quiz["choice"] = i["choice"]
            pass
            dic_quiz["answer"] = i["answer"]
            dic_quiz["score"] = i["score"]
            list_quiz.append(dic_quiz)
        return list_quiz

quit_input = input("다음 응시자가 있나요? (계속: c, 종료: x): ")
if quit_input == 'x':  
    print("프로그렘이 종료되었습니다.")
    break
elif quit_input == 'c':
    name = input("응시자 이름을 입력하세요: ")

       
    