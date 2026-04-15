import random

class QuickSort:
    # 初始化：传入要排序的数组
    def __init__(self, arr):
        self.arr = arr

    # 分区函数：随机选轴 + 划分左右
    def partition(self, low, high):
        # 核心：随机选择轴
        pivot_idx = random.randint(low, high)
        self.arr[pivot_idx], self.arr[high] = self.arr[high], self.arr[pivot_idx]

        pivot = self.arr[high]
        i = low - 1

        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    # 递归排序
    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)

    # 对外调用的排序方法（最方便）
    def sort(self):
        self.quick_sort(0, len(self.arr) - 1)
        return self.arr

# ------------------- 测试 -------------------
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 56,111, 5]
    qs = QuickSort(arr)  # 创建排序对象
    res = qs.sort()      # 排序
    print("排序结果：", res)