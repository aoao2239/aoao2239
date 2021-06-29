
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import csv, re, operator

app = Flask(__name__)

person = {
    'first_name': '熊',
    'last_name' : '佳慧',
    'address' : '湖北师范大学',
    'job': '后端工程师,微信小程序开发',
    'tel': '000-000-000',
    'email': 'qq邮箱',
    'description' : '描述语句',
    'img': 'img/img_nono.jpg',
    'experiences' : [
        {
            'title' :"飞机航班系统",
            'company': '学期实训',
            'description' : '通过运用java知识,进行文件读写操作,以及可视化界面操作,达到对机票航班的预订购买,订单的支付删除操作.',
            'timeframe' : ' 2018/12 -  2019/1'
        },
        {
            'title' : '团子记账微信小程序',
            'company': '3人小团体',
            'description' : '这是一个记账类微信小程序,可以实现设置预算,记录账单,获得自己的消费分类数据统计,账单清单等部分',
            'timeframe' : '2021/6月至今'
        },
        {
            'title' : '网上商城',
            'company': '个人',
            'description' : '运用javaweb,jdbc,springmvc框架,实现简单的网上购物商城,可进行登陆分类购买订单管理',
            'timeframe' : '2020 - 2021'
        }
    ],
    'project':[
        {"name":"英文取名大数据分析",
         "text":"python/爬虫开发"
        },
{"name":"网上商城",
         "text":"javaweb/Mysql/springMVC/JSP"
        }   ,
{"name":"机票航班系统",
         "text":"java/JDBC"
        }
    ],
    'education' : [
        {
            'university': '湖北师范大学',
            'degree': '软件工程22届本科毕业生',
            'description' : '计算机与信息工程学院',
            'mention' : 'aoao',
            'timeframe' : '2018- 2022'
        }
    ],
    'programming_languages' : {
        'java':3,
        "javaweb":3,
        'Python': 2,
        'MySQL' : 3,
        'HMTL' : 1,
        'CSS' : 1,
        'JS' :1
    },
    'languages' : {'普通话' : '二甲', 'English' : "CET4"},
    }

@app.route('/')
def cv(person=person):
    return render_template('index2.html', person=person)

@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(int(request.args.get('data')))
   
@app.route('/chart')
def index():
    return render_template('chartsajax.html',  graphJSON=gm(),graphJSON1=gm1(),graphJSON3=gm3(),graphJSON4=gm4(),graphJSON5=gm5(),graphJSON6=gm6(),graphJSON7=gm7(),
                           graphJSON8=gm8(),graphJSON9=gm9(),graphJSON10=gm10(),graphJSON11=gm11(),graphJSON12=gm12())
#1 花的种类花萼的宽和高的分布的散点图
def gm(species_id=1):
    df = pd.DataFrame(px.data.iris())
    fig=px.scatter(df[df["species_id"]==species_id], x="sepal_width", y="sepal_length", color="species")
    graphJSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    return graphJSON
#3 三种花萼总体分布图
def gm3():
    df = pd.DataFrame(px.data.iris())
    fig=px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    marginal_x="histogram",
    marginal_y="rug")
    graphJSON3 = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    return graphJSON3
#6 三种花萼的散点矩阵图
def gm6():
    df = pd.DataFrame(px.data.iris())
    fig=px.scatter_matrix(df,  # 传入绘图数据
                  dimensions=["sepal_width","sepal_length","petal_width","petal_length"],  # 维度设置
                  color="species")  # 颜色取值
    graphJSON6 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON6

#8 鸢尾花的花萼宽和花萼高的等高线图
def gm8():
    df=pd.DataFrame(px.data.iris())
    fig=px.density_contour(df,  # 数据集
                   x="sepal_width",  # xy轴
                   y="sepal_length",
                   color="species"  # 颜色取值
                  )
    graphJSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    return graphJSON

