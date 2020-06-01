import unittest
from leetcode_75 import Solution

class MyTest(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        pass

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('22222')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        pass

    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        self.solution = Solution()

    def test_run(self):
        nums = [1, 2, 0, 2, 1, 0, 0, 1, 1]
        self.assertEqual([0,0,0,1,1,1,1,2,2], self.solution.sortColors(nums))  # 测试用例
        nums = [2, 2, 2, 1, 1, 1, 0, 0, 0]
        self.assertEqual([0, 0, 0, 1, 1, 1, 2, 2, 2], self.solution.sortColors(nums))  # 测试用例

if __name__ == '__main__':
    unittest.main()  # 运行所有的测试用例