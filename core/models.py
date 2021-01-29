from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    pub_date = models.DateTimeField('date published')
    image = models.ImageField("Првеью новости", upload_to="News/")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class AvtoPark(models.Model):
    """Сервис"""
    title = models.CharField("Название", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse("auto_park", kwargs={"slug": self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "АвтоПарк"
        verbose_name_plural = "Авто Праки"


class AvtoExample(models.Model):
    """Подкласс авто парк"""
    title = models.CharField("Название автобуса/трам...", max_length=100)
    disc = models.CharField("Имя автобаса", max_length=100)
    disc1 = models.CharField("Багажное отделение", max_length=100)
    disc2 = models.CharField("Кондиционер", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="Avto/")
    avto = models.ForeignKey(AvtoPark, verbose_name="Авто парк", on_delete=models.CASCADE)
    price = models.PositiveIntegerField('Цена', default=0, help_text='Указываем сумму!*ПУК*')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Авто-парк экземляр"
        verbose_name_plural = "Авто-парк экземпляры"


class Transportation(models.Model):
    """Сервис"""
    title = models.CharField("Название", max_length=100)
    descriptions = models.TextField("Описание")
    poster = models.ImageField("Картинка", upload_to="transports/")
    prelog = models.TextField("Описание c многоточием в оглавлении")
    url = models.SlugField(max_length=160, unique=True)
    price = models.PositiveIntegerField('Цена', default=0, help_text='Указываем сумму.')

    def get_absolute_url(self):
        return reverse("transport_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Перевозка"
        verbose_name_plural = "Перевозки"


class Services(models.Model):
    """Сервис"""
    title = models.CharField("Название", max_length=100)
    descriptions = models.TextField("Описание")
    poster = models.ImageField("Картинка", upload_to="service/")
    prelog = models.TextField("Описание c многоточием в оглавлении")
    url = models.SlugField(max_length=160, unique=True)
    price = models.PositiveIntegerField('Цена', default=0, help_text='Указываем сумму.')

    def get_absolute_url(self):
        return reverse("services_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"


class Reprand(models.Model):
    """Категории"""
    name = models.CharField("Ремонт и обслуживание", max_length=100)
    descriptions = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    tcategory = models.ForeignKey(
        Services, verbose_name='обьекты', on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ремонт и обслуживание"
        verbose_name_plural = "Ремонт и обслуживание"


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=100)
    descriptions = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категоия"
        verbose_name_plural = "Категоии"


class Сustomers(models.Model):
    name = models.CharField("Назвапние компании", max_length=20)
    poster = models.ImageField("Картинка", upload_to="customer/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Driver(models.Model):
    """"Водители"""
    name = models.CharField("Имя", max_length=100)
    image = models.ImageField("Изображение", upload_to='driver/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Водитель"
        verbose_name_plural = "Водители"


class Reviews(models.Model):
    """"Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщения", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.CASCADE
    )
    service = models.ForeignKey(Services, verbose_name='Сервисы', on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.name} - {self.service}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class About(models.Model):
    """Сервис"""
    title = models.CharField("Название", max_length=100)
    descriptions = models.TextField("Описание")
    poster = models.ImageField("Картинка", upload_to="transports/")
    prelog = models.TextField("Описание c многоточием в оглавлении")
    url = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse("transport_detail", kwargs={"slug": self.url})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Перевозка"
        verbose_name_plural = "Перевозки"
