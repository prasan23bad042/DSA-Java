class Solution {
    int row_x[] = {-1, 0, 1, 0};
    int col_x[] = {0, -1, 0, 1};
    public void dfs(int[][] image, int r, int c, int ini, int color) {
        for (int i = 0; i < 4; i++) {
            if (r + row_x[i] >= 0 &&
                r + row_x[i] < image.length &&
                c + col_x[i] >= 0 &&
                c + col_x[i] < image[0].length &&
                image[r + row_x[i]][c + col_x[i]] == ini) {

                image[r + row_x[i]][c + col_x[i]] = color;
                dfs(image, r + row_x[i], c + col_x[i], ini, color);
            }
        }
    }
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int ini = image[sr][sc];
        if (ini != color) {
            image[sr][sc] = color;
            dfs(image, sr, sc, ini, color);
        }
        return image;
    }
}
