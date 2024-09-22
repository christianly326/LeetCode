class Solution {
    public int removeElement(int[] nums, int val) {
        int left = 0;
        int length = nums.length;
        for (int right = 0; right<length; right ++){
            if (nums[right] != val){
                nums[left] = nums[right];
                left += 1;
            }
        }
        return left;
    }
}

// Time complexity O(n)
// Space complexity O(1)