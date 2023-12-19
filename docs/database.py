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
# print(list_quiz)
class quest():
    def __init__(self,mongo_server_link,database_name):                                                                   # collection에 연결하는 함수 
        from pymongo import MongoClient
        self.mongoClient = MongoClient(mongo_server_link)                                                                 # mongo DB 서버에 연결
        self.database = self.mongoClient[database_name]                                                                   # 데이터 베이스에 연결
        self.quiz_list = self.database["quiz_list"]                                                                     # collection "todos_list"에 연결
        self.participate = self.database["participate"]                                                                 # collection "participants"에 연결
        self.participants_scoring = self.database["participants_scoring"]                                                       # collection "participants_todo"에 연결
    def upload_quiz_list(self,list):
        self.quiz_list.delete_many({})
        self.quiz_list.insert_many(list)
    def find_quiz_list(self):
        quiz = self.quiz_list.find({},{"question":1,"choice":1,"answer":1,"score":1})
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



if __name__ == "__main__":        
    quest_database = quest("mongodb://192.168.0.164:27017","toy_nosqls")
    quest_database.quiz_list
    quest_database.upload_quiz_list(list_quiz)
    quest_database.find_quiz_list()