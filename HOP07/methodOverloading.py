class OverloadDemo:
    #sum method with one default para
    def sum(self, a,b,c = 0):
        s = a + b + c
        return s

od = OverloadDemo()

#Calling method with 2 args
sum = od.sum(7,8)
print("Sum is - ", sum)

#Calling medthod with 3 args
sum = od.sum(7,8,9)
print("Sum is - ", sum)