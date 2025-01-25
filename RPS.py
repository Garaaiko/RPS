CL = ["R","P","S"]
Q = input("Are you ready to play (Y/N):")
if Q != "Y" and Q != "N":
     while Q != "Y" and Q != "N":
        Q = input("I said (Y/N): ")

if Q == "Y":
    A = 0
    B = 0
    import random
    while A < 3 and B < 3:
        I = input("(R)ock, (P)aper, or (S)cissors: ")
        if I != "R" and I != "P" and I != "S":
            while I != "R" and I != "P" and I != "S":
                I = input("R, P, or S: ")
        C = (random.choice(CL))
        
        if C == "R": 
            print("I choose rock!")
        if C == "P":
           print("I choose paper!")
        if C == "S":
            print("I choose scissors!")

        if C == I:
            print("Tie! Try again")
        
        if C == "R" and I == "P":
            B += 1
            print("You win! " + "Me: " + str(A) + " , You: " + str(B))
        if C == "P" and I == "S":
            B += 1
            print("You win! " + "Me: " + str(A) + " , You: " + str(B))
        if C == "S" and I == "R":
            B += 1
            print("You win! " + "Me: " + str(A) + " , You: " + str(B))
        
        if C == "P" and I == "R":
            A += 1
            print("I win! " + "Me: " + str(A) + " , You: " + str(B))
        if C == "S" and I == "P":
            A += 1
            print("I win! " + "Me: " + str(A) + " , You: " + str(B))
        if C == "R" and I == "S":
            A += 1
            print("I win! " + "Me: " + str(A) + " , You: " + str(B))

    if A == 3:
        print("I won! Better luck next time")
    elif B == 3:
        print("You won! Great job")
if Q == "N":
    print("Ok then")
