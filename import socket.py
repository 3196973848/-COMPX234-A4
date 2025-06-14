import socket
import sys
import hashlib
import os

def calculate_md5(data):
    """计算数据的MD5哈希值"""
    hash_md5 = hashlib.md5()
    hash_md5.update(data)
    return hash_md5.hexdigest()
