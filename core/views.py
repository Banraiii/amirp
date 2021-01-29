from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import News, Services, Reviews, Category, Transportation, Reprand, AvtoPark, AvtoExample, Сustomers
from django.contrib import messages
from .forms import ContactForm

from django.contrib.flatpages.models import FlatPage


class ServiceCategory:
    """Категории и сервисы"""

    def get_last_news(self):
        """Вывод 5 последних новостей"""
        return News.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]

    def get_customer(self):
        return Сustomers.objects.all()

    def get_category(self):
        return Category.objects.all()

    def get_transPut(self):
        return Transportation.objects.all()

    def get_servic(self):
        return Services.objects.all()

    def get_reprand(self):
        return Reprand.objects.all()

    def get_avto(self):
        return AvtoPark.objects.all()

    def get_avtoEX(self):
        return AvtoExample.objects.all()


def servicesendmail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],
                             'prima_sendmail@mail.ru', ['sleperstime@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Писмо отправленно')
                return render(request, 'sendmail/form_service.html', {"form": form})
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = ContactForm()
    return render(request, 'sendmail/form_service.html', {"form": form})

def serviceSendmailtwo(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],
                             'prima_sendmail@mail.ru', ['sleperstime@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Писмо отправленно')
                return render(request, 'sendmail/form_service.html', {"form": form})
            else:
                messages.error(request, 'Ошибка отправки')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = ContactForm()
    return render(request, 'sendmail/form_service_vlas.html', {"form": form})


class FlatPage1(ServiceCategory, ListView):
    model = FlatPage
    template_name = "pages/about.html"


class FlatPage2(ServiceCategory, ListView):
    model = FlatPage
    template_name = "pages/landing_page.html"


class FlatPage3(ServiceCategory, ListView):
    model = FlatPage
    template_name = "pages/broner.html"


class ServiceView(ServiceCategory, ListView):
    """Сервисы"""
    model = Services
    queryset = Services.objects.all()
    template_name = "pages/home.html"


class ServiceViewNum2(ServiceCategory, ListView):
    """Сервисы"""
    model = Services
    queryset = Services.objects.all()
    template_name = "pages/service_list.html"


class TransportationListView(ServiceCategory, ListView):
    """Сервисы"""
    model = Transportation
    queryset = Services.objects.all()
    template_name = "pages/transport_list.html"


class ServiceDetailView(ServiceCategory, DetailView):
    """Полное описание фильма"""
    model = Services

    slug_field = "url"
    template_name = "pages/service_detail.html"


class TransportationDetailView(ServiceCategory, DetailView):
    """Полное описание фильма"""
    model = Transportation

    slug_field = "url"
    template_name = "pages/transport_detail.html"


class Search(ServiceCategory, ListView):
    """Поиск по сату"""
    template_name = "pages/service_list.html"

    def get_queryset(self):
        print(self.request.GET.get("q"))
        return Services.objects.filter(title__icontains=self.request.GET.get("q"))


class AvtoParkDitail(ServiceCategory, DetailView):
    """Авто парк"""
    model = AvtoPark

    slug_field = "url"
    template_name = "pages/avtopa_detail.html"


class AboutView(View):
    template_name = "pages/about.html"
