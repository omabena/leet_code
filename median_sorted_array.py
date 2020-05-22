class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        L = nums1 + nums2
        self.quicksort(L) 
        if (len(L)%2 == 0):
            return (L[int(len(L)/2)-1] + L[int(len(L)/2)])/2
        else:
            return L[int(len(L)/2)]

    
    def quicksort(self, L):
        return self.sort(L, 0, len(L)-1)

    def sort(self, L, start, end):
        if start < end:
            index = self.partition(L, start, end)
            self.sort(L, start, index - 1)
            self.sort(L, index + 1, end)
        return L

    def partition(self, L, start, end):
        pivot = L[end]
        index = start
        current = start
        while(current < end):
            if L[current] <= pivot: 
                L[index], L[current] = L[current], L[index]
                index += 1
            current += 1
        L[index], L[end] = L[end], L[index]
        return index 
    
nums1 = [1, 3]
nums2 = [2]
s = Solution()
#median = s.findMedianSortedArrays(nums1, nums2)
#print(median)

nums1 = [1, 2]
nums2 = [3, 4]
median = s.findMedianSortedArrays(nums1, nums2)
print(median)