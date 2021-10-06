#WRITE YOUR CODE IN THIS FILE
#ok

def countA(w):

    Bub = 0

    for i in range(0, len(w)):
        if w[i] == "a":
            Bub = Bub + 1
    return Bub

    
print(countA("armadilloo"))