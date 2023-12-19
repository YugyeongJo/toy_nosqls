import quizlist

list_quiz = quizlist.quizmaking()

def answermaking():
    list_user_answer = []
    while True:
        list_answer = []
        str_username = input("응시자의 이름을 입력하세요: ")
        index_number = 1
        for i in range(len(list_quiz)):
            quizs = list_quiz[i]["question"]
            print("문항{}: {}".format(index_number, quizs))
            index_number += 1
            choices = list_quiz[i]["choice"]
            print("선택지")
            for j in range(len(choices)):
                print("{}. {}".format(j+1, choices[j]))
            user_answer = input("답: ")
            list_answer.append(user_answer)
            print("--------------")
        dic_user = {}
        dic_user['name'] = str_username
        dic_user['user_answer'] = list_answer
        list_user_answer.append(dic_user)
        quit_input = input("다음 응시자가 있나요? (계속: c, 종료: x): ")
        if quit_input == 'x':
            print("프로그램이 종료되었습니다.")
            return list_user_answer
        elif quit_input == 'c':
            continue

list = answermaking()

print(list)