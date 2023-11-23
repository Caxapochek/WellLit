

menu = [
    {'title':"Главная", 'dropdown':False, 'url_name':'main'},
    {'title':"Услуги", 'dropdown':True, 'dropdown_menu':[
        {'title':"Прайс-лист", 'dropdown':False, 'url_name':'price-list'},
        {'title':"Калькулятор", 'dropdown':False, 'url_name':'calculator'},
        {'title':"Слив воды", 'dropdown':False, 'url_name':'sliv-vodi'},
    ]},
    {'title':"Блог", 'dropdown':True, 'dropdown_menu':[
        {'title':"Процесс монтажа", 'dropdown':False, 'url_name':'installation-procedure'},
        {'title':"Цвета и фактуры", 'dropdown':False, 'url_name':'colors-and-textures'}
    ]},
    {'title':"Наши работы", 'dropdown':False, 'url_name':'portfolio'},
    {'title':"Контакты", 'dropdown':False, 'url_name':'contactus'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
            # на будующие
        context['menu'] = user_menu
        return context