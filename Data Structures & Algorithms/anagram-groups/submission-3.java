class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> map = new HashMap<>();
        for(String s:strs){
            char []c=s.toCharArray();
            Arrays.sort(c);
            String newS=new String(c);
            if(map.containsKey(newS))map.get(newS).add(s);
            else map.put(newS,new ArrayList<>(Arrays.asList(s)));
        }

        return new ArrayList<>(map.values());
    }
}
