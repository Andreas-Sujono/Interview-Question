import random
class Solution:
    def generatePiExact(self):
        # using Leibniz formula for π
        current = 0
        iteration = 10000000000000
        i = 0
        while(True):
            current += 4*((-1)**i * 1/(2*i+1) )
            i+=1
            if(i % iteration == 0):
                print(current)
        return 
    
    def generatePiApproximate(self,iteration, typePi):
        # approximation by random number inside circle
        if(typePi == 1): 
            point_inside = 0
            point_total = 0

            for _ in range(iteration):
                x = random.random()
                y = random.random()
                distance = x ** 2 + y ** 2
                if(distance <= 1):
                    point_inside += 1
                point_total += 1
            return 4*(point_inside/point_total)

        else:
            print('not a valid type')
            return False

#Solution().generatePiExact()
print(Solution().generatePiApproximate(1000000,1))
