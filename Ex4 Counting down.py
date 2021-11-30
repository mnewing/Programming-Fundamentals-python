# ask the user for their fav number
# count down to 0 displaying the countdown
# requires
#   using variables
#   getting user input
#   using system functions
#   binary operators
#   while loops

favNum = input("what is your fav number? ")
print("your fav amount is £"+favNum)

counter = int(favNum)
while counter > 0:
    print(counter)
    counter = counter - 1
print(counter) #print the final 0 as well
