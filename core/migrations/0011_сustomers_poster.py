# Generated by Django 3.1.4 on 2021-01-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210112_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='сustomers',
            name='poster',
            field=models.ImageField(default='sdas', upload_to='customer/', verbose_name='Картинка'),
            preserve_default=False,
        ),
    ]
