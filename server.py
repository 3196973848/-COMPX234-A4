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
    while True:
        # 接收客户端请求
        data, client_address = server_socket.recvfrom(1024)
        filename = data.decode('utf-8')
        print(f"Received request for file: {filename}")
        
        # 步骤1：文件准备 - 检查文件是否存在
        if not os.path.isfile(filename):
            server_socket.sendto("FILE_NOT_FOUND".encode('utf-8'), client_address)
            print(f"File {filename} not found")
            continue