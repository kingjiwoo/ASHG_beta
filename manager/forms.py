from multiprocessing import managers

from django import forms
from django.utils.translation import gettext_lazy as _
import datetime

from .models import managers, schedule


class ManagerInfoForm(forms.ModelForm):
    user_id = forms.CharField(
        label=_('유저 번호'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('유저 번호'),
                'required': 'True',
            }
        )
    )
    account = forms.CharField(
        label=_('매니저 계정 명'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('ex)서울강남0142'),
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
    monitoring_time = forms.IntegerField(
        label=_('모니터링 시간'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('단위: 분'),
                'required': 'True',
            }
        )
    )

    monitoiring_cnt = forms.IntegerField(
        label=_('모니터링 업소 갯수'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('모니터링 업소 갯수'),
                'required': 'True',
            }
        )
    )
    class Meta:
        model = managers
        fields = ('user_id', 'account')

class ManagerChangeForm(forms.ModelForm):
    user_id = forms.CharField(
        label=_('유저 번호'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('유저 번호'),
                'required': 'True',
            }
        )
    )
    account = forms.CharField(
        label=_('매니저 계정 명'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('ex)서울강남0142'),
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
    monitoring_time = forms.IntegerField(
        label=_('모니터링 시간'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('단위: 분'),
                'required': 'True',
            }
        )
    )

    monitoiring_cnt = forms.IntegerField(
        label=_('모니터링 업소 갯수'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('모니터링 업소 갯수'),
                'required': 'True',
            }
        )
    )
    class Meta:
        model = managers
        fields = ('user_id', 'account')

    def save(self, commit=True):
        # Save the provided password in hashed format
        manager = super(ManagerInfoForm, self).save(commit=False)
        if commit:
            manager.save()
        return manager


class ScheduleInput(forms.ModelForm):
    user_id = forms.CharField(
        label=_('유저 식별 번호'),
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
        label=_('매니저 계정 명'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('ex)서울강남0142'),
                'required': 'True',
            }
        )
    )

    lo1 = forms.CharField(
        label=_('1번 째 업소'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('1번 째 업소'),
                'required': 'True',
            }
        )
    )
    lo2 = forms.CharField(
        label=_('2번 째 업소'),
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('2번 째 업소'),
                'required': 'False',
            }
        )
    )
    lo3 = forms.CharField(
        label=_('3번 째 업소'),
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('3번 째 업소'),
                'required': 'False',
            }
        )
    )
    lo4 = forms.CharField(
        label=_('4번 째 업소'),
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('4번 째 업소'),
                'required': 'False',
            }
        )
    )
    lo5 = forms.CharField(
        label=_('5번 째 업소'),
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('5번 째 업소'),
                'required': 'False',
            }
        )
    )
    lo6 = forms.CharField(
        label=_('6번 째 업소'),
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('6번 째 업소'),
                'required': 'Fasle',
            }
        )
    )
    class Meta:
        model = schedule
        fields = ('user_id',)

class ScheduleChange(forms.ModelForm):
    
    user_id = forms.CharField(
        label=_('유저 식별 번호'),
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
        label=_('매니저 계정 명'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('ex)서울강남0142'),
                'required': 'True',
            }
        )
    )

    lo1 = forms.CharField(
        label=_('1번 째 업소'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('1번 째 업소'),
                'required': 'True',
            }
        )
    )
    lo2 = forms.CharField(
        label=_('2번 째 업소'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('2번 째 업소'),
                'required': 'False',
            }
        )
    )
    lo3 = forms.CharField(
        label=_('3번 째 업소'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('3번 째 업소'),
                'required': 'False',
            }
        )
    )
    lo4 = forms.CharField(
        label=_('4번 째 업소'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('4번 째 업소'),
                'required': 'False',
            }
        )
    )
    lo5 = forms.CharField(
        label=_('5번 째 업소'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('5번 째 업소'),
                'required': 'False',
            }
        )
    )
    lo6 = forms.CharField(
        label=_('6번 째 업소'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('6번 째 업소'),
                'required': 'False',
            }
        )
    )
    class Meta:
        model = schedule
        fields = ('user_id',)