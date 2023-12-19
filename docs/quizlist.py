question_type = int(input("문제 유형을 입력하세요. 숫자만 입력하세요."))
num_questions = int(input("문항 수를 입력하세요."))

print("문제와 선택지를 입력하세요.")

list_quiz = []

def quizmaking():
    for quiz in range(num_questions):
        dict_quizlist = {}
        dict_quizlist["question"] = input("문항 : ")
        dict_quizlist["choice"] = []
        for choice in range(question_type) : 
            dict_quizlist["choice"].append(input("보기 : "))
        dict_quizlist["answer"] = input("정답 : ")
        dict_quizlist["score"] = int(input("배점 : "))
        list_quiz.append(dict_quizlist)
    return dict_quizlist

quizmaking()