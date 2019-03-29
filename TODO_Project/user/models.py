# from django.db import models
#
# # Create your models here.
# from django.db import models
#
#
# class User(models.Model):
#     """
#      用户表
#     """
#     username = models.CharField(max_length=20, unique=True, null=True, blank=True, verbose_name="姓名")
#     password = models.CharField(max_length=255, verbose_name="密码")
#     GENDER = (
#         ("male", u"男"),
#         ("female", u"女")
#     )
#     gender = models.CharField(max_length=6, choices=GENDER, default="female",
#                               verbose_name="性别")
#
#
#     class Meta:
#         db_table = 'tb_user'
