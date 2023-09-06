from django.contrib import admin

# Register your models here.


from .models import *
admin.register(DocData)(admin.ModelAdmin)
admin.register(docma)(admin.ModelAdmin)
admin.register(doc_holder)(admin.ModelAdmin)
admin.register(doc_type)(admin.ModelAdmin)