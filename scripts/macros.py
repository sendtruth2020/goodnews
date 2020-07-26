#!/usr/bin/python
# coding: utf-8

git_base_url = "https://github.com/begood0513/goodnews/blob/master/pages"


head = '####  [法轮功真相](../../../../basic/blob/master/README.md) &nbsp;|&nbsp; [九评共产党](../../../../9ping.md/blob/master/README.md) &nbsp;|&nbsp; [解体党文化](../../../../jtdwh.md/blob/master/README.md)  &nbsp;|&nbsp; [共产主义的终极目的](../../../../gczydzjmd.md/blob/master/README.md) &nbsp;|&nbsp; [魔鬼在统治我们的世界](../../../../mgztzwmdsj.md/blob/master/README.md) \n\n'
#'#### [💌武汉肺炎来势凶凶， 我要抛弃中共邪党保命](https://github.com/begood0513/goodnews/blob/master/quit/letter.md)\n\n'

menu = "#### [首页](../../README.md)  &nbsp;&nbsp;|&nbsp;&nbsp; _channellink_  &nbsp;&nbsp;|&nbsp;&nbsp; [热点推荐](../../indexes/热点推荐.md)  &nbsp;&nbsp;|&nbsp;&nbsp; [法轮功真相](../../../../../basic/blob/master/README.md) &nbsp;&nbsp;|&nbsp;&nbsp; [翻墙教程](https://github.com/gfw-breaker/guides/blob/master/README.md)\n\n"

links = "\n\n"
links += "#### [ 💌 疫情象最后通牒 让世界远离中共](https://github.com/begood0513/goodnews/blob/master/pages/recommended/406691.md) &nbsp; "
links += "| &nbsp;[退出中共组织 良心的选择](https://github.com/begood0513/goodnews/blob/master/quit/letter.md) \n\n"
links += "#### [ 🎬  翻墙必看视频（八九六四、法轮功、709大抓捕、香港反送中 ...）](https://github.com/gfw-breaker/banned-news1/blob/master/pages/link4.md)\n\n"
links += "#### [ 🎬 《伪火》- 天安门自焚真相](http://158.247.193.181:10000/videos/blog/weihuo.html)&nbsp; "
links += "| &nbsp;[《六月黑夜》- 六四天安门大屠杀](http://158.247.193.181:10000/videos/88/kent.html)\n\n"
links += "#### 网站代理：[大纪元新闻网](http://158.247.194.169:10080/gb/) &nbsp;|&nbsp; [新唐人电视台](http://158.247.194.169:8808/gb/) &nbsp;|&nbsp; [YouTube热门频道](http://158.247.193.181/youtube.html)\n\n"

tail = ""

def write_page(channel, f_name, f_path, title, link, content):
	clink = '[{}](../../indexes/{}.md) '.format(channel, channel)
	nmenu = menu.replace('_channellink_', clink)
	new_link = git_base_url + '/' + channel + '/' + f_name
	body = '### ' + title
	body += "\n------------------------\n\n" + nmenu + "\n\n" +  content
	body += "\n<hr/>\n手机上长按并复制下列链接或二维码分享本文章：<br/>"
	body += "\n" + new_link + " <br/>"
	body += "\n<a href='" + new_link + "'><img src='" + new_link + ".png'/></a> <br/>"
	body += "\n原文地址（需翻墙访问）：" + link + "\n"
	body += "\n\n------------------------\n" + nmenu 
	body += "\n<img src='http://gfw-breaker.win/goodnews/" + f_path[3:] + "' width='0px' height='0px'/>"
	fh = open(f_path, 'w')
	fh.write(body)
	fh.close()


def get_links():
	result = ""
	idx_file = '/usr/local/nginx/html/videos/news/readme.txt'
	site_base_url = "http://158.247.193.181:10000/videos/news/"
	lines = open(idx_file, "r").read().splitlines()
	for line in lines[1:4]:
		cols = line.split(',')
		url_path = site_base_url + cols[0] + '.html'
		title = cols[1]
		md_link = "#### [ 🎬 %s](%s)\n\n" % (title, url_path)
		result = result + md_link
	return result


links += get_links()

