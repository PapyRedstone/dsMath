class Point:
    def __init__(self, coor):
        self.coordonees = coor

    def print(self):
        print(self.coordonees)

    def distance(self, point):
        if(len(point.coordonees) != len(self.coordonees)):
            raise RuntimeError("Les points ne sont pas de la même dimension, vous ne pouvez pas comparez leur distance")
        distance = 0
        for i in range(len(self.coordonees)):
            distance += pow(self.coordonees[i] - point.coordonees[i],2)
        return pow(distance,0.5)

class Classe:
    def __init__(self):
        self.objets = []
        return

    def ajouterObjet(self, o):
        self.objets.append(o)

    def distance(self, point):
        mini = 999999999999999
        for i in range(len(self.objets)):
            d = self.objets[i].distance(point)
            if d < mini:
                mini = d
        return mini

    def distance_tableau(self, points):
        mini = 99999999999
        index = -1
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                d = self.distance(points[j])
            
                if d < mini:
                    mini = d
                    index = i
        return index

    def print(self):
        for o in self.objets:
            o.print()
                

def distance_tableau(points):
    mini = 99999999999
    index1 = -1
    index2 = -1
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            d = points[i].distance(points[j])

            if d < mini:
                mini = d
                index1 = i
                index2 = j
    return (index1, index2)

points = [
    Point((0,4)),
    Point((1,1)),
    Point((1,2)),
    Point((1,5)),
    Point((3,4)),
    Point((4,3)),
    Point((6,2))
]

gamma = Classe()

i,j = distance_tableau(points)
gamma.ajouterObjet(points[i]) #ajouter les points a la classe gamma 1
gamma.ajouterObjet(points[j])
points.pop(i) #retirez les points des points qui sont dans une classe
points.pop(j-1)

while(len(points)):
    i = gamma.distance_tableau(points)
    tmp = gamma
    gamma = Classe()
    gamma.ajouterObjet(tmp)
    gamma.ajouterObjet(points[i])
    points.pop(i)

gamma.print()
