class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Keep track of total product, and if the nums has zero
        totalProduct = 1
        hasZero = False

        # Loop through once to get product
        for num in nums:
            # Multiply non-zeroes
            if num != 0:
                totalProduct *= num
            # More than one zero, all values will be 0
            elif hasZero:
                totalProduct = 0
                break
            # First zero, set the flag
            else:
                hasZero = True

        # Build the results
        result = []
        for num in nums:
            # If zero, use the total product (may be 0 if another 0 was found)
            if num == 0: 
                result.append(totalProduct)
                continue
            # No zero in the nums, do division
            if not hasZero:
                result.append(totalProduct//num)
            # non zero number, but zero in num array, set product to zero
            else:
                result.append(0)

        # Return the results!
        return result