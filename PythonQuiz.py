import time
#Megadott név amiből kiolvassa a kérdéseket
txtName = "PythonQuizQuestion.txt"
correctAnswers = 0
numberOfQuestions = 0

def Quiz():
    def SplitCorrection():
        # opening the file in read mode
        file = open(txtName, "r", encoding="utf8")
        replacement = ""
        questionNumber = 0
        # using the for loop
        for line in file:
            questionNumber += 1
            if questionNumber != 1:
                line = line.strip()
                changes = line.replace("*", "@*")
                replacement = replacement + changes + "\n"
            else:
                line = line.strip()
                name = line + " "
                if questionNumber == 1:
                    changes = ""
                else:
                    changes = line.replace("*", "@*")
                replacement = name + changes + "\n"

        file.close()
        # opening the file in write mode
        fout = open(txtName, "w", encoding="utf8")
        fout.write(replacement)
        fout.close()
    def FinalCorrection():
        # opening the file in read mode
        file = open(txtName, "r", encoding="utf8")
        replacement = ""
        questionNumber = 0
        # using the for loop
        for line in file:
            questionNumber += 1
            if questionNumber != 1:
                line = line.strip()
                changes = line.replace("@@", "@")
                replacement = replacement + changes + "\n"
            else:
                line = line.strip()
                name = line + " "
                if questionNumber == 1:
                    changes = ""
                else:
                    changes = line.replace("@@", "@")
                replacement = name + changes + "\n"

        file.close()
        # opening the file in write mode
        fout = open(txtName, "w", encoding="utf8")
        fout.write(replacement)
        fout.close() 
    def AnswerCheck():
        #Megkéri a felhasználót hogy adjon meg egy számot ami egyezik a válasz számával
         userAnswer = int(input("Adja meg a helyes válasz számát: "))
         #Meg nézzük hogy a felhasználó által adott válasz egyenlő-e a helyes válasszal
         
         global correctAnswers
         if (userAnswer == 1) and (len(CorrectAnswerOne) == 2):
             print("Helyes válasz!")
             #+1 a helyes pont
             
             correctAnswers += 1
         #Ha nem a helyes válasz betűjelét adja meg mikor a helyes válasz volna megadja mi lenne a helyes válasz és tovább megyünk
         elif not((userAnswer == 1)) and (len(CorrectAnswerOne) == 2):
             print("A helyes válasz a 1-as lett volna")


         #Meg nézzük hogy a felhasználó által adott válasz egyenlő-e a helyes válasszal
         elif (userAnswer == 2) and (len(CorrectAnswerTwo) == 2):
             print("Helyes válasz!")
             correctAnswers += 1
         #Ha nem a helyes válasz betűjelét adja meg mikor a helyes válasz volna megadja mi lenne a helyes válasz és tovább megyünk
         elif (len(CorrectAnswerTwo) == 2) and not((userAnswer == 2)):
             print("A helyes válasz a 2-as lett volna")


         #Meg nézzük hogy a felhasználó által adott válasz egyenlő-e a helyes válasszal
         elif (userAnswer == 3) and ((len(CorrectAnswerThree) == 2)):
             print("Helyes válasz!")
             correctAnswers += 1
         #Ha nem a helyes válasz betűjelét adja meg mikor a helyes válasz volna megadja mi lenne a helyes válasz és tovább megyünk
         elif ((len(CorrectAnswerThree) == 2)) and not((userAnswer == 3)):
             print("A helyes válasz a 3-as lett volna")


         #Meg nézzük hogy a felhasználó által adott válasz egyenlő-e a helyes válasszal
         elif (userAnswer == 4) and ((len(CorrectAnswerFour) == 2)):
             print("Helyes válasz!")
             correctAnswers += 1
         #Ha nem a helyes válasz betűjelét adja meg mikor a helyes válasz volna megadja mi lenne a helyes válasz és tovább megyünk
         elif ((len(CorrectAnswerFour) == 2)) and not((userAnswer == 4)):
             print("A helyes válasz a 4-as lett volna")
         #Ha a válasz hibás de valami véletlen tönkre ment ez fog meg jelleni

         elif ((userAnswer == 0)) and (len(CorrectAnswerOne ) != 2 or len(CorrectAnswerTwo ) != 2 or len(CorrectAnswerThree ) != 2 or len(CorrectAnswerFour ) != 2):
             print("Helyes válasz!")
             correctAnswers += 1
         elif (userAnswer != 0) and (len(CorrectAnswerOne ) != 2 or len(CorrectAnswerTwo ) != 2 or len(CorrectAnswerThree ) != 2 or len(CorrectAnswerFour ) != 2):
             print("Egyik sem a helyes válasz! (Vagyis a 0)")
         
         else:
             print("Rossz válasz!")
    def Difficulty():
        global numberOfQuestions
        warning = "\n Figyelmeztetés! \n  A helyes válaszokat 0-4-ig lehet választani, a 0 arra utal ha nincs helyes válasz!\n"
        difficulty = " 1) Nagyon Könnyű (10) \n 2) Könnyű (20) \n 3) Közepes (30) \n 4) Nehéz (50) \n 5) Ultra Nehéz (100) \n 6) Halál mod (200) \n 7) Egyéb"
        print(warning)
        difficultyDisplay = print(difficulty)
        difficultyChoosing = int(input("Válassz egy nehézséget (1-7): "))
        while (difficultyChoosing > 7) or (difficultyChoosing < 0):
            difficultyChoosing = int(input("Válassz egy nehézséget (1-7): "))
        if difficultyChoosing == 1:
            numberOfQuestions = 10
        elif difficultyChoosing == 2:
            numberOfQuestions = 20
        elif difficultyChoosing == 3:
            numberOfQuestions = 30
        elif difficultyChoosing == 4:
            numberOfQuestions = 50
        elif difficultyChoosing == 5:
            numberOfQuestions = 100
        elif difficultyChoosing == 6:
            numberOfQuestions = 200
        elif difficultyChoosing == 7:
            numberOfQuestions = int(input("Hány kérdéssel akarsz játszani?: "))
        else:
            print("Rossz")
    #Kérdés/Válaszok helyének kiolvasására felyügyelő számok
    quest = 0
    answerOne = 1
    answerTwo = 2
    answerThree = 3
    answerFour = 4

    Difficulty()
    SplitCorrection()
    FinalCorrection()
    #For loop ami végig megy az összes kérdésen és ahoz tartozó válaszon majd kiírja őket
    for q in range(1, numberOfQuestions + 1):
        #Meg nyitja a kivánt txt file-t
        with open(txtName, "r", encoding="utf8") as x:
            #Ki olvassa a txt file sorait
            lines = x.readlines()
            CorrectAnswerOne = lines[answerOne].split("@")
            CorrectAnswerTwo = lines[answerTwo].split("@")
            CorrectAnswerThree = lines[answerThree].split("@")
            CorrectAnswerFour = lines[answerFour].split("@")
            print("\n")
            print("Question "+str(q)+": ", lines[quest]) #lines[quest] a kérdés sorára utal melyet kiír a program
            print("A1: ", CorrectAnswerOne[0].replace("\n", "")) #lines[answerOne/Two/Three/Four] a válasz(ok) sorára utal melyet kiír a program
            print("A2: ", CorrectAnswerTwo[0].replace("\n", ""))
            print("A3: ", CorrectAnswerThree[0].replace("\n", ""))
            print("A4: ", CorrectAnswerFour[0].replace("\n", ""))
            print("\n")
            
            AnswerCheck()
            
            #Megáll egy 1s-re
            time.sleep(1)
            #Megnöveljük a kérdések/válaszok számát
            quest += 6 
            answerOne += 6
            answerTwo += 6
            answerThree += 6
            answerFour += 6

    #A quiz végén kiírjuk hány helyes válaszod van
    print("\n")
    print("Helyes válaszok száma:", correctAnswers,"/",numberOfQuestions)
    #Meg kérdezi akarsz-e ujra játszani
    restart = str(input("Akarsz újra játszani?: "))
    #Szimpla while loop ami nézi hogy a válasz igen vagy sem ha a válasz nem igen vagy nem vissza dobja azt hogy Igen-t vagy nem-et kell megadni
    while (restart != "igen" ) or (restart != "Igen"):
        if (restart == "igen") or (restart == "Igen"):
            Quiz()
        #Ha a válas nem kilép a programból
        elif (restart == "nem") or (restart == "Nem"):
            print("Találkozunk késöbb")
            time.sleep(5)
            exit()
        print('Hiba, kérem adjon meg helyes választ "Igen" vagy "Nem"!')
        time.sleep(1)
        restart = str(input("Akarsz újra játszani?: "))       
