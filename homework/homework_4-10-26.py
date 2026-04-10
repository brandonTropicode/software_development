def evaluate_score(score):
    if score > 110 or score < 0:
        print("that isn't a grade")
        return
    if score > 79:
        print("excellent")
    elif score > 50:
        print("average")
    else:
        print("you are stupid")
score_input = int(input("what is your score? "))
evaluate_score(score_input)