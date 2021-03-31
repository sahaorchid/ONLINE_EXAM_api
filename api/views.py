from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import qusform
from .serializer import qusformserializer
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializer import allansserializer
from django.views.decorators.csrf import csrf_exempt
def api_view(request):
    if request.method=="POST":
        qus=request.POST['qus']
        qno=request.POST['qno']
        op1= request.POST['op1']
        op2 = request.POST['op2']
        op3 = request.POST['op3']
        op4 = request.POST['op4']
        data=qusform(qno=qno,qus=qus,op1=op1,op2=op2,op3=op3,op4=op4)
        data.save()
    return render(request,'index.html')
@csrf_exempt
def qus_detail(request,no):
    data=qusform.objects.get(qno=no)
    serialize=qusformserializer(data)
    return JsonResponse(serialize.data,safe=False)

@csrf_exempt
def get_allans(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=allansserializer(data=pythondata)
        if(serializer.is_valid()):
            serializer.save()
            res={'msg':'ans saved'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

