#list_quiz의 정답 dict와 answer가 같으면
#점수 합산.

# import database

# 뭐시기뭐시기 = database.function  # list quiz값 받아오기

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


pass

import database
quest_database = database.quest("mongodb://192.168.0.164:27017","toy_nosqls")
list_user_answer = [{"user_name":'문석천',"user_answer":['A','B','C','D','D']},
                    {"user_name":'노주현',"user_answer":['B','C','D','A','A']},
                    {"user_name":'조유경',"user_answer":['C','D','A','B','C']},
                    {"user_name":'서정민',"user_answer":['D','A','B','C','D']}]
print(list_user_answer)

pass

def calculating(list_user_answer,list_quiz):
    sum = 0
    list_sum = []
    for number in range(len(list_user_answer)) :                              #list_quiz 내용만큼 숫자 받아 for구문 돌리기
        for num_question in range(len(list_quiz)) :
            if list_quiz[num_question]["answer"] == list_user_answer[number]["user_answer"][num_question] :
                sum = sum + list_quiz[number]["score"]      #한사람의 점수 합계구하기
                list_sum.append(sum)
    return list_sum
def averazing(list_sum,list_user_answer):               
    total_score = 0
    for i in range(len(list_sum)):
        total_score = total_score + list_sum[i]
    print(total_score)
    average = total_score/len(list_user_answer)    # sum 합계를 list_user_answer의 
    print("응시자별 채점결과:")
    for number in range(len(list_user_answer)) :
        print("{}:{}점".format(list_user_answer[number]["user_name"],list_sum[number]))    #list answer에 해당하는 순서의 참여자 이름, 합계
    print("과목 평균 점수: {}".format(average))
    return  average



if __name__ == "__main__":
    apple = calculating(list_user_answer,list_quiz)
    averazing(apple,list_user_answer)
