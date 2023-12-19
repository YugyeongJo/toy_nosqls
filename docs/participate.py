import quizlist

list_quiz = quizlist.quizmaking()

def answermaking():
    list_user_answer = []
    while True:
        list_answer = []
        str_username = input("응시자의 이름을 입력하세요: ")
        index_number = 1
        for i in range(len(list_quiz)):
            print("문항{}: {}".format(index_number, list_quiz[i]["question"]))
            index_number += 1
            print(list_quiz[i]["choice"])
            user_answer = input("답: ")
            list_answer.append(user_answer)
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