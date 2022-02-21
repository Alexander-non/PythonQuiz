import time
import datetime
import random
#Megadott név amiből kiolvassa a kérdéseket
txtName = "PythonQuizQuestion.txt"
correctAnswers = 0
numberOfQuestions = 0
maxNumberOfQuestions = 0
firstRun = True

def Documenting(UsageMode, FirstElement, SecondElement, ThierdElement, FourthElement):
    txtDocumentingName = "naplozás.txt"
    #Quiz mód választás naplózása
    if UsageMode == 2:
        with open(txtDocumentingName, "a", encoding="utf8") as b:
            if FourthElement == 2:
                FourthElement = "Quiz Játék"
            else:
                FourthElement = "Quiz készítés"
            b.write("A felhasználó által választott mód: {} \n".format(FourthElement))
    #Elkezdés naplózása
    elif UsageMode == 3:
        with open(txtDocumentingName, "a", encoding="utf8") as b:
            b.write("A felhasználó elkezdte a Quiz-t: {} \n".format(datetime.datetime.now().strftime("%c")))
    #Nehézségi mód és kérdések számának naplózása
    elif UsageMode == 4:
        with open(txtDocumentingName, "a", encoding="utf8") as b:
            b.write("A felhasználó által választott nehézségi mód: {} \n".format(FirstElement))
            b.write("A felhasználó által kért kérdések száma: {} \n".format(SecondElement))
    #Újra kezdés naplózása
    elif UsageMode == 5:
        with open(txtDocumentingName, "a", encoding="utf8") as b:
            b.write("A felhasználó újra kezdte a Quiz-t: {} \n".format(datetime.datetime.now().strftime("%c")))
