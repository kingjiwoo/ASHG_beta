from django.contrib import admin
from django.utils.translation import gettext_lazy as _


from .forms import ManagerInfoForm, ManagerChangeForm, ScheduleInput, ScheduleChange
from .models import managers, schedule, timeline


# Register your models here.
class ManagerAdmin(admin.ModelAdmin):


    list_display = ('id','user_id', 'account','area','monitoring_time','monitoring_cnt',)
    list_display_links = ('id','user_id',)
    list_filter = ('area',)
    fieldsets = (
        (None, {'fields': ('user_id', 'account',)}),
        (_('Manager info'), {'fields': ( 'area','monitoring_time','monitoring_cnt',)}),
        
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'account','area','monitoring_time','monitoring_cnt',)}
         ),
    )
    search_fields = ('id','account')
    ordering = ('id','user_id', 'account',)

    filter_horizontal = ()


#등록
admin.site.register(managers, ManagerAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    

    list_display = ('id','lo1','lo2','lo3','lo4','lo5','lo6','lo7','lo8',)
    list_display_links = ('id',)
    list_filter = ('id',)
    fieldsets = (
        (None, {'fields': ('id',)}),
        (_('Schedule info'), {'fields': ('lo1','lo2','lo3','lo4','lo5','lo6','lo7','lo8',)}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id','lo1','lo2','lo3','lo4','lo5','lo6','lo7','lo8',)}
         ),
    )
    search_fields = ('id',)
    ordering = ('id',)
    filter_horizontal = ()

class TimelineAdmin(admin.ModelAdmin):
    

    list_display = ('id','tl1','tl2','tl3','tl4','tl5','tl6','tl7','tl8',)
    list_display_links = ('id',)
    list_filter = ('id',)
    fieldsets = (
        (None, {'fields': ('id',)}),
        (_('Schedule info'), {'fields': ('tl1','tl2','tl3','tl4','tl5','tl6','tl7','tl8',)}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id','tl1','tl2','tl3','tl4','tl5','tl6','tl7','tl8',)}
         ),
    )
    search_fields = ('id',)
    ordering = ('id',)
    filter_horizontal = ()


#등록
admin.site.register(schedule, ScheduleAdmin)
admin.site.register(timeline, TimelineAdmin)