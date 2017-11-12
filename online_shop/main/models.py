# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Feedback(models.Model):
	name = models.CharField(max_length=255, verbose_name='Имя')
	email = models.CharField(max_length=255, verbose_name='E-mail')
	message = models.TextField(verbose_name='Сообщение')

	class Meta:
		verbose_name = 'Заказ обратной связи'
		verbose_name_plural = 'Заказы обратной связи'

	def __str__(self):
		return 'Заказ №' + str(self.id)