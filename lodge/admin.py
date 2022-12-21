from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import lodges

# Register your models here.

class LodgeAdmin(admin.ModelAdmin):
    


    list_display = ('id','user_id', 'account','contract_extension','status','address','building_type','grade', 'patent','facilities',
    'cnt_room', 'size','manager','area','officer_name', 'officer_contact','monitoring_time', 'latest_monitoring',)
    list_display_links = ('id','user_id',)
    list_filter = ('status', 'building_type','grade','patent',)
    fieldsets = (
        (None, {'fields': ('user_id', 'account',)}),
        (_('Lodge info'), {'fields': ('contract_extension','status','address', 'building_type', 'grade','patent','facilities',
    'cnt_room', 'size','manager','area','officer_name', 'officer_contact','monitoring_time', 'latest_monitoring',)}),
        
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'account','contract_extension','status','address','building_type','grade', 'patent','facilities',
    'cnt_room', 'size','manager','area','officer_name', 'officer_contact','monitoring_time', 'latest_monitoring',
    )}
         ),
    )
    search_fields = ('id','account')
    ordering = ('id','user_id', 'account',)
    filter_horizontal = ()


#등록
admin.site.register(lodges, LodgeAdmin)


