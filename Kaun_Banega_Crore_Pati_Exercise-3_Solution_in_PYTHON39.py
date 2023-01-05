questions=[
    ["Which language was used to create fb?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create wp?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create yt?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create twtr?","Python","French","JavaScript","Php","Nne",1],
    ["Which language was used to create ls?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create wpb?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create vyt?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create ytwitter?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create yfb?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create owp?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create ykt?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create ztwitter?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create vyt?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create ctwitter?","Python","French","JavaScript","Php","None",1]
]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,480000,1000000,5000000,10000000] 
money=0
for i in range(0,len(questions)):
    print()
    question=questions[i]
    print(f"Question-{i+1}:",f"(for RS.{levels[i]})","Yea raha aapke computer screen pe !")
    print()
    print(question[0])
    print()
    print(f"a.{question[1]}     b.{question[2]}")   
    print(f"c.{question[3]}     d.{question[4]}") 
    print() 
    reply=int(input("Enter your answer (1-4) or (0) to quit the game: "))
    if(reply==0):
            break;
    elif(reply==question[-1]):
        print(f"correct answer,you have won RS.{levels[i]} :)")
        money+=levels[i]
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong Answer!")
        break  
    print() 
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")  
print(f"You have won RS.{money} aur isike saath aapko bidaay dete hain !:)");          