def create_ques_bank():
    question_list = []
    option_list = []
    zip_qo = []
    ques_file = open("Quiz_file", 'r')
    for question in ques_file:
# Adding question onto list
        if question.startswith("Question"):
            question.rstrip("\n")
            question_list.append(question)
# Adding options as a list onto list
            semi_final = []
            for opt in range(4):
                opt = ques_file.readline()
                opt.rstrip("\n")
                semi_final.append(opt)
            option_list.append(semi_final)
    ques_file.close()
    zip_qo = dict(zip(question_list, option_list))
    return zip_qo


print(create_ques_bank())
