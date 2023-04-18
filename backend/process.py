import sys
import rda
def process(binary_path):
    # 此处用 binary_path 变量代替实际的二进制文件路径
    # 在此处添加处理二进制文件的代码
    # ...

    # 将 stdout 输出
    func_name = 'doSystem'
    arg_pos = 1
    rda.check_function(binary_path,func_name,arg_pos)
    #sys.stdout.write("Some output")

if __name__ == "__main__":
    binary_path = sys.argv[1]
    process(binary_path)
