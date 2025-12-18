class Solution {
    public double fractionalKnapsack(int[] val, int[] wt, int capacity) {
        int n = val.length;
        double [][] arr = new double[n][2];
        for(int i=0;i<n;i++){
            arr[i][0] = val[i];
            arr[i][1] = wt[i];
        }
        double c = 0;
        Arrays.sort(arr,(a,b)->Double.compare(a[1]/b[1],a[0]/b[0]));
        for(int i=0;i<n;i++){
            if(arr[i][1]<=capacity){
                c += arr[i][0];
                capacity -= arr[i][1];
            }
            else{
                c += (arr[i][0]/arr[i][1])*capacity;
                capacity = 0;
            }
        }
        return c;
    }
}