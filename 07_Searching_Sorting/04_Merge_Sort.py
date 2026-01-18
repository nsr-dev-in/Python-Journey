class Solution:
    # MERGE SORT -- DIVIDE AND CONQUER
    def merge(self, nums, l, mid, r):
        # create temporary arrays
        left = nums[l:mid + 1]
        right = nums[mid + 1:r + 1]

        i = j = 0
        k = l

        # merge while both arrays have elements
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        # copy remaining elements of left array
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        # copy remaining elements of right array
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, nums, l, r):
        # base case
        if l >= r:
            return

        mid = (l + r) // 2

        # recursive calls
        self.mergeSort(nums, l, mid)
        self.mergeSort(nums, mid + 1, r)

        # merge sorted halves
        self.merge(nums, l, mid, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums
