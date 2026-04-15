import random

class ThreeWayQuickSort:
    def __init__(self, arr):
        self.arr = arr  # 保存要排序的数组

    # 三路分区核心：小于 pivot / 等于 pivot / 大于 pivot
    def three_way_partition(self, low, high):
        # 随机选轴（优化，避免最坏情况）
        pivot_idx = random.randint(low, high)
        self.arr[pivot_idx], self.arr[low] = self.arr[low], self.arr[pivot_idx]

        pivot = self.arr[low]
        lt = low         # 小于区的最后一个位置
        gt = high        # 大于区的第一个位置
        i = low + 1      # 遍历指针

        while i <= gt:
            if self.arr[i] < pivot:
                # 小于：放到小于区
                self.arr[i], self.arr[lt] = self.arr[lt], self.arr[i]
                lt += 1
                i += 1
            elif self.arr[i] > pivot:
                # 大于：放到大于区
                self.arr[i], self.arr[gt] = self.arr[gt], self.arr[i]
                gt -= 1
            else:
                # 等于：直接跳过
                i += 1
        return lt, gt

    # 三路快排递归
    def three_quick_sort(self, low, high):
        if low >= high:
            return

        lt, gt = self.three_way_partition(low, high)
        self.three_quick_sort(low, lt - 1)   # 排序小于区
        self.three_quick_sort(gt + 1, high)  # 排序大于区

    # 对外接口：一行调用排序
    def sort(self):
        self.three_quick_sort(0, len(self.arr) - 1)
        return self.arr


# ------------------- 测试 -------------------
if __name__ == "__main__":
    # 大量重复元素，三路快排最强
    arr = [5, 1, 3, 5, 2, 5, 9, 5, 0, 5, 99, 9, 7, 5]
    sorter = ThreeWayQuickSort(arr)
    res = sorter.sort()
    print("三路快排结果：", res)