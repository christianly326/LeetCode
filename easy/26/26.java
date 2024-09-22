class Solution {
    public int removeDuplicates(int[] nums) {
        int l=1,r=0,length=nums.length-1;
        while (r<length){
            if (nums[r] != nums[r + 1]){
                nums[l] = nums[r + 1];
                l++;
            }
            r++;
        }
        return l;
    }
        
}
// Time complexity O(n)
// Space complexity O(1)
