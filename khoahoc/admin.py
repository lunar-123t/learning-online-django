from django.contrib import admin

from khoahoc.models import Khoahoc


@admin.register(Khoahoc)
class KhoahocAdmin(admin.ModelAdmin):
    list_display = ("ten_khoa_hoc",)