class Solution {
    public int minPlatform(int arr[], int dep[]) {
        int n = arr.length;
        Arrays.sort(arr);
        Arrays.sort(dep);
        int i = 0;
        int j = 0;
        int cnt = 0;
        int max_cnt = 0;
        while(i<n){
            if(arr[i] <= dep[j]){
                cnt += 1;
                i += 1;
            }
            else{
                cnt -= 1;
                j += 1;
            }
            max_cnt = Math.max(max_cnt,cnt);
        }
        return max_cnt;
    }
}