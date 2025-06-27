from Question import Question

question_prompts = [
    "What is the color of Moon?\na.White\nb.Green\nc.Yellow\n\n",
    "Pick the odd one out.\na.Dog\nb.Cat\nc.Pigeon.\n\n",
    "What are color of Bananas?\na.Pink\nb.Yellow\nc.Green\n\n"
]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"b")
]

def run_Test(questions):
    score = 0
    for ques in questions:
        answer = input(ques.qns)
        if answer == ques.ans:
            score += 1
    print("You got "+str(score)+ "/"+str(len(questions))+" correct!")


run_Test(questions)