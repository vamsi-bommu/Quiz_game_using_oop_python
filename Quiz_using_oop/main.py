from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for i in question_data:
    q=i["question"]
    a= i['correct_answer']
    question_bank.append(Question(q, a))

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
        quiz.next_question()
        

print("\n\nYou have completed the quiz.")
print(f"Your final score was {quiz.score}/{len(question_bank)}.") 