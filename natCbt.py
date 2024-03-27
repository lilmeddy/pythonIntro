cbt = [{"question":"1) What is my full name ","option":["a)Osamede\n","b)Osamide\n","c)Ayomide\n","d)Shush"],"correctAnswer":"a"},
       {"question":"2) Akinbola Righteousness Oluwatobilola is a bad person ","option":["a)Obviously, are you just knowing ire nhi\n","b)Yes he is,Ire is a bad person an I don't like him at all\n","c)I'm disappointed in you for just knowing yes he is\n","d)All of the above"],"correctAnswer":"d"},
       {"question":"3) Idowu Abisayo Ebun Gift is a bad person ","option":["a)Obviously bisayo is a bad person\n","b)Are you just knownin she is a very very bad person\n","c)She is my love so she is not a bad person jare\n","d)b and c\n","e)All of the above hehe "],"correctAnswer":"e"}]
correct = ["a","b","c","d","e"];score = int(0)
studentName =input("Enter your name\n");regNum =int(input("Enter your regestration number (not less than or greater than 5)\n")); covert = str(regNum)
while (len(covert)) != 5:
    print("Omo read what you're to do and don't stress me 5 character idiot");regNum = int(input("enter reg num kid\n")); covert = str(regNum)
fullreg = input(f"Hello {studentName[:3]}{covert[:3]} press enter to start your exam")
for questions in cbt:
    print(questions["question"])
    for options in questions["option"]:
        print(options)
    studentAns = input("Enter your answer (a,b,c,d,e)\n").lower()
    while studentAns not in correct:
        studentAns = input("This is why people fail simple instruction you can't follow idiot\nEnter your answer (a,b,c,d,e)\n").lower()
    if studentAns == questions["correctAnswer"]:
       score+=100;print(f"Awwn so smart you passed now your score is now {score} "); print("___________________________________________________________________");print() 
    else:
        score +=0;print(f"Awwwn such an idiot you failed it hehe you can do better lol your score is {score}"); print("________________________________________________________________");print()
meanScore = score/3     
if (meanScore >= 70):
    print(f"Dear {studentName[:3]}{covert[:3]} your average score is {meanScore}.\n\nYou Passed cute hehe aburo osamede hehe ")
else:
    print(f"Dear {studentName[:3]}{covert[:3]} your average score is {meanScore}.\n\nIdiot you failed sad hehe olodo \n\nTry again next year mumu aburo ire hahah")
    