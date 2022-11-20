from django.contrib import admin

from khoahoc.models import LevelKhoaHoc, MonHoc, KhoaHoc, BaiHoc


@admin.register(KhoaHoc)
class KhoahocAdmin(admin.ModelAdmin):
    list_display = ("ten_khoa_hoc",)


@admin.register(LevelKhoaHoc)
class LevelKhoahocAdmin(admin.ModelAdmin):
    list_display = ("ten_level","khoa_hoc")


@admin.register(MonHoc)
class MonHocAdmin(admin.ModelAdmin):
    list_display = ("ten_mon_hoc","level",)

@admin.register(BaiHoc)
class BaiHocAdmin(admin.ModelAdmin):
    list_display = ("ten_bai",)