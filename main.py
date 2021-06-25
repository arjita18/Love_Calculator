true = "true"
cnt1 = 0
cnt2 = 0
love = "love"

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

for i in range(0, len(true)):
    cnt1 += name1.count(true[i])
    cnt1 += name2.count(true[i])

for i in range(0, len(love)):
    cnt2 += name1.count(love[i])
    cnt2 += name2.count(love[i])

loveScore = str(cnt1) + str(cnt2)
loveScore = int(loveScore)
if (loveScore < 10) or (loveScore > 90):
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif (loveScore >= 40) and (loveScore <= 50):
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}")