def Quiz():
    def SplitCorrection():
        # opening the file in read mode
        with open(txtName, "r", encoding="utf8") as x:
            replacement = ""
            # using the for loop
            for line in x:
                line = line.strip()
                changes = line.replace("*", "@*")
                replacement = replacement + changes + "\n"
        # opening the file in write mode
        with open(txtName, "w", encoding="utf8") as y:
            y.write(replacement)
    def FinalCorrection():
        # opening the file in read mode
        with open(txtName, "r", encoding="utf8") as x:
            replacement = ""
            # using the for loop
            for line in x:
                line = line.strip()
                changes = line.replace("@@", "@")
                replacement = replacement + changes + "\n"
        # opening the file in write mode
        with open(txtName, "w", encoding="utf8") as y:
            y.write(replacement)
    def AnswerCheck():
        getPoints = True
        canContinue = False
        notCorrect = 0
        CorrectAnswerList = [CorrectAnswerOne, CorrectAnswerTwo, CorrectAnswerThree, CorrectAnswerFour]
        Answers = [0,0,0,0,0]
        userAnswer = str(input("Adja meg a helyes válasz számát: ")).split(',')
        #Felhasználó válaszellenőrzés
        while canContinue == False:
            #Leellenőrizzük a felhasználó által adott válasz(oka)t
            for i in range(len(userAnswer)):
                if (int(userAnswer[i]) <= 0) or (int(userAnswer[i]) > 5):
                    userAnswer.clear()
                    userAnswer = str(input("Adja meg a helyes válasz számát: ")).split(',')
                    canContinue = False
                else:
                    canContinue = True
                    #Az "Answers" listának annak a helyére amennyit a felhasználó megadott beÍunk egy 1-t
                    for k in range(len(userAnswer)):
                        Answers[int(userAnswer[k])-1] = 1
        
        global correctAnswers
        for x in range(len(CorrectAnswerList)):
            if len(CorrectAnswerList[x]) == 2:
                if int(Answers[x]) == 1:
                    print("Helyes válasz!")
                else:
                    #Ha nem a helyes válasz betűjelét adja meg mikor a helyes válasz volna megadja mi lenne a helyes válasz és tovább megyünk
                    print("A helyes válasz a {}-es lett volna".format(x+1))
                    getPoints = False
            else:
                notCorrect+=1
                if int(Answers[x]) == 1:
                    getPoints = False
                if notCorrect == 4:
                    if int(Answers[4]) == 1:
                        getPoints = True
                        print("Helyes válasz!")
                    else:
                        print("Egyik sem volt helyes!")
        if getPoints == True:
            #+1 a helyes pont
            correctAnswers += 1
    def Difficulty():
        global numberOfQuestions
        global maxNumberOfQuestions
        global correctAnswers
        correctAnswers = 0
        very_easy = 10
        easy = 20
        medium = 30
        hard = 50
        ultra_hard = 100
        death_mode = 200
        with open(txtName, "r", encoding="utf8") as x:
            lines = x.readlines()
            maxNumberOfQuestions = int((len(lines)+1)/6)

        warning = "\n Figyelmeztetés! \n A helyes válaszokat 1-5-ig lehet választani, az 5-ös arra utal ha nincs helyes válasz!\n"
        difficulty = " 1) Nagyon Könnyű ({}) \n 2) Könnyű ({}) \n 3) Közepes ({}) \n 4) Nehéz ({}) \n 5) Ultra Nehéz ({}) \n 6) Halál mód ({}) \n 7) Egyéb".format(very_easy, easy, medium, hard, ultra_hard, death_mode)
        print(warning + difficulty)
        difficultyChoosing = int(input("Válassz egy nehézséget (1-7): "))
        while (difficultyChoosing > 7) or (difficultyChoosing < 0):
            difficultyChoosing = int(input("Válassz egy nehézséget (1-7): "))
        if difficultyChoosing == 1:
            Documenting(4, "Nagyon Könnyű", very_easy, "", "")
            numberOfQuestions = very_easy
        elif difficultyChoosing == 2:
            Documenting(4, "Könnyű", easy, "", "")
            numberOfQuestions = easy
        elif difficultyChoosing == 3:
            Documenting(4, "Közepes", medium, "", "")
            numberOfQuestions = medium
        elif difficultyChoosing == 4:
            Documenting(4, "Nehéz", hard, "", "")
            numberOfQuestions = hard
        elif difficultyChoosing == 5:
            Documenting(4, "Ultra Nehéz", ultra_hard, "", "")
            numberOfQuestions = ultra_hard
        elif difficultyChoosing == 6:
            Documenting(4, "Halál mód", death_mode, "", "")
            numberOfQuestions = death_mode
        elif difficultyChoosing == 7:
            numberOfQuestions = int(input("Hány kérdéssel akarsz játszani?: "))
            while numberOfQuestions > maxNumberOfQuestions:
                print("Az általad megadott kérdések száma ("+str(numberOfQuestions)+") túl sok.")
                numberOfQuestions = int(input("Hány kérdéssel akarsz játszani?: "))
            Documenting(4, "Egyéb", numberOfQuestions, "", "")
        else:
            print("Hiba történt nehézség választáskor!")
    def Leaderboard(yourScore, scoreablePoints):
        global firstRun
        leaderboardTxtName = "Ranglista.txt"
        file = open(leaderboardTxtName, "a", encoding="utf8")
        fileRead = open(leaderboardTxtName, "r", encoding="utf8")
        usersName = str(input("Meg adja a nevét a ranglistán?: ")).lower()
        while usersName != None:
            if usersName == "igen":
                leaderboardName = str(input("Adja meg a nevét: "))
                break
            elif usersName == "nem":
                leaderboardName = "Ismeretlen"
                break
            else:
                usersName = str(input("Meg adja a nevét a ranglistán?: ")).lower()
        with file as x:
            x.write("{}: {}/{}\n".format(leaderboardName, yourScore, scoreablePoints))

    SplitCorrection()
    FinalCorrection()
    Difficulty()
    #Kérdés/Válaszok helyének kiolvasására felyügyelő számok
    quest = random.randrange(0, (maxNumberOfQuestions*6), 6)
    #Blockolt számok listájának készitése kérdés duplázódás ellen
    BlockedNumbers = []
    BlockedNumbers.append(quest)
    answerOne = quest+1
    answerTwo = answerOne+1
    answerThree = answerTwo+1
    answerFour = answerThree+1
    
    #For loop, ami végig megy az összes kérdésen és ahhoz tartozó válaszon majd kiírja őket
    for q in range(1, numberOfQuestions + 1):
        #Megnyitja a kivánt txt file-t
        with open(txtName, "r", encoding="utf8") as x:
            #Ki olvassa a txt file sorait
            lines = x.readlines()
            CorrectAnswerOne = lines[answerOne].split("@")
            CorrectAnswerTwo = lines[answerTwo].split("@")
            CorrectAnswerThree = lines[answerThree].split("@")
            CorrectAnswerFour = lines[answerFour].split("@")
            print("\n" + str(q) +". Kérdés" + ": ", lines[quest]) #lines[quest] a kérdés sorára utal melyet majd kiír a program
            print("1. Válasz: ", CorrectAnswerOne[0].replace("\n", "")) #Kiírja a válaszok sorainak azt a részét ami csak a válasz részt tartalmazza
            print("2. Válasz: ", CorrectAnswerTwo[0].replace("\n", ""))
            if lines[answerThree].replace("\n", "") == "":
                print("")
            else:
                print("3. Válasz: ", CorrectAnswerThree[0].replace("\n", ""))
            if lines[answerFour].replace("\n", "") == "":
                print("")
            else:
                print("4. Válasz: ", CorrectAnswerFour[0].replace("\n", ""))
            print("\n")
            
            AnswerCheck()
            
            #Megáll egy 1s-re
            time.sleep(1)
            #Megnöveljük a kérdések/válaszok számát 6-tal
            quest = random.randrange(0, (maxNumberOfQuestions*6), 6)
            for w in range(len(BlockedNumbers)):
                if quest == BlockedNumbers[w]:
                    quest = random.randrange(0, (maxNumberOfQuestions*6), 6)
                else:
                    break
            answerOne = quest+1
            answerTwo = answerOne+1
            answerThree = answerTwo+1
            answerFour = answerThree+1        

    #A quiz végén kiírjuk hány helyes válaszod van és hozzá adjuk a felhaználót a ranglistához
    print("\nHelyes válaszok száma: {} / {}".format(correctAnswers, numberOfQuestions))
    Leaderboard(correctAnswers, numberOfQuestions)
    #Meg kérdezi akarsz-e ujra játszani
    restart = str(input("Akarsz újra játszani?: ")).lower()
    #Szimpla while loop ami nézi hogy a válasz igen vagy sem ha a válasz nem igen vagy nem vissza dobja azt hogy Igen-t vagy nem-et kell megadni
    while restart != None:
        if restart == "igen":
            Documenting(5, "", "", "", "")
            Quiz()
        #Ha a válasz nem, akkor kilép a programból
        elif restart == "nem":
            print("Találkozunk később")
            time.sleep(5)
            exit()
        else:
            print('Hiba, kérem adjon meg egy helyes választ: "Igen" vagy "Nem"!')
            time.sleep(1)
            restart = str(input("Akarsz újra játszani?: ")).lower()
