from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from checklist.models import  features, checklist
from lodge.models import lodges
from manager.models import managers
from user.models import User
from datetime import datetime

# Create your views here.
def index(request, lodge_id,room_num):
    check_start = datetime.now()
    if request.method == "GET":
        
        feature = features.objects.all().order_by('question_id')
        infos = [ (feat.question_id,feat.question,feat.division,feat.place) for feat in feature]
    
    
        context = {'infos':infos,
                    'lodge_id': lodge_id,
                    'check_start': check_start,
                    'room_num':room_num}

        return render(request, 'checklist.html', context)


def checkListPost(request, lodge_id, room_num):

    #끝나는 시간
    check_finish = datetime.now()
    # 체크리스트 인스턴스 적재
    #instance = checklist.objects.filter(lodge_id = lodge_id).order_by('id').last()
    instance = checklist.objects.filter(lodge_id = lodge_id)
    instance = instance.filter(room_num = room_num).order_by('id').last()
    instance.q1 = request.POST['q1']
    instance.q2 = request.POST['q2']
    instance.q3 = request.POST['q3']
    instance.q4 = request.POST['q4']
    instance.q5 = request.POST['q5']
    instance.q6 = request.POST['q6']
    instance.q7 = request.POST['q7']
    instance.q8 = request.POST['q8']
    instance.q9 = request.POST['q9']
    instance.q10 = request.POST['q10']
    instance.q11 = request.POST['q11']
    instance.q12 = request.POST['q12']
    instance.q13 = request.POST['q13']
    instance.q14 = request.POST['q14']
    instance.q15 = request.POST['q15']
    instance.q16 = request.POST['q16']
    instance.q17 = request.POST['q17']
    instance.q18 = request.POST['q18']
    instance.q19 = request.POST['q19']
    instance.q20 = request.POST['q20']
    instance.q21 = request.POST['q21']
    instance.q22 = request.POST['q22']
    instance.q23 = request.POST['q23']
    instance.q24 = request.POST['q24']
    instance.q25 = request.POST['q25']
    instance.q26 = request.POST['q26']
    instance.q27 = request.POST['q27']
    instance.q28 = request.POST['q28']
    instance.q29 = request.POST['q29']
    instance.q30 = request.POST['q30']
    instance.q31 = request.POST['q31']
    instance.q32 = request.POST['q32']
    instance.q33 = request.POST['q33']
    instance.q34 = request.POST['q34']
    instance.q35 = request.POST['q35']
    instance.q36 = request.POST['q36']
    instance.q37 = request.POST['q37']
    instance.q38 = request.POST['q38']
    instance.q39 = request.POST['q39']
    instance.q40 = request.POST['q40']
    instance.q41 = request.POST['q41']
    instance.q42 = request.POST['q42']
    instance.q43 = request.POST['q43']
    instance.q44 = request.POST['q44']
    instance.q45 = request.POST['q45']
    instance.q46 = request.POST['q46']
    instance.q47 = request.POST['q47']
    instance.q48 = request.POST['q48']
    instance.q49 = request.POST['q49']
    instance.check_finish = check_finish
    instance.save()

    #lodge 최근 모니터링 시간 갱신
    lodge_update = lodges.objects.get(id = lodge_id)
    lodge_update.latest_monitoring = check_finish
    lodge_update.save()

    return redirect('/manager/')

        

