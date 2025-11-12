# 创建一个字典
nums = {}
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    # 查看字典是否记录了该级台阶及对应方法数
    if n in nums:
        return nums[n]
    # 递归关系
    nums[n] = f(n-1)+f(n-2)
    return nums[n]
print(f(999))



