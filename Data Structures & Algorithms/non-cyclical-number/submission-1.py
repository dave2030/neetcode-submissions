class Solution:
    def isHappy(self, n: int) -> bool:
        cycle=set()
        while n not in cycle:
            cycle.add(n)
            n=self.computeHappy(n)
            if n==1:
                return True

        return False
        
        # slow=n
        # fast=self.computeHappy(n)
        # while slow!=fast:
        #     fast=self.computeHappy(fast)
        #     fast=self.computeHappy(fast)
        #     slow=self.computeHappy(slow)
        # return True if fast==1 else False

    
    def computeHappy(self,n):
            res=0
            digit=0
            while n>0:
                res=n%10
                digit+=res**2
                n=n//10
            return digit


        

       