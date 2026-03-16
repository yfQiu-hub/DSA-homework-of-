# #正确的有序数组插入方法
# from typing import Any
# from collections.abc import Sequence
#
# class OrderedArrayInsert:
#     """
#     有序数组的插入
#     """
#     def __init__(self, iterable: Sequence[Any], need_bubble_sort: bool = False):
#         """
#         :param iterable: 有序数组初始化
#         :param need_bubble_sort: 是否对输入数组执行冒泡排序，默认False（不排序）
#         """
#         self.iterable = list(iterable)
#         self.len = len(self.iterable)
#
#         # 如果需要冒泡排序，执行排序逻辑
#         if need_bubble_sort and self.len > 1:
#             self._bubble_sort()
#
#     def _bubble_sort(self):
#         """
#         私有方法：冒泡排序（升序），仅内部调用
#         """
#         # 冒泡排序核心逻辑：相邻元素比较，大的后移
#         for i in range(self.len - 1):
#             swapped = False  # 优化：标记是否发生交换，提前终止
#             for j in range(self.len - 1 - i):
#                 if self.iterable[j] > self.iterable[j + 1]:
#                     # 交换相邻元素
#                     self.iterable[j], self.iterable[j + 1] = self.iterable[j + 1], self.iterable[j]
#                     swapped = True
#             if not swapped:
#                 break  # 没有交换说明已排序，提前退出
#
#     def insert(self, element: Any) -> None:
#         """
#         插入元素
#         :param element: 待插入的元素
#         """
#         insert_index: int = self.len
#
#         for index, value in enumerate(self.iterable):
#             if element < value:
#                 insert_index = index
#                 break
#
#
#         self.iterable.append("")
#         for i in range(self.len, insert_index - 1, -1):
#             self.iterable[i] = self.iterable[i - 1]
#
#         self.iterable[insert_index] = element
#         self.len +=1
#
#
# orderedarrayinsert=OrderedArrayInsert([1,91,45,60],True)
# orderedarrayinsert.insert(75)
# print(orderedarrayinsert.iterable)
# orderedarrayinsert.insert(33)
# print(orderedarrayinsert.iterable)
# orderedarrayinsert.insert(89)
# print(orderedarrayinsert.iterable)




from typing import Any, Iterable, Optional, Set

class CustomSetHandler:
    """
    自定义集合处理器：支持接收任意可迭代类型并转为集合，实现查询、插入、删除功能
    支持输入类型：列表、元组、字符串等可迭代对象
    """

    # 👇 关键修复：自定义打印格式
    def __str__(self) -> str:
        """
        返回集合的字符串表示
        """
        return f"{self._set_data}"

    # 👇 可选：让交互式环境中也能直观显示
    def __repr__(self) -> str:
        return f"CustomSetHandler({self._set_data})"

    def __init__(self, input_data: Optional[Iterable[Any]] = None):
        """
        初始化：将任意可迭代输入转为集合
        :param input_data: 可迭代数据（默认空），非可迭代类型会抛出TypeError
        """
        # 初始化空集合
        self._set_data: Set[Any] = set()

        # 处理输入数据：若传入数据则转为集合
        if input_data is not None:
            # 校验是否为可迭代类型（排除字符串的特殊情况？可选）
            if not isinstance(input_data, Iterable):
                raise TypeError(f"输入类型 {type(input_data)} 不可迭代，请传入列表、元组、字符串等可迭代对象")

            self._set_data = set(input_data)

    def insert(self, element: Any) -> bool:
        """
        插入元素
        :param element: 待插入元素
        :return: 插入成功（元素不存在）返回True，重复返回False
        """
        if element not in self._set_data:
            self._set_data.add(element)
            return True
        return False

    def contains(self, element: Any) -> bool:
        """
        查询元素是否存在
        :param element: 任意类型待查询元素
        :return: 存在返回True，不存在返回False
        """
        return element in self._set_data

    def delete(self, element: Any) -> bool:
        """
        删除指定元素（元素不存在时返回False，避免KeyError）
        :param element: 待删除元素
        :return: 删除成功返回True，元素不存在返回False
        """
        if element in self._set_data:
            self._set_data.remove(element)
            return True
        return False

    def get_set(self) -> Set[Any]:
        """
        返回当前集合（副本）
        """
        return self._set_data.copy()

    def clear(self) -> None:
        """清空集合"""
        self._set_data.clear()


if __name__ == "__main__":
    # 1. 测试1：输入列表（最常用场景）
    list_input = [1, 2, 2, 3, "a", "b"]
    set1 = CustomSetHandler(list_input)
    print("列表转集合：", set1)  # 输出：CustomSetHandler({1, 2, 3, 'a', 'b'})

    # 2. 测试2：输入元组
    tuple_input = (10, 20, 20, 30)
    set2 = CustomSetHandler(tuple_input)
    print("元组转集合：", set2)  # 输出：CustomSetHandler({10, 20, 30})

    # 3. 测试3：输入字符串（按字符拆分）
    str_input = "hello"
    set3 = CustomSetHandler(str_input)
    print("字符串转集合：", set3)  # 输出：CustomSetHandler({'h', 'e', 'l', 'o'})

    # 4. 测试4：输入字典（自动取key）
    dict_input = {"name": "张三", "age": 18, "gender": "男"}
    set4 = CustomSetHandler(dict_input)
    print("字典转集合（取key）：", set4)  # 输出：CustomSetHandler({'name', 'age', 'gender'})

    # 5. 核心功能测试
    set5 = CustomSetHandler([1, 2, 3])
    print("插入元素4：", set5.insert(4))  # True
    print("重复插入2：", set5.insert(2))  # False
    print("查询元素3：", set5.contains(3))  # True
    print("删除元素1：", set5.delete(1))  # True
    print("删除不存在的5：", set5.delete(5))  # False
    print("最终集合：", set5.get_set())  # {2, 3, 4}

