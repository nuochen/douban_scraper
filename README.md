### 豆瓣简易爬虫 ###
### A simple Douban.com scraper ###

by nuo

python version: 2.7

Everything is ephemeral, including your digital accounts. The rest is what they call history.

A simple scraper to extract and save public-facing Douban data into spreadsheets. Output columns include:
- name
- rating
- tag
- comment
- date

Sample use case:

We want to extract all movies from this Doulist: https://www.douban.com/doulist/969571/
There are 5 pages in total.

Running the following will save a file named 'doulist.csv' to your current working directory
```
crawl('https://www.douban.com/doulist/969571/','doulist.csv')
```
--------
用途：抓取任何用户标记看过/想看/在看的电影/图书和音乐列表并输出为表格式文档（csv)。表格文档会产生以下五种信息：

- 名称
- 评分
- 标签
- 评论
- 日期

使用示例：

我们想要抓取这个豆列里的所有电影：https://www.douban.com/doulist/969571/

运行以下代码，就会自动下载一个名为doulist.csv的文档
```
crawl('https://www.douban.com/doulist/969571/','doulist.csv')
```
---------

This is currently a WIP. Future potential feature addition includes:
- pulling from multiple lists and aggregate them in one file
- customize fields to extract
- extracting public-facing articles 
