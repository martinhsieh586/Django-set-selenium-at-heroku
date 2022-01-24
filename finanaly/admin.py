from django.contrib import admin
from finanaly.models import user, bussinessinfo, pocket

#資料庫在admin頁面呈現樣式
class useradmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'useremail', 'userpassword')
class bussinessinfoadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
class pocketadmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'url')

#register your model here
admin.site.register(user, useradmin)
admin.site.register(bussinessinfo, bussinessinfoadmin)
admin.site.register(pocket, pocketadmin)
