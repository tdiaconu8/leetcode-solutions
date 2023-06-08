class Solution {
    public int countNegatives(int[][] grid) {

        // O(n+m)

        int res = 0;
        int r = grid.length;
        int c = grid[0].length;
        int i = 0;
        int j = c-1;

        while (i < r) {
            while (j >= 0 && grid[i][j] < 0) {
                j --;
            }
            res += (c-j-1); 
            i ++;
        }

        return res;
    }
}