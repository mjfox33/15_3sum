from code_15_3sum import Solution

def test_example_1():
    s = Solution()
    nums = [-1,0,1,2,-1,-4]
    result = [[-1,-1,2],[-1,0,1]]
    assert s.threeSum(nums) == result

def test_example_2():
    s = Solution()
    nums = []
    result = []
    assert s.threeSum(nums) == result

def test_example_3():
    s = Solution()
    nums = [0]
    result = []
    assert s.threeSum(nums) == result