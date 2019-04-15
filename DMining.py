print("PERSONALITY TEST")
quesE = []
quesN = []
quesA = []
quesC = []
quesO = []

print("Do you feel if you're the life of the party?")
quesE.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))
 
print("Do you talk a lot?")
quesE.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you start conversations?")
quesE.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you have little to say?")
quesE.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you like to draw attention to yourself?")
quesE.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you get stressed out easily?")
quesN.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))
 
print("Do you worry about things?")
quesN.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you seldom feel blue?")
quesN.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Are you easily disturbed?")
quesN.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Does your your mood change a lot?")
quesN.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you feel little concern for others?")
quesA.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))
 
print("Are you interested in people?")
quesA.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you insult people?")
quesA.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you sympathize with others' feelings?")
quesA.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Are you interested in other people's problems?")
quesA.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you leave your belongings around?")
quesC.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you pay attention to details?")
quesC.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))
 
print("Do you make a mess of things?")
quesC.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you get chores done right away?")
quesC.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you often forget to put things back in their proper place?")
quesC.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you have a rich vocabulary?")
quesO.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you have difficulty in understanding abstract ideas?")
quesO.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you have a vivid imagination?")
quesO.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))
 
print("Do you have a good imagination?")
quesO.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Do you use difficult words?")
quesO.append(int(input("\nScore from 1-5 where 1=lowest and 5=highest:\n")))

print("Your Answers:")
for i in quesE:
    print(i, end=" ")

for i in quesN:
    print(i, end=" ")

for i in quesA:
    print(i, end=" ")

for i in quesC:
    print(i, end=" ")

for i in quesO:
    print(i, end=" ")
    
print("\n")
sumE = sum(quesE)
print("Extroversion:{} %".format(sumE*4))

sumN = sum(quesN)
print("Neuroticism:{} %".format(sumN*4))

sumA = sum(quesA)
print ("Agreeableness:{} %".format(sumA*4))

sumC = sum(quesC)
print ("Concientiousness:{} %".format(sumC*4))

sumO = sum(quesO)
print ("Openness:{} %".format(sumO*4))

if (sumE*4) > 49 and (sumE*4) > (sumN*4) and (sumE*4) > (sumC*4) and (sumE*4) > (sumA*4) and (sumE*4) > (sumO*4):
    print("You are more extrovert!")
elif (sumN*4) > 49 and (sumN*4) > (sumA*4) and (sumN*4) > (sumC*4) and (sumN*4) > (sumO*4):
    print("You are more neuroctic!")
elif (sumA*4) > 49 and (sumA*4) > (sumO*4) and (sumA*4) > (sumC*4):
    print("You are more agreeable!")
elif (sumC*4) > 49 and (sumC*4) > (sumO*4): 
    print("You are more conscientious!")
elif (sumO*4) > 49:
    print("You are more open!")
else:
    print("You are a combination of OCEAN!!!")
