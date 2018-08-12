class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                return True
            if nums[end] > nums[begin]:
                if nums[mid] > target:
                    end = mid - 1
                else:
                    begin = mid + 1
            else:
                if nums[mid] > nums[begin]:
                    if target < nums[mid] and target >= nums[begin]:
                        end = mid - 1
                    else:
                        begin = mid + 1
                elif nums[mid] < nums[end]:
                    if target > nums[mid] and target <= nums[end]:
                        begin = mid + 1
                    else:
                        end = mid - 1
                else:
                    if nums[begin] != target:
                        begin += 1
                    else:
                        return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.search([2,3,4,5,6,0,0,1], 0))
    print(s.search([1,1,1,1,1,1,1,1,1,3,1,1], 3))
