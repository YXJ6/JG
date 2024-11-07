import socket

server_ip = input("Enter server IP: ")#输入IP
server_port = int(input("Enter server port: "))#输入端口号

# 创建UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
file_path = input("Enter the path of the file to send: ")#输入要发送的文件路径
# 打开要发送的文件
with open(file_path, 'rb') as file:
    while True:
        # 读取文件内容
        data = file.read(1024)#最多读取1024字节
        if not data:
            break  # 文件读取完毕
        # 发送数据
        client_socket.sendto(data, (server_ip, server_port))

# 发送一个空包表示文件传输完成
client_socket.sendto(b'', (server_ip, server_port))

print("File sent successfully.")#提示发送完成

# 关闭socket
client_socket.close()

#运行环境：Windows下的PyCharm
