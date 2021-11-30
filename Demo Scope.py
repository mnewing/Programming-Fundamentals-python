# all variables have scrope or where they can be accessed from.
# scope can be global or local to a function or block of code

def testScope():
    age = 5  #asignment creates local copy only avaible in the function
    print(age)
#end of testScope function


def testScopeAge():
    print(age)   # uses the global var as no local one defined
#end of testScopeAge function


def testScopeAgeAssignment():
    global age # uses the global var called age
    age = 25
    print(age)   
#end of testScopeAgeAssignment function


#main program
age = 10 #global verions
print(age)
testScope()
testScopeAge()
testScopeAgeAssignment()
print(age)
print('done')
