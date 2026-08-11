class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> mp = new HashMap<>();
        mp.put('I',1);
        mp.put('V',5);
        mp.put('X',10);
        mp.put('L',50);
        mp.put('C',100);
        mp.put('D',500);
        mp.put('M',1000);

        int ans = 0;
        for(int i=0;i<s.length() - 1;i++){
            int x = mp.get(s.charAt(i));
            int y = mp.get(s.charAt(i + 1));
            if(x < y){
                ans = ans - x;
            }
            else{
                ans = ans + x;
            }
        }
        ans += mp.get(s.charAt(s.length() - 1));
        return ans;
    }
}