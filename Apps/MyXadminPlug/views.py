from django.shortcuts import render
from django.views import View
from django.db.models import Q

from MyXadminPlug.models import DefinedFund

from . import config

from django.http import JsonResponse

from django.http import HttpResponse
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def getJson(request):

    StuNum = request.GET.get('StuNum', None)
    StartTime = request.GET.get('StartTime', None)
    EndTime = request.GET.get('EndTime', None)

    print(StuNum, StartTime, EndTime)

    res = {}

    # 数据库返回如下值：{'rows': [], 'columns': []}
    res['rows'] = config.data
    # res['columns'] = ['ID', 'StuNum', 'Grade']

    return JsonResponse(res, safe=False)


class DefinedXadminView(View):
    """
        xadmin自定义页面
    """

    def get(self, request):
        return render(request, 'myxadmin.html', {})
