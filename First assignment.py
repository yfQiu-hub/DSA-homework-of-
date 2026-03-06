from typing import Iterable,Any

class DeleteItem:
    """
    从列表中删除元素
    """

    def __init__(self,iterable :Iterable[Any]):
        """
        :param  iterable :可迭代对象,从其内部删除元素
        """
        self.iterable = list(iterable)

    def delete(self,index_to_delete :int)->list[Any]:
        """
        从列表中删除元素

        :param index_to_delete:需要删除位置的索引
        :return: 返回删除后的新列表
        """
        if not isinstance(index_to_delete, int):
            raise TypeError("索引必须是整数类型")
        length_of_iterable = len(self.iterable)
        if 0 <= index_to_delete < len(self.iterable):
            # 切片创建新列表（不修改类内存储的原始列表）
            new_list = self.iterable[:index_to_delete] + self.iterable[index_to_delete + 1:]
        else:
            # 索引无效时，返回原始列表的拷贝
            new_list = self.iterable.copy()
        return new_list

    def get_original_list(self) -> list:
        """
        获取原始列表（返回拷贝，避免外部修改）
        """
        return self.iterable.copy()

# 测试示例
if __name__ == "__main__":
    # 1. 创建类实例
    my_list = [1, 2, 3, 4, 5]
    remover = DeleteItem(my_list)

    # 2. 测试正常删除（索引2）
    new_list1 = remover.delete(2)
    print("原始列表:", remover.get_original_list())  # 输出：[1, 2, 3, 4, 5]（原列表未变）
    print("删除索引2后的新列表:", new_list1)  # 输出：[1, 2, 4, 5]