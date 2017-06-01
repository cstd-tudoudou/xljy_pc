import os
from py2neo import Graph

def init():
    print("歡迎使用雪梨教育爬蟲系統-土豆豆出品，首次運行，即將進入初始化")
    user=input("請輸入neo4j資料庫的使用者名")
    paw=input("請輸入neo4j資料庫的密碼")
    with open('config', 'wt') as f:
        f.write("{\"user\":\""+user+"\",")
        f.write("\"password\":\""+paw+"\"}")
    f = str(open('config', 'rt').read())
    f=eval(f)
    # graph = Graph("http://localhost:7474/db/data", user="neo4j", password="neo4j")
    try:
        try:
            try:
                graph = Graph("http://localhost:7474/db/data", user=f['user'], password=f['password'])
            except OSError:
                print("未安裝neo4j資料庫，請安裝後在運行")
                os._exit(1)
        except:
            print("neo4j的使用者名密碼錯誤")
    except:
        print("未知程式錯誤，即將終止，請回饋ctudoudou@foxmail.com進行修復")
        os._exit(1)

