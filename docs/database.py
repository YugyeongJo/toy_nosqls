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
                  "chocie":['A. if','B. for','C. while','D. until'],
                  "answer":'D',
                  "score": 10}]
print(list_quiz)
# class quest():
#     def __init__(self,mongo_server_link,database_name):                                                                   # collection에 연결하는 함수 
#         from pymongo import MongoClient
#         self.mongoClient = MongoClient(mongo_server_link)                                                                 # mongo DB 서버에 연결
#         self.database = self.mongoClient[database_name]                                                                   # 데이터 베이스에 연결
#         self.todos_list = self.database["quiz_list"]                                                                     # collection "todos_list"에 연결
#         self.participants = self.database["participate"]                                                                 # collection "participants"에 연결
#         self.participants_todo = self.database["participants_todo"]                                                       # collection "participants_todo"에 연결
        