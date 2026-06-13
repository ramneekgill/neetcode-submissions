class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        char[] chars = s.toCharArray();
        char[] chart = t.toCharArray();
        Arrays.sort(chars);
        Arrays.sort(chart);
        String sSorted = new String(chars);
        String tSorted = new String(chart);
        for(int i = 0; i<sSorted.length(); i++){
            if(sSorted.charAt(i) != tSorted.charAt(i)){
                return false;
            }
        }
        return true;


    }
}
