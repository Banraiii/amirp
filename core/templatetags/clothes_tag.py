from django import template
from core.models import Services, Reviews, Category, Transportation, Reprand, AvtoPark


register = template.Library()


@register.simple_tag()
def get_category(self):
    return Category.objects.all()


@register.simple_tag()
def get_transPut(self):
    return Transportation.objects.all()


@register.simple_tag()
def get_servic(self):
    return Services.objects.all()


@register.simple_tag()
def get_reprand(self):
    return Reprand.objects.all()


@register.simple_tag()
def get_avtostop(self):
    """"Авто спот"""
    return AvtoPark.objects.all()
