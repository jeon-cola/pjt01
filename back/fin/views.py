from django.shortcuts import render
# views.py
import requests
from django.http import JsonResponse
from .models import DepositModel,SavingModel
from django.db.models import Q
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
    data=[]
    response = requests.get(url, params=params)
    data.append(response.json().get('result'))
    result=response.json()
    save_saving(result) 
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '030300',
        'changeOrigin': True,
    }
    for i in range(1,4):
        params['pageNo'] = i
        response = requests.get(url, params=params)
        data.append(response.json().get('result'))
        result=response.json()
        save_saving(result) 
    return JsonResponse(data,safe=False)


def get_deposit(request):
    url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth': API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
        'changeOrigin': True,
    }
    data=[]
    response = requests.get(url, params=params)
    data.append(response.json().get('result'))
    result=response.json()
    save_deposit(result)     

    params = {
        'auth': API_KEY,
        'topFinGrpNo': '030300',
        'changeOrigin': True,
    }
    for i in range(1,5):
        params['pageNo'] = i
        response = requests.get(url, params=params)
        result=response.json()
        save_deposit(result)    
        data.append(response.json()['result'])
    return JsonResponse(data,safe=False)
def send_deposit(request):
     d=DepositModel.objects.all()
     lst = [
    {
        "kor_co_nm": i.kor_co_nm,
        "fin_prdt_nm": i.fin_prdt_nm,
        "join_way": i.join_way,
        "mtrt_int": i.mtrt_int,
        "spcl_cnd": i.spcl_cnd,
        "etc_note": i.etc_note,
        "intr_rate": i.intr_rate,
        "intr_rate2": i.intr_rate2,
        "intr_rate_type_nm": i.intr_rate_type_nm,
        "save_trm": i.save_trm,
    }
    for i in d
]
     return JsonResponse(lst,safe=False)
    
def save_deposit(data):
    # for result in data:  # data는 리스트이므로 각 요소를 순회
        baseList = data.get('result').get('baseList',[])
        optionList = data.get('result').get('optionList',[])
        for i in baseList:
             for j in optionList:
                  if i['fin_prdt_cd'] == j['fin_prdt_cd']:
                        # 중복 확인
                        if DepositModel.objects.filter(
                        kor_co_nm=i['kor_co_nm'],
                        fin_prdt_nm=i['fin_prdt_nm'],
                        join_way=i['join_way'],
                        mtrt_int=i['mtrt_int'],
                        spcl_cnd=i['spcl_cnd'],
                        etc_note=i['etc_note'],
                        intr_rate=j['intr_rate'],
                        intr_rate2=j['intr_rate2'],
                        intr_rate_type_nm=j['intr_rate_type_nm'],
                        save_trm=j['save_trm'],
                        ).exists():
                            print('skip')
                            continue
                        else:
                        # 데이터 저장
                            DepositModel.objects.create(
                                kor_co_nm=i['kor_co_nm'],
                                fin_prdt_nm=i['fin_prdt_nm'],
                                join_way=i['join_way'],
                                mtrt_int=i['mtrt_int'],
                                spcl_cnd=i['spcl_cnd'],
                                etc_note=i['etc_note'],
                                intr_rate=j['intr_rate'],
                                intr_rate2=j['intr_rate2'],
                                intr_rate_type_nm=j['intr_rate_type_nm'],
                                save_trm=j['save_trm'],
                            )

def save_saving(data):
    # for result in data:  # data는 리스트이므로 각 요소를 순회
        baseList = data.get('result').get('baseList',[])
        optionList = data.get('result').get('optionList',[])
        for i in baseList:
             for j in optionList:
                  if i['fin_prdt_cd'] == j['fin_prdt_cd']:
                        # 중복 확인
                        if SavingModel.objects.filter(
                        kor_co_nm=i['kor_co_nm'],
                        fin_prdt_nm=i['fin_prdt_nm'],
                        join_way=i['join_way'],
                        mtrt_int=i['mtrt_int'],
                        spcl_cnd=i['spcl_cnd'],
                        etc_note=i['etc_note'],
                        intr_rate=j['intr_rate'],
                        intr_rate2=j['intr_rate2'],
                        intr_rate_type_nm=j['intr_rate_type_nm'],
                        save_trm=j['save_trm'],
                        rsrv_type_nm= j['rsrv_type_nm']
                        ).exists():
                            print('skip')
                            continue
                        else:
                        # 데이터 저장
                            SavingModel.objects.create(
                                kor_co_nm=i['kor_co_nm'],
                                fin_prdt_nm=i['fin_prdt_nm'],
                                join_way=i['join_way'],
                                mtrt_int=i['mtrt_int'],
                                spcl_cnd=i['spcl_cnd'],
                                etc_note=i['etc_note'],
                                intr_rate=j['intr_rate'],
                                intr_rate2=j['intr_rate2'],
                                intr_rate_type_nm=j['intr_rate_type_nm'],
                                save_trm=j['save_trm'],
                                rsrv_type_nm= j['rsrv_type_nm']
                            )
def send_saving(request):
     d=SavingModel.objects.all()
     lst = [
    {
        "kor_co_nm": i.kor_co_nm,
        "fin_prdt_nm": i.fin_prdt_nm,
        "join_way": i.join_way,
        "mtrt_int": i.mtrt_int,
        "spcl_cnd": i.spcl_cnd,
        "etc_note": i.etc_note,
        "intr_rate": i.intr_rate,
        "intr_rate2": i.intr_rate2,
        "intr_rate_type_nm": i.intr_rate_type_nm,
        "save_trm": i.save_trm,
        'rsrv_type_nm':i.rsrv_type_nm,
    }
    for i in d
]
     return JsonResponse(lst,safe=False)
def exchange_rate(request):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': EXCHANGE_KEY,
        'data':'AP01',
        'searchdate': '20241118',
    }
    response = requests.get(url, params=params)
    print('---------------------')
    print(response)
    data = response.json()
    return JsonResponse(data,safe=False,verify=False)
