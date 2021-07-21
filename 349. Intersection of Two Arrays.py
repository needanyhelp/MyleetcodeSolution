def solution(nums1, nums2):
    result=list(set([x for x in nums1 if x in nums2]))
    return result


