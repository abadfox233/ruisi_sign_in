import requests , requests.utils , pickle #用来连接睿思后保存cookies
import re
from urllib.parse import urlencode

class creat_cookies(object):
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
    }
    data ={
        'formhash':'',
        'referer':'http://rs.xidian.edu.cn/portal.php',
        'username':'最美不过泡沫',
        'password':'6254d2fdd4d3f7a38054f38627d8c5f3',
        'questionid':'0',
        'answer':'',
        'cookietime':'2592000'
    }
    logindata ={
        'mod': 'logging',
        'action': 'login',
        'loginsubmit': 'yes',
        'frommessage': '',
        'loginhash':'',
        'inajax': '1'
    }


    def creat(self):

        p = requests.Session()
        p.headers = creat_cookies.header
        p1 = p.get('http://rs.xidian.edu.cn/member.php?mod=logging&action=login&infloat=yes&frommessage&inajax=1&ajaxtarget=messagelogin')
        html = p1.text
        pattern1 = re.compile(r'<input type="hidden" name="formhash" value="(.*?)" />')
        pattern2 = re.compile(r"'returnmessage3_(.*?)'")
        result1 = pattern1.findall(html)#获取postkey
        result2 = pattern2.findall(html)#获取loginkey
        creat_cookies.logindata['loginhash']= result2[0]
        creat_cookies.data['formhash']= result1[0]
        login = p.post(url='http://rs.xidian.edu.cn/member.php?'+urlencode(creat_cookies.logindata), data=creat_cookies.data)#登陆
        print(login.text)
        with open('cookie.txt', 'wb') as f:#保存cookies
            pickle.dump(requests.utils.dict_from_cookiejar(p.cookies), f)
