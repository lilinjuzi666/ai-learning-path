print("这句话无论何时都会运行") # 1. 定义函数或变量时，通常会运行

def my_function():
    print("我是函数里的代码")

print(f"当前的 __name__ 是: {__name__}") # 2. 打印当前身份

if __name__ == "__main__":
    print("我是被直接运行的，所以执行了 main")
    my_function()
else:
    print("我是被导入的，所以跳过了 main")
