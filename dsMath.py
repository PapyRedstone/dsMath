def distancePoints(A,B):
#    print("c:",A,B)
    tmp = 0;
    for i in range(len(A)):
        tmp += pow(A[i]-B[i],2)
    return pow(tmp,0.5)

def distance(A,B):
#    print(type(A).__name__)
#    print(type(B).__name__)
    if type(A).__name__ == "tuple" and type(B).__name__ == "tuple":
        return distancePoints(A,B)
    
    elif type(A).__name__ == "list":
        return min([distance(a,B) for a in A])

    elif type(B).__name__ == "list":
        return min([distance(A,b) for b in B])
"""
    else:
        d = float("Inf")
        for a in A:
            d = min(d, min([distancePoints(b,a) for b in B]))
        return d"""

def distance_tableau(tab):
    mini = float("Inf")
    best = None
    for i in range(len(tab)):
        for j in range(i+1,len(tab)):
            d = distance(tab[i],tab[j])
            if d < mini:
                mini = d
                best = [tab[i],tab[j]]

    return best

def printMatrice(tab):
    print("|",end='')
    for i in range(len(tab)):
        print("    ,"*i,end='')
        for j in range(i,len(tab)):
            print("%.2f," % distance(tab[i],tab[j]),end='')
        print("\b|\n|",end='')
    print("\b ")

points = [
    (0,4),
    (1,1),
    (1,2),
    (1,5),
    (3,4),
    (4,3),
    (6,2)
]

gammas = []

objets = points

printMatrice(objets)
print("")

while len(points) or len(gammas) != 1:
    closest = distance_tableau(objets)
#    print(closest)
    try:
        points.remove(closest[0])
    except:
        pass
    try:
        points.remove(closest[1])
    except:
        pass
    try:
        gammas.remove(closest[0])
    except:
        pass
    try:
        gammas.remove(closest[1])
    except:
        pass
    gammas += [closest]
    objets = points + gammas

    printMatrice(objets)
    print("")
