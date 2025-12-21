class Solution {
    public int countPrimes(int n) {
        if(n==0 || n==1) return 0;
        boolean [] check = new boolean[n];
        int c = 2;
        while(c*c < n){
            int f = c*c;
            while(f < n){
                check[f]  = true;
                f = f + c;
            }
            c += 1;
        }
        int ans = 0;
        for(int i=2;i<check.length;i++){
            if(check[i] == false){
                ans += 1;
            }
        }
        return ans;
    }
}