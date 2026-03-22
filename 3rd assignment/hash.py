class MultipleDict:
    def __init__(self, size: int):
        """
        :param size: 列表的长度
        """
        self.size: int = size
        self.table: list[list[tuple[str, int]]] = [[] for _ in range(size)]


    def _hash_function(self, key):
        """
        结合内置hash和取模，映射到数组索引
        :param key: 要哈希的键（可哈希类型：str/int/tuple等）
        :return: 数组索引（0 ~ size-1）
        """
        # hash(key) 返回唯一的哈希值（整数），取模确保索引在数组范围内
        return hash(key) % self.size


    def put(self, key: str, value: int) -> None:
        """
        向字典中增加元素

        :param key: 键
        :param value: 值
        """
        _hash_result: int = self._hash_function(key)
        bucket: list[tuple[str, int]] = self.table[_hash_result]

        for index, (old_key, old_value) in enumerate(bucket):
            # 如果有旧值就替换
            if key == old_key:
                bucket[index] = (key, value)
                return
        # 如果所有位置没有旧值，就追加
        else:
            bucket.append((key, value))


    def get(self, key: str) -> int | None:
        """
        获取键对应的值
        :param key: 键
        :return: 值，如果值不存在则返回None
        """
        _hash_result: int = self._hash_function(key)
        # 按计算结果找到对应桶
        bucket: list[tuple[str, int]] = self.table[_hash_result]
        # 桶内东西不多，直接线性查找
        for bucket_key, bucket_value in bucket:
            if bucket_key == key:
                return bucket_value
        # 遍历完未找到匹配键，返回None
        return None

    def delete(self, key: str) -> None:
        """
        删除键对应的值
        :param key: 键
        """
        _hash_result: int = self._hash_function(key)
        bucket: list[tuple[str, int]] = self.table[_hash_result]

        for index, (bucket_key, bucket_value) in enumerate(bucket):
            if key == bucket_key:
                del bucket[index]
        return None
        # 遍历并删除所有符合元素

    def __str__(self) -> str:
        """
        打印字典
        :return: 字典的字符串表示
        """
        items = {}
        for bucket in self.table:
            for key, value in bucket:
                items[key] = value
        return str(items)


multiple_dict = MultipleDict(size=12)
multiple_dict.put("abc", 1001)
multiple_dict.put("acd", 1002)
multiple_dict.put("abd", 1003)
print(multiple_dict.get("acd"))  # 输出: 1002
print(multiple_dict)  # 输出: {'abc': 1001, 'acd': 1002, 'abd': 1003}（顺序可能不同）