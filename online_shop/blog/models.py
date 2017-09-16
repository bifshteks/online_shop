# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Posts(models.Model):
	title = models.CharField(max_length=255, verbose_name="Название статьи")
	text = models.TextField(verbose_name="Текст")


	class Meta():
		verbose_name = 'Статьи'
		verbose_name_plural = 'Статьи'

	def __str__(self):
		return self.title


