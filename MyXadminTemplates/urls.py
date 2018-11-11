"""MyXadminTemplates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from extra_apps import xadmin
from django.conf.urls import url

from MyXadminPlug.views import IndexView, DefinedXadminView, DefinedPageView, DefinedSearchPageView

urlpatterns = [
    url('^xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name='index'),

    url(r'^xadmin/myxadmin/$', DefinedXadminView.as_view(), name='addxadmin'),  # 后台自定义页面（总）

    url('^definedpage/$', DefinedPageView.as_view(), name='definedpage'),  # 后台数据展示页（表格数据、分页）

    url('^definedsearchpage/$', DefinedSearchPageView.as_view(), name='definedsearchpage'),  # 后台数据搜索页

]
