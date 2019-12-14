import subprocess
import threading
import time
class Ping:
    def __call__(self,host):
        result = subprocess.run(
            'ping -c2 %s &> /dev/null' % host, shell=True
        )
        if result.returncode == 0:
            print('%s:up' % host)
        else:
            print('%s:down' % host)

if __name__ == '__main__':
    ips = ['176.19.5.%s' % i for i in range(1, 255)]
    print(time.ctime())
    for ip in ips:
        #创建Ping的实例
        t = threading.Thread(target=Ping(), args=(ip,))
        # 启动线程，即执行target(*args)
        t.start()
    print(time.ctime())