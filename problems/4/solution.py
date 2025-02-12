class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Determine which array is longer and shorter
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1  # Ensure nums1 is the longer array
        
        # Insert nums2 into nums1 at the correct position
        i = 0
        j = 0
        result = []
        
        # Merge arrays as we would in a merge step of merge sort
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        
        # If there are remaining elements in nums1, append them
        result.extend(nums1[i:])
        
        # If there are remaining elements in nums2, append them
        result.extend(nums2[j:])
        
        # Calculate the length of the new combined array
        l = len(result)

        # Check if the length is odd or even
        if l % 2 == 1:
            return result[l // 2]
        else:
            a = l // 2
            b = a - 1
            return (result[a] + result[b]) / 2
