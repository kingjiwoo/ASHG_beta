from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class checklist(models.Model):
    id = models.AutoField(primary_key = True)
    manager_id = models.ForeignKey(
        'manager.managers', to_field = 'id', 
        on_delete=models.CASCADE, 
        related_name = 'check_manager')
    lodge_id = models.ForeignKey(
        'lodge.lodges', to_field = 'id', 
        on_delete=models.CASCADE,
        related_name = 'check_lodge')
    check_date = models.DateField()
    room_num = models.CharField(max_length=10)
    check_start = models.DateTimeField(
        verbose_name=_('Monitoring_Start'),
        null= True
    )
    check_finish = models.DateTimeField(
        verbose_name=_('Monitoring_Finished'),
        default=timezone.now,
        null=True
    )
    
    q1 = models.CharField(max_length= 10,null=True)
    q2 = models.CharField(max_length= 10,null=True)
    q3 = models.CharField(max_length= 10,null=True)
    q4 = models.CharField(max_length= 10,null=True)
    q5 = models.CharField(max_length= 10,null=True)
    q6 = models.CharField(max_length= 10,null=True)
    q7 = models.CharField(max_length= 10,null=True)
    q8 = models.CharField(max_length= 10,null=True)
    q9 = models.CharField(max_length= 10,null=True)
    q10 = models.CharField(max_length= 10,null=True)
    q11 = models.CharField(max_length= 10,null=True)
    q12 = models.CharField(max_length= 10,null=True)
    q13 = models.CharField(max_length= 10,null=True)
    q14 = models.CharField(max_length= 10,null=True)
    q15 = models.CharField(max_length= 10,null=True)
    q16 = models.CharField(max_length= 10,null=True)
    q17 = models.CharField(max_length= 10,null=True)
    q18 = models.CharField(max_length= 10,null=True)
    q19 = models.CharField(max_length= 10,null=True)
    q20 = models.CharField(max_length= 10,null=True)
    q21 = models.CharField(max_length= 10,null=True)
    q22 = models.CharField(max_length= 10,null=True)
    q23 = models.CharField(max_length= 10,null=True)
    q24 = models.CharField(max_length= 10,null=True)
    q25 = models.CharField(max_length= 10,null=True)
    q26 = models.CharField(max_length= 10,null=True)
    q27 = models.CharField(max_length= 10,null=True)
    q28 = models.CharField(max_length= 10,null=True)
    q29 = models.CharField(max_length= 10,null=True)
    q30 = models.CharField(max_length= 10,null=True)
    q31 = models.CharField(max_length= 10,null=True)
    q32 = models.CharField(max_length= 10,null=True)
    q33 = models.CharField(max_length= 10,null=True)
    q34 = models.CharField(max_length= 10,null=True)
    q35 = models.CharField(max_length= 10,null=True)
    q36 = models.CharField(max_length= 10,null=True)
    q37 = models.CharField(max_length= 10,null=True)
    q38 = models.CharField(max_length= 10,null=True)
    q39 = models.CharField(max_length= 10,null=True)
    q40 = models.CharField(max_length= 10,null=True)
    q41 = models.CharField(max_length= 10,null=True)
    q42 = models.CharField(max_length= 10,null=True)
    q43 = models.CharField(max_length= 10,null=True)
    q44 = models.CharField(max_length= 10,null=True)
    q45 = models.CharField(max_length= 10,null=True)
    q46 = models.CharField(max_length= 10,null=True)
    q47 = models.CharField(max_length= 10,null=True)
    q48 = models.CharField(max_length= 10,null=True)
    q49 = models.CharField(max_length= 10,null=True)
       
    class Meta:
            ordering = ('-id',)

    def __str__(self):
          return str(self.id)

    
class features(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.IntegerField(
        verbose_name=('question_num'),
    )

    division = models.CharField(
        verbose_name=('분류'),
        max_length=10,
    )

    place = models.CharField(
        verbose_name=('장소'),
        max_length=10,
    )

    object = models.CharField(
        verbose_name=('대상'),
        max_length=10,
    )

    question = models.CharField(
        verbose_name=('질문 내용'),
        max_length=70,
    )

    class Meta:
        ordering = ('question_id',)

    def __str__(self):
          return str(self.id)

