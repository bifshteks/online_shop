# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager


class Category(models.Model):
	name = models.CharField(max_length=255, unique=True, verbose_name="Название категории")
	discount = models.IntegerField(verbose_name="Скидка в процентах", blank=True, default=0)

	class Meta():
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name


class Product(models.Model):
	title = models.CharField(max_length=255, verbose_name="Наименование")
	slug = models.CharField(max_length=255, verbose_name="Краткое описание")
	description = models.TextField(verbose_name="Описание")
	price = models.IntegerField(verbose_name="Цена")
	category = models.ForeignKey(Category, verbose_name="Категория", blank=True, null=True, default=None, on_delete=models.SET_NULL)
	img1 = models.FileField(upload_to='', verbose_name="Изображение 1")
	discount = models.IntegerField(verbose_name="Скидка в процентах", blank=True, default=0)
	tags = TaggableManager(help_text='Введите ключевые слова или словосочетания в нижнем регистре, разделенные запятой', blank=True, verbose_name="Ключевые слова")
	# img2 = models.FileField(upload_to='', verbose_name="Изображение 2")
	# img3 = models.FileField(upload_to='', verbose_name="Изображение 3")
	# img4 = models.FileField(upload_to='', verbose_name="Изображение 4")

	class Meta():
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.title

	def get_discount_price(self):
		price_with_self_discount =  int(self.price * (100 - self.discount) / 100)
		price_with_category_discount =  int(self.price * (100 - self.category.discount) / 100)
		return min([price_with_self_discount, price_with_category_discount])


class ItemsInCart(models.Model):
	session_key = models.CharField(max_length=255, verbose_name="Сессия")
	item = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.SET_NULL)
	amount = models.IntegerField()
	price_per_item = models.IntegerField(default=0)
	total_price = models.IntegerField(default=0)
	is_active = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Корзина'
		verbose_name_plural = 'Корзина'

	def __str__(self):
		return self.session_key


	def save(self, *args, **kwargs):
		price_per_item = self.item.get_discount_price()
		self.price_per_item = price_per_item
		self.total_price = int(self.amount) * price_per_item
		print('%%%%%%%%$#$#$#$#$$#$', int(self.amount))
		print(self.total_price)
		return super(ItemsInCart, self).save(*args, **kwargs)
