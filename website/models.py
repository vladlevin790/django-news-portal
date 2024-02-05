from django.db import models
from datetime import datetime as dt
from django.conf import settings


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
class Categories(models.Model):
    name = models.CharField(verbose_name="Название",
                            max_length=30,
                            blank=False)
    discription = models.TextField(verbose_name="Описание")
    
    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
    
    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(verbose_name="Заголовок",
                             max_length=30,
                             blank=False)
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateTimeField(verbose_name="Создано в",
                                      auto_now_add=True)
    published_at = models.DateTimeField(verbose_name="Опубликовать в", 
                                        default=dt.now())
    photo = models.ImageField(verbose_name="Путь к фото",
                              upload_to="photo_for_news/",
                              blank=True)
    is_published = models.BooleanField(verbose_name="Статус публикации", 
                                       default=True)
    category = models.ForeignKey(verbose_name="Категория",
                                 to=Categories, 
                                 on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    
    def __str__(self):
        return self.title

    
    