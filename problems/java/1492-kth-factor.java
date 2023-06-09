class Solution {
    public int kthFactor(int n, int k) {
        
        // T: O(n), S: O(1)
        int i = 1;

        for (int num = 1; num <= n; num++) {
            if (n%num == 0) {
                if (i == k) {
                    return num;
                }
                i++;
            }
        }
        return -1;
    }
}