'''Create a program capable of displaying questions to the user like KBC.
USE List Datatype to store the questions and their correct answers.
Display the final amount the person is taking home after playing the game
'''
Questions=["What is the name of your Grandfather's father ?","What is the name of your Grandfather's mother ?"]
Answers=[["A.Banamali B.Banabasi c.Bandhutwa D.Bandhuta",],["A.Srimasi B.Srimati c.Srimattwa D.Srimata",]]
bankbalance=0
for i in range(2):
    print(Questions[i])
    print(Answers[i])
    ans=input("Submit answer: ")
    if i==0 and (ans=='A' or ans=='a'):
        print("Sahi Jawab,1crore")
        bankbalance+=10000000
        print("You have won Rupees",bankbalance,"Answer next questions")
    elif i==1 and (ans=='B' or ans=='b'):
        print("Sahi Jawab,1crore")
        bankbalance+=10000000
        print("You have won Rupees",bankbalance,"Answer next questions")
    else:
        print("Apne kosish Achi kithi,par Galat Jawab! \nAur aapko bahat dukh se bankbalance",bankbalance,"rupayee ke sath biday de rahe hein.")    
        break    
        