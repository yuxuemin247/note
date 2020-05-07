import json

from django.shortcuts import render, HttpResponse

# Create your views here.

def asset(request):

    if request.method == 'POST':
        ### 提交过来的data数据
        ### {'content-type': 'application/json'}

        ### {'content-type': application/www-form-urlencode}
        info = json.loads(request.body)
        print(info)

        ### disk分析入库
    else:
        ### 连接数据库
        return ['c1.com', 'c2.com']


    return HttpResponse('ok')