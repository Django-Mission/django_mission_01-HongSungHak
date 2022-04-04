from ctypes import resize
from re import I
from unittest import result
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def lotto(reqeust):
    result = random.sample(range(1,47),7)
    print(result)
    return render(reqeust, 'lotto.html',{'result' : random.sample(range(1,47),7)})


    