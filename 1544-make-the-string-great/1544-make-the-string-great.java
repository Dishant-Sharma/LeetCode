class Solution {
    public String makeGood(String s) {
        StringBuilder sb = new StringBuilder();
//        boolean hasChanged = true;
////        while (hasChanged) {
//            hasChanged = false;

            for (char c : s.toCharArray()) {
                if (sb.length() > 0 && Character.toLowerCase(sb.charAt(sb.length() - 1)) == Character.toLowerCase(c) && sb.charAt(sb.length() - 1) != c) {
                sb.deleteCharAt(sb.length() - 1);
            } else {
                    sb.append(c);
                }
//            }
        }
        return sb.toString();
    
        // String t = "";
        // while(s != t) {
        //     t = s;
        //     for(int i = 0; i < s.length() - 1; i++) {
        //         if(s.charAt(i) == s.charAt(i + 1) + 32 || s.charAt(i) + 32 == s.charAt(i + 1)) {
        //             s = s.substring(0, i) + s.substring(i + 2);
        //         }
        //     }
        // }
        // return s;
    }
}