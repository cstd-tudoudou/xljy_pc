#coding=utf-8
# 編寫：土豆豆
# 時間：2017年5月7日
# 代碼說明：數據庫編輯模塊
# 項目網址：https://github.com/cstd-tudoudou/xljy_pc
# 碼雲：https://git.oschina.net/doudoutu
# github：https://github.com/cstd-tudoudou
# 完成狀態：未完成

# 導入數據庫包文件（在此使用py2neo作爲連接包）
from py2neo import Graph,Node,Relationship

# 建立數據庫連接
f = str(open('config', 'rt').read())
f=eval(f)
graph = Graph("http://localhost:7474/db/data", user=f['user'], password=f['password'])
con=graph.begin()


# 插入節點數據並連接函數  A -> B
def insert_connect_data(Type="People",A=["name","data-username","nickname","fan_num","png"],B=["name","data-username","nickname","fan_num","png"],relation=":KNOW"):
    try:
        if not A[1]=="data-username" or B[1]=="data-username":
            a = Node(
                Type,
                name=A[0],
                data_username=A[1],
                nickname=A[2],
                fan_num=A[3],
                picture=A[4]
            )
            b = Node(
                Type,
                name=B[0],
                data_username=B[1],
                nickname=B[2],
                fan_num=B[3],
                picture=B[4]
            )
            create_node(a)
            create_node(b)
            create_connection(a,b,relation)
        else:
            print("節點名稱異常錯誤")
            return False
    except:
        print("節點插入異常錯誤")
        return False


# 查找節點
def find_node(Type,key,value):
    try:
        node=graph.find_one(
            Type,
            key,
            value
        )
        try:
            node["nickname"]
            return True,node
        except:
            return False
    except:
        print("節點查找模塊異常")



# 建立節點關系 A->b
def create_connection(a,b,relation):
    try:
        con=graph.begin()
        ab=Relationship(a,relation,b)
        con.create(ab)
        con.commit()
        # graph.exists(ab)
    except:
        print("節點關系創建失敗")



# 創建節點
def create_node(node):
    con=graph.begin()
    con.create(node)
    con.commit()



# 查找節點並連接  b -> a
def connect(a=["Type","key","value"],Type="People",B=[],relation=":KNOW"):
    try:
        b = Node(
            Type,
            name=B[0],
            data_username=B[1],
            nickname=B[2],
            fan_num=B[3],
            picture=B[4]
        )
        con = graph.begin()
        create_node(b)
        bo, node = find_node(a[0], a[1], a[2])
        ab = Relationship(b, relation, node)
        con.create(ab)
        con.commit()
    except:
        print("查找節點並連接模塊異常")

def create_nodeonly(Type,A):
    A = Node(
        Type,
        name=A[0],
        data_username=A[1],
        nickname=A[2],
        fan_num=A[3],
        picture=A[4]
    )
    create_node(A)





# def buildNodes(nodeRecord):
#     data = {"id": str(nodeRecord.n._id), "label": next(iter(nodeRecord.n.labels))}
#     data.update(nodeRecord.n.properties)
#
#     return {"data": data}
#
# def buildEdges(relationRecord):
#     data = {"source": str(relationRecord.r.start_node._id),
#             "target": str(relationRecord.r.end_node._id),
#             "relationship": relationRecord.r.rel.type}
#
#     return {"data": data}
#
# def get_graph():
#     # nodes = map(buildNodes, graph.cypher.execute('MATCH (n) RETURN n'))
#     # edges = map(buildEdges, graph.cypher.execute('MATCH ()-[r]->() RETURN r'))
#     nodes = map(buildNodes, graph.data('MATCH (n) RETURN n'))
#     edges = map(buildEdges, graph.data('MATCH ()-[r]->() RETURN r'))
#
#     return jsonify(elements={"nodes": nodes, "edges": edges})



# 調試代碼區



# def test_1(Type,value):
#     selector = NodeSelector(graph)
#     node = selector.select(
#         Type,
#         data_username=value
#     )
#     print(type(node))       # <class 'py2neo.database.selection.NodeSelection'>
#     print(node)             # <py2neo.database.selection.NodeSelection object at 0x7f73a8c51d68>
#     print(list(node))       # [(d493bfa:People {data_username:"data_name",fan_num:"fan_num_1",name:"nane_1",nickname:"nickname_1",picture:"pngmap"})]
#     find=graph.find_one("People","data_username","data_name")
#     print(type(find))       # <class 'py2neo.types.Node'>
#     print(find)             # (cc64214:People {data_username:"data_name",fan_num:"fan_num_1",name:"nane_1",nickname:"nickname_1",picture:"pngmap"})
#     print(find['fan_num'])  # fan_num_1


# 測試此模塊使用函數
# if __name__=="__main__":
    # get_data()
    # database.insert_connect_data("People","NAMEA","NAMEB")
    # database.find_node()
    # database.insert_connect_data("People",["nane_1","data_name","nickname_1","fan_num_1","pngmap"],["nane_2","data_name_2","nickname_2","fan_num_2","pngmap_2"],":KNOW")
    # database.connect(["People","fan_num","fan_num_2"],"People",["nane_3","data_name3","nickname_3","fan_num_3","pngmap3"],":KNOW1")
    # database.find_node("People","fan_num","fan_num_1")
    # js=get_graph()
    # print(js)
