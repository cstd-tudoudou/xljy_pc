#coding=utf-8
# 編寫：土豆豆
# 時間：2017年5月7日
# 代碼說明：網站數據分析模塊
# 項目網址：https://github.com/cstd-tudoudou/xljy_pc
# 碼雲：https://git.oschina.net/doudoutu
# github：https://github.com/cstd-tudoudou
# 完成狀態：未完成

import urllib.request as ure
from bs4 import BeautifulSoup

# 標準請求頭
weburl = "http://www.edu2act.cn"
webheader = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586',
    'Host': 'www.edu2act.cn',
    'DNT': '1'
}

# 全局變量區，節省一下內存使用
username=[];src=[];funnum=[];name=[];da=""


# 根據用戶名獲取網站並分析構架網站代碼
# 傳入用戶名
def get_page(user):
    user_url = weburl + "/" + user + "/fans/"
    result = ure.Request(url=user_url, headers=webheader)
    webPage = ure.urlopen(result)
    data = webPage.read()
    data = data.decode('UTF-8')
    data = BeautifulSoup(data, "lxml")
    return data


# 獲取梳理數據，並分析取出有效值
def get_urimg(data):
    username=[];src=[];funnum=[];name=[]
    num=0
    for a in data.find_all("img", class_="fans-img at-popup"):
        usna=str(data.find_all("img", class_="fans-img at-popup")[num].attrs.get("data-username"))
        username.append(usna)
        src.append(str(data.find_all("img", class_="fans-img at-popup")[num].attrs.get("src")))
        name.append(str(data.find_all("span", class_="nickname")[num].string))
        # id="id_fans_count"+str(username[num])
        id_="id_fans_count"+usna
        funnum.append(str(data.find_all("span", id=id_)[0].string))
        num+=1
    return username,src,funnum,name


# 調用分析網站數據函數，返回打包好的數據結果
def get_data(processed_data):
    username,imgsrc,fun,name=get_urimg(processed_data)
    da=zip(name,username,name,fun,imgsrc)
    src = [];funnum = [];name = []
    return list(da),username


# # 測試此模塊使用函數
# if __name__=="__main__":
#     page_data=get_page("taozhuo")
#     data,page_username=get_data(page_data)





