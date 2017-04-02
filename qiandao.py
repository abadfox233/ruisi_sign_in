import re
import requests
import pickle
import time

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'
}

post_data={
    'formhash': '',
    'qdxq': 'fd',
    'qdmode': '3',
    'todaysay': '',
    'fastreply': '0'
}


def get_qiandao_index(session):
    print('正在请求界面。。。')
    try:
        result = session.get(url='http://rs.xidian.edu.cn/plugin.php?id=dsu_paulsign:sign')
        if result.status_code == 200:
            return result.text
    except:
        print('error')

def prase_frsah(html):
    print('正在解析formhash。。。')
    pattern1 = re.compile(r'<input type="hidden" name="formhash" value="(.*?)" />')
    formhash = pattern1.findall(html)
    return formhash

def qiandao(session):
    print('已获取formhash', post_data['formhash'], '正在签到。。。')
    try:
        result = session.post(url='http://rs.xidian.edu.cn/plugin.php?id=dsu_paulsign:sign&operation=qiandao&infloat=1&inajax=1',data=post_data)
        if result.status_code == 200:
            pattern1 = re.compile(r'<em id="return_win">(.*?)</em>')
            pattern = re.compile(r'<div class="c">\s+?(.*?)</div>')
            result2 = pattern.findall(result.text)
            result3 = pattern1.findall(result.text)
            print(result3[0], '\n', result2[0])
            time.sleep(0.5)
    except:
        print('error')


if __name__ =='__main__':
    session = requests.Session()
    session.headers = header
    with open('cookie.txt', 'rb') as f:  # load cookies
        cookies = requests.utils.cookiejar_from_dict(pickle.load(f))
        session.cookies = cookies
    html = get_qiandao_index(session=session)
    post_data['formhash']=prase_frsah(html)
    qiandao(session)
