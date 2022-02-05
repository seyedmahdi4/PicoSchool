# Generated by Django 3.2 on 2022-02-05 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20220204_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.CharField(default='1400-11-16', max_length=120, verbose_name='تاریخ کلاس'),
        ),
        migrations.AlterField(
            model_name='classes',
            name='books',
            field=models.ManyToManyField(related_name='books_class', to='manager.Books', verbose_name='کتاب های کلاس'),
        ),
    ]
