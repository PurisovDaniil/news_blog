from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.translation import LANGUAGE_SESSION_KEY



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    background = models.ImageField('Фон профиля', blank=True, null=True, upload_to='users/bg')
    avatar = models.ImageField('Аватар', blank=True, null=True, upload_to='users/avatars')
    phone = models.CharField('Номер пользователя', max_length=13)
    birth_date = models.DateField('Дата рождения', null=True)

    class Meta:
        verbose_name = 'Дополнительное поле пользователя'
        verbose_name_plural = 'Дополнительные поля пользователя'

    def __str__(self):
        return self.user.username

class Image(models.Model):
    image = models.ImageField('Картинка', upload_to = 'image/')
    title = models.CharField('Заголовок', max_length = 100)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField('Заголовок', max_length = 255)
    slug = models.SlugField('Ссылка', unique = True) 
    image = models.ImageField('Картинка', blank = True, null = True)
    
    class Meta():
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def get_link(self):
        return reverse('category_detail_url', kwargs = {'slug': self.slug})
    
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField('Заголовок',max_length=150)
    slug = models.SlugField('Ссылка' ,max_length=150, unique=True)
    text = models.TextField('Текст' ,blank=True, null=True)
    preview = models.ForeignKey(Image, on_delete = models.SET_NULL, null=True, blank=True, verbose_name = 'Обложка')
    gallery = models.ManyToManyField(Image, verbose_name = 'Галарея', related_name = 'posts')
    category = models.ManyToManyField(Category, verbose_name = 'Категории', related_name = 'posts')
    date = models.DateTimeField('Дата' ,default = timezone.now)
    views = models.IntegerField('Просмотры', default = 0)
    publish = models.BooleanField('Опубликовано', default = False)


    def get_link(self):
        return reverse('post_detail_url', kwargs={'slug':self.slug})

    class Meta():
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'Автор')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, verbose_name = 'Новость')
    text = models.TextField('Текст комментария')
    date = models.DateTimeField('Дата', default = timezone.now)

    class Meta():
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.user.username