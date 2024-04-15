class Solution {
    public String makeGood(String s) { String t = "";
        while(s != t) {
            t = s;
            for(int i = 0; i < s.length() - 1; i++) {
                if(s.charAt(i) == s.charAt(i + 1) + 32 || s.charAt(i) + 32 == s.charAt(i + 1)) {
                    s = s.substring(0, i) + s.substring(i + 2);
                }
            }
        }
        return s;
    }
}