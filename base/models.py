from django.db import models

# Create your models here.


class Topic(models.Model):
    title = models.CharField(max_length=63, null=True, verbose_name='عنوان')
    topic_image = models.ImageField(upload_to='topic_banner/', null=True, verbose_name='بنر')
    topic_icon = models.ImageField(upload_to='topic_icon/', verbose_name='آیکون')


    class Meta:
        verbose_name = "تاپیک"  
        verbose_name_plural = "تاپیک ها"  

    def __str__(self):
        return self.title
    

class Item(models.Model):
    title = models.CharField(max_length=63, null=True, verbose_name='عنوان سفارش')
    description = models.TextField(max_length=511, null=True, verbose_name='توضیحات سفارش')
    item_image = models.ImageField(upload_to='item_images/', null=True, verbose_name='تصویر سفارش')
    price = models.CharField(max_length=63, default='70,000', null=True, verbose_name='قیمت به تومان')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='items', null=True, verbose_name='تاپیک')
    visiable = models.BooleanField(default=True, verbose_name='قابل مشاهده')

    class Meta:
        verbose_name = "آیتم"
        verbose_name_plural = "آیتم ها" 

    def __str__(self):
        return self.title