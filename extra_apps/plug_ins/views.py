from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .db_config import DB_helper


def getJson(request):
    """
    后台表格所需数据
    """
    dbheper = DB_helper()

    ProductName = request.GET.get('Name', None)
    StartTime = request.GET.get('StartTime', None)
    EndTime = request.GET.get('EndTime', None)
    NowTime = request.GET.get('NowTime', None)
    Path = request.GET.get('Path', None)

    if Path == '/xadmin/ta/menu1/':
        massages = dbheper.select_menu_1(ProductName, StartTime, EndTime, NowTime)
        keys = ['date', 'productname', 'stunum', 'grade']

    elif Path == '/xadmin/ta/menu2/':
        massages = dbheper.select_menu_2(ProductName, StartTime, EndTime, NowTime)
        keys = ['date', 'productname', 'stunum', 'grade']

    elif Path == '/xadmin/ta/menu2/':
        massages = dbheper.select_menu_3(ProductName, StartTime, EndTime, NowTime)
        keys = ['date', 'productname', 'stunum', 'grade']

    list_json = [dict(zip(keys, item)) for item in massages]
    res = {}
    res['rows'] = list_json

    return JsonResponse(res, safe=False)


class MenuOneXadminView(View):
    """
        功能一
    """

    def get(self, request):
        return render(request, 'plug_ins/menu1.html', {})


class MenuTwoXadminView(View):
    """
        功能二
    """

    def get(self, request):
        return render(request, 'plug_ins/menu2.html', {})


class MenuTheXadminView(View):
    """
        功能三
    """

    def get(self, request):
        return render(request, 'plug_ins/menu3.html', {})
