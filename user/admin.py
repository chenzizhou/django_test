from django.contrib import admin

from user.models import Account


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ['pk', 'account', 'password', 'platform']


admin.site.register(Account, AccountAdmin)
