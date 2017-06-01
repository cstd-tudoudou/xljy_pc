
from py2neo import Graph

f = str(open('config', 'rt').read())
f=eval(f)
graph = Graph("http://localhost:7474/db/data", user=f['user'], password=f['password'])


# 返回所有点及信息,返回id和姓名dictidna
# [{'ID': 'bfed69a', '名字': 'taozhuo', '粉丝数': '233', '姓名': '陶卓', '用户名': '陶卓', '头像': '未知'}, {'ID': 'd0874b5', '名字': 'sillyy123', '粉丝数': '1', '姓名': '8班-王泽鑫', '用户名': '8班-王泽鑫', '头像': '/static/img/m.png'}, {'ID': 'b1a5228', '名字': '727720811', '粉丝数': '1', '姓名': '7班-王自豪', '用户名': '7班-王自豪', '头像': '/static/img/m.png'}, {'ID': 'bfbac39', '名字': 'paper', '粉丝数': '1', '姓名': '7班-常丛丛', '用户名': '7班-常丛丛', '头像': '/static/img/m.png'}, {'ID': 'e96c9df', '名字': '7-gaoliang', '粉丝数': '0', '姓名': '7班-高亮', '用户名': '7班-高亮', '头像': '/static/img/m.png'},...]
def get_da():
    data_username = "名字";fan_num = "粉丝数";name = "姓名";nickname = "用户名";picture = "头像";resu = [];dictidna={}
    results = graph.data("MATCH (n) RETURN n")
    for result in results:
        # res=copy.deepcopy(result)
        result = str(result['n'])
        ID = result[1:8]
        result = "{\"ID\":\"" + ID + "\"," + result.split("{")[1][0:-2] + "}"
        r=eval(result)
        resu.append(r)
        dictidna[r['ID']]=r['姓名']
    # print(dictidna)
    return resu,dictidna

# 返回节点之间点关系
# [['a68b1c9', 'cb77aef'], ['d910583', 'cb77aef'], ['c4884cf', 'cb77aef'], ['fe860ad', 'cb77aef'],。。。]
def get_li():
    links_list = []
    links = graph.data('MATCH ()-[r]->() RETURN r')
    for link in links:
        f = str(link['r'])[1:8]
        e = str(link['r'])[-8:-1]
        links_list.append([f, e])
    # print(links_list)
    return links_list


# 重组函数
# {
#     "name": "九門道",
#     "symbolSize": 5,
#     "draggable": "False",
#     "value": 0,
#     "category": "战争史研究WHS"
# }

# "source": "新浪体育",
# "target": "阿根廷人小马"
def reorganization():
    fi=[];li={};resu=[];se=[];th=[];t={};id=0
    detailed,dic=get_da()
    links=get_li()
    for m in detailed:
        li={};t={}
        li["id"]=m["ID"]
        li["name"]=m["姓名"]
        li["symbolSize"]=7
        li["draggable"]="False"
        li["value"]=0
        # li["category"]="陶卓"
        li["label"]={"normal":{"show": "True"}}
        t["name"]=m["姓名"]
        fi.append(li);th.append(t)
    del m
    resu.append(fi)
    for m in links:
        li={}
        try:
            li["source"] = m[0]
            li["target"] = m[1]
        except:
            pass
        se.append(li)
    resu.append(se)
    resu.append(th)
    resu.append("雪梨教育用户关系爬虫系统实现，土豆豆出品")
    # print(resu)
    return resu


def delete():
    graph.delete_all()

