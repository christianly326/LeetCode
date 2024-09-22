import java.util.HashMap;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> freq = new HashMap<Character, Integer>();
        for (int i=0;i<magazine.length();i++){
            char c = magazine.charAt(i);
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        for(int j=0;j<ransomNote.length();j++){
            char d = ransomNote.charAt(j);
            freq.put(d, freq.getOrDefault(d, 0) - 1);
            if (freq.get(d) < 0){
                return false;
            }
        }
        return true;
    }
}
// Time complexity O(n + m)
// Space complexity O(k) where k is the length of the unique characters in magazine