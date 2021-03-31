from django.contrib import admin
from .models import qusform,allans

@admin.register(qusform)
class apiAdmin(admin.ModelAdmin):
    list_display = [ 'qno','qus','op1','op2','op3','op4' ]

@admin.register(allans)
class postapiAdmin(admin.ModelAdmin):
    list_display = [ 'qusno','qus','ans',]
