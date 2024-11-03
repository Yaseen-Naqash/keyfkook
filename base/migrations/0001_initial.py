# Generated by Django 5.1.2 on 2024-11-03 00:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63, null=True, verbose_name='عنوان')),
                ('topic_image', models.ImageField(null=True, upload_to='topic_banner/', verbose_name='بنر')),
                ('topic_icon', models.ImageField(upload_to='topic_icon/', verbose_name='آیکون')),
            ],
            options={
                'verbose_name': 'تاپیک',
                'verbose_name_plural': 'تاپیک ها',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63, null=True, verbose_name='عنوان سفارش')),
                ('description', models.TextField(max_length=511, null=True, verbose_name='توضیحات سفارش')),
                ('item_image', models.ImageField(null=True, upload_to='item_images/', verbose_name='تصویر سفارش')),
                ('price', models.CharField(default='70,000', max_length=63, null=True, verbose_name='قیمت به تومان')),
                ('visiable', models.BooleanField(default=True, verbose_name='قابل مشاهده')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='base.topic', verbose_name='تاپیک')),
            ],
            options={
                'verbose_name': 'آیتم',
                'verbose_name_plural': 'آیتم ها',
            },
        ),
    ]