#Szipla quiz készitő funciton
def QuizMaker():
    quest = 0
    answerOne = 1
    answerTwo = 2
    answerThree = 3
    answerFour = 4
    txtfile = str(input("Adja meg a kivánt txt file nevét (Ez tartja majd a kérdéseket!): "))

    while True:
        with open(txtfile + ".txt", "a", encoding="utf8") as x:
            x.write(str(input("Adjon meg egy kérdést: ")))
            x.write("\n")
            x.write(str(input("Adja meg az első választ a kérdésre: ")))
            x.write("\n")
            x.write(str(input("Adja meg az második választ a kérdésre: ")))
            x.write("\n")
            x.write(str(input("Adja meg az harmadik választ a kérdésre: ")))
            x.write("\n")
            x.write(str(input("Adja meg az negyedik választ a kérdésre: ")))
            for newline in range(2):
                x.write("\n")
            print("Kérdés sikeresen hozzáadva!")

        check = str(input("Szerednéd le ellenőrizni?: "))
        if check == "igen":
                with open(txtfile + ".txt", "r", encoding="utf8") as x:
                    lines = x.readlines()
                    print("\n")
                    print(lines[quest])
                    print(lines[answerOne])
                    print(lines[answerTwo])
                    print(lines[answerThree])
                    print(lines[answerFour])
                    time.sleep(1)
        else:
            print("ok")

