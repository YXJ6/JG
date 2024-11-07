import socket

server_ip = '192.168.103.131'  # 监听IP地址
server_port = 12345#监听的端口号

# 创建UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定IP和端口
server_socket.bind((server_ip, server_port))

print(f"Server is listening on {server_ip}:{server_port}")#正在监听中

# 打开文件准备以二进制写入
with open('received_file.txt', 'wb') as file:
    while True:
        # 接收数据和客户端地址
        data, addr = server_socket.recvfrom(1024)
        if data:
            print(f"Received data from {addr}")#提示接收来源
            file.write(data)#将接收到的数据写入文件
            if len(data) < 1024:
                break  # 文件传输完成

print("File transfer completed.")
# 关闭socket释放资源
server_socket.close()

#运行环境：ubuntu