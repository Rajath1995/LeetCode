class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        original_list= nums
        num_to_be_searched = target
        mid_element = (len(original_list) - 1)//2

        if num_to_be_searched == original_list[mid_element]:
            return mid_element
        elif mid_element == 0 and len(original_list) == 2:
            return 1 if original_list[1] == num_to_be_searched else -1
        elif mid_element == 0:
            return 0 if original_list[0] == num_to_be_searched else -1

        first_half = original_list[0: mid_element]
        second_half = original_list[mid_element+1:]

        try1 = binary_search(first_half, num_to_be_searched)
        if try1 == -1:
            b = binary_search(second_half, num_to_be_searched)
            return b+mid_element+1 if b!=-1 else b
        else:
            return try1
        
            
