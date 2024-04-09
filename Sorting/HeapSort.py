from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def max_heapify(size,idx):
            left_child =  2*idx+1
            right_child = left_child + 1
            max_child = None
            if left_child < size and nums[left_child] > nums[idx]:
                max_child = left_child
            if right_child < size and nums[right_child] > nums[idx] and (max_child is None or nums[right_child] > nums[max_child]):
                max_child = right_child
            if max_child:
                nums[idx], nums[max_child] = nums[max_child],nums[idx]
                max_heapify(size,max_child)

        for i in range(len(nums)-1,-1,-1):
            max_heapify(len(nums),i)

        for i in range(len(nums)):
            # swap value
            nums[0],nums[len(nums)-i-1]=nums[len(nums)-i-1],nums[0]
            # maxify
            max_heapify(len(nums)-i-1,0)
        return nums



if __name__ == "__main__":
    example = [-2,3,-5]
    S = Solution()
    print(S.sortArray(example))