from django.db import models
from django.contrib import admin


# Create your models here.
class SiteSetting(models.Model):
    name = models.CharField(max_length=150, verbose_name="name")
    value = models.CharField(max_length=500, verbose_name="value")
    sequence = models.IntegerField(verbose_name="Sequence", default=0)

    class Meta:
        ordering = ("sequence",)

    def __str__(self):
        return self.name


class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ("name", "value", "sequence")
    list_editable = ("sequence",)


class Dict(models.Model):
    name = models.CharField(max_length=500, verbose_name="Name")
    sequence = models.IntegerField(verbose_name="Sequence", default=0)
    is_hidden = models.BooleanField(verbose_name="Hidden")

    class Meta:
        ordering = ("sequence",)

    def __str__(self):
        return self.name


class DictAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sequence", "is_hidden")
    list_editable = ("sequence",)


class DictItem(models.Model):
    parent = models.ForeignKey(to=Dict, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name="Name")
    value = models.CharField(max_length=150, verbose_name="Value")
    sequence = models.IntegerField(verbose_name="Sequence", default=0)

    class Meta:
        ordering = ("sequence",)

    def __str__(self):
        return self.name


class DictItemAdmin(admin.ModelAdmin):
    list_display = ("id", "parent", "name", "value", "sequence")
    list_filter = ("parent",)
    list_display_links = ("parent",)
    list_editable = ("sequence",)
    list_select_related = ("parent",)
