
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'first_name': 'Nohossat',
    'last_name' : 'TRAORE',
    'address' : '9 rue Léon Giraud · PARIS · FRANCE',
    'job': 'Web developer',
    'tel': '0678282923',
    'email': 'nohossat.tra@yahoo.com',
    'description' : 'Suite à une expérience internationale en développement web et dans le domaine des arts, l’impact de l’intelligence artificielle dans nos vies me surprend de jour en jour. \n Aujourd’hui, je souhaite changer de cap et comprendre les secrets que recèlent nos données. J’aimerais mettre à profit ces découvertes au service des entreprises/associations à dimension sociale.',
    'social_media' : [
        {
            'link': 'https://www.facebook.com/nono',
            'icon' : 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/nono',
            'icon' : 'fa-github'
        },
        {
            'link': 'linkedin.com/in/nono',
            'icon' : 'fa-linkedin-in'
        },
        {
            'link': 'https://twitter.com/nono',
            'icon' : 'fa-twitter'
        }
    ],
    'img': 'img/img_nono.jpg',
    'experiences' : [
        {
            'title' : 'Web Developer',
            'company': 'AZULIK',
            'description' : 'Project manager and lead developer for several AZULIK websites.',
            'timeframe' : 'July 2018 - November 2019'
        },
        {
            'title' : 'Freelance Web Developer',
            'company': 'Independant',
            'description' : 'Create Wordpress websites for small and medium companies. ',
            'timeframe' : 'February 2017 - Present'
        },
        {
            'title' : 'Sharepoint Intern',
            'company': 'ALTEN',
            'description' : 'Help to manage a 600 Sharepoint sites platform (audit, migration to Sharepoint newer versions)',
            'timeframe' : 'October 2015 - October 2016'
        }
    ],
    'project':[
        {"name":"project1",
         "text":"使用语言"
        },
{"name":"project2",
         "text":"使用语言"
        }   ,
{"name":"project3",
         "text":"使用语言"
        }
    ],
    'education' : [
        {
            'university': 'Paris Diderot',
            'degree': 'Projets informatiques et Startégies d\'entreprise (PISE)',
            'description' : 'Gestion de projets IT, Audit, Programmation',
            'mention' : 'Bien',
            'timeframe' : '2015 - 2016'
        },
        {
            'university': 'Paris Dauphine',
            'degree': 'Master en Management global',
            'description' : 'Fonctions supports (Marketing, Finance, Ressources Humaines, Comptabilité)',
            'mention' : 'Bien',
            'timeframe' : '2015'
        },

        {
            'university': 'Lycée Turgot - Paris Sorbonne',
            'degree': 'CPGE Economie & Gestion',
            'description' : 'Préparation au concours de l\'ENS Cachan, section Economie',
            'mention' : 'N/A',
            'timeframe' : '2010 - 2012'
        }
    ],
    'programming_languages' : {
        'HMTL' : ['fa-html5', '100'], 
        'CSS' : ['fa-css3-alt', '100'], 
        'SASS' : ['fa-sass', '90'], 
        'JS' : ['fa-js-square', '90'],
        'Wordpress' : ['fa-wordpress', '80'],
        'Python': ['fa-python', '70'],
        'Mongo DB' : ['fa-database', '60'],
        'MySQL' : ['fa-database', '60'],
        'NodeJS' : ['fa-node-js', '50']
    },
    'languages' : {'French' : 'Native', 'English' : 'Professional', 'Spanish' : 'Professional', 'Italian' : 'Limited Working Proficiency'},
    'interests' : ['Dance', 'Travel', 'Languages']
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
                           graphJSON8=gm8(),graphJSON9=gm9(),graphJSON10=gm10())
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
    fig =px.line_geo(
        df[df["year"]=="2002"],
        locations="iso_alpha",
        color=px.colors.sequential.Plasma,
    projection="orthographic")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

#10 矩阵式树状结构图
def gm10():
    df = px.data.gapminder()
    fig =px.treemap(
    df[df["year"]=="2002"], # 数据
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
