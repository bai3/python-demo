from django.http import HttpResponse

from TestModel.models import Test


# 数据库操作
def testdb(request):
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()
    return  HttpResponse('<p>修改成功</p>')