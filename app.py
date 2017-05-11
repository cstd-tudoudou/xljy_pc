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


# 運行主函數
if __name__=="__main__":
    start_user="taozhuo"   # 起始用戶網址 陶老師的粉絲實在太多了，所以就從陶老師下手了，【壞笑】
    page_data = get_db.get_page(start_user)
    data,page_username=get_db.get_data(page_data)


