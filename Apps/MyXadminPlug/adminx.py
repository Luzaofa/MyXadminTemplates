__author__ = 'Luzaofa'
__date__ = '2018/11/9 20:45'

import xadmin

from .models import UserMessage, DefinedFund

from xadmin import views


class BaseSetting(object):
    """
    配置主题
    """
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    """
    配置抬头和尾部，以及列表显示
    """
    site_title = '股民之家后台管理系统'
    site_footer = '股民之家版权所有'
    menu_style = 'accordion'

    # 自定义菜单
    def get_site_menu(self):
        return [
            {
                'title': '自定义菜单',
                'icon': 'fa fa-bar-chart-o',
                'menus': (
                    {
                        'title': '自定义菜单1',
                        'icon': 'fa fa-smile-o',
                        'url': '/xadmin/myxadmin/'
                    },
                )
            }
        ]

class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class DefinedFundAdmin(object):
    list_display = ['StuID', 'StuNum', 'Grade']
    search_fields = ['StuID', 'StuNum', 'Grade']
    list_filter = ['StuID', 'StuNum', 'Grade']


xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(DefinedFund, DefinedFundAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

