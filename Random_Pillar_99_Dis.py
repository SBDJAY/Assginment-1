import random
import time
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Level 1
def displayThe_Throne_World():
    print("\033[1;36;40m\n")  #Ghost Dialogue
    print("You have just enetered Savathun's Throne World")
    time.sleep(3)
    print('From here you will have to find the way to the Pyrmaid ship to defeat the Witness')
    time.sleep(3)
    print("I think the way to the Pyramid ship is right past Savathun right there, but your gonna have to defeat her to get through")
    time.sleep(3)
    print("Try stadning on a certain pillar maybe that will take down her sheilds, that will give us the perfect window to attack")
    time.sleep(3)
    print()

def choosePillar():
    pillar = ""
    while pillar != "Darkness" and pillar != "Tower": # input validation
        pillar = input("Choose a Pillar to stand on(Darkness   Tower): ")

    return pillar

correctPillar = ['Darkness', "Tower"]
correctPillar = random.choice(correctPillar)

def checkSavathun_The_Witch_Queen(chosenPillar):
    print("\033[1;36;40m\n")  #Ghost Dialogue
    print('It seems to me that this is a test from The Witness')
    time.sleep(2)
    print()
    print("\033[1;31;40m\n")#Enemy Dialogue
    print('The Witness has seen your offering...')
    time.sleep(2)
    print()

    answerCorrect = False
    gaurdianHealth = 100
    while not answerCorrect and gaurdianHealth > 0:

        if chosenPillar == str(correctPillar):
            print('"\033[1;31;40m\n"') #Enemy Dialogue
            print('The Witness accepts your offering....')
            time.sleep(3)
            print()
            print("\033[1;36;40m\n") #Ghost Dialogue
            print('Eyes up Gaurdian, the witness accepted your offering, Savathun is unproteceted we can take her down NOW!')
            answerCorrect = True
            print()
        
            displayThe_Pyramid()
            choice = choosePillar()
            checkThe_Obelisk(choice)

        elif chosenPillar != str(correctPillar):
            print("\033[1;31;40m\n") #Enemy Dialogue
            print('the witness does not accept your offering')

            if gaurdianHealth > 0 and chosenPillar != str(correctPillar):
                print("\033[1;36;40m\n") #Ghost Dialogue
                print("Try giving another offering, no point in stopping here")
                gaurdianHealth -= 10
                print('Your reslience decreased to ' + str(gaurdianHealth))
                choosePillar()
            
            elif gaurdianHealth <= 1:
                print("\033[1;31;40m\n") #Enemy Dialogue
                print('the witness does not accept your offering')
                time.sleep(1)
                print('The Darkness Consumes you')


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Level 2
def displayThe_Pyramid():
    print("\033[1;36;40m\n")  #Ghost Dialogue
    print("Great Work Gaurdian you have defeated Savathun for now, I would not be supprised if she ha some trick up her sleeve,")
    time.sleep(1)
    print("But lets not have that get in the way of the mission at hand")
    time.sleep(1)
    print("Now that we are in the Pyramid my scanners are reading some sort of obelisk maybe we try to interact with the same way, let me get more data on the surrounding area too...")
    time.sleep(2)
    print()
    print("\033[1;31;40m\n")#Enemy Dialogue
    print("Child of the light Excel in this next test and the answers you are looking for will be found, or maybe you already have the answers then I can help you open your eyes...")
    time.sleep(2)
    print("\033[1;36;40m\n")  #Ghost Dialogue
    print("Well I activated the obelisk act fast gaurdian the same pillars have jsut re-appeared select one fast")
    time.sleep(2)
    print()

