class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>0 and x<10: return True
        if x<0: return False 
        tmp=x
        num=0
        while tmp>0:
            num= num*10 + (tmp%10)
            tmp=tmp//10
        print(tmp)
        print(num)
        return tmp==num
