# Movie Knowledge Graph

## 项目介绍：

本项目是为北航知识工程大作业。主要展示了由影视及相关出版物的数据构建的知识图谱。(!!! 项目未完全提交，不要clone)


## 目录结构：

```
.
├── Doc
├── Neo4j               //存放空间数据库Neo4j的数据脚本
│   └── Scripts
│       └── moive.txt
├── README.md           //项目介绍
└── web
    └── movie           
        ├── db.sqlite3
        ├── manage.py   //启动脚本
        ├── model       //数据模型层：获取neo4j数据，以及CSV数据
        │   ├── __init__.py
        │   ├── neo_models.py
        ├── movie       //业务控制层：网站业务
        │   ├── __init__.py
        │   ├── __init__.pyc
        │   ├── detail_view.py
        │   ├── index_view.py
        │   ├── relation_view.py
        │   ├── settings.py
        │   ├── urls.py
        │   ├── wsgi.py
        ├── static   //网站静态资源
        │   ├── css
        │   │   └── jquery-ui-1.10.4.min.css
        │   ├── img
        │   └── js
        │       ├── echarts.common.min.js
        │       ├── jquery-1.8.3.min.js
        │       └── jquery-ui-1.10.4.min.js
        ├── templates //视图层，网站页面模版
        │   ├── 404.html
        │   ├── base.html
        │   ├── detail.html
        │   ├── entity.html
        │   └── index.html
        └── toolkit  //工具集，数据库连接，数据分析，分词
            ├── __init__.py
            ├── pre_load.py
            └── pre_load.pyc

```



## 数据资源获取

- wikipedia电影词条
- 互动百科 

## Neo4j数据组织

```
MATCH (p {name: "Tom Hanks"}) RETURN p

MATCH (p {title: "The Matrix"}) RETURN p

MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(tomHanksMovies) RETURN tom,tomHanksMovies


MATCH (cloudAtlas {title: "Cloud Atlas"})<-[:DIRECTED]-(directors) RETURN directors


MATCH (people:Person)-[relatedTo]-(:Movie {title: "Cloud Atlas"}) RETURN people, Type(relatedTo), relatedTo


MATCH p=shortestPath(
  (bacon:Person {name:"Kevin Bacon"})-[*]-(meg:Person {name:"Meg Ryan"})
)
RETURN p


MATCH (n1:Person {name:"Tom Hanks"})- [rel] -> (n2) RETURN n1, Type(rel),n2

MATCH (n1:Movie {title:"The Matrix"})<- [rel] - (n2) RETURN n1, Type(rel),n2
```

## 项目配置

**系统需要安装：**

- django     ---web框架
- neo4j      ---图数据库
- py2neo     ---python连接neo4j的工具

**项目部署：**

1. 安装neo4j，并启动数据库，在脚本执行的browser里执行movie.txt 。 （neo4j网址）https://neo4j.com/ 

2. 安装py2neo (以来与python3，推荐通过pip3安装)

3. 安装django （python3 支持版本）

4. 在moive目录执行python3 manage.py runserver

5. 启动了django，http://127.0.0.1:8000 页面

## 项目使用

1. waiting for upload!!
