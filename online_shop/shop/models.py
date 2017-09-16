# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
	title = models.CharField(max_length=255, verbose_name="Наименование")
	slug = models.CharField(max_length=255, verbose_name="Краткое описание")
	description = models.TextField(verbose_name="Описание")
	price = models.IntegerField(verbose_name="Цена")
	img1 = models.FileField(upload_to='', verbose_name="Изображение 1")
	img2 = models.FileField(upload_to='', verbose_name="Изображение 2")
	img3 = models.FileField(upload_to='', verbose_name="Изображение 3")
	img4 = models.FileField(upload_to='', verbose_name="Изображение 4")

	class Meta():
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

	def __str__(self):
		return self.title


