class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] new_arr = new int[m + n];
        int l1 = 0, l2 = 0, cnt = 0;
        while (l1 < m && l2 < n) {
            if (nums1[l1] > nums2[l2]) {
                new_arr[cnt++] = nums2[l2];
                l2 ++;
            } else {
                new_arr[cnt++] = nums1[l1];
                l1 ++;
            }
        }

        if (l1 < m) {
            for (; l1 < m; l1 ++) {
                new_arr[cnt++] = nums1[l1];
            }
        } else if (l2 < n) {
            for (; l2 < n; l2 ++) {
                new_arr[cnt++] = nums2[l2];
            }
        }
        for (int i = 0; i < m + n; i ++) {
            nums1[i] = new_arr[i];
        }
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums1 = {1, 3, 4, 0, 0, 0};
        int[] nums2 = {2, 3, 3};
        s.merge(nums1, 3, nums2, 3);
        for (int i:nums1) {
            System.out.println(i);
        }
    }

}