# első kérdés meg kérdezi kezdhetünk-e
question = str(input("Kezdhetünk?: "))

#Szimpla while loop ami nézi hogy a válasz igen vagy sem ha a válasz NEM igen vagy nem vissza dobja azt hogy Igen-t vagy nem-et kell megadni
while (question != "igen" ) or (question != "Igen"):
    #Ha a válasz IGEN a program tovább halad a következő kérdésre
    if (question == "igen") or (question == "Igen"):

        #Ha igent választunk megkérdezi quiz-t akrunk csinálni vagy az eleve megcsinált quiz-t játszani
        question2 = int(input("Quizt irnál vagy probálnál? (1 / 2): "))
        while (question2 != 1) or (question2 != 2):
            #Elindítja a Quiz készitő programot ha a válasz 1
            if question2 == 1:
                #Quiz készítő
                QuizMaker()
            #Elindítja a Quiz programot ha a válasz 2
            elif question2 == 2:
                #Quiz Játék
                Quiz()
            #Ha a válasz question 2-re nem 1 vagy 2 vissza dobja a kérdést
            else:
                print("Adjon meg egy valid számot 1 és 2 között")
                question2 = int(input("Quizt irnál vagy probálnál? (1 / 2): "))

    #Ha a válasz NEM kilép a programból
    elif (question == "nem") or (question == "Nem"):
        print("Találkozunk késöbb")
        time.sleep(5)
        exit()

    #Hiba üzenet ami meg ami megszabja hogy igen-t vagy nem-et adj meg + vissza dobja a kérdést hogy müködjön a while loop 
    print('Hiba, kérem adjon meg helyes választ "Igen" vagy "Nem"!')
    time.sleep(1)
    question = str(input("Kezdhetünk?: "))