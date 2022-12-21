from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from .models import managers
from lodge.models import lodges
from django.db.models import Sum
from manager.models import schedule, managers,timeline
from user.models import User
import requests
from datetime import datetime
from checklist.models import checklist

# Create your views here.
def index(request):
    return render(request,'landing_page.html')

def info(request):
    if request.user.is_authenticated:
        manager = managers.objects.get(user_id= request.user.id)
        monitoring_cnt = lodges.objects.filter(manager__contains = manager.user_id).count()
        moving_time = monitoring_cnt * 15 
        working_time = lodges.objects.filter(manager__contains = manager.user_id).aggregate(Sum('monitoring_time'))
        monitoring_time = moving_time + working_time['monitoring_time__sum']

    return render(request, 'info.html', {'manager':manager,'monitoring_cnt':monitoring_cnt, 'monitoring_time': monitoring_time})

def schedules(request):
    if request.user.is_authenticated:
        manager = managers.objects.get(user_id= request.user.id) 
        if schedule.objects.filter(id = manager.id).count() == 0:
            test = schedule.objects.filter(id = 2).count()

            context = {
                'test':test
            }
            
        else:
            schedules = schedule.objects.get(id = manager.id)
            timelines = timeline.objects.get(id = manager.id)
            lodge_1 = lodges.objects.filter(id__contains = schedules.lo1).values().get()
            lodge_2 = lodges.objects.filter(id__contains = schedules.lo2).values().get()
            lodge_3 = lodges.objects.filter(id__contains = schedules.lo3).values().get()
            lodge_4 = lodges.objects.filter(id__contains = schedules.lo4).values().get()
            lodge_5 = lodges.objects.filter(id__contains = schedules.lo5).values().get()
            lodge_6 = lodges.objects.filter(id__contains = schedules.lo6).values().get()
            lodge_7 = lodges.objects.filter(id__contains = schedules.lo7).values().get()
            lodge_8 = lodges.objects.filter(id__contains = schedules.lo8).values().get()
            
            context = {
                'schedules':schedules,
                'timelines':timelines,
                'lodge_1':lodge_1,
                'lodge_2':lodge_2,
                'lodge_3':lodge_3,
                'lodge_4':lodge_4,
                'lodge_5':lodge_5,
                'lodge_6':lodge_6,
                'lodge_7':lodge_7,
                'lodge_8':lodge_8,
            }
        
                
    return render(request, 'schedules.html', context)

def target1(request):
    if request.user.is_authenticated:
        manager = managers.objects.get(user_id= request.user.id)  
        schedules = schedule.objects.get(id = manager.id)
        lodge = lodges.objects.filter(id__contains = schedules.lo1).values().get()
        lodge_id = lodge['id']
        user_table = User.objects.get(id = lodge['user_id_id'])
        address = user_table.address
        client_id = 'qdu3m0mwb7'    
        client_pw = 'dFFYwEMquabyEwAYo4gWE8eNKKrTcq4CZi3JpQ58'
        endpoint = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
        url = f"{endpoint}?query={address}"
        # 헤더
        headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_pw,
        }
        # 요청
        res = requests.get(url, headers=headers)
        res = res.json()
        x = res['addresses'][0]['x']
        y = res['addresses'][0]['y'] 

        context = {'schedules':schedules,
                'lodge':lodge, 'address':address, 
                'x': x, 'y':y,
                'lodge_id':lodge_id}

        
    return render(request, 'target1.html',context)

