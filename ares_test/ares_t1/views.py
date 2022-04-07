import time
from django.shortcuts import render
#from models import cookie1
from ares_t1.models import cookie1
from django.http import HttpResponse
import requests, json
# Create your views here.
def write_cookie(request):
    if request.method == "POST":
        cookes = request.POST.get('cookie')
    cookie1.objects.filter(id=1).update(cookie1=cookes)
    a = cookie1.objects.get(id=1)
    print(a.cookie1)
    #return render(request, 'tt.html')
    return HttpResponse(1)
def readcookie():
    a = cookie1.objects.get(id=1)
    return a.cookie1
cookie = readcookie()
print(cookie)

header = {"Connection": "keep-alive", "Accept": "application/json, text/plain, */*",
              "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
              "Content-Type": "application/x-www-form-urlencoded",
              "Origin": "http://ares-sit.yonghuivip.com",
              "Referer": "http://ares-sit.yonghuivip.com/",
              "Accept-Language": "zh-CN,zh;q=0.9",
              #"Host": "ares-sit.yonghuivip.com:8090",
              "Connection": "keep-alive",
              "Cookie": cookie
              }

def index(request):
    # url = 'http://ares-sit.yonghuivip.com:8090/testCase/v2/planList'
    # data = {"planName": "", "planKey": "", "oaAccount": "", "almCode": "hcyx", "env": "", "planTypeApi": "", "currentpage": 1, "pagesize": 10}
    # res = requests.post(url=url, data=data, headers=header).json()['departments']
    # print(res)
    # a=[]
    # b=[]
    # for i in res:
    #     a.append(i['planName'])
    #     b.append(i['planKey'])
    # d={}
    # c={}
    # d["name"]=a
    # d["value"]=b
    # d=json.dumps({'aa': [{"name":1,"value":2},{"name":3,"value":4}]})

    return render(request, 'create_hr.html')
def do_test1(case_id):
    '''执行测试计划'''
    url = 'http://ares-sit.yonghuivip.com:8090/testPlanV2/execute_plan?planKey='+str(case_id)+'&env=sit'
    #data = {"planKey": str(case_id), "env": "sit"}
    print(url)
    res = requests.get(url=url, headers=header)
    print("****************")
    print(res.text)
def do_test2(case_id):
    '''
    获取测试报告地址
    '''
    url = 'http://ares-sit.yonghuivip.com:8090/report/planResult'
    data = {"planKey": str(case_id), "planName": "", "currentpage": 1, "pagesize": 10, "almCode": "hcyx",
            "status": "", "userName": "", "type": "", "startTime": "", "endTime": ""}
    res = requests.post(url=url, data=data, headers=header)
    #print(res.json())
    prid = res.json()["departments"][0]["prId"]
    print(prid)
    url1 = 'http://ares-sit.yonghuivip.com:8090/report/'+str(case_id)+'_'+str(prid)+'/index.html'
    return url1
def do_test(request):
    print("*************")
    print(header)
    if request.method == 'GET':
        case_id = request.GET.get('a')
    print(case_id)
    do_test1(case_id)
    time.sleep(1)
    aa = do_test2(case_id)
    print(aa)
    #aa = 'http://ares-sit.yonghuivip.com:8090/report/hcyx_20010_17602/index.html'
    context = {'urlt2': aa,'urlt1': case_id}
    return render(request, 'tt.html', context)
if __name__ == "__main__":
    index()
