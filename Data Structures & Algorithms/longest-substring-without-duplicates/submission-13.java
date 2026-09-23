class Solution {
    public int lengthOfLongestSubstring(String s) {
        int p2=0;
        int maxLength=0;
        Set<Character> set = new HashSet<>();
        for(int p1=0;p1<s.length();p1++){
            Character l=s.charAt(p1);
  
            while(set.contains(l)){
                set.remove(s.charAt(p2));
                p2+=1;
            }
            set.add(l);
            maxLength=Math.max(maxLength,p1-p2+1);

        }
            

      
        return maxLength;
    }
}
