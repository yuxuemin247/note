import json

from django.shortcuts import render, HttpResponse

# Create your views here.
from repository import models
def asset(request):

    if request.method == 'POST':
        ### 提交过来的data数据
        ### {'content-type': 'application/json'}

        ### {'content-type': application/www-form-urlencode}
        info = json.loads(request.body)
        print(info)


        hostname = info['basic']['data']['hostname']

        server_obj = models.Server.objects.filter(hostname=hostname).first()

        if not server_obj:
            return HttpResponse('资产不存在')

        if info['disk']['code'] == '10000':
            ### disk分析入库
            ## 获取旧的 slot set
            ## post过来的新slot set

            ### 增加:
            ### add_slot = new-old (new.difference(old))

            ### 删除:
            ### del_slot = old-new (old.difference(new))

            ## 更新:
            ### up_slot = old.intersection(new)

            pass


        else:
            models.ErrorLog.objects.create(content=info['disk']['data'], asset_obj=server_obj.asset)




    else:
        ### 连接数据库
        return ['c1.com', 'c2.com']


    return HttpResponse('ok')