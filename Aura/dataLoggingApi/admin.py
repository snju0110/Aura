from django.contrib import admin

# Register your models here.


from .models import *
admin.register(demDatatable)(admin.ModelAdmin)
admin.register(demDailyData)(admin.ModelAdmin)
admin.register(foodDailyData)(admin.ModelAdmin)
admin.register(settingDemCategory)(admin.ModelAdmin)