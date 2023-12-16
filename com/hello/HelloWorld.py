print('hello world!')
print("Hello, World!")

my_dict = {'a': 1, 'b': 2, 'c': 3}

# 遍历字典中的每一个键值对
for key, value in my_dict.items():
    # 打印出键和值
    print(f"{key}: {value}")


# 冒泡排序
def bubble_sort(arr):
    # 获取数组长度
    n = len(arr)
    # 遍历数组
    for i in range(n):
        # 内层循环，从i开始，到n-i-1结束
        for j in range(0, n - i - 1):
            # 如果arr[j]大于arr[j+1]，则交换位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# 示例
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("排序后的数组：")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
