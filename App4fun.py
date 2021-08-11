title="Welcome to a created quiz (by me) which will tell you which element you are"
question1=input("Do you like personality quizzes? Y-N:")
y=("y")
n=("n")
print(title)
print(question1)
if (question1==y):
    print("Great! So now you will be asked 4 questions and you will have however long it takes to answer (I am very patient).")
    print("Make sure to count your points! Lets gooo!")
    print("Question 1:")
    print(" What is your favourite time of the day? Mine is... ")
    print("  a) Morning")  
    print("  b) Evening")
    print("  c) Noon-Afternoon")
    a=("a")
    b=("b")
    c=("c")
    answer=input("choose a,b,c (type a,b or c):")
    print(answer)
    if (answer==a):
        print("+20 points")
    elif (answer==b):
        print("+10 points")  
    else:
        print("+30 points")  


    print("Question 2:")
    print(" If you found an injured rabbit? I would... ")
    print("  a) Make it as a pet")  
    print("  b) Heal it and return it to the family")
    print("  c) Ignore it! I don't care")
    answer=input("choose a,b,c (type a,b or c):")
    print(answer)
    if (answer==a):
        print("+20 points")
    elif (answer==b):
        print("+30 points")  
    else:
        print("+10 points")     
    print("Question 3:")
    print(" You get lost at a crowded shopping area? You would... ")
    print("  a) Just wait! someone will help me")  
    print("  b) Try to find my way on my own")
    print("  c) Aks some for directions")
    answer=input("choose a,b,c (type a,b or c):")
    print(answer)
    if (answer==a):
        print("+10 points")
    elif (answer==b):
        print("+20 points")  
    else:
        print("+30 points")
    print("Question 4 ( Last question ):")
    print(" I would spend my weekend... ")
    print("  a) studying! that math test is around the corner")  
    print("  b) partying! I am not wasting this weekend")
    print("  c) Sleeping! I need to get my beauty sleep")
    answer=input("choose a,b,c (type a,b or c):")
    print(answer)
    if (answer==a):
        print("+30 points")
    elif (answer==b):
        print("+10 points")  
    else:
        print("+20 points")

        print(" If you got 10-20 points your element is: Air") 
        print(" You are easy-going and don't believe in war! you are shy but you can achieve alot more than expected!")  
    
        print( "If you got 30-40 points your element is: Water")
        print(" You are calm about almost everything! You can make a good leader, but you need to work one your confidence!")
  
        print(" If you got 50-60 points your element is : Fire")
        print(" You are hot-tempered and angry if someone messes with your family! You care about your loved ones!")
   
        print(" If you got 70-80 points your element is : Earth")
        print(" You stand up for yourself! You won't go down easily! You have the ability of starting a revolution!")  
    
        print(" If you got 90-100 points your element is : Metal")
        print(" You are strong and independant! You also have a bit of an earth gene inside of yourself and you are underestimated alot!")  
    
        print(" If you got 110-120 points your element is : lightning")
        print(" You are legendary and unique and rare! everyone wants you because you are a good leader and ready for anything!")            
else:
    print("ok then :( ! I am not sad! Who said I am sad!!?? Have a good Day-Night-Afternoon-Evening or whatever the time is!")    
