class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character,Character> map = new HashMap<>();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        for(char st:s.toCharArray()){
            if(map.containsKey(st)){
                if(!stack.isEmpty() && stack.peek()==map.get(st))stack.pop();
                else return false;
            }
            else{
                stack.add(st);
            }

        }
        return stack.isEmpty();

        }
}
