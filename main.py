#Short quiz
correct = 0
incorrect = 0

answer1 = input("""1. Which password is the strongest? \n
A. password123 \n
B. Jason2004 \n
C. T7!qP9@zL2# \n
D. 12345678 \n
Answer:""").strip().upper()

if answer1 == 'A':
    incorrect += 1
    print("Incorrect")
elif answer1 == 'B':
    incorrect += 1
    print("Incorrect")
elif answer1 == 'C':
    print("Correct")
    correct += 1
elif answer1 == 'D':
    incorrect += 1
    print("Incorrect")

else:
   print("Invalid input")
   exit()



answer2 = input("""2. What should you do if you receive a suspicious email link? \n
A. Click to see where it leads \n
B. Forward it to friends \n
C. Reply with your personal information \n
D. Avoid clicking it and report the email \n
Answer:""").strip().upper()

if answer2 == 'A':
    incorrect += 1
    print("Incorrect")
elif answer2 == 'B':
    incorrect += 1
    print("Incorrect")
elif answer2 == 'C':
    print("Incorrect")
    incorrect += 1
elif answer2 == 'D':
    correct += 1
    print("Correct")

else:
   print("Invalid input")
   exit()

answer3 = input("""3. What does two-factor authentication do?\n
A. Requires a second verification method \n
B. Creates two usernames \n
C. Lets two people share an account \n
D. Requires you to enter your password twice \n
Answer:""").strip().upper()

if answer3 == 'A':
    correct += 1
    print("Correct")
elif answer3 == 'B':
    incorrect += 1
    print("Incorrect")
elif answer3 == 'C':
    print("Incorrect")
    incorrect += 1
elif answer3 == 'D':
    incorrect += 1
    print("Incorrect")

else:
   print("Invalid input")
   exit()


print("\n")
print("Score:")
print("Correct:",correct)
print("Incorrect:",incorrect)

overall = round((correct/3)*100, 1)


print(overall,"%")

if correct == 1:
    print("Grade: F")
elif correct == 2:
    print("Grade: D")
elif correct == 3:
    print("Grade: A")
elif correct == 0:
    print("Grade: F")


