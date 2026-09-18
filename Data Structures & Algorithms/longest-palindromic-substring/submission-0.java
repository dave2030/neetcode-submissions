class Solution {
    public String longestPalindrome(String s) {
        String res="";
        for(int i=0;i<s.length();i++){
          String s1=palindrome(s,i,i);
          String s2=palindrome(s,i,i+1);
        
            if (s1.length() > res.length()) {
        res = s1;
    }

    if (s2.length() > res.length()) {
        res = s2;
    }
        }
        
        return res;
        
    }


    public String palindrome(String s,int a, int b){
        while (a>=0 && b<s.length() && s.charAt(a)==s.charAt(b)){
            a--;
            b++;
        }
        return s.substring(a+1,b);
    }
}
