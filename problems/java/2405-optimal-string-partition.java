class Solution {
    public int partitionString(String s) {

        // T: O(n), S: O(n)

        int res = 1;
        HashSet letters = new HashSet();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (! letters.contains(c)) {
                letters.add(c);
            }
            else {
                letters = new HashSet();
                letters.add(c);
                res ++;
            }
        }

        return res;
        
    }
}