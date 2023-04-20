from cfgexplorer import cfg_explore
import sys


if __name__ == "__main__":
    binary_path = sys.argv[1]
    if binary_path:
        cfg_explore(binary_path,launch=False,output='./cfg_output.svg')
    else: 
        print("can't CFG")