from django.contrib import admin
from .models import Conference
from users.models import *
from django.db.models import Count



# Register your models here.
class ReservationInLine(admin.StackedInline):
    model=Reservation
    extra=1
    readonly_fields=('reservation_date',)
    can_delete=True
class ParticipantFilter(admin.SimpleListFilter):
    title='participant_number'
    parameter_name='participants'
    def lookups(self,request,model_admin):
        return(
            ('0',('no_participants')),
            ('more',('more than one  participant'))
        )
    def queryset(self,request,queryset):
        if self.value()=='0':
            return queryset.annotate(participant_count=Count('reservation')).filter(participant_count=0)

        if self.value()=='more':
            return queryset.annotate(participant_count=Count('reservation')).filter(participant_count__gt=0)
            
            

    


class ConferenceAdmin(admin.ModelAdmin):
    list_display=['title','location','start_date','end_date','price','created_at','update_at']
    search_fields=('title',)
    list_per_page=2
    ordering=('start_date','title')
    fieldsets=(
        ('description',{
            'fields':('title','description','category','location','price','capacity')
        }),
         ('horraire',{
            'fields':('start_date','end_date')
        }),
         ('Documents',{
            'fields':('program',)
        })
    
        
    )
    
    
    readonly_fields=('created_at','update_at')
    inlines=[ReservationInLine]
    autocomplete_fields=('category',)
    list_filter=('title',ParticipantFilter)














admin.site.register(Conference,ConferenceAdmin)

