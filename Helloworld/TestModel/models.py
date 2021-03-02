from django.db import models

# Create your models here.

class BlocktestModel(models.Model):
    IPaddress=models.TextField(verbose_name='IP地址')
    MACaddress=models.TextField(verbose_name='MAC地址')
    Arrowflag = models.BooleanField(verbose_name='是否安装双箭头')
    # ps_persons=models.CharField(max_length=255,verbose_name='评审人员')
    # jd_persons = models.CharField(max_length=255, verbose_name='监督人员')
    Updatetime = models.DateTimeField(verbose_name='更新时间')
    class Meta():
        db_table='Address_table'