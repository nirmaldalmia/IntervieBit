class car(): 
      
    # init method or constructor 
    def __init__(self, A): 
        self.A = A
          
    def show(self):
        B = []
        length = len(A)
        i = length - 1
        while (A[i] == 9 & i >= 0):
            B.insert(0,0)
            print(B)
            i = i-1
        print(B)
          
# both objects have different self which  
# contain their attributes 
A = [9,9,9,9]
test = car(A)
test.show()