import socket
import sys
import hashlib
import os

def calculate_md5(data):
    """计算数据的MD5哈希值"""
    hash_md5 = hashlib.md5()
    hash_md5.update(data)
    return hash_md5.hexdigest()
def main():
    """UDP文件传输客户端主函数"""
    # 步骤3：启动客户端 - 检查命令行参数
    if len(sys.argv) != 4:
        print("Usage: python3 UDPClient.py <server_hostname> <server_port> <files.txt>")
        sys.exit(1)
    
    server_hostname = sys.argv[1]
    server_port = int(sys.argv[2])
    files_list = sys.argv[3]
    
    # 创建UDP套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)