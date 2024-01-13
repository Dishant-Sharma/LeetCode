public class Solution {
    public int MinSteps(string s, string t) {
        int [] sCount = new int[26];
        int [] tCount = new int[26];
        int ans = 0;
        
        foreach (char i in s){
            sCount[i - 'a']++;
            
        }
        
        foreach (char i in t){
            tCount[i - 'a']++;
            
        }
        
        for(int i = 0; i < 26; i++){
            if(sCount[i] > tCount[i]){
                ans += sCount[i] - tCount[i];                
            }
        }
        return ans;        
    }
}