class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();
        for(String s:strs){
            int[]alphabet=new int[26];
            for(char letter:s.toCharArray()){
                alphabet[letter-'a']+=1;
            }
            String alpha=Arrays.toString(alphabet);
            map.computeIfAbsent(alpha,k->new ArrayList<>()).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
