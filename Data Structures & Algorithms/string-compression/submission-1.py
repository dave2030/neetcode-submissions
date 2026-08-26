class Solution:
    def compress(self, chars: List[str]) -> int:
        p1,p2=0,0
        length=0
        while p1<len(chars):
            p2=p1+1
            chars[length]=chars[p1]
            length+=1
            while p2<len(chars) and chars[p1]==chars[p2]:
                p2+=1
            if p2-p1>1:
                for i in str(p2-p1):
                    chars[length]=i 
                    length+=1
            
            p1=p2
        print(chars)
        return length
