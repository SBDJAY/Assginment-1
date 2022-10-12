#-----------------------------------------------------------
# Pyramid Raid
# Daniel Pius
# Muhammad Asif
# Class: 1229_4013: Programming Principles
# October 7th 2022
#-----------------------------------------------------------
import Warlock
import Hunter
import Titan
import Random_Pillar_50_Dis
import Random_Pillar_75_Dis
import Random_Pillar_99_Dis
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Intro/Gaurdian Selction
def intro():
    print("\033[1;36;40m\n") #Ghost Dailogue
    print("Gaurdaian we have a big mission ahead of us, Scanners on the tower have been going off near Savathuns Throne World, our scanners showed a signal from a Pyramid ship and unexplaid anomolys")
    print("Your tasked wih investigating the contetns of the pyramid ship aswell as the anomoly")
    print("This is the first time any gaurdain has been tasked with investigatting a pyramid ship let alone going in completly blind")
    print("You can choose between three diffrent builds to get you all preped for the fight ahead of you ")

    print("\033[1;32;40m\n") #Menu Text
    print('Warlock - Resilience: 80   Discipline: 99')
    print('Hunter - Resilience: 95    Discipline: 75')
    print('Titan - Resilience: 115    Discipline: 50')

def game():
    subclass = input('Choose a Subclass ')
    print('You have chosen: ', subclass )  
        
    if subclass == 'Warlock':
        subclass = Warlock
        playAgain = "yes"
    while playAgain == "yes":
        Random_Pillar_99_Dis.displayThe_Throne_World()
        choice = Random_Pillar_99_Dis.choosePillar()
        Random_Pillar_99_Dis.checkSavathun_The_Witch_Queen(choice)
    playAgain = input("Your Light Fades away do you want to play again? (yes to continue playing): ")

    if subclass == 'Hunter':
        subclass = Hunter
        playAgain ="yes"
    while playAgain == "yes":
        Random_Pillar_75_Dis.displayThe_Throne_World()
        choice = Random_Pillar_75_Dis.choosePillar()
        Random_Pillar_75_Dis.checkSavathun_The_Witch_Queen(choice)
    playAgain = input("Your Light Fades away do you want to play again? (yes to continue playing): ")
        
    if subclass == 'Titan':
        subclass = Titan
        playAgain ="yes"
    while playAgain == "yes":
        Random_Pillar_50_Dis.displayThe_Throne_World()
        choice = Random_Pillar_50_Dis.choosePillar()
        Random_Pillar_50_Dis.checkSavathun_The_Witch_Queen(choice)
    playAgain = input("Your Light Fades away do you want to play again? (yes to continue playing): ")


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Class
intro()
game()