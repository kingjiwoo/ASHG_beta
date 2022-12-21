from django.db import models
from django.db.models import Sum


# Create your models here.

class lodges(models.Model):
    #Fields
    id = models.AutoField(primary_key=True,  help_text='Unique ID for this particular lodges ')
    user_id = models.OneToOneField(
        'user.User', to_field = 'id', 
        on_delete=models.CASCADE, null=True, 
        related_name= 'lodge_id')
    account = models.CharField(
        verbose_name=('업소 계정명'),
        max_length=30,
        unique=True
    )
    contract_extension =  models.DateTimeField(
        verbose_name=('마지막 계약 연장일'),
        null = True
    )

    READY = '준비중'
    CONTRACT = '계약중'
    EXPIRED = '계약만료'

    CONTRACT_STATUS = (
        (READY, 'Ready'),
        (CONTRACT, 'Contract'),
        (EXPIRED, 'Expired')
    )

    status = models.CharField(
        max_length = 10,
        choices = CONTRACT_STATUS,
        default=True,
        help_text = '계약 상태를 입력하세요'
    )

    address = models.CharField(
        max_length = 30,
        default=True,
        help_text = '상세주소를 입력하세요'
    )

    A = '단독주택'
    B = '빌라'
    C = '아파트'
    D = '오피스텔'
    E = '상가'
    F = '빌딩'
    G = '모텔'

    BUILDING_TYPE = (
        (A, '단독주택'),
        (B, '빌라'),
        (C, '아파트'),
        (D, '오피스텔'),
        (E, '상가'),
        (F, '빌딩'),
        (G, '모텔'),
    )

    building_type = models.CharField(
        max_length = 10,
        choices = BUILDING_TYPE,
        default=True,
        help_text = '단독주택/빌라/아파트/오피스텔/상가/빌딩/모텔 중 하나를 입력하세요'
    )

    officer_name = models.CharField(
        verbose_name=('담당자'),
        max_length=10,
        unique=True
    )

    officer_contact = models.CharField(
        verbose_name=('담당자 연락처'),
        max_length=30,
        unique=True
    )

    BK = 'bk'
    BL = 'bl'
    GR = 'gr'

    GRADE = (
        (BK ,'bk'),
        (BL, 'bl'),
        (GR, 'gr'),
    )

    grade = models.CharField(
        max_length = 10,
        choices = GRADE,
        default=True,
        help_text = '계약 상태를 입력하세요'
    )

    YES = '획득'
    NO = '미획득'

    PATENT = (
        (YES, '획득'),
        (NO, '미획득'),
    )

    patent = models.CharField(
        max_length = 10,
        choices = PATENT,
        default=True,
        help_text = '계약 상태를 입력하세요'
    )

    area =  models.CharField(
        verbose_name=('배정구역'),
        max_length= 10,
    )

    manager =  models.CharField(
        verbose_name=('담당 매니저'),
        max_length=10,
        
    )

    size = models.CharField(
        verbose_name=('객실 평균 면적'),
        max_length=10,
    )

    cnt_room = models.CharField(
        verbose_name=('객실 갯수'),
        max_length=10,
    )

    facilities = models.CharField(
        verbose_name=('부대 시설'),
        max_length=200,
    )

    monitoring_time = models.IntegerField(
        verbose_name=('모니터링 소요시간'),
        help_text ='단위: 분'
    )


    latest_monitoring = models.DateTimeField(
        verbose_name=('최근 모니터링 일시'),
        null = True
    )

    class Meta:
            ordering = ('-id',)

    def __str__(self):
          return str(self.id)







