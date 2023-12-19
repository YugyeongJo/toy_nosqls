import quizlist, database, participate,scoring

list_quiz=quizlist.quizmaking()
pass
quest_database = database.quest("mongodb://192.168.0.164:27017","toy_nosqls")
pass
quest_database.upload_quiz_list(list_quiz)
pass
list_quiz = quest_database.find_quiz_list()
pass
list_user_answer = participate.answermaking(list_quiz)
pass
quest_database.upload_participate(list_user_answer)
pass
list_participate = quest_database.find_participate()
pass
list_sum = scoring.calculating(list_user_answer,list_quiz)
pass
scoring.averazing(list_sum,list_user_answer)
pass
quest_database.scoring_upload(list_sum,list_participate)