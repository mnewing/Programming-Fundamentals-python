totalPrice = 0
f = open("/home/mary/dev/python/tickets.txt", "r")
for line in f:
    #print(line)
    
    ticket_holder_info = line.split(', ')
    print(ticket_holder_info)
    age = int(ticket_holder_info[2])
    
    if age < 5:
        print("infant")
        totalPrice = totalPrice + 0
    elif age >= 5 and age <13 :
        print("child")
        totalPrice = totalPrice + 10
    else:
       print("adult")
       totalPrice = totalPrice + 30

print(totalPrice)
