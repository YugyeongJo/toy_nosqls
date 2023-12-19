# [Naming Rule]

# list_quiz - 문항, 선택지, 점수, 정답모음
# dict_quizlist - 문항 1개

# list_username - 응시자 이름 list_answer - 응시자의 답변

# list_userscore - 응시자별 채점 결과

# 문제 유형을 입력하세요 (4지 선다형): 4지 선다형
# 문항 수를 입력하세요 (5문항): 5
# import quizlist
# quest_database = database.quest("mongodb://192.168.0.164:27017","toy_nosqls")
# quiz = quest_database.find_quiz_list()
# pass
# print (quizlist.quizmaking())
list_quiz = [{"question": '파이썬의 기본 자료형이 아닌 것은 무엇인가요?',
              "choice": ['A. 정수(int)', 'B. 실수(float)', 'C. 문자열(str)','D. 불대수(bool)'],
              "answer": 'D',
              "score": 10},
              {"question": '다음 중 파이썬의 주요 특징이 아닌 것은 무엇인가요?',
               "choice": ['A. 객체 지향적 언어','B. 동적 타이핑 지원', 'C. 메모리 관리 자동화', 'D. 컴파일 언어'],
               "answer": 'D',
               "score": 10},
               {"question":'파이썬에서 리스트를 복사할 때 얕은 복사(shallow copy)를 수행하는 방법으로 옳지 않은 것은 무엇인가요?',
                "choice": ['A. new_list = old_list.copy()','B. new_list = old_list[:]','C. new_list = list(old_list)','D. new_list = old_list + []'],
                "answer": 'D',
                "score": 10},
                {"question":'다음 중 파이썬에서 제공하는 빌트인 함수가 아닌 것은 무엇인가요?',
                 "choice":['A. len()','B. type()','C. print()','D. append()'],
                 "answer": 'D',
                 "score": 10},
                 {"question":'파이썬에서 제어문으로 사용되지 않는 것은 무엇인가요?',
                  "choice":['A. if','B. for','C. while','D. until'],
                  "answer":'D',
                  "score": 10}]
# str_username = input("응시자의 이름을 입력하세요: ")
# num_user_answer = input("답: ")
# str_add_user = input("다음 응시자가 있나요?(계속: c, 종료: x): ")



# list_user_answer = []

# def find_quiz_list(quiz):
#         list_quiz = []
#         for i in quiz:
#             dic_quiz = {}
#             dic_quiz["question"] = i["question"]
#             pass
#             dic_quiz["choice"] = i["choice"]
#             pass
#             dic_quiz["answer"] = i["answer"]
#             dic_quiz["score"] = i["score"]
#             list_quiz.append(dic_quiz)
#         return list_quiz
      
# list_quiz = find_quiz_list(quiz)


while True:
    list_answer = []
    str_username = input("응시자의 이름을 입력하세요: ")
    for i in range(len(list_quiz)):
        print(list_quiz[i]["question"])
        print(list_quiz[i]["choice"])
        user_answer = input("답: ")
        list_answer.append(user_answer)
    dic_user = {}
    dic_user['name'] = str_username
    dic_user['user_answer'] = list_answer

    quit_input = input("다음 응시자가 있나요? (계속: c, 종료: x): ")
    if quit_input == 'x':  
        print("프로그렘이 종료되었습니다.")
        break   
    elif quit_input == 'c':
        pass
       
    