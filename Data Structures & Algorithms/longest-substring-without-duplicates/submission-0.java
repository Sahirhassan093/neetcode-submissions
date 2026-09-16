class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> str = new HashSet<>();
        int l = 0;
        int r = 0;
        int w_len = 0;
        while (r < s.length()){
            while (str.contains(s.charAt(r))){
                str.remove(s.charAt(l));
                l = l + 1;
            }
            str.add(s.charAt(r));
            w_len = Math.max(w_len,r-l+1);
            r = r + 1;
        }
        return w_len;
    }
}
