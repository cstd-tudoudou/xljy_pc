#coding=utf-8
# 編寫：土豆豆
# 時間：2017年5月7日
# 代碼說明：主文件
# 項目網址：https://github.com/cstd-tudoudou/xljy_pc
# 碼雲：https://git.oschina.net/doudoutu
# github：https://github.com/cstd-tudoudou
# 完成狀態：未完成

import get_db
import database
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def run():
    database.create_nodeonly('People', ["陶卓", 'taozhuo', "陶卓", '233', '未知'])  # 先建立一個陶老師的節點
    # start_user = "taozhuo"  # 起始用戶網址 陶老師的粉絲實在太多了，所以就從陶老師下手了，【壞笑】
    num = 0;
    username = ['taozhuo'];
    username_using = [""]
    error = 0
    while error < 1000:
        start_user = str(username[num])
        if username[num] not in username_using:
            page_data = get_db.get_page(start_user)
            data, un = get_db.get_data(page_data)
            r = len(data)
            for a in range(r):
                database.connect(['People', 'data_username', start_user], 'People', data[a], ":follow")
            username.extend(un)
            num += 1
            error=0
        else:
            error += 1
        username_using.append(start_user)

@app.route('/graph')
def get():
    import api
    end=api.reorganization()
    return jsonify(end)

@app.route('/')
def index():
    return render_template('index.html')

# 運行主函數
if __name__=="__main__":

    # run()
    # app.config['JSON_AS_UTF'] = False
    app.config['JSON_AS_ASCII']=False
    app.run(debug=True)
    # database.insert_connect_data("People",data[0],["陶卓",'taozhuo',"陶卓",'233','未知'],":KNOW")
    # print(len(page_username))
    # for a in range(2,233):
    #     database.connect(['People', 'data_username', 'taozhuo'], 'People', data[a], ':KNOW')
