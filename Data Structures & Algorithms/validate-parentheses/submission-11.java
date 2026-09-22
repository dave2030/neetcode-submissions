class Solution {
    public boolean isValid(String s) {
        Map<Character,Character> map = new HashMap<>();
        Deque<Character> stack = new ArrayDeque<>();
        map.put(')','(');
        map.put(']','[');
        map.put('}','{');
        for(char c:s.toCharArray()){
            if (c=='[' || c=='{' || c=='('){
                stack.push(c);
            }else{
                if(stack.isEmpty() || stack.peek()!=map.get(c))return false;
                while(!stack.isEmpty() && stack.peek()==map.get(c)){   
                    stack.pop();
                }
            }
        }
        return stack.isEmpty();
    }
}
