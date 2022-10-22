from django.db import models

class KhoaHoc(models.Model):
    ten_khoa_hoc = models.CharField(max_length=50)
    url_anh = models.CharField(max_length=100)

    def __str__(self):
        return self.ten_khoa_hoc
class LevelKhoaHoc(models.Model):
    ten_level = models.CharField(max_length=50)
    khoa_hoc = models.ForeignKey(KhoaHoc, on_delete=models.CASCADE)
    def __str__(self):
        return self.ten_level +" " + str(self.khoa_hoc)
class MonHoc(models.Model):
    ten_mon_hoc = models.CharField(max_length=50)
    url_anh = models.CharField(max_length=100)
    level = models.ForeignKey(LevelKhoaHoc, on_delete=models.CASCADE)
    def __str__(self):
        return self.ten_mon_hoc
class BaiHoc(models.Model):
    ten_bai = models.CharField(max_length=50)
    url_anh = models.CharField(max_length=100)
    thoi_luong = models.CharField(max_length=100)
    video_id = models.IntegerField()
    oder = models.CharField(max_length=50)