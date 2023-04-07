from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.SiteSetting, models.SiteSettingAdmin)
admin.site.register(models.Dict, models.DictAdmin)
admin.site.register(models.DictItem,models.DictItemAdmin)

