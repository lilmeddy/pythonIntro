cbt = [{"question":"1) What is my full name ","option":["a)Osamede","b)Osamide","c)Ayomide","d)"],"correctAnswer":"a"},{"question":"1) What is my full name ","option":["a)Osamede","b)Osamide"],"correctAnswer":"b"},{"question":"1) What is my full name ","option":["a)Osamede","b)Osamide"],"correctAnswer":"c"}]
correct = ["a","b","c"];score = int(0);userAnswer =[];options = ["a","b","c","d"]
studentName =input("Enter your name\n");regNum =int(input("Enter your regestration number (not less than or greater than 5)\n")); covert = str(regNum)
while (len(covert)) != 5:
    print("Omo read what you're to do and don't stress me 5 character idiot");regNum = int(input("enter reg num kid\n")); covert = str(regNum)
fullreg = input(f"Hello {studentName[:3]}{covert[:3]} press enter to start your exam")
for questions in cbt:
    print(questions["question"])
    for options in questions["option"]:
        print(options)
    studentAns = input("Enter your answer (a,b,c,d,e)\n"); print("_______________________________");print()
    print()
    while studentAns not in correct:
        studentAns = input("This is why people fail simple instruction you can't follow idiot\nEnter your answer (a,b,c,d,e)\n")
    userAnswer.append(studentAns)
    if studentAns == questions["correctAnswer"]:
       score+=100
       print(f"Awwn so smart you passed now you have + {score} ") 
    else:
        score -=50
        print(f"Awwwn such an idiot you failed it hehe you can do better lol {score}")
meanScore = score/5      
if (meanScore >= 70):
    print(f"Dear{studentName[:3]}{covert[:3]} your average score is {meanScore}.\nYou Passed cute hehe aburo osamede hehe ")
else:
    print(f"Dear{studentName[:3]}{covert[:3]} your average score is {meanScore}.\nIdiot you failed sad hehe olodo try again next year mumu aburo ire hahah")
