#coding:utf-8
from sele import webutils
import json

s1 = json.load(open('config.json'))
go=webutils()
print s1['a']
go.getUrl('http://www.google.com')
go.Click(s1['a'])