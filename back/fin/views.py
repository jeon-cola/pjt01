from django.shortcuts import render
# views.py
import requests
from django.http import JsonResponse
def get_saving(request):
    url = 'https://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
        'changeOrigin': True,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return JsonResponse(data)


def get_deposit(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
        'changeOrigin': True,
    }
    response = requests.get(url, params=params)
    data = response.json()
    return JsonResponse(data)

def exchange_rate(request):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': EXCHANGE_KEY,
        'data':'AP01',
        'changeOrigin': True,
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    return JsonResponse(data,safe=False)
