void sortColors(int* nums, int numsSize){
        int p0 = -1;           /*p0指向连续一串0的最后一个*/
        int p2 = numsSize;     /*p2指向连续一串2的第一个*/
        int i = 0;             /*i用于遍历数组*/
        while(i < p2)
        {
            if(nums[i] == 0)   /*当前位置为0,则与p0的下一个位置交换数据，然后p0加1*/
            {
                p0 += 1;
                nums[i] = nums[p0];
                nums[p0] = 0;
            }
            else if(nums[i] == 2)  /*当前位置为2,则与p2的前一个位置交换数据，然后p2减1*/
            {
                p2 -= 1;
                nums[i] = nums[p2];
                nums[p2] = 2;
                i -= 1;            /*对交换数据后的当前位置再次判断，因为其可能为0*/
            }
            i += 1;
        }
}