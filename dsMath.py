import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage

#calcule d'une distance entre deux points a n dimensions
def distancePoints(A,B):
    tmp = 0;
    for i in range(len(A)):
        tmp += pow(A[i]-B[i],2)
    return pow(tmp,0.5)

#determination du calcul de la distance a effectuer (2 points/point et classe/2 classes)
def distance(A,B):
    if type(A).__name__ == "tuple" and type(B).__name__ == "tuple":
        return distancePoints(A,B)
    
    elif type(A).__name__ == "list":
        return min([distance(a,B) for a in A])

    elif type(B).__name__ == "list":
        return min([distance(A,b) for b in B])
    
#calcul de la distance minimum entre les points d'un tableau
#retourne les deux plus proches
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

#affichage de la matrice des dsitances
def printMatrice(tab):
    print("|",end='')
    for i in range(len(tab)):
        print("    ,"*i,end='')
        for j in range(i,len(tab)):
            print("%.2f," % distance(tab[i],tab[j]),end='')
        print("\b|\n|",end='')
    print("\b ")
"""
points = [
    (0,4),
    (1,1),
    (1,2),
    (1,5),
    (3,4),
    (4,3),
    (6,2)
]
"""
points = [
    (314,353.5,72.6,26.3,51.6,30.30,21,70,20),
    (314,238,209.8,25.1,63.7,6.4,22.6,70,27),
    (401,112,259.4,33.3,54.9,1.2,26.6,120,41),
    (342,336,211.1,28.9,37.1,27.5,20.2,90,27),
    (264,314,215.9,19.5,103,36.4,23.4,60,20),
    (367,256,264,28.8,48.8,5.7,23,90,30),
    (344,192,87.2,27.9,90.1,36.3,19.5,80,36),
    (292,276,132.9,25.4,116.4,32.5,17.8,70,25),
    (406,172,182.3,32.5,76.4,4.9,26,110,28),
    (399,92,220.5,32.4,55.9,1.3,29.2,120,51),
    (308,222,79.2,25.6,63.6,21.1,20.5,80,13),
    (327,148,272.2,42.7,65.7,5.5,24.7,80,44),
    (378,148,272.2,24.7,65.7,5.5,24.7,80,44),
    (206,160,72.8,18.5,150.5,31,11.1,50,16),
    (292,390,168.5,24,77.4,5.5,16.8,70,20),
    (80,41,146.3,3.5,50,20,8.3,10,11),
    (115,25,94.8,7.8,64.3,22.6,7,30,10),
    (338,311,236.7,29.1,46.7,3.6,20.4,90,40),
    (347,285,219,29.5,57.6,5.8,23.6,80,30),
    (381,240,334.6,27.5,90,5.2,35.7,80,46),
    (142,22,78.2,10.4,63.4,20.4,9.4,20,10),
    (300,223,156.7,23.4,53,4,21.1,70,22),
    (355,232,178.9,28,51.5,6.8,22.4,90,25),
    (309,272,202.3,24.6,73.1,8.1,19.7,80,30),
    (370,432,162,31.2,83.5,13.3,18.7,100,25),
    (298,205,261,23.3,60.4,6.7,23.3,70,26),
    (321,252,125.5,27.3,62.3,6.2,21.8,80,20),
    (321,140,218,29.3,49.2,3.7,17.6,80,30),
    (70,91,215.7,3.4,42.9,2.9,4.1,13,14)
]

dist_mat = points[:]
    
gammas = []

objets = points

printMatrice(objets)
print("")

#determination de toutes les classes
while len(points) or len(gammas) != 1:
    closest = distance_tableau(objets)
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

#affichage du dendrogramme
linkage_matrix = linkage(dist_mat,"ward")
dendrogram(linkage_matrix)
plt.show()
