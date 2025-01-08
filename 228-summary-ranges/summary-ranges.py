from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:  # Handle empty array
            return []
        
        output = []
        a = nums[0]  # Start of the current range

        for i in range(1, len(nums)):
            # Check if the current number is not consecutive
            if nums[i] != nums[i - 1] + 1:
                # Add the completed range to the output
                if a == nums[i - 1]:  # Single number range
                    output.append(str(a))
                else:  # Multiple number range
                    output.append(f"{a}->{nums[i - 1]}")
                a = nums[i]  # Update the start of the next range
        
        # Handle the final range
        if a == nums[-1]:
            output.append(str(a))
        else:
            output.append(f"{a}->{nums[-1]}")

        return output
