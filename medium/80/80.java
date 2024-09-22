class Solution {
    public int removeDuplicates(int[] nums) {
        int count=1,l=1,r=1;
        while (r<nums.length){
            if (nums[r] == nums[r-1]){
                count++;
            }
            else count=1;
            if (count<=2){
                nums[l] = nums[r];
                l++;
            }
            r++;
        }
        return l;
    }
}

// Time complexity O(n)
// Space complexity O(1)