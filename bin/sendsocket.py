import socket

class SendSocket:
    def send(self,ip,port,req):
        #链接本地
        tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        tcp_socket.connect((ip,port))
        #将xml格式转化 为bytest，计算bytest长度，并右对齐，指定长度，不够的补0
        stk_code=str(len(bytes(req,encoding="utf-8"))).zfill(6)
        final_data=stk_code+req#将发送长度与发送内容合并
        tcp_socket.send(bytes(final_data,encoding="utf-8"))
        data=tcp_socket.recv(2048).decode("utf-8")#接收数据
        newdata=data.replace(data[0:6],"")# 去掉返回报文前六个字段
        tcp_socket.close()
        return newdata
if __name__ == '__main__':
      cc=SendSocket()
      cc.send('ip',port,req)
#req:为xml配置文件，可直接拼接，也可配置一个配置文件，进行读取