from django import forms
from django.utils.translation import gettext_lazy as _
import datetime

from .models import lodges

# 업소 정보 기입 폼
class LodgeInfoForm(forms.ModelForm):
    user_id = forms.CharField(
        label=_('업소 식별 번호'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('유저 식별 번호'),
                'required': 'True',
            }
        )
    )
    account = forms.CharField(
        label=_('업소 계정 명'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('ex)서울강남0142'),
                'required': 'True',
            }
        )
    )
    contract_extension = forms.DateTimeField(required=True)
    status = forms.CharField(
        label=_('계약 상태'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Phone Number'),
                'required': 'True',
            }
        )
    )
    address = forms.CharField(
        label=_('업소 주소'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('업소 주소'),
                'required': 'True',
            }
        )
    )
    building_type = forms.CharField(
        label=_('건물 유형'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('건물 유형'),
                'required': 'True',
            }
        )
    )
    officer_name = forms.CharField(
        label=_('업소 담당자 이름'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('업소 담당자 이름'),
                'required': 'True',
            }
        )
    )
    officer_contact = forms.CharField(
        label=_('업소 담당자 연락처'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('업소 담당자 연락처'),
                'required': 'True',
            }
        )
    )
    grade = forms.CharField(
        label=_('인증 등급'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('인증 등급'),
                'required': 'True',
            }
        )
    )
    patent = forms.CharField(
        label=_('인증 듬급 획득 여부'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('인증 등급 획득 여부'),
                'required': 'True',
            }
        )
    )
    area = forms.CharField(
        label=_('배정 구역'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('배정 구역'),
                'required': 'True',
            }
        )
    )
    manager = forms.CharField(
        label=_('담당 매니저'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('담당 매니저'),
                'required': 'True',
            }
        )
    )
    size = forms.IntegerField(
        label=_('면적'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('면적'),
                'required': 'True',
            }
        )
    )
    cnt_bed = forms.IntegerField(
        label=_('방 갯수'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('방 갯수'),
                'required': 'True',
            }
        )
    )
    cnt_bath = forms.IntegerField(
        label=_('욕실 갯수'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('욕실 갯수'),
                'required': 'True',
            }
        )
    )
    facilities =forms.CharField(
        label=_('보유 시설'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('보유 시설'),
                'required': 'True',
            }
        )
    )
    monitoring_time = forms.IntegerField(
        label=_('모니터링 소요 시간'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('단위: 분'),
                'required': 'True',
            }
        )
    )
    condition_monitoring = forms.IntegerField(
        label=_('모니터링 가능 여부'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('모니터링 가능여부'),
                'required': 'False',
            }
        )
    )
    latest_monitoring = forms.DateTimeField(required=True)
    
    class Meta:
        model = lodges
        fields = ('id', 'account', 'status', 'building_type', 'grade', 'patent', 'area')

# 업소 정보 변경 폼 
class LodgeChangeForm(forms.ModelForm):
    account = forms.CharField(
        label=_('업소 계정 명'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('ex)서울강남0142'),
                'required': 'True',
            }
        )
    )
    contract_extension = forms.DateTimeField(required=True)
    status = forms.CharField(
        label=_('계약 상태'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('준비중/ 계약중/ 계약만료'),
                'required': 'True',
            }
        )
    )
    address = forms.CharField(
        label=_('업소 주소'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('업소 주소'),
                'required': 'True',
            }
        )
    )
    building_type = forms.CharField(
        label=_('건물 유형'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('건물 유형'),
                'required': 'True',
            }
        )
    )
    officer_name = forms.CharField(
        label=_('업소 담당자 이름'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('업소 담당자 이름'),
                'required': 'True',
            }
        )
    )
    officer_contact = forms.CharField(
        label=_('업소 담당자 연락처'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('업소 담당자 연락처'),
                'required': 'True',
            }
        )
    )
    grade = forms.CharField(
        label=_('인증 등급'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('인증 등급'),
                'required': 'True',
            }
        )
    )
    patent = forms.CharField(
        label=_('인증 듬급 획득 여부'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('인증 등급 획득 여부'),
                'required': 'True',
            }
        )
    )
    area = forms.CharField(
        label=_('배정 구역'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('배정 구역'),
                'required': 'True',
            }
        )
    )
    manager = forms.CharField(
        label=_('담당 매니저'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('담당 매니저'),
                'required': 'True',
            }
        )
    )
    size = forms.IntegerField(
        label=_('면적'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('면적'),
                'required': 'True',
            }
        )
    )
    cnt_bed = forms.IntegerField(
        label=_('방 갯수'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('방 갯수'),
                'required': 'True',
            }
        )
    )
    cnt_bath = forms.IntegerField(
        label=_('욕실 갯수'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('욕실 갯수'),
                'required': 'True',
            }
        )
    )
    facilities =forms.CharField(
        label=_('보유 시설'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('보유 시설'),
                'required': 'True',
            }
        )
    )
    monitoring_time = forms.IntegerField(
        label=_('모니터링 소요 시간'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('단위: 분'),
                'required': 'True',
            }
        )
    )
    condition_monitoring = forms.IntegerField(
        label=_('모니터링 가능 여부'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('모니터링 가능여부'),
                'required': 'False',
            }
        )
    )
    latest_monitoring = forms.DateTimeField(required=True)
    
    class Meta:
        model = lodges
        fields = ('id', 'account', 'status', 'building_type', 'grade', 'patent', 'area')

