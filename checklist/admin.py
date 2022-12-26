from django.contrib import admin
from .models import checklist, features

# Register your models here.
# class ChecklistAdmin(admin.ModelAdmin):
#     list_display =
#     list_display_links = 
#     list_filter = 


class FeatureAdmin(admin.ModelAdmin):
    list_display = ( 'question_id','division','place','object','question',)
    list_display_links = ('question_id',)
    list_filter = ('division', 'place','object','question',)
    fieldsets = (
        (None, {'fields': ( 'question_id',)}),
        (('feature info'), {'fields': ('division', 'place','object','question',
        )}),
        
    )
 

admin.site.register(checklist)
admin.site.register(features,FeatureAdmin)

