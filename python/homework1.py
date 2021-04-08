# Defining problem:
# total bill amount (from the user)
#levels (from the user): good (20%), fair (15%), or bad (10%)

#declare some variable that stores total 

# request that number from the user's bill
# request that number from the user 
userBill = int(input("Total bill amount"))

# declare some variable that stores the level of service 
# request the number from the user
servicelevel = input("level of service? ")

# declare a variable that will store the tip
userTip = 0
endingBill = 0

# endingBill = userTotal + tip
# tip (15%)
# total * 0.20 good
if servicelevel == "good":
    userTip = userBill * 0.2
# total * 0.15 fair
elif servicelevel == "fair":
    userTip = userBill * 0.15
# total * 0.10 bad
elif servicelevel == "bad":
    userTip = userBill * 0.10
else:
    print("invalid input.")

# Final total = the user's tip + initial amount
endingBill = userTip + userBill

# output to user
print(f'tip amount: {userTip}')
print(f'total amount: {endingBill}')

# 1 star
# 3 star
# 5 star
# 7 stars 

# each row increment by 2

for x in range(1, 8, 2):
    print(("*" * x).center(7))

# multiplication
#increaments of 1 to 10 

num = 1
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)