def target2(request):
    if request.user.is_authenticated:
        manager = managers.objects.get(user_id= request.user.id)  
        schedules = schedule.objects.get(id = manager.id)
        lodge = lodges.objects.filter(id__contains = schedules.lo2).values().get()
        lodge_id = lodge['id']
        user_table = User.objects.get(id = lodge['user_id_id'])
        address = user_table.address
        client_id = 'qdu3m0mwb7'    
        client_pw = 'dFFYwEMquabyEwAYo4gWE8eNKKrTcq4CZi3JpQ58'
        endpoint = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
        url = f"{endpoint}?query={address}"
        # 헤더
        headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_pw,
        }
        # 요청
        res = requests.get(url, headers=headers)
        res = res.json()
        x = res['addresses'][0]['x']
        y = res['addresses'][0]['y'] 

        context = {'schedules':schedules,
                'lodge':lodge, 'address':address, 
                'x': x, 'y':y,
                'lodge_id':lodge_id}

        
    return render(request, 'target2.html',context)
    

def target3(request):
    if request.user.is_authenticated:
        manager = managers.objects.get(user_id= request.user.id)  
        schedules = schedule.objects.get(id = manager.id)
        lodge = lodges.objects.filter(id__contains = schedules.lo3).values().get()
        lodge_id = lodge['id']
        user_table = User.objects.get(id = lodge['user_id_id'])
        address = user_table.address
        client_id = 'qdu3m0mwb7'    
        client_pw = 'dFFYwEMquabyEwAYo4gWE8eNKKrTcq4CZi3JpQ58'
        endpoint = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
        url = f"{endpoint}?query={address}"
        # 헤더
        headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_pw,
        }
        # 요청
        res = requests.get(url, headers=headers)
        res = res.json()
        x = res['addresses'][0]['x']
        y = res['addresses'][0]['y'] 

        context = {'schedules':schedules,
                'lodge':lodge, 'address':address, 
                'x': x, 'y':y,
                'lodge_id':lodge_id}

        
    return render(request, 'target3.html',context)

def target4(request):
    if request.user.is_authenticated:
        manager = managers.objects.get(user_id= request.user.id)  
        schedules = schedule.objects.get(id = manager.id)
        lodge = lodges.objects.filter(id__contains = schedules.lo4).values().get()
        lodge_id = lodge['id']
        user_table = User.objects.get(id = lodge['user_id_id'])
        address = user_table.address
        client_id = 'qdu3m0mwb7'    
        client_pw = 'dFFYwEMquabyEwAYo4gWE8eNKKrTcq4CZi3JpQ58'
        endpoint = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
        url = f"{endpoint}?query={address}"
        # 헤더
        headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_pw,
        }
        # 요청
        res = requests.get(url, headers=headers)
        res = res.json()
        x = res['addresses'][0]['x']
        y = res['addresses'][0]['y'] 

        context = {'schedules':schedules,
                'lodge':lodge, 'address':address, 
                'x': x, 'y':y,
                'lodge_id':lodge_id}

        
    return render(request, 'target4.html',context)

def target5(request):
    if request.user.is_authenticated:
        manager = managers.objects.get(user_id= request.user.id)  
        schedules = schedule.objects.get(id = manager.id)
        lodge = lodges.objects.filter(id__contains = schedules.lo5).values().get()
        lodge_id = lodge['id']
        user_table = User.objects.get(id = lodge['user_id_id'])
        address = user_table.address
        if schedules.lo5 != '미정':
            client_id = 'qdu3m0mwb7'    
            client_pw = 'dFFYwEMquabyEwAYo4gWE8eNKKrTcq4CZi3JpQ58'
            endpoint = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
            url = f"{endpoint}?query={address}"
            # 헤더
            headers = {
                "X-NCP-APIGW-API-KEY-ID": client_id,
                "X-NCP-APIGW-API-KEY": client_pw,
            }
            # 요청
            res = requests.get(url, headers=headers)
            res = res.json()
            x = res['addresses'][0]['x']
            y = res['addresses'][0]['y'] 

            context = {'schedules':schedules,
                    'lodge':lodge, 'address':address, 
                    'x': x, 'y':y,
                    'lodge_id':lodge_id}

            
            return render(request, 'target5.html',context)
        else:
            return render(request, 'target5.html')


