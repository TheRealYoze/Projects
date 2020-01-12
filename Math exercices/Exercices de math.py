from random import randint

def performTest(operation): 
    ## complete your work here ##
    if operation == 0:
        correctCounts = 0
        for i in range(10):
            run = True
            while run:
                try:
                    n1 = randint(1,9)
                    n2 = randint(1,9)
                    print("\nQuestion ", i+1, " of 10 : ", n1, " + ", n2, "?", sep="")
                    solution = n1 + n2
                    user_answer = int(input("Answer: "))
                except ValueError:
                    print("Allo")
            
            if user_answer == solution:
                print("Correct!")
                correctCounts += 1
                
            else:
                print("Incorrect.")
                print("The correct answer is ", solution, ".", sep="")
                        
    elif operation == 1:
        correctCounts = 0
        for i in range(10):
            
            n1 = randint(1,9)
            n2 = randint(1,9)
            print("\nQuestion ", i+1, " of 10 : ", n1, " * ", n2, "?", sep="")
            solution = n1 * n2
            user_answer = int(input("Answer: "))
            
            if user_answer == solution:
                print("Correct!")
                correctCounts += 1
                
            else:
                print("Incorrect.")
                print("The correct answer is ", solution, ".", sep="")
    
    return correctCounts
    
print("This software tests you with 10 questions …… ");
operation = int(input("0) Addition \n1) Multiplication\nPlease make a selection (0 or 1): "))
      
correctCounts = performTest(operation)
        
if correctCounts <= 6 :
  print("\nYour grade is: ", correctCounts, "/10.\n", "Please ask your teacher for help.", sep="")
else:
  print("\nYour grade is: ", correctCounts, "/10.\n", "Congratulations!", sep="")
