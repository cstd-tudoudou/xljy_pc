/**
 * Created by apple on 2017/6/1.
 */
// 获取数据
var uploadedDataURL = "/graph";
// 基于准备好的dom，初始化echarts实例
// var uploadedDataURL = "http://gallery.echartsjs.com/asset/get/s/data-1495595908173-rk2KsOfWb.json";

$.getJSON(uploadedDataURL, function(linedata) {
    var data = linedata[0];
    var links = linedata[1];
    var categories = linedata[2];
    var cont = linedata[3];
    var mid = linedata[4];
    var user1 = linedata[5];
    option = {

        title: {
            text: "雪梨教育用户关系数据系统",
            subtext: '@土豆豆',
            sublink: mid,
            top: "top",
            left: "center"
        },

        tooltip: {},

        toolbox: {
            show: true,
            feature: {
                dataView: {
                    show: true,
                    readOnly: true
                },
                restore: {
                    show: true
                },
                saveAsImage: {
                    show: true
                }
            }
        },
        animationDuration: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [{
            name: '雪梨教育',
            type: 'graph',
            layout: 'force',

            force: {
                //initLayout:'circular'
                edgeLength: 50,
                repulsion: 100,
                gravity: 0.9
            },
            data: data,
            edges: links,
            categories: categories,
            focusNodeAdjacency: true,
            roam: true,
            label: {
                normal: {
                    position: 'right',
                    formatter: '{b}'
                }
            },
            lineStyle: {
                normal: {
                    //color: 'target',
                    curveness: 0
                }
            }
        }]
    };
    myChart.setOption(option)
})
