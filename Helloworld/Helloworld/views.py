from django.shortcuts import render,HttpResponse, redirect
from  TestModel.models import BlocktestModel
from django.forms.models import model_to_dict
import json
import datetime
import time

# Create your views here.
def handler(request):
    if request.method == "POST":
        action = request.POST.get('action')

        # if action=='gs':
        #     # record_data = ExtractRecordModel.objects.all().values()#得到的数据是字典格式
        #     record_data = ExtractRecordModel.objects.filter()#得到的数据是dt格式
        #     # print(record_data)
        #     data=[]
        #     for value in record_data:
        #         data.append({"id":value.id,"recordtime":value.recordtime.strftime("%Y-%m-%d %H:%M:%S"),"projectname":value.projectname,"ps_persons":value.ps_persons,"jd_persons":value.ps_persons})
        #     count = ExtractRecordModel.objects.all().count()
        #     jsontemp={"code":0,"msg":"","count":str(count),"data":data}
        #     return HttpResponse(json.dumps(jsontemp))
        if action=='sd':
            data = request.POST.get('data')
            listipinfo=json.loads(data)
            updatetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            for listip in listipinfo:
                ipinfo = BlocktestModel.objects.filter(IPaddress=listip[0])
                if ipinfo.exists():
                    BlocktestModel.objects.filter(IPaddress=listip[0]).update(Updatetime= updatetime)
                else:
                    test1 =BlocktestModel(IPaddress=listip[0],MACaddress=listip[1],Arrowflag='True',Updatetime= updatetime)
                    test1.save()
            return HttpResponse("ok")