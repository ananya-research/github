class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:

        # nums=[]

        # for i in numbers:
        #     nums.append(int(i))

        # print(sorted(nums))

        # for i in range(len(nums)-1):
        #     if nums[i]+1==nums[i+1]:
        #         return True

        # return False

        # nums=[]

        # for i in numbers:
        #     nums.append(int(i))

        # print(sorted(nums))

        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if numbers[i] in numbers[j][:len(numbers[i])] and i!=j:
                    print(numbers[i], numbers[j])
                    return False

        return True


        
        