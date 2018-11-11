from django.shortcuts import render
from django.views import View
from django.db.models import Q

from MyXadminPlug.models import DefinedFund

from .plug import pagination
from . import config


class IndexView(View):
    """
        首页展示
    """

    def get(self, request):
        massages = config.massages
        keys = ['ID', 'StuNum', 'Grade']
        contacts, part_page = pagination(request, massages, keys, 7)
        return render(request, 'index.html', {'contacts': contacts, 'part_page': part_page})


class DefinedXadminView(View):
    """
        xadmin自定义页面
    """

    def get(self, request):
        return render(request, 'myxadmin.html', {})


class DefinedPageView(View):
    """
        首页展示
    """

    def get(self, request):
        DB_Massages = DefinedFund.objects.all().values_list('StuID', 'StuNum', 'Grade')
        massages = []
        for mass in DB_Massages:
            mass_ = []
            for i in mass:
                mass_.append(i)
            massages.append(mass_)

        # massages = config.massages
        keys = ['ID', 'StuNum', 'Grade']
        contacts, part_page = pagination(request, massages, keys, 7)
        return render(request, 'ma_admin_page_one.html', {'contacts': contacts, 'part_page': part_page})


class DefinedSearchPageView(View):
    """
        自定义搜索
    """

    massages, DB_Massages = '', ''

    def get(self, request):

        StuNum = request.GET.get('XadminSearchStuNum')
        Grade = request.GET.get('XadminSearchGrade')

        global DB_Massages, massages

        if StuNum == ' ' and Grade != '':
            DB_Massages = DefinedFund.objects.filter(Grade__contains=Grade)

        elif StuNum != '' and Grade == ' ':
            DB_Massages = DefinedFund.objects.filter(StuNum__contains=Grade)

        elif StuNum != ' ' and Grade != ' ' and StuNum != None and Grade != None:
            DB_Massages = DefinedFund.objects.filter(Q(StuNum__contains=StuNum) & Q(Grade__contains=Grade))

        elif StuNum == ' ' and Grade == ' ':
            DB_Massages = DefinedFund.objects.all()

        else:
            pass

        massages = []
        for mass in DB_Massages:
            mass_ = []
            mass_.append(mass.StuID)
            mass_.append(mass.StuNum)
            mass_.append(mass.Grade)

            massages.append(mass_)

        # massages = config.massages
        keys = ['ID', 'StuNum', 'Grade']
        contacts, part_page = pagination(request, massages, keys, 7)

        return render(request, 'myxadmin.html', {'contacts': contacts, 'part_page': part_page})
