# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


class Posts(models.Model):
	title = models.CharField(max_length=255, verbose_name="Название статьи")
	# text = models.TextField(verbose_name="Текст")
	text = RichTextUploadingField(verbose_name="Текст")
	img = models.FileField(upload_to='', verbose_name="Изображение", null=True, default=None)
	date_pub = models.DateField(auto_now_add=True, verbose_name="Дата публикации", blank=True, null=True)
	tags = TaggableManager(help_text='Введите ключевые слова или словосочетания, разделенные запятой', blank=True, verbose_name="Ключевые слова")


	class Meta():
		verbose_name = 'Статьи'
		verbose_name_plural = 'Статьи'

	def __str__(self):
		return self.title


