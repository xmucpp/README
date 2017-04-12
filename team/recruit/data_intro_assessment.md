# data_intro&assessment 

##  What are we doing 

* 负责商品评论的挖掘，即利用商品的评论信息评估商品质量；

  目前该任务处于从零到一的初期阶段，后期可能考虑做推荐系统而优化

* 通过用户形象数据，行为数据及评论信息进行电商平台的刷单行为识别；

* 通过商品描述信息做到商品分类，涉及图像处理及文本分类知识；

* 等等......

  欢迎一切基于个人爱好的小项目。


## Requirements for Recruitments

### 数据分析向

#### Goal
- 采集豆瓣电影某一类电影的数据A，及任选某一热评电影评论数据B（3+X）
- 对A数据做简单描述和简单回归、并做可视化；对B数据做数据清洗（7+X）
- 对结果进行表达，包括专栏文章和Presentation（2+X）

#### Step
- 数据采集：豆瓣电影（如战争板块）：https://movie.douban.com/tag/%E6%88%98%E4%BA%89
  - 建议A数据条目：电影名、类型、上映日期、评分（重要）、评价人数（重要）等。
  - 建议B数据条目：短评内容（重要）、短评评分（重要）、发表日期、有用数目等。
      - 基础数据条目：3分
      - 额外数据条目+合理使用：1分（附加分）
  - 待选数据条目：豆瓣成员常用标签
      - 豆瓣网站列举的价格：2分（附加分）
      - 各个网站价格：每个2分（附加分）
  - 其他：有突出架构设计或者有新工具的使用，每个2分（X）

- A数据分析：参考https://zhuanlan.zhihu.com/p/24815577
  - 预处理：包括缺失值处理、重复值处理、异常值处理等（1分）
  - 描述性统计：包括观测值数量、平均值、最大值、最小值、标准差等（1分）
  - 简单的回归：评分和制片地区的关系、评分和人数的关系等等（1分）地区的关系、评分和人数的关系等等（1分）
  - 可视化：散点图（相关关系）、直方图（概率分布）等（1分）
  - 其他：前面几点的扩展，或者其他方面，每个1分（附加分）

- B数据预处理
  - 评论文本根据评分存入不同txt文本 （1分）
  - 根据评论特点筛选补充停用词词典 （1分）
  - 数据清洗：去重去除无意义评论、中文分词、停用词过滤 （1分）
  - 其他：有额外补充清洗内容，每个1分（X）
  
- 表达结果：
  - Github：上传到项目GitHub Organization（1分）
  - Presentation：LaTeX+beamer制作slides，组会Pre（1分）
  - 其他：某一点特别突出或者有其他加分项，1分（附加分）

#### Tools
- Python3.6.x
- LaTeX

#### Timing
  - 两个星期以内：4分
  - 一个月以内：3分
  - 一个月到一个半月：1分
  - 一个半月以上：0分

  


### 文本分析向

#### Goal
- 采集某一热评电影评论数据（3+X）
- 针对短评文本做基于机器学习的情感分析（10+X）
- 对结果进行表达，包括Presentation（2+X）

#### Step
- 数据采集：豆瓣电影栏目下某一热评电影
  - 建议数据条目：短评内容（重要）、短评评分（重要）、发表日期、有用数目等。
      - 基础数据条目：3分
  - 其他：有突出架构设计或者有新工具的使用（X）

- 数据分析：
  - 文档切分:根据评分将评论数据分类（可粗分4星及4星+，与3星及3星-；也可细分）（1分）
  - 文本分词与词性标注：包括词性标注，可利用jieba,THULAC等包，或在NLTK中调用standord中文分词接口（1分）
  - 去除停用词：可在网络上下载相关字典，在此基础上改动（1分）
  - 词频统计：统计去重后词语出现次数（1分）
  - 特征提取与选择：选取具有分类特征的词及其他信息，通过一定统计方法（词频/TF-IDF/卡方统计量/信息熵）筛选特征 （2+X）
  - 文本向量化：将文本信息利用矩阵形式表征（2分）
  - 训练分类器：可利用sklearn包，尝试多种分类方法效果（2分）
  - 其他：视过程优化及分类结果加分（X）

- 表达结果：
  - Github：上传到项目GitHub Organization（1分）
  - Presentation：LaTeX+beamer制作slides，组会Pre（1分）
  - 其他：某一点特别突出或者有其他加分项（X）

#### Tools
- Python3.6.x
- LaTeX

### Timing
  - 两个星期以内：5分
  - 一个月以内：3分
  - 一个月到一个半月：1分
  - 一个半月以上：0分



## References(to be filled)

### Python入门
- 简单：http://res.crossincode.com
- 中等：https://github.com/qiwsir/StarterLearningPython
- 困难：http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000

### Python进阶
- 略

### 爬虫

- Python爬虫入门
  - https://xlzd.me/tag/crawler/
  - https://zhuanlan.zhihu.com/p/21511857

- 豆瓣爬虫实例
  - https://www.zhihu.com/question/21234530
  - https://github.com/lanbing510/DouBanSpider/blob/master/doubanSpider.py

- HTML、CSS、JS等
  - http://www.w3school.com.cn

- requests
  - http://www.python-requests.org

- bs4
  - https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

### 数据分析
- pandas：http://pandas.pydata.org/pandas-docs/version/0.19.0/
  - Quick Start: http://pandas.pydata.org/pandas-docs/version/0.19.0/10min.html
  - Data Structure: http://pandas.pydata.org/pandas-docs/version/0.19.0/dsintro.html
  - Group By: http://pandas.pydata.org/pandas-docs/version/0.19.0/groupby.html
  - Merge: http://pandas.pydata.org/pandas-docs/version/0.19.0/merging.html
  - IO: http://pandas.pydata.org/pandas-docs/version/0.19.0/io.html
  - Visualization: http://pandas.pydata.org/pandas-docs/version/0.19.0/visualization.html

- statsmodels: http://statsmodels.sourceforge.net

### 文本分析
- 简要概述：https://zhuanlan.zhihu.com/p/25065579?utm_source=itdadao&utm_medium=referral
- 利用gensim与sklearn文本搭建分类器：http://blog.csdn.net/u014595019/article/details/52433754
- 我爱自然语言处理网: http://www.52nlp.cn/
- 建议在 google/bing/CSDN/github 等搜索相关关键词
- Nltk: http://www.nltk.org/ 
- jieba: https://github.com/fxsjy/jieba/  
- sklearn: http://scikit-learn.org/stable/
  - svm: http://scikit-learn.org/stable/modules/svm.html
  - Naive_Bayes: http://scikit-learn.org/stable/modules/naive_bayes.html
  - ...
- gensim: http://radimrehurek.com/gensim/


### LaTeX
- 入门
  - https://zhuanlan.zhihu.com/p/21511857
- beamer
  - https://en.wikipedia.org/wiki/Beamer_(LaTeX)

### 专栏
- https://zhuanlan.zhihu.com/p/24455935?refer=xmucpp
