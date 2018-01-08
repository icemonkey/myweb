# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import HttpResponse

# Create your views here.
def about(request):
    quote = {'quote':'<p>dfsf fdsssds既然'}
    return render_to_response('myblog/about.html',quote)

def post(request,year,mon,day,post_num):
    val = '{}/{}/{}: Post Number is {}'.format(year,mon,day,post_num)
    quote = {'quote':val}
    return render_to_response('myblog/post.html',quote)

def listdate(request,list_date):
    list_date1 = '{}'.format(list_date)
    list_date = 'Listdate is {}'.format(list_date)
    
    b = []
    [b.append(int(n)) for n in list_date1.split('/')]
    total = sum(b)
    val = {'quote':list_date,'total':total}
    print total
    return render_to_response('myblog/post.html',val)
