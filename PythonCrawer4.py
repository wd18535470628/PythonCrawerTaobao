#encoding:utf-8 
'''
Created on 2018-2-8

@author: Administrator
'''
import urllib
import urllib2
import re 
from sgmllib import SGMLParser
class GetIdList(SGMLParser):  
    def reset(self):  
        self.IDlist = []  
        self.flag = False  
        self.getdata = False  
        self.verbatim = 0  
        SGMLParser.reset(self)  
          
    def start_div(self, attrs):  
        if self.flag == True:  
            self.verbatim +=1 #进入子层div了，层数加1  
            return  
        for k,v in attrs:#遍历div的所有属性以及其值  
            if k == 'class' and v == 'pai-info':#确定进入了<div class='pai-info'>  
                self.flag = True  
                return  
  
    def end_div(self):#遇到</div>  
        if self.verbatim == 0:  
            self.flag = False  
        if self.flag == True:#退出子层div了，层数减1  
            self.verbatim -=1  
  
    def start_p(self, attrs):  
        if self.flag == False:  
            return  
        self.getdata = True  
          
    def end_p(self):#遇到</p>  
        if self.getdata:  
            self.getdata = False  
    
    def handle_data(self, text):#处理文本  
        if self.getdata:  
            self.IDlist.append(text)  
              
    def printID(self):
        for index,content in enumerate(self.IDlist): 
            print index,content
            
response = urllib2.urlopen("https://sf.taobao.com/sf_item/558166478506.htm")
content = response.read().decode("gbk")
              
lister = GetIdList()  
lister.feed(content)  
lister.printID()  