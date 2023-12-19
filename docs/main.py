import quizlist, database
list_quiz=quizlist.quizmaking()

quest_database = database.quest("mongodb://192.168.0.164:27017","toy_nosqls")

quest_database.upload_quiz_list(list_quiz)
