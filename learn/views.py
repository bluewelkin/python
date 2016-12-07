#coding:utf-8
from django.shortcuts import render
 
 
def home(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    return render(request, 'home.html', {'string': string})
