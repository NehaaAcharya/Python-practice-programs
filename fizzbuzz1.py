# FIZZBUZZ 1:
# FIZZ    : MULTIPLE OF 3
# BUZZ    : MULTIPLE OF 5
# FIZZBUZZ: MULTIPLE OF 3 AND 5

print("WELCOME TO FIZZBUZZ GAME:")
def fizzbuzz(r):   
    for i in range(1,r):
        if(i%3==0 and i%5==0):
            print(i,"=FIZZBUZZ")
        elif(i%3==0):
            print(i,"=FIZZ")
        elif(i%5==0):
            print(i,"=BUZZ")
        
        else:    
            print(i)
