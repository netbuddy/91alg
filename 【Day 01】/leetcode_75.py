import random
import time

class Solution1:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        for i in range(len_nums):
            if(nums[i] == 1):
                item = nums.pop(i)
                nums.insert(0, item)
        for i in range(len_nums):
            if(nums[i] == 0):
                item = nums.pop(i)
                nums.insert(0, item)

class Solution2:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_1 = []
        l_2 = []
        len_nums = len(nums)
        for i in range(len_nums):
            item = nums.pop()
            if(item == 0):
                nums.insert(0, item)
            elif(item == 1):
                l_1.append(item)
            elif(item == 2):
                l_2.append(item)
        nums.extend(l_1)
        nums.extend(l_2)

class Solution3:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = -1
        p1 = -1
        p2 = len(nums)
        i = 0
        #print(nums)
        while(i < p2):
            if(nums[i] == 0):
                p0 += 1
                nums[i] = nums[p0]
                nums[p0] = 0
            elif(nums[i] == 2):
                p2 -= 1
                nums[i] = nums[p2]
                nums[p2] = 2
                i -= 1
            i += 1
            #print(i+1, nums)

def main():
    nums = []
    for i in range(100000):
        nums.append(random.choice([0,1,2]))
    sorted_num = nums.copy()
    sorted_num.sort()

    # #解法1
    # time_start = time.time()
    # nums1 = nums.copy()
    # Solution1().sortColors(nums1)
    # time_end = time.time()
    # print("解法1:")
    # print('time cost', time_end - time_start, 's')
    # print(sorted_num == nums1)
    #
    # #解法2
    # time_start = time.time()
    # nums2 = nums.copy()
    # Solution2().sortColors(nums2)
    # time_end = time.time()
    # print("解法2:")
    # print('time cost', time_end - time_start, 's')
    # print(sorted_num == nums2)

    #解法3
    time_start = time.time()
    nums2 = nums.copy()
    Solution3().sortColors(nums2)
    time_end = time.time()
    print("解法2:")
    print('time cost', time_end - time_start, 's')
    print(sorted_num == nums2)

if __name__ == '__main__':
    main()
