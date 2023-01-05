from django.contrib import admin
from .models import User, Type,Comfort,SettingSize
# Register your models here.
admin.site.register(User)
admin.site.register(SettingSize)
admin.site.register(Type)
admin.site.register(Comfort)

