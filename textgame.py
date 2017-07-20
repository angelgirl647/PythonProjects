def question5():
    answer5=input("What kind of computer are we using? a.Microsoft Windows LATITUDE E7340 b.Microsoft Windows Version 6.1.7601 c.Microsoft Windows Version 7.2.9042")
    if answer5 == "b" or answer5== " b" or answer5=="B" or answer5==" B":
        print("Congrats. You're as smart as we are. Join the club.")

    else:
        print("YEP.You're an idiot. GAME OVER!!!")
        exit()

def question4():
    answer4=input("What is an informal language that has no syntax rules and is not meant to be compiled or executed called?")
    if answer4 == "pseudocode" or answer4 == " pseudocode" or answer4=="Pseudocode" or answer4==" Pseudocode":
        print("Good one. On to the next question.")
        question5()
    else:
        print("You're an idiot. GAME OVER!!!")
        exit()

def question3():
    answer3=input("How do you write a for-loop formula using x as a variable in Python?")
    if answer3 == "for x in range(x)" or answer3== " for x in range(x)":
        print("Phew. That was hard.")
        question4()
    else:
        print("You're an idiot. GAME OVER!!!")
        exit()

def question2():
    answer2=input("What is default message for the 'think ___ for _ seconds' in Scratch? a.hello b.hmm... c.hmmm")
    if answer2 == "b" or answer2==" b" or answer2=="B" or answer2==" B" or answer2=="hmm..." or answer2==" hmm...":
        print("Pure Luck")
        question3()
    else:
        print("You're an idiot. GAME OVER!!!")
        exit()

def question1():
    answer1=input("What represents a line of text, a character, or a number and can change throughout a program? a.variable b.constant c.string")
    if answer1 == "a" or answer1==" a" or answer1=="A" or answer1==" A" or answer1=="variable" or answer1==" variable" or answer1=="a.variable" or answer1==" a.variable":
        print("You're a smart fellah :)")
        question2()
    else:
        print("You're an idiot. GAME OVER!!!")
        exit()

start = input("Can you outsmart us?")
if start == "Yes" or start == "yes" or start=="YES":
    print("We'll see about that")
    question1()
else:
    print("GAME OVER!!!")
    exit()





