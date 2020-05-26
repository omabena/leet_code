class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        intersect_list = []
        nums1.sort()
        nums2.sort()
        if len(nums1) < len(nums2):
            list_tranverse = nums1
            list_compare = nums2
        else:
            list_tranverse = nums2
            list_compare = nums1

        n = len(list_tranverse)
        i = 0
        while i < n:
            current = list_tranverse[i]
            current_l_1 = list(filter(lambda x: x == current, list_tranverse))
            current_l_2 = list(filter(lambda x: x == current, list_compare))
            if len(current_l_1) == 0 or len(current_l_2) == 0:
                i = i + 1
                continue

            if len(current_l_1) < len(current_l_2):
                intersect_list.extend(current_l_1)
            else:
                intersect_list.extend(current_l_2)

            i = i + len(current_l_1)

        return intersect_list
        