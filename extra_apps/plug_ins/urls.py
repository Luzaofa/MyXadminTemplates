from django.conf.urls import url

from .views import getJson, MenuOneXadminView, MenuTwoXadminView, MenuTheXadminView

urlpatterns = [
    url(r'^getJson/', getJson, name='getJson'),  # 获取数据

    url(r'^menu1/$', MenuOneXadminView.as_view(), name='menu1'),
    url(r'^menu2/$', MenuTwoXadminView.as_view(), name='menu2'),
    url(r'^menu3/$', MenuTheXadminView.as_view(), name='menu3'),
]
