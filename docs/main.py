import quizlist, database, participate
list_quiz=quizlist.quizmaking()

quest_database = database.quest("mongodb://192.168.0.164:27017","toy_nosqls")

quest_database.upload_quiz_list(list_quiz)
list_quiz = quest_database.find_quiz_list()
list_user_answer = participate.answermaking(list_quiz)
quest_database.upload_participate(list_user_answer)
    