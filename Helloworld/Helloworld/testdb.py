# from django.http import HttpResponse
# from Block_test_Model.models import Block_test_Model
#
# #数据库操作
# def testdb(requet):
#     # 初始化
#     response = ""
#     response1 = ""
#     response2 = ""
#     # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
#     list = Test.objects.all()
#
#     # filter相当于SQL中的WHERE，可设置条件过滤结果
#     list2 = Test.objects.filter()
#
#     # 获取单个对象
#     response3 = Test.objects.get(id=1)
#
#     # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
#     Test.objects.order_by('fullname')[0:2]
#
#     # 数据排序
#     Test.objects.order_by("id")
#
#     # 上面的方法可以连锁使用
#     Test.objects.filter(fullname="runoob").order_by("id")
#
#     # 输出所有数据
#     for var in list:
#         response1 += var.fullname + " "
#     response = response1
#     for var in list2:
#         response2 += var.fullname + " "
#     response = response1
#     return HttpResponse("<p>" + response2 + "</p>")
