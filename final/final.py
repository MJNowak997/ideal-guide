'''
Madeline Nowak
7/18/2025
Program: Hangman
Algorithm: 
generate random word from list
have player guess letters
if incorrect, hang man
'''


import random
import words
#imported random(Python) and words(local)

noose = "    ___________\n   |           |\n               |\n               |\n               |\n               |\n               |\n   ____________|"
head = "    ___________\n  _|_          |\n |___|         |\n               |\n               |\n               |\n               |\n   ____________|"
torso = "    ___________\n  _|_          |\n |___|         |\n   |           |\n   |           |\n   |           |\n               |\n   ____________|"
larm = "    ___________\n  _|_          |\n |___|         |\n __|           |\n   |           |\n   |           |\n               |\n   ____________|"
rarm = "    ___________\n  _|_          |\n |___|         |\n __|__         |\n   |           |\n   |           |\n               |\n   ____________|"
lleg = "    ___________\n  _|_          |\n |___|         |\n __|__         |\n   |           |\n  _|           |\n |             |\n   ____________|"
rleg = "    ___________\n  _|_          |\n |___|         |\n __|__         |\n   |           |\n  _|_          |\n |   |         |\n   ____________|"
#created lineart for each Hangman step

stages = [noose, head, torso, larm, rarm, lleg, rleg]
#put hangman stages in order so cna be numbered

answer = random.choice(words.words)
#chose a random word from words

stage = 0
written = "_"
guesses = []
ovscore = 0
#defined overarching variables

def guess():
    global guesses
    global written
    global rorw
    #used global variables for above 
    choice = input("Your guess: ")
    if choice in guesses:
        print("You already guessed that. Try again!")
        rorw = True
        #repeat guesses won't be penalized
    elif choice in answer:
        guesses = guesses + [choice]
        sofar = ""
        for letter in answer:
            if letter in guesses:
                sofar += letter
                sofar += " "
            else:
                sofar += "_ "
        print(sofar)
        written = sofar
        rorw = True
        #changes blanks to correct guess and adds correct guess to guess list
    else:
        sofar = ""
        for letter in answer:
            if letter in guesses:
                sofar += letter
                sofar += " "
            else:
                sofar += "_ "
        guesses = guesses + [choice]
        print(f"Nope!\n {sofar}")
        rorw = False
        #shows current blanks/correct guesses and adds incorrect guess to guess list

def game():
    global guesses
    global written
    global stage
    global rorw
    global win
    print("Welcome to Hangman!\nLet's get started.")
    for letter in answer:
        print("_", end=" ")
    print(f"\n{noose}\n")
    #start game
    guess()
    #first guess
    if rorw is False:
            stage = stage + 1
            print(stages[stage])
            win = False
    if rorw is True:
            print(stages[stage])
            win = False
    #if right or wrong (rorw) is false(incorrect guess), hangs man
    #if right or wrong (rorw) is true(correct guess), shows progress
    while "_" in written:
    #if any letters unguessed, keep looping
        guess()
        if rorw is False:
            stage = stage + 1
            print(stages[stage])
            win = False
        #see line 76
        if stage == 6:
            print("Game Over.")
            guesses = []
            stage = 0
            win = False
            break
        #if guesses used up, ends game
        if rorw is True:
            print(stages[stage])
            win = False
        #see line 77
    else:
        print("You Win!")
        guesses = []
        stage = 0
        win = True
    #if no more blanks and didn't fail, win

def playagain():
    global ovscore
    pscore = 0
    oncemore = input("Would you like to play again? y/n\n")
    #play again function
    if oncemore == "y":
        main()
    #if yes, play again
    elif oncemore == "n":
        print("Thanks for playing!")
        prevsb = input("Have you played this game before? y/n \n")
        if prevsb == "y":
            with open("scoreboard.txt", "r") as oscore:                          
                pscore = int(oscore.read().strip())                        
            oscore.close()
            print("Scoreboard Found.")
        #if scoreboard from old game exists, get it's total
        if prevsb == "n":
            pscore = 0
            print("Scoreboard Created.")
        #if no old scoreboard, previous total = 0
        fscore = ovscore + pscore
        #add previous and new scores
        scoreboard = open("scoreboard.txt", "w")
        scoreboard.write(str(fscore))
        scoreboard.close()
        print("Scoreboard Updated.")
    #if no more, tally score and record
    else:
        print("Invalid input.")
        pscore = 0
        print("Overwriting Scoreboard.")
        fscore = ovscore + pscore
        scoreboard = open("scoreboard.txt", "w")
        scoreboard.write(str(fscore))
        scoreboard.close()
        print("New Scoreboard Created.")
    #if invalid input, tally score and record, old score lost, but no errors

def main():
    global answer
    answer = random.choice(words.words)
    game()
    #play
    global ovscore
    if win is True:
        ovscore = ovscore + 1
    #if win, add to score
    playagain()

main()


def testcorrect():
    global guesses, stage   
    assert guesses == []
    assert stage == 0
    print("Test Passed.")
#tests that everything reset correctly

testcorrect()
#run the tests