#Szipla quiz készitő funciton [NINCS KÉSZ]
def QuizMaker():
    txtfile = str(input("Adja meg a kivánt txt file nevét (Ez tartja majd a kérdéseket!): ")) 
    while True:
        with open(txtfile + ".txt", "a", encoding="utf8") as x:
            print("Tipp: Ha nem akar kérdést megadni csak nyomjon 'Enter'-t.\n Helyes kérdéseket egy csillag '*' megjelölésévek jelezze.")
            x.write(str(input("Adjon meg egy kérdést: ")) + "\n")
            for element in ["első", "második", "harmadik", "negyedik"]:
                x.write(str(input("Adja meg az {} választ a kérdésre: ".format(element))) + "\n")
            x.write("\n")
            print("Kérdés sikeresen hozzáadva!")
        check = str(input("Szerednéd le ellenőrizni?: ")).lower()
        if check == "igen":
            with open(txtfile + ".txt", "r", encoding="utf8") as x:
                lines = x.readlines()
                print("\n")
                for i in range(4): print(lines[i])
                time.sleep(1)
        elif check == "nem":
            check2 = str(input("Szerednél vissza menni a 'kezdőképernyőre?': ")).lower()
            if check2 == "igen":
                question2 = int(input("Quiz-t írnál vagy probálnál? (1 / 2): "))
                while question2 != None:
                    if question2 == 1:
                        Documenting(2, "", "", "", 1)
                        QuizMaker()
                    elif question2 == 2:
                        Documenting(2, "", "", "", 2)
                        Quiz()
            elif check2 == "nem":
                print("Találkozunk később")
                time.sleep(5)
                exit()
        else:
            print('Hiba, kérem adjon meg egy helyes választ: "Igen" vagy "Nem"!')
            check = str(input("Szerednéd le ellenőrizni?: ")).lower()

# első kérdés meg kérdezi kezdhetünk-e
question = str(input("Kezdhetünk?: ")).lower()
#Szimpla while loop ami nézi hogy a válasz igen vagy sem ha a válasz NEM igen vagy nem vissza dobja azt hogy Igen-t vagy nem-et kell megadni
while question != None:
    #Ha a válasz IGEN a program tovább halad a következő kérdésre
    if question == "igen":
        Documenting(3, "", "", "", "")
        #Ha igent választunk megkérdezi quiz-t akrunk csinálni vagy az eleve megcsinált quiz-t játszani
        question2 = int(input("Quiz-t írnál vagy probálnál? (1 / 2): "))
        while question2 != None:
            #Elindítja a Quiz készitő programot ha a válasz 1
            if question2 == 1:
                #Quiz készítő
                Documenting(2, "", "", "", 1)
                QuizMaker()
            #Elindítja a Quiz programot ha a válasz 2
            elif question2 == 2:
                #Quiz Játék
                Documenting(2, "", "", "", 2)
                Quiz()
            #Ha a válasz question 2-re nem 1 vagy 2 vissza dobja a kérdést
            else:
                print("Adjon meg egy érvényes számot 1 és 2 között")
                question2 = int(input("Quiz-t írnál vagy probálnál? (1 / 2): "))
    #Ha a válasz NEM kilép a programból
    elif question == "nem":
        print("Találkozunk később")
        time.sleep(5)
        exit()
    #Hiba üzenet ami meg ami megszabja hogy igen-t vagy nem-et adj meg + vissza dobja a kérdést hogy müködjön a while loop 
    else: 
        print('Hiba, kérem adjon meg egy helyes választ: "Igen" vagy "Nem"!')
        time.sleep(1)
        question = str(input("Kezdhetünk?: ")).lower()
