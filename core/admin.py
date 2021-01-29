from django.contrib import admin
from .models import News, Services, Category, Reviews, Driver, Сustomers, Transportation, AvtoPark, AvtoExample

admin.site.register(Driver)
admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(Services)
admin.site.register(Сustomers)
admin.site.register(Transportation)
admin.site.register(AvtoPark)
admin.site.register(AvtoExample)
admin.site.register(News)