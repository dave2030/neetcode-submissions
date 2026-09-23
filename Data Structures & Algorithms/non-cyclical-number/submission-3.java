class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();
        int num=n;
        while(num!=1){
            if(set.contains(num))return false;
            set.add(num);
            num=happyCompute(num);
        }
        return true;
        
    
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
