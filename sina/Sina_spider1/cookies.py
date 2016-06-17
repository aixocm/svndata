# encoding=utf-8
import json
import base64
import requests

"""
输入你的微博账号和密码，可去淘宝买，一元七个。
建议买几十个，微博限制的严，太频繁了会出现302转移。
或者你也可以把时间间隔调大点。
"""
myWeiBo = [
    {"no": "qyjdo40474@163.com", "psw": "tttt5555"},
    {"no": "lhyu62535@163.com", "psw": "tttt5555"},
    {"no": "chkrv0040@163.com", "psw": "tttt5555"},
    {"no": "nuobi04808602@163.com", "psw": "tttt5555"},
    {"no": "oeeq6294931@163.com", "psw": "tttt5555"},
    {"no": "gkon6506167@163.com", "psw": "tttt5555"},
    {"no": "afqq9005442@163.com", "psw": "tttt5555"},
    {"no": "ucku84684@163.com", "psw": "tttt5555"},
    {"no": "hfude2974@163.com", "psw": "tttt5555"},
    {"no": "uogjo2690@163.com", "psw": "tttt5555"},
    {"no": "ycuog7568@163.com", "psw": "tttt5555"},
    {"no": "kzqzz6221@163.com", "psw": "tttt5555"},
    {"no": "cuues47857@163.com", "psw": "tttt5555"},
    {"no": "mcsu69236@163.com", "psw": "tttt5555"},
    {"no": "mvoah14474@163.com", "psw": "tttt5555"},
    {"no": "fgnx7776@163.com", "psw": "tttt5555"},
    {"no": "mgcw3121@163.com", "psw": "tttt5555"},
    {"no": "jznx4302@163.com", "psw": "tttt5555"},
    {"no": "nrrb0802@163.com", "psw": "tttt5555"},
    {"no": "jjxbl8380@163.com", "psw": "tttt5555"},
    {"no": "mebbx14487@163.com", "psw": "tttt5555"},
    {"no": "nbfrx96006@163.com", "psw": "tttt5555"},
    {"no": "ldvxx81416@163.com", "psw": "tttt5555"},
    {"no": "neqw3708@163.com", "psw": "tttt5555"},
    {"no": "keqgi45551@163.com", "psw": "tttt5555"},
    {"no": "beiycijjy2256@163.com", "psw": "tttt5555"},
    {"no": "shibiyxvu7329@163.com", "psw": "tttt5555"},
    {"no": "zhufiztdg3530@163.com", "psw": "tttt5555"},
    {"no": "wengpmdfs9531@163.com", "psw": "tttt5555"},
    {"no": "xiangbxyzxt49@163.com", "psw": "tttt5555"},
    {"no": "zhanzabtci542@163.com", "psw": "tttt5555"},
    {"no": "jinnrwqf3511@163.com", "psw": "tttt5555"},
    {"no": "shenjuclwo395@163.com", "psw": "tttt5555"},
    {"no": "shunnaazko662@163.com", "psw": "tttt5555"},
    {"no": "leidefodm2869@163.com", "psw": "tttt5555"},
    {"no": "jiwhwfck3766@163.com", "psw": "tttt5555"},
    {"no": "xurolmpa9799@163.com", "psw": "tttt5555"},
    {"no": "zhouowxfpe085@163.com", "psw": "tttt5555"},
    {"no": "juanlgkdhz672@163.com", "psw": "tttt5555"},
    {"no": "fuiuegyy7627@163.com", "psw": "tttt5555"},
    {"no": "duuwmdpz3901@163.com", "psw": "tttt5555"},
    {"no": "caidmkelt8712@163.com", "psw": "tttt5555"},
    {"no": "tiaoexzrny873@163.com", "psw": "tttt5555"},
    {"no": "wannsvxuj3391@163.com", "psw": "tttt5555"},
    {"no": "tianfzhtoo200@163.com", "psw": "tttt5555"},
    {"no": "houcywcqs0363@163.com", "psw": "tttt5555"},
    {"no": "zhuzxxdfw8195@163.com", "psw": "tttt5555"},
    {"no": "bianugvehd052@163.com", "psw": "tttt5555"},
    {"no": "tijqksdr6737@163.com", "psw": "tttt5555"},
    {"no": "qianngfztd039@163.com", "psw": "tttt5555"},
    {"no": "kuokswxdo2456@163.com", "psw": "tttt5555"},
    {"no": "baccpmow1492@163.com", "psw": "tttt5555"},
    {"no": "queumyknk8538@163.com", "psw": "tttt5555"},
    {"no": "xingiviewm832@163.com", "psw": "tttt5555"},
    {"no": "guqraipw8908@163.com", "psw": "tttt5555"},
    {"no": "yipvdnqs2747@163.com", "psw": "tttt5555"},
    {"no": "jianeowddk901@163.com", "psw": "tttt5555"},
    {"no": "yinynjvg4034@163.com", "psw": "tttt5555"},
    {"no": "dangrgffjf222@163.com", "psw": "tttt5555"},
    {"no": "yanarrsda6404@163.com", "psw": "tttt5555"},
    {"no": "zpftv4650@163.com", "psw": "tttt5555"},
    {"no": "nvxdd3248@163.com", "psw": "tttt5555"},
    {"no": "kwnt92477@163.com", "psw": "tttt5555"},
    {"no": "ecski7412@163.com", "psw": "tttt5555"},
    {"no": "tlll30121@163.com", "psw": "tttt5555"},
    {"no": "ljfd15818@163.com", "psw": "tttt5555"},
    {"no": "wkqq42295@163.com", "psw": "tttt5555"},
    {"no": "dtzdv50774@163.com", "psw": "tttt5555"},
    {"no": "dtlv5495@163.com", "psw": "tttt5555"},
    {"no": "ywjk4102@163.com", "psw": "tttt5555"},
    {"no": "aoer9100@163.com", "psw": "tttt5555"},
    {"no": "mdxi6026@163.com", "psw": "tttt5555"},
    {"no": "utygy9610@163.com", "psw": "tttt5555"},
    {"no": "pymxp66867@163.com", "psw": "tttt5555"},
    {"no": "ptzlv7141@163.com", "psw": "tttt5555"},
    {"no": "tengatdgid999@163.com", "psw": "tttt5555"},
    {"no": "luvctnpa3136@163.com", "psw": "tttt5555"},
    {"no": "dianffwlsm015@163.com", "psw": "tttt5555"},
    {"no": "wajljhbf4858@163.com", "psw": "tttt5555"},
    {"no": "gelcebeg5516@163.com", "psw": "tttt5555"},
    {"no": "qippcxky7825@163.com", "psw": "tttt5555"},
    {"no": "xuiuccxi8073@163.com", "psw": "tttt5555"},
    {"no": "jielmsimm6176@163.com", "psw": "tttt5555"},
    {"no": "chengeutuoh39@163.com", "psw": "tttt5555"},
    {"no": "sangudcruc400@163.com", "psw": "tttt5555"},
    {"no": "xueuoqlw1938@163.com", "psw": "tttt5555"},
    {"no": "daictuymq0203@163.com", "psw": "tttt5555"},
    {"no": "nongbuopyj860@163.com", "psw": "tttt5555"},
    {"no": "qineysidm1748@163.com", "psw": "tttt5555"},
    {"no": "nongxzgabq750@163.com", "psw": "tttt5555"},
    {"no": "ranmoldnr7166@163.com", "psw": "tttt5555"},
    {"no": "bancjcrul0142@163.com", "psw": "tttt5555"},
    {"no": "guanfbgmrb731@163.com", "psw": "tttt5555"},
    {"no": "ganggwqjhc290@163.com", "psw": "tttt5555"},
    {"no": "xiangfncknb99@163.com", "psw": "tttt5555"},
    {"no": "xiangeuvbax83@163.com", "psw": "tttt5555"},
    {"no": "yanaotzyg2413@163.com", "psw": "tttt5555"},
    {"no": "rongkbbuze841@163.com", "psw": "tttt5555"},
    {"no": "yurhfsvq8309@163.com", "psw": "tttt5555"},
    {"no": "zaojvrxyr0225@163.com", "psw": "tttt5555"},
    {"no": "xiangggwpup78@163.com", "psw": "tttt5555"},
    {"no": "maihzsyrf7554@163.com", "psw": "tttt5555"},
    {"no": "shukzkplf2733@163.com", "psw": "tttt5555"},
    {"no": "baoiwolpi6089@163.com", "psw": "tttt5555"},
    {"no": "bodfwffx3575@163.com", "psw": "tttt5555"},
    {"no": "kanramvlu1328@163.com", "psw": "tttt5555"},
    {"no": "duravwcj6750@163.com", "psw": "tttt5555"},
    {"no": "gongpndtdt158@163.com", "psw": "tttt5555"},
    {"no": "yeruyeto8507@163.com", "psw": "tttt5555"},
    {"no": "fujcjtwq6790@163.com", "psw": "tttt5555"},
    {"no": "fanziqogb2912@163.com", "psw": "tttt5555"},
    {"no": "aigfqtqt6981@163.com", "psw": "tttt5555"},
    {"no": "fufjhheh1310@163.com", "psw": "tttt5555"},
    {"no": "xunmugkhq4541@163.com", "psw": "tttt5555"},
    {"no": "shihshjcy0961@163.com", "psw": "tttt5555"},
    {"no": "shenpcsexa521@163.com", "psw": "tttt5555"},
    {"no": "kuangjbeavu45@163.com", "psw": "tttt5555"},
    {"no": "zhuucsefq3468@163.com", "psw": "tttt5555"},
    {"no": "haiyxqdus6622@163.com", "psw": "tttt5555"},
    {"no": "mingusjheo962@163.com", "psw": "tttt5555"},
    {"no": "mingwcnowy323@163.com", "psw": "tttt5555"},
    {"no": "huantcwuer988@163.com", "psw": "tttt5555"},
    {"no": "wangngsctq910@163.com", "psw": "tttt5555"},
    {"no": "kaonaifxd9439@163.com", "psw": "tttt5555"},
    {"no": "fuwdbhhi1933@163.com", "psw": "tttt5555"},
    {"no": "biqvyqno3818@163.com", "psw": "tttt5555"},
]


def getCookies(weibo):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    for elem in weibo:
        account = elem['no']
        password = elem['psw']
        username = base64.b64encode(account.encode('utf-8')).decode('utf-8')
        postData = {
            "entry": "sso",
            "gateway": "1",
            "from": "null",
            "savestate": "30",
            "useticket": "0",
            "pagerefer": "",
            "vsnf": "1",
            "su": username,
            "service": "sso",
            "sp": password,
            "sr": "1440*900",
            "encoding": "UTF-8",
            "cdult": "3",
            "domain": "sina.com.cn",
            "prelt": "0",
            "returntype": "TEXT",
        }
        session = requests.Session()
        r = session.post(loginURL, data=postData)
        jsonStr = r.content.decode('gbk')
        info = json.loads(jsonStr)
        if info["retcode"] == "0":
            print "Get Cookie Success!( Account:%s )" % account
            cookie = session.cookies.get_dict()
            cookies.append(cookie)
        else:
            print "Failed!( Reason:%s )" % info['reason']
    return cookies


cookies = getCookies(myWeiBo)
print "Get Cookies Finish!( Num:%d)" % len(cookies)
