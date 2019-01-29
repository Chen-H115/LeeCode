class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
         int M = triangle.size();
         int N = triangle.get(M-1).size();
         int[][] dp = new int[M+1][N+1];
         for (int i = 0; i < N+1; i++) {dp[M][i] = 0;}
            for (int i = M-1; i >= 0; i--){
                N = triangle.get(i).size();
                for (int j = 0; j < N; j++){
                    dp[i][j] = Math.min(dp[i+1][j], dp[i+1][j+1]) + triangle.get(i).get(j);
                }
            }
         return dp[0][0];
    }
}
