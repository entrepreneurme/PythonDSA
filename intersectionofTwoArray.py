class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        result = []
        if len(list(set1)) >= len(list(set2)):
            for i in list(set2):
                if i in list(set1):
                    result.append(i)
        else:
            for i in list(set1):
                if i in list(set2):
                    result.append(i)
        return result
