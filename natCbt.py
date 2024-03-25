cbt = [{"question":"1) What is my full name ","option":["a)Osamede","b)Osamide"],"correctAnswer":"a"},{"question":"1) What is my full name ","option":["a)Osamede","b)Osamide"],"correctAnswer":"b"},{"question":"1) What is my full name ","option":["a)Osamede","b)Osamide"],"correctAnswer":"c"}]
correct = ["a","b","c"];score = int(0);userAnswer =[];options = ["a","b","c","d"]
studentName =input("Enter your name\n");regNum =int(input("Enter your regestration number (not less than or greater than 5)\n")); covert = str(regNum)
while (len(covert)) != 5:
    print("Omo read what you're to do and don't stress me 5 character idiot");regNum = int(input("enter reg num kid\n")); covert = str(regNum)
fullreg = input(f"Hello {studentName[:3]}{covert[:3]} press enter to start your exam")
for questions in cbt:
    print(questions["question"]);print("_______________________________");print()
    for options in questions["option"]:
        print(options)
print()
