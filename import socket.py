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
    with open(files_list, 'r') as f:
        files = [line.strip() for line in f if line.strip()]
    
    for filename in files:
        print(f"Requesting file: {filename}")
        
        # 发送文件请求
        client_socket.sendto(filename.encode('utf-8'), (server_hostname, server_port))
        
        # 接收响应
        data, server_address = client_socket.recvfrom(1024)
        response = data.decode('utf-8')
        
        # 处理文件不存在的情况
        if response == "FILE_NOT_FOUND":
            print(f"File {filename} not found on server")
            continue
        
        # 接收MD5校验和
        expected_md5 = response
        
        # 接收文件内容
        file_data = bytearray()
        while True:
            try:
                # 设置超时以检测文件传输结束
                client_socket.settimeout(1.0)
                data, server_address = client_socket.recvfrom(1024)
                file_data.extend(data)
            except socket.timeout:
                break