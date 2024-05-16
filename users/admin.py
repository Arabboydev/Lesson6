from django.contrib import admin
from .models import CustomUser


# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'username', 'first_name', 'date_joined')
#     list_filter = ['is_staff', 'is_superuser', 'first_name', 'last_name']
#     list_display = []


admin.site.register(CustomUser)
# admin.site.register(CustomUser, CustomUserAdmin)
