import math as math
from decimal import Decimal

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)
            self.magnitude = math.sqrt(sum([x**2 for x in self.coordinates]))
            self.direction = [x/Decimal(self.magnitude) for x in self.coordinates]

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def plus(self,v):
        new_coordinates = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)
    def minus(self,v):
        new_coordinates = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(new_coordinates)
    def timesScalar(self,c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)
    def dotProduct(self,v):
        dotPrd = [x*y for x,y in zip(self.coordinates,v.coordinates)]
        return sum(dotPrd)
    def angle(self,v):
        dtPrd = self.dotProduct(v);
        try:
            return math.acos(dtPrd/(self.magnitude*v.magnitude))
        except ZeroDivisionError:
            raise Exception("Cannot divide by zero")
            
    def isParallel(self,v):
        angle = math.degrees(self.angle(v))
        return angle==0 or angle ==180
            
    def isOrthogonal(self,v):
        angle = math.degrees(self.angle(v))
        return angle==90
    def projection(self,v):
        dotPrd = self.dotProduct(Vector(v.direction))
        return  Vector(v.direction).timesScalar(dotPrd) 
    def orthComp(self,v):
        return self.minus(self.projection(v))
    def crossProduct(self,v):
        crsPrd=[]
        a = self.coordinates[1]*v.coordinates[2] - self.coordinates[2]*v.coordinates[1]
        crsPrd.append(a)  
        b = -1*(self.coordinates[0]*v.coordinates[2] - self.coordinates[2]*v.coordinates[0])
        crsPrd.append(b) 
        c = -1*(self.coordinates[0]*v.coordinates[1] - self.coordinates[1]*v.coordinates[0])
        crsPrd.append(c)
        return Vector(crsPrd)
       
        
        
                           
 
'''q4a = Vector([-0.221,7.437])
q4b = Vector([8.813,-1.331,-6.247])
q4c = Vector([5.581,-2.136])
q4d = Vector([1.996,3.108,-4.554])
print(q4a.magnitude)
print(q4b.magnitude)
print(q4c.direction)
print(q4d.direction)
q5a = Vector([7.887,4.138])
q5b = Vector([-8.802,6.776])
q5c=Vector([-5.955,-4.904,-1.874])
q5d=Vector([-4.496,-8.755,7.103])
print(q5a.dotProduct(q5b))
print(q5c.dotProduct(q5d))
print("----------")
q5e = Vector([3.183,-7.627])
q5f = Vector([-2.668,5.319])
q5g=Vector([7.35,0.221,5.188])
q5h=Vector([2.751,8.259,3.985])
print("radians :"+str(q5e.angle(q5f))+" ----"+"degrees :"+str(math.degrees(q5e.angle(q5f))))
print("radians :"+str(q5g.angle(q5h))+" ----"+"degrees :"+str(math.degrees(q5g.angle(q5h))))
q5a = Vector([-7.579,-7.88])
q5b = Vector([22.737,23.64])
q5a = Vector([-2.029,9.97,4.172])
q5b = Vector([-9.231,-6.639,-7.245])
q5a = Vector([-2.328,-7.284,-1.214])
q5b = Vector([-1.821,1.072,-2.94])
print(q5a.dotProduct(q5b))
print("radians :"+str(q5a.angle(q5b))+" ----"+"degrees :"+str(math.degrees(q5a.angle(q5b))))
print(q5a.isParallel(q5b))
print(q5a.isOrthogonal(q5b))
q5a = Vector([3.039,1.879])
q5b = Vector([0.825,2.036])
print(q5a.projection(q5b))
q5c = Vector([-9.88,-3.264,-8.159])
q5d = Vector([-2.155,-9.353,-9.473])
print(q5c.orthComp(q5d))
q6a = Vector([3.009,-6.172,3.692,-2.51])
q6b = Vector([6.404,-9.144,2.759,8.718])
print("----------------")
print(q6a.projection(q6b))
print(q6a.orthComp(q6b))
q7a = Vector([5,3,-2])
q7b = Vector([-1,0,3])
print(q7a.crossProduct(q7b))
print(q7a.crossProduct(q7b).magnitude)'''
q7a = Vector([8.462,7.893,-8.187])
q7b = Vector([6.984,-5.975,4.778])
'''print(q7a.crossProduct(q7b))
q7a = Vector([-8.987,-9.838,5.031])
q7b = Vector([-4.268,-1.861,-8.866])
print(q7a.crossProduct(q7b).magnitude)
q7a = Vector([1.5,9.5473,3.691])
q7b = Vector([-6.007,0.124,5.772])
print(q7a.crossProduct(q7b).magnitude/2)'''