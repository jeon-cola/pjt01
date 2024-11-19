from django.shortcuts import render
# views.py
import requests
from django.http import JsonResponse
API_KEY='c22c8b2d800dd8097f28d84f4506fc54'
EXCHANGE_KEY='Q03jnie3N7LkEkXU7jFRd272z0Ur2zmI'
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
        'searchdate': '20241118',
    }
    response = requests.get(url, params=params)
    data = response.json()
    return JsonResponse(data,safe=False)