#2 年增长pop人数
def gm1():
    df=px.data.gapminder()
    fig=px.bar(df,x = "continent",y= "pop",color = "continent",animation_frame = "year",animation_group = "country",range_y = [0, 4000000000])
    graphJSON1 = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    return graphJSON1

#7 各地区的每年的
def gm7():
    df = px.data.gapminder()
    fig =px.choropleth(
        df,  # 数据
        locations="iso_alpha",  # 简称
        color="lifeExp",  # 颜色取值
        hover_name="country",  # 悬停数据
        animation_frame="year",  # 播放按钮设置
        color_continuous_scale=px.colors.sequential.Plasma,  # 颜色变化取值
        projection="natural earth"  # 使用的地图设置
        )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
#9 基于line_geo线型地图
def gm9():
    df = pd.DataFrame(px.data.gapminder())
    fig =px.line_geo(df.query("year==2007"), locations="iso_alpha",
            color="continent", projection="orthographic")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

#10 矩阵式树状结构图
def gm10():
    df = pd.DataFrame(px.data.gapminder())
    fig =px.treemap(
    df.query("year==2007"), # 数据
    path=[px.Constant('world'), 'continent', 'country'],   # 绘图路径：world---continent---country
    values='pop',  # 数据取值
    color='pop',   # 颜色取值
    hover_data=['iso_alpha'])  # 显示数据：国家简称
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
# 4 订单流水图
def gm4():
    df=px.data.tips()
    fig=px.scatter(df, x="total_bill", y="tip", color="size", facet_col="sex",
           color_continuous_scale=px.colors.sequential.Viridis,
           render_mode="webgl")
    graphJSON4 = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    return graphJSON4

#直方图，在图表的上方增加细条图,显示小费随着总账单的变化关系
def gm11():
    df = px.data.tips()
    fig =px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug",
             hover_data=df.columns)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

#12箱形图，设置使用槽口绘制框,显示天数账单和是否吸烟的关系
def gm12():
    df = px.data.tips()
    fig =px.box(df, x="day", y="total_bill", color="smoker", notched=True)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
#5 2013年蒙特利尔市长选举,不同区域结果图
def gm5():
    df=px.data.election()
    fig=px.scatter_3d(df, x="Joly", y="Coderre", z="Bergeron", color="winner",
              size="total", hover_name="district",symbol="result",
              color_discrete_map = {"Joly": "blue", "Bergeron": "green",
              "Coderre":"red"})
    graphJSON5 = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    return graphJSON5


























@app.route('/senti')
def main():
    text = ""
    values = {"positive": 0, "negative": 0, "neutral": 0}

    with open('ask_politics.csv', 'rt') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for idx, row in enumerate(reader):
            if idx > 0 and idx % 2000 == 0:
                break
            if  'text' in row:
                nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
                text = nolinkstext

            blob = TextBlob(text)
            for sentence in blob.sentences:
                sentiment_value = sentence.sentiment.polarity
                if sentiment_value >= -0.1 and sentiment_value <= 0.1:
                    values['neutral'] += 1
                elif sentiment_value < 0:
                    values['negative'] += 1
                elif sentiment_value > 0:
                    values['positive'] += 1

    values = sorted(values.items(), key=operator.itemgetter(1))
    top_ten = list(reversed(values))
    if len(top_ten) >= 11:
        top_ten = top_ten[1:11]
    else :
        top_ten = top_ten[0:len(top_ten)]

    top_ten_list_vals = []
    top_ten_list_labels = []
    for language in top_ten:
        top_ten_list_vals.append(language[1])
        top_ten_list_labels.append(language[0])

    graph_values = [{
                    'labels': top_ten_list_labels,
                    'values': top_ten_list_vals,
                    'type': 'pie',
                    'insidetextfont': {'color': '#FFFFFF',
                                        'size': '14',
                                        },
                    'textfont': {'color': '#FFFFFF',
                                        'size': '14',
                                },
                    }]

    layout = {'title': '<b>意见挖掘</b>'}

    return render_template('index2.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
