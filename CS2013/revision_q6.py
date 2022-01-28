class Calculations:


    def __init__(self):

        print("Instance of Calculation module v1.0 created")



    def isGreaterThan(self, num1, num2):

        if num2 > num1:
            return True
        elif num1 > num2:
            return False
        else:
            return -1


    def getHighestOccuringSequence(self, arr):

        counts = {}
        for i in arr:
            count = arr.count(i)
            counts[i] = count
        
        return max(counts, key = counts.get)

        

# ------- main --------------------------------

calc_1 = Calculations()
print(calc_1.getHighestOccuringSequence([1,1,2,2,2,3,3,3,3,2,2,1,1,1,1]))