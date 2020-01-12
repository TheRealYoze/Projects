def tableMultiplication():
    
    # "Parameters" of the table #
    start = int(input("Type the start of the table: "))
    end = int(input("Type the end of the table: "))
    base = int(input("Type the base of the table: "))
    i = start

    while i <= end:
        print(i, "*", base, "=", base*i)
        i += 1
    


def tableMultiplication2():
    
 # "Parameters" of the table #
    start = int(input("Type the start of the table: "))
    end = int(input("Type the end of the table: "))
    base = int(input("Type the base of the table: "))

    question = 1
    correct_answers = 0
    i = 0
    run = True
    question_nb = round((end-start)/base)+1
    for j in range(start, end+1, base):
        while run:
                try:
                    print("\nQuestion ", question, " of ", question_nb, ": ", sep="")
                    print(start+i, " * ", base, " = ", end="", sep="")
                    user_answer = int(input())

                    question += 1
                    i += 1
                    run = False
                    if user_answer == j:
                         print("Correct!")
                         correct_answers += 1
                    else:
                        print("Incorrect.\nThe correct answer is ", j, ".", sep="")
                except ValueError:
                    print("Please enter a valid number")
    percentage = round(correct_answers/question_nb*100, 2)
    print("\nYour score is ", correct_answers, "/", question_nb, ".\n", percentage, "%.", sep="")
        

tableMultiplication()
