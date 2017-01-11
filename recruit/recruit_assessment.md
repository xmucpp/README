# Recruit Assessment

## Requirement

### Goal
- 采集豆瓣读书某一分类（比如经济学）的数据（2+X）
- 对数据做简单描述和简单回归、并做可视化（4+X）
- 对结果进行表达，包括专栏文章和Presentation（4+X）

### Step
- 数据采集：豆瓣读书（如经济学板块）：https://book.douban.com/tag/经济学
  - 建议数据条目：ID、书名、出版日期、评分（重要）、评价人数（重要）、纸质版价格（重要）等。
      - 基础数据条目：2分
      - 额外数据条目+合理使用：1分（附加分）
  - 待选数据条目：各个网站纸质版价格
      - 豆瓣网站列举的价格：2分（附加分）
      - 各个网站价格：每个2分（附加分）
  - 其他：有突出架构设计或者有新工具的使用，每个2分（附加分）

- 数据分析：参考https://zhuanlan.zhihu.com/p/24815577
  - 预处理：包括缺失值处理、重复值处理、异常值处理等（1分）
  - 描述性统计：包括观测值数量、平均值、最大值、最小值、标准差等（1分）
  - 简单的回归：评分和价格的关系、评分和人数的关系等等（1分）
  - 可视化：散点图（相关关系）、直方图（概率分布）等（1分）
  - 其他：前面几点的扩展，或者其他方面，每个1分（附加分）

- 表达结果：
  - 专栏文章：数据来源、采集策略、预处理、描述性统计、简单回归（2分）
  - Presentation：LaTeX+beamer制作slides，组会Pre（2分）
  - 其他：某一点特别突出或者有其他加分项，1分（附加分）

## Tools
- Python2.7.x（9以上）
- LaTeX

### Timing
  - 两个星期以内：3分
  - 一个月以内：2分
  - 一个月到一个半月：1分
  - 一个半月以上：0分


## Grading
- A+：15分，优，分组组长
- A：12分，优，主力成员
- A-：10分
- B+：9分
- B：8分，良，正式成员
- B-：7分
- C+：6分
- C：5分，合格，预备成员
- C-：4分
- D+：3分
- D：2分
- D-：1分
- F：0分


## References(to be filled)

### Python入门
- 简单：http://res.crossincode.com
- 中等：https://github.com/qiwsir/StarterLearningPython
- 困难：http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000

### Python进阶
- 略

### 爬虫

- Python爬虫入门：
  - https://xlzd.me/tag/crawler/
  - https://zhuanlan.zhihu.com/p/21511857

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

### LaTex

- 入门
  - https://zhuanlan.zhihu.com/p/21511857

- beamer
  - https://en.wikipedia.org/wiki/Beamer_(LaTeX)

### 专栏
- https://zhuanlan.zhihu.com/p/24455935?refer=xmucpp