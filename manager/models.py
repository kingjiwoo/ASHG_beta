
from django.db import models
from lodge.models import lodges



# Create your models here.
class managers(models.Model):
    #Fields
    id = models.AutoField(primary_key=True, help_text='Unique ID for this particular manager ')
    user_id = models.OneToOneField(
        'user.User', to_field = 'id', 
        on_delete=models.CASCADE,
        related_name = 'manager_id')
    account = models.CharField(
        verbose_name=('매니저 계정명'),
        max_length=30,
        unique=True
    )


    area =  models.CharField(
        verbose_name=('배정구역'),
        max_length=10,
    )

    monitoring_cnt = models.IntegerField(
        verbose_name=('모니터링 횟수'),
        help_text ='단위: 회'
    )

    monitoring_time = models.IntegerField(
        verbose_name=('모니터링 소요시간'),
        help_text ='단위: 분'
    )
    #monitoring_cnt = lodges.objects.filter(manager__contains = user_id).count()
    #monitoring_time = 15 * monitoring_cnt + lodges.objects.filter(manager__contains = user_id).aggregate(Sum('monitoring_time'))


    



    class Meta:
            ordering = ('-id',)

    def __str__(self):
          return str(self.id) 


class schedule(models.Model):
    id = models.OneToOneField(
        'managers', to_field = 'user_id', 
        on_delete=models.CASCADE,
        related_name = 'manager_id',
        primary_key = True)

    lo1 = models.ForeignKey(
        'lodge.lodges', to_field = 'account', 
        on_delete=models.CASCADE, null=True, 
        related_name= 'lo1')
   
    lo2 = models.ForeignKey(
        'lodge.lodges', to_field = 'account', 
        on_delete=models.CASCADE, null=True, 
        related_name= 'lo2',)

    lo3 = models.ForeignKey(
        'lodge.lodges', to_field = 'account', 
        on_delete=models.CASCADE, null=True, 
        related_name= 'lo3')

    lo4 = models.ForeignKey(
        'lodge.lodges', to_field = 'account', 
        on_delete=models.CASCADE, null=True, 
        related_name= 'lo4')

    lo5 = models.ForeignKey(
        'lodge.lodges', to_field = 'account', 
        on_delete=models.CASCADE, null=True, 
        related_name= 'lo5')

    lo6 = models.ForeignKey(
        'lodge.lodges', to_field = 'account', 
        on_delete=models.CASCADE, null=True, 
        related_name= 'lo6')

    lo7 = models.ForeignKey(
        'lodge.lodges', to_field = 'account', 
        on_delete=models.CASCADE, null=True, 
        related_name= 'lo7')

    lo8 = models.ForeignKey(
        'lodge.lodges', to_field = 'account', 
        on_delete=models.CASCADE, null=True, 
        related_name= 'lo8')

    class Meta:
            ordering = ('-id',)

    def __str__(self):
          return str(self.id)

    #def lo1(self):
        #return int(self.lo1)

# 시간을 입력하는 클래스 
class timeline(models.Model):
    id = models.OneToOneField(
        'managers', to_field = 'user_id', 
        on_delete=models.CASCADE,
        related_name = 'manager_id2',
        primary_key = True)

    tl1 = models.CharField(
        verbose_name=('1번째 일정'),
        max_length=50,
        default = '미정'
    )

    tl2 = models.CharField(
        verbose_name=('2번째 일정'),
        max_length=50,
        default = '미정',
        
    )
    tl3 = models.CharField(
        verbose_name=('3번째 일정'),
        max_length=50,
        default = '미정'
    )
    tl4 = models.CharField(
        verbose_name=('4번째 일정'),
        max_length=50,
        default = '미정'
    )
    tl5 = models.CharField(
        verbose_name=('5번째 일정'),
        max_length=50,
        default = '미정'
    )
    tl6 = models.CharField(
        verbose_name=('6번째 일정'),
        max_length=50,
        default = '미정'
    )

    tl7 = models.CharField(
        verbose_name=('6번째 일정'),
        max_length=50,
        default = '미정'
    )

    tl8 = models.CharField(
        verbose_name=('6번째 일정'),
        max_length=50,
        default = '미정'
    )
    class Meta:
            ordering = ('-id',)

    def __str__(self):
          return str(self.id)

    


