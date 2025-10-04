import random
#for dice rolls 
def printtalents(strength,wisdom,intelligence,constitution,dexterity,charisma,talentpoints):
    print("strength: ", strength)
    print("constitution: ", constitution)
    print("wisdom: ", wisdom)
    print("intelligence: ", intelligence)
    print("charisma: ", charisma)
    print("dexterity: ",dexterity)
    print("Total talent points left: ",talentpoints)
    print("--------------------------------------------------------------")
#function to bring up and print all the talents
name=input("Enter your character name")
age=int(input("Enter your age"))
#age is not too srs in the game, just for small dialouge option
gameentry=0
wisdom=0
charisma=0
strength=0
intelligence=0
dexterity=0
constitution=0
health=100
talentpoints=42
#talents style inspired by dnd game play
while gameentry<10000000:
    print("Game Menu")
    print("1.Start")
    print("2.Change your name and age")
    print("3.End")
    print("---------------------------------------")
    menuans=int(input("Enter the number of the selection you want"))
    print("--------------------------------------------------------")
    if menuans==1:
         if age<30:
             print("Hello there young", name," ,what awaits your adventure")
             print("1.I'm not sure")
             print("2.I'm ready for anything")
             print("3.money money money MONEYYYY!!!!")
             print("----------------------------------------------")
             scene1ans=int(input("Choose your answer"))
             if scene1ans==1:
                 print("Well young adventurer, nothing is set in stone,so surprises will always catch you and your options are limitless!")
             elif scene1ans==2:
                 print("Young adventurer, that's an amazing mindset!!")
             elif scene1ans==3:
                 print("Greed is never a good thing young adventurer!")
         else:
             print("Greetings adventurer",name,", what awaits your adventure")
             print("1.I'm not sure")
             print("2.I'm ready for anything")
             print("3.money money money MONEYYYY!!!!")
             print("----------------------------------------------")
             scene1ans=int(input("Choose your answer"))
             if scene1ans==1:
                 print("Well adventurer, nothing is set in stone,so surprises will always catch you and your options are limitless!")
             elif scene1ans==2:
                 print("that's an amazing mindset!!")
             elif scene1ans==3:
                 print("Greed is never a good thing!")
    print("------------------------------------------------------------------")
    print("Roles")
    print("1.Bard")
    print("2.Knight")
    print("3.Wizard")
    print("4.Monk")
    print("5.Rouge")
    print("------------------------------------------------------------------")
    roleans=int(input("Choose your role"))
    match roleans:
        case 1:
            charisma+=1
            intelligence+=1
            role="Bard"
        case 2:
            strength+=1
            constitution+=1
            role="Knight"
        case 3:
            wisdom+=1
            intelligence+=1
            role="Wizard"
        case 4:
            intelligence+=1
            charisma+=1
            role="Monk"
        case 5:
            strength+=1
            dexterity+=1
            role="Rouge"
    print("--------------------------------------------------------------------")
    printt1=printtalents(strength,wisdom,intelligence,constitution,dexterity,charisma)
    print("Total talent points left: ", talentpoints)
    addtpoints=input("Would you like to add your talent points or randomize it? Add/Randomize")
    if addtpoints=="Randomize":
        strength+=random.randint(1,20)
        constitution+=random.randint(1,20)
        wisdom+=random.randint(1,20)
        intelligence+=random.randint(1,20)
        charisma+=random.randint(1,20)
        dexterity+=random.randint(1,20)
        printt2=printtalents(strength,wisdom,intelligence,constitution,dexterity,charisma)
    elif addtpoints=="Add":
        #i havent finished the code beyond the project yetm but i will
        
            
   
    
    
    
 
    
        
            
        
    
             
                 
        