def checkThe_Obelisk(chosenPillar):
    print("\033[1;36;40m\n")  #Ghost Dialogue
    print("Well Warlock it was pretty easy the fist time around give the pillars another go...")
    print("Lets just hope we dont find out if we stand on the wrong pillar")
    time.sleep(2)
    print()
    print("\033[1;31;40m\n")#Enemy Dialogue
    print("Child of the light we have seen your offering lets see if your worthy of our services")
    time.sleep(2)
    print()

    correctPillar = ["Darkness", "Tower"]
    correctPillar = random.choice(correctPillar)

    answerCorrect = False
    gaurdianHealth = 80
    while not answerCorrect and gaurdianHealth > 0:

        if chosenPillar == str(correctPillar):
            print('"\033[1;31;40m\n"') #Enemy Dialogue
            print('The Witness accepts your offering....')
            time.sleep(3)
            print()
            print("\033[1;36;40m\n")  #Ghost Dialogue
            print('Gaurdian you did, that was a lot more easier than expected')
            time.sleep(1)
            print("A large door has opened and based of my scanner, There are some enemies coming ahead and these are not the tye we have face before, Stay vigalent and ready")
            answerCorrect =True
        
            displayThe_Acquisition()
            choice = choosePillar()
            checkThe_CareTaker(choice)

        elif chosenPillar != str(correctPillar):
            print("\033[1;31;40m\n") #Enemy Dialogue
            print('the witness does not accept your offering')

            if gaurdianHealth > 0 and chosenPillar != str(correctPillar):
                print("\033[1;36;40m\n") #Ghost Dialogue
                print("Try giving another offering, no point in stopping here")
                gaurdianHealth -= 10
                print('Your reslience decreased to ' + str(gaurdianHealth))
                choosePillar()

        elif gaurdianHealth <= 1:
            print("\033[1;31;40m\n") #Enemy Dialogue
            print('the witness does not accept your offering')
            time.sleep(1)
            print("The Oblelisk Proceeds to spin and orange beams begin to shoot out, red fog apears and you are consumed by the Darkness")
            print()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Level 3
def displayThe_Acquisition():
    print("\033[1;36;40m\n") #Ghost Dialogue
    print("Gaurdian, Big guy up ahead, looks like a Scron Ogre, but the Darkness have made it there own...")
    time.sleep(2)
    print("This place its fille with items and relics i have never scene before, and so many obelisks...")
    time.sleep(1)
    print("it looks like hes ignoring us I guess if i activate one of these obelisks again maybe we can take out the Ogre and get to the witness")
    print()
    print("\033[1;31;40m\n") #Enemy Dialogue
    print("Gaurdian, what is it really that you seek if it is not answers then is it our death, why is it that you seek something of the sort have we not made it clear we are your salvation")
    time.sleep(2)
    print("If it is death that you seek then it is Death that you will get...")
    print()
    print("\033[1;36;40m\n") #Ghost Dialogue
    print("Gaurdian I dont think the Witness is happy with us being here anymore, lets show this Ogre our titan strength and make are way to the witness!!!")

def checkThe_CareTaker(chosenPillar):
    print("\033[1;36;40m\n")  #Ghost Dialogue
    print("Alright Gaurdian this time we got to do alot of damage to that Caretaker,all we have to do is guess the right pillars, should be easy...")
    time.sleep(2)
    print()
    print("\033[1;31;40m\n")#Enemy Dialogue
    print("The offering has been recieved...")
    time.sleep(2)
    print()

    correctPillar = ["Darkness", "Tower"]
    correctPillar = random.choice(correctPillar)

    answerCorrect = False
    gaurdianHealth = 80
    while not answerCorrect and gaurdianHealth > 0:

        if chosenPillar == str(correctPillar):
            print('"\033[1;31;40m\n"') #Enemy Dialogue
            print('The Offering has been accpeted A Pool of Darkness has opened....')
            time.sleep(3)
            print()
            print("\033[1;31;40m\n") #Ghost Dialogue
            print('Great work Gaurdian, now lay down some lead')
            time.sleep(1)
            print()

            displayThe_Dominion()
            choice = choosePillar()
            checkRhulk_Disciple_Of_The_Witness(choice)

        elif chosenPillar != str(correctPillar):
            print("\033[1;31;40m\n") #Enemy Dialogue
            print('the witness does not accept your offering')

            if gaurdianHealth > 0 and chosenPillar != str(correctPillar):
                print("\033[1;36;40m\n") #Ghost Dialogue
                print("Try giving another offering, no point in stopping here")
                gaurdianHealth -= 10
                print('Your reslience decreased to ' + str(gaurdianHealth))
                choosePillar()

        elif gaurdianHealth <= 1:
            print("\033[1;31;40m\n") #Enemy Dialogue
            print('the witness does not accept your offering')
            time.sleep(1)
            print("*The Caretaker lifts its arm into the air orange constructs spin in the air plumetting and exploding when in contact of you, your are then consumed by the darkness...")
            print()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Final Level 
