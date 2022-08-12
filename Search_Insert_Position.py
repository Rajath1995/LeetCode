class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(arr, x):
            low = 0
            high = len(arr) - 1
            mid = 0

            while low <= high:

                mid = (high + low) // 2

                # If x is greater, ignore left half
                if arr[mid] < x:
                    low = mid + 1

                # If x is smaller, ignore right half
                elif arr[mid] > x:
                    high = mid - 1

                # means x is present at mid
                else:
                    return mid
            return -1
        x= binary_search(nums, target)
        if x!=-1:
            return x
        else:
            nums.append(target)
            nums.sort()
            y = binary_search(nums, target)
            return y
