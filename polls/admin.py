from django.contrib import admin
from .models import Question,Choice,Token,Passwordresetcodes

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Token)
admin.site.register(Passwordresetcodes)
# Register your models here.
