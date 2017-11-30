from django.contrib import admin
from user.models import Notice, Noticeforowner, UserProfile
from django.contrib.auth.models import User

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('subject', 'cr_date')
    list_filter = ['cr_date']
    search_fields = ['subject']
admin.site.register(Notice, NoticeAdmin)
class NoticeforownerAdmin(admin.ModelAdmin):
    list_display = ('subject','cr_date')
    list_filter=['cr_date']
    search_fields=['subject']
admin.site.register(Noticeforowner, NoticeforownerAdmin)
class UserprofileAdmin(admin.ModelAdmin):
    list_display= ('user','pname','email_id')
admin.site.register(UserProfile,UserprofileAdmin)
