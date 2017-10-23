# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=255, unique=True, verbose_name="Название категории")

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
	category = models.ForeignKey(Category, verbose_name="Категория")
	img1 = models.FileField(upload_to='', verbose_name="Изображение 1")
	img2 = models.FileField(upload_to='', verbose_name="Изображение 2")
	img3 = models.FileField(upload_to='', verbose_name="Изображение 3")
	img4 = models.FileField(upload_to='', verbose_name="Изображение 4")

	class Meta():
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.title


class ItemsInCart(models.Model):
	session_key = models.CharField(max_length=255, verbose_name="Сессия")
	item = models.ForeignKey(Product, blank=True, null=True, default=None)
	amount = models.IntegerField()
	price_per_item = models.DecimalField(max_digits=20, decimal_places=2, default=0)
	total_price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
	is_active = models.BooleanField(default=True)

	class Meta():
		verbose_name = 'Корзина'
		verbose_name_plural = 'Корзина'

	def __str__(self):
		return self.session_key


	def save(self, *args, **kwargs):
		price_per_item = self.item.price
		self.price_per_item = price_per_item
		self.total_price = int(self.amount) * price_per_item
		print(self.total_price)
		return super(ItemsInCart, self).save(*args, **kwargs)







class Order(models.Model):
	name = ''
	phone = ''
	email = ''



