class Solution {
    public boolean isHappy(int n) {
        int slow=n;
        int fast=happyCompute(happyCompute(n));
        while(slow!=fast){
            slow=happyCompute(slow);
            fast=happyCompute(happyCompute(fast));
        }
        return slow==1;
    
    }

    public int happyCompute(int n){
        int res=0;
        while (n>0){
            int remainder=n%10;
            res+=(remainder*remainder);
            n/=10;
        }
        return res;
    }
}
