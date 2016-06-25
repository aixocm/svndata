from django.contrib import admin
import models
# Register your models here.
class CategroyAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','author','hidden','publish_date')
admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Category,CategroyAdmin)
admin.site.register(models.Comment)
admin.site.register(models.ThumbUp)
admin.site.register(models.UserGroup)
admin.site.register(models.UserProfiles)
