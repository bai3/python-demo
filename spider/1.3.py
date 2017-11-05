# -*- coding: UTF-8 -*-
import urllib2
import re


class Spider:

    def __init__(self):
        self.enable = True
        self.page = 1
    """
        内涵段子爬虫
    """
    def load_page(self, page):
        """
        :param page: 需要请求第几页
        :return: 返回的页面html
        """
        url = "http://www.neihan8.com/article/list_5_" + str(page) + ".html"
        user_agent = "'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0"
        header = {'User-Agent': user_agent}
        req = urllib2.Request(url, headers=header)
        response = urllib2.urlopen(req)
        html = response.read()
        gbk_html = html.decode('gbk').encode('utf-8')
        # print gbk_html
        # f = open('test.html', 'w+')
        # f.write(gbk_html)
        # f.close()
        pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
        item_list = pattern.findall(gbk_html)
        return item_list

    def printonepage(self, item_list, page):
        print "*******第%d页 爬取完毕*********" %page
        for item in item_list:
            item = item.replace("<p>", "").replace("</p>", "").replace("<br />", "").replace("&ldquo;", "")\
                .replace("&rdquo;", "").replace("&hellip;", "")
            self.writetofile(item)

    def writetofile(self, text):
        myFile = open("MyStory.txt", 'a')
        myFile.write(text)
        myFile.write("-------------------------------------------------------------------------")
        myFile.close()

    def dowork(self):
        while self.enable:
            try:
                item_list = self.load_page(self.page)
            except urllib2.URLError, e:
                print e.reason
                continue
            self.printonepage(item_list, self.page)
            self.page += 1
            print "按回车继续"
            print "输入quit退出"
            command = raw_input()
            if (command == "quit"):
                self.enable = False
                break

if __name__ == "__main__":
    print '''
    ==========================
          内涵段子小爬虫
    ==========================
    '''
    print '请按下回车开始'
    raw_input()
    # 定义一个spider对象
    myspider = Spider()
    myspider.dowork()
