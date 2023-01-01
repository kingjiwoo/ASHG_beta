from django.contrib import admin
from .models import checklist, features

#Register your models here.
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('id','manager_id','lodge_id','check_date','room_num','check_start','check_finish',
                    'q1','q2','q3','q4','q5','q6','q7','q8','q9','q10',
                    'q11','q12','q13','q14','q15','q16','q17','q18','q19','q20',
                    'q21','q22','q23','q24','q25','q26','q27','q28','q29','q30',
                    'q31','q32','q33','q34','q35','q36','q37','q38','q39','q40',
                    'q41','q42','q43','q44','q45','q46','q47','q48','q49',)
    list_display_links = ('id')
    list_filter = ('manager_id','lodge_id','check_date')



class FeatureAdmin(admin.ModelAdmin):
    list_display = ( 'question_id','division','place','object','question',)
    list_display_links = ('question_id',)
    list_filter = ('division', 'place','object','question',)
    fieldsets = (
        (None, {'fields': ( 'question_id',)}),
        (('feature info'), {'fields': ('division', 'place','object','question',
        )}),
        
    )
 

admin.site.register(checklist, ChecklistAdmin)
admin.site.register(features,FeatureAdmin)

