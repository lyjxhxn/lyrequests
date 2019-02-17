import requests,re
from pymysql import connect
from random import choice
from retrying import retry
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 屏蔽 证书验证错误代码
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class LYRequests(object):
    def __init__(self):
        self.conn = connect(host='127.0.0.1',port=3306,database='proxy_ip',user='root',password='123',charset='utf8')
        self.cursor = self.conn.cursor()
        self.cursor.execute("select ip from ip_pool;")
        self.ip_list= self.cursor.fetchall()
        
    
    def __del__(self):
        
        self.cursor.close() # 关闭游标
        self.conn.close() # 关闭连接

    # def execute_sql(self,sql):
        
        # self.cursor.execute(sql) #执行sql命令
        # self.conn.commit()
    
    def Ip_get(self):
        ip = choice(self.ip_list)[0]
        proxies = {
            "http":"http://" + ip,
            "https":"https://" + ip,
        }
        return proxies

    def __headers(self):

        return [
            # safari 5.1 – MAC
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            # safari 5.1 – Windows
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            # IE 9.0
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
            # IE 8.0
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
            # Firefox 4.0.1 – MAC
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            # Firefox 4.0.1 – Windows
            "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
            # Opera 11.11 – MAC
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
            # Opera 11.11 – Windows
            "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
            # Chrome 17.0 – MAC
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            # 傲游（Maxthon）
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
            # 腾讯TT
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
            # 世界之窗（The World） 2.x
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            # 世界之窗（The World） 3.x
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
            # 搜狗浏览器 1.x
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
            # 360浏览器
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
            # Avant
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
            # Green Browser
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            # 移动设备端：
            # safari iOS 4.33 – iPhone
            "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            # safari iOS 4.33 – iPod Touch
            "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            # safari iOS 4.33 – iPad
            "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
            # Android N1
            "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            # Android QQ浏览器 For android
            "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            # Android Opera Mobile
            "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
            # Android Pad Moto Xoom
            "Mozilla/5.0 (LinuxUAndroid 3.0en-us Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
            # BlackBerry
            "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
            # WebOS HP Touchpad
            "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
            # Nokia N97
            "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
            # Windows Phone Mango
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
            # UC无
            "UCWEB7.0.2.37/28/999",
            # UC标准
            "NOKIA5700/ UCWEB7.0.2.37/28/999",
            # UCOpenwave
            "Openwave/ UCWEB7.0.2.37/28/999",
            # UC Opera
            "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999", ]

    def UserAgent_get(self):
        """随机返回一个 User-Agent
        
        Returns:
            [type] -- "User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
        """

        # return {"User-Agent": self.__headers()[randint(0, len(self.__headers())-1)]}
        return {"User-Agent": choice(self.__headers())}

    @retry(stop_max_attempt_number=5)
    def _parse_url(self,url,method,data,proxies,verify):
        if method=="POST":
            response = requests.post(url,data=data,headers=self.UserAgent_get(),timeout=5,proxies=self.Ip_get(),verify=verify)
        else:
            response = requests.get(url,headers=self.UserAgent_get(),timeout=5,proxies=self.Ip_get(),verify=verify)
        assert  response.status_code == 200
        return response

    def parse_url(self,url,method="GET",data=None,proxies={},verify=True):
        try:
            html_str = self._parse_url(url,method,data,proxies,verify)
        except:
            html_str = None
        return html_str

if __name__ == "__main__":
    url = "https://ip.cn/"
    ly = LYRequests()
    html = ly.parse_url(url,verify=False)
    ip = re.search(r"<code>(.*?)</code>",html.text).group(1)
    print(ip)