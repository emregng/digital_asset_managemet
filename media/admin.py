from django.contrib import admin

from .models import Video, Tag, Account

# Register your models here.
admin.site.register(Video)
admin.site.register(Account)
admin.site.register(Tag)