def target6(request):
    if request.user.is_authenticated:
        manager = managers.objects.get(user_id= request.user.id)  
        schedules = schedule.objects.get(id = manager.id)
        lodge = lodges.objects.filter(id__contains = schedules.lo6).values().get()
        lodge_id = lodge['id']
        user_table = User.objects.get(id = lodge['user_id_id'])
        address = user_table.address
        client_id = 'qdu3m0mwb7'    
        client_pw = 'dFFYwEMquabyEwAYo4gWE8eNKKrTcq4CZi3JpQ58'
        endpoint = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
        url = f"{endpoint}?query={address}"
        # 헤더
        headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_pw,
        }
        # 요청
        res = requests.get(url, headers=headers)
        res = res.json()
        x = res['addresses'][0]['x']
        y = res['addresses'][0]['y'] 

        context = {'schedules':schedules,
                'lodge':lodge, 'address':address, 
                'x': x, 'y':y,
                'lodge_id':lodge_id}

        
    return render(request, 'target6.html',context)

def target7(request):
    if request.user.is_authenticated:
        manager = managers.objects.get(user_id= request.user.id)  
        schedules = schedule.objects.get(id = manager.id)
        lodge = lodges.objects.filter(id__contains = schedules.lo7).values().get()
        lodge_id = lodge['id']
        user_table = User.objects.get(id = lodge['user_id_id'])
        address = user_table.address
        client_id = 'qdu3m0mwb7'    
        client_pw = 'dFFYwEMquabyEwAYo4gWE8eNKKrTcq4CZi3JpQ58'
        endpoint = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
        url = f"{endpoint}?query={address}"
        # 헤더
        headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_pw,
        }
        # 요청
        res = requests.get(url, headers=headers)
        res = res.json()
        x = res['addresses'][0]['x']
        y = res['addresses'][0]['y'] 

        context = {'schedules':schedules,
                'lodge':lodge, 'address':address, 
                'x': x, 'y':y,
                'lodge_id':lodge_id}

        
    return render(request, 'target7.html',context)

def target8(request):
    if request.user.is_authenticated:
        manager = managers.objects.get(user_id= request.user.id)  
        schedules = schedule.objects.get(id = manager.id)
        lodge = lodges.objects.filter(id__contains = schedules.lo8).values().get()
        lodge_id = lodge['id']
        user_table = User.objects.get(id = lodge['user_id_id'])
        address = user_table.address
        client_id = 'qdu3m0mwb7'    
        client_pw = 'dFFYwEMquabyEwAYo4gWE8eNKKrTcq4CZi3JpQ58'
        endpoint = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode'
        url = f"{endpoint}?query={address}"
        # 헤더
        headers = {
            "X-NCP-APIGW-API-KEY-ID": client_id,
            "X-NCP-APIGW-API-KEY": client_pw,
        }
        # 요청
        res = requests.get(url, headers=headers)
        res = res.json()
        x = res['addresses'][0]['x']
        y = res['addresses'][0]['y'] 

        context = {'schedules':schedules,
                'lodge':lodge, 'address':address, 
                'x': x, 'y':y,
                'lodge_id':lodge_id}

        
    return render(request, 'target8.html',context)
    
def targetLink(request, lodge_id):
     # 매니저 숙박 업소 정보 가져오기 
    manager = managers.objects.get(user_id= request.user.id)
    
    # 체크리스트 인스턴스 적재
    instance = checklist()
    instance.manager_id = manager
    instance.lodge_id = lodges.objects.get(id = lodge_id)
    instance.room_num = request.POST['room_num']
    instance.check_date = datetime.now().date()
    instance.check_start = datetime.now()
    instance.check_finish = datetime.now() # 다음 페이지에서 수정되어야 함
    instance.save()

    room_num = request.POST['room_num']



    return HttpResponseRedirect(reverse('checklist:checklist', kwargs= {'lodge_id':lodge_id,'room_num':room_num}))
    