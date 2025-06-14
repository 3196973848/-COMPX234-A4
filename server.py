import socket
import sys
import hashlib
import os

def calculate_md5(filename):
    """计算文件的MD5哈希值"""
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
def main():
    """UDP文件传输服务器主函数"""
    # 步骤2：启动服务器 - 检查命令行参数
    if len(sys.argv) != 2:
        print("Usage: python3 UDPServer.py <server_port>")
        sys.exit(1)
    
    server_port = int(sys.argv[1])
    
    # 创建UDP套接字并绑定到指定端口
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', server_port))
    
    print(f"Server started on port {server_port}")
    print("Waiting for client requests...")