import time
def Quiz():
    #Megadott név amiből kiolvassa a kérdéseket
    txtName = "PythonQuizQuestion.txt"
    #Kérdés/Válaszok helyének kiolvasására felyügyelő számok
    quest = 0
    answerOne = 1
    answerTwo = 2
    answerThree = 3
    answerFour = 4
    #Heyles válaszok számát jelölő érték
    correctAnswers = 0
    #Kérdések száma amenyit le akarsz futtatni
    numberOfQuestions = int(input("Hány kérdéssel akarna játszani?: "))
    
    
    #For loop ami végig megy az összes kérdésen és ahoz tartozó válaszon majd kiírja őket
    for q in range(1, numberOfQuestions + 1):
        #Meg nyitja a kivánt txt file-t
        with open(txtName, "r", encoding="utf8") as x:
            #Ki olvassa a txt file sorait
            lines = x.readlines()
            CorrectAnswerOne = lines[answerOne].split()
            CorrectAnswerTwo = lines[answerTwo].split()
            CorrectAnswerThree = lines[answerThree].split()
            CorrectAnswerFour = lines[answerFour].split()
            print("\n")
            print("Question " + str(q) + ": ", lines[quest]) #lines[quest] a kérdés sorára utal melyet kiír a program
            print("A1: ", CorrectAnswerOne[0]) #lines[answerOne/Two/Three/Four] a válasz(ok) sorára utal melyet kiír a program
            print("A2: ", CorrectAnswerTwo[0])
            print("A3: ", CorrectAnswerThree[0])
            print("A4: ", CorrectAnswerFour[0])

            #Megkéri a felhasználót hogy adjon meg egy számot ami egyezik a válasz számával
            userAnswer = int(input("Adja meg a helyes válasz számát: "))
            #Meg nézzük hogy a felhasználó által adott válasz egyenlő-e a helyes válasszal
            
            if (userAnswer == 1) and (CorrectAnswerOne[1]):
                print("Helyes válasz!")
                #+1 a helyes pont
                correctAnswers += 1
            #Ha nem a helyes válasz betűjelét adja meg mikor a helyes válasz volna megadja mi lenne a helyes válasz és tovább megyünk
            elif (CorrectAnswerOne[1].__contains__("*")) and not((userAnswer == 1)):
                print("A helyes válasz a 1-as lett volna")

            #Meg nézzük hogy a felhasználó által adott válasz egyenlő-e a helyes válasszal
            elif (userAnswer == 2) and (CorrectAnswerTwo[1].__contains__("*")):
                print("Helyes válasz!")
                correctAnswers += 1
            #Ha nem a helyes válasz betűjelét adja meg mikor a helyes válasz volna megadja mi lenne a helyes válasz és tovább megyünk
            elif not((userAnswer == 2)):
                for i in range(len(CorrectAnswerTwo)):
                    if (CorrectAnswerTwo[i].__contains__("*")) and not((userAnswer == 2)):
                        print("A helyes válasz a 2-as lett volna")

            #Meg nézzük hogy a felhasználó által adott válasz egyenlő-e a helyes válasszal
            elif (userAnswer == 3) and (CorrectAnswerThree[1]):
                print("Helyes válasz!")
                correctAnswers += 1
            #Ha nem a helyes válasz betűjelét adja meg mikor a helyes válasz volna megadja mi lenne a helyes válasz és tovább megyünk
            elif (CorrectAnswerThree[1].__contains__("*")) and not((userAnswer == 3)):
                print("A helyes válasz a 3-as lett volna")

            #Meg nézzük hogy a felhasználó által adott válasz egyenlő-e a helyes válasszal
            elif (userAnswer == 4) and (CorrectAnswerFour[1]):
                print("Helyes válasz!")
                correctAnswers += 1
            #Ha nem a helyes válasz betűjelét adja meg mikor a helyes válasz volna megadja mi lenne a helyes válasz és tovább megyünk
            elif (CorrectAnswerFour[1].__contains__("*")) and not((userAnswer == 4)):
                print("A helyes válasz a 4-as lett volna")
            #Ha a válasz hibás de valami véletlen tönkre ment ez fog meg jelleni
            else:
                print("Rossz válasz!")
            
            #Megáll egy 1s-re
            time.sleep(1)
            #Megnöveljük a kérdések/válaszok számát
            quest += 6 
            answerOne += 6
            answerTwo += 6
            answerThree += 6
            answerFour += 6

    #A quiz végén kiírjuk hány helyes válaszod van
    print("Helyes válaszok száma:", correctAnswers ,"/100")
    #Meg kérdezi akarsz-e ujra játszani
    restart = str(input("Akarsz újra játszani?: "))
    #Szimpla while loop ami nézi hogy a válasz igen vagy sem ha a válasz nem igen vagy nem vissza dobja azt hogy Igen-t vagy nem-et kell megadni
    while (question != "igen" ) or (question != "Igen"):
        if (question == "igen") or (question == "Igen"):
            Quiz()
        #Ha a válas nem kilép a programból
        elif (question == "nem") or (question == "Nem"):
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