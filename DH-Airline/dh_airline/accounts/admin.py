# April 16, 2020
# Gerardo Pena
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from accounts.models import Account

class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined','last_login','is_admin','is_staff')
	search_fields = ('email','username')
	readonly_fields = ('date_joined','last_login')
	
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	
admin.site.register(Account,AccountAdmin)