def displayThe_Dominion():
    print("\033[1;31;40m\n") #Enemy Dialogue
    print('Child of the light, You come come into our chambers, dispose of our Caretaker, and our what we give you was not enough...')
    print('Foolish creatures being mislead by the traveler Rhulk will dispose of you know or you can give yourselves to the Darkness')
    print("\033[1;36;40m\n")  #Ghost Dialogue
    print("Gaurdian this is not looking good at all like, this could be the end of us...")
    time.sleep(1)
    print("But dont let that get to your head, If we defeat Rhulk we can gain the knowlege we need and get on step closer to stop the Witness")
    time.sleep(1)
    print("Go get em Gaurdian!!!")

def checkRhulk_Disciple_Of_The_Witness(chosenPillar):
    print("\033[1;36;40m\n")  #Ghost Dialogue
    print("This is not our first Rodeo get the irght pillar and hit them where it hurts")
    time.sleep(2)
    print()
    print("\033[1;31;40m\n")#Enemy Dialogue
    print("The offering has been recieved...")
    time.sleep(2)
    print()

    correctPillar = ['Darkness', 'Tower']
    correctPillar = random.choice(correctPillar)

    answerCorrect = False
    gaurdianHealth = 80
    while not answerCorrect and gaurdianHealth > 0:

        if chosenPillar == str(correctPillar):
            print('"\033[1;31;40m\n"') #Enemy Dialogue
            print('The Offering has been accpeted Rhulk sheilds have been lowered....')
            time.sleep(3)
            print()
            print("\033[1;31;40m\n") #Ghost Dialogue
            print('This is it gaurdian, push yourself to the limit, and then we can get on out of here')
            time.sleep(1)
            print()

            finalMessage()

        elif chosenPillar != str(correctPillar):
            print("\033[1;31;40m\n") #Enemy Dialogue
            print('the witness does not accept your offering')

            if gaurdianHealth > 0 and chosenPillar != str(correctPillar):
                print("\033[1;36;40m\n") #Ghost Dialogue
                print("Try giving another offering, no point in stopping here")
                gaurdianHealth -= 10
                print('Your reslience decreased to ' + str(gaurdianHealth))
                choosePillar()

        elif gaurdianHealth <= 1:
            print("\033[1;31;40m\n") #Enemy Dialogue
            print('the witness does not accept your offering')
            time.sleep(1)
            print("You have failed Gaurdian Neither The light or any oher Gaurdians can save you know, you have forsakened yourself, only you...")
            time.sleep(1)
            print('* Rhulk lifts his axe made of the constructs of Darkness and in one sweeping blow strips of any life and any trace of your existacne you have been consumed by the darkness...')
            print('DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN DROWN')
            print()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Final Message

def finalMessage():
    print("\033[1;36;40m\n") #Ghost Dialogue
    print('Gaurdain you did what no other gaurdian has been capable of doing before, you wilol be writtien in histroy books of how you single handedly ran into a pyramid and defeated everything in you path')
    print('Well Gaurdain go collect your plunder and head on home, this is jsut the beginning of a long, long war against the Darkness')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Call
