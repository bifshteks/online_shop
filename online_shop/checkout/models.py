from django.db import models
from shop.models import ItemsInCart

class Order(models.Model):

	OPEN = 'Открыт'
    PROCESS = 'В процессе'
    PAID = 'Оплачен'
    DELIVERIED = 'Доставлен'
    CLOSED = 'Закрыт'
    CHOICES = (
        (OPEN, 'Открыт'),
	    (PROCESS, 'В процессе'),
	    (PAID, 'Оплачен'),
	    (DELIVERIED, 'Доставлен'),
	    (CLOSED, 'Закрыт'),
    )


	session_key =  models.CharField(max_length=255, verbose_name="Сессия")
	name = models.CharField(verbose_name="Имя", max_length=255, blank=True, null=True, default=None)
	email = models.CharField(verbose_name="E-mail", max_length=255, blank=True, null=True, default=None)
	phone = models.CharField(verbose_name="Телефон", max_length=20, blank=True, null=True, default=None)
	ordered_items = models.ForeignKey(ItemsInCart, blank=True, null=True, default=None, on_delete=models.SET_NULL)
	delivery_address = models.TextField(verbose_name="Адрес доставки", blank=True, null=True, default=None)
	details = models.TextField(verbose_name="Детали к заказу", blank=True, null=True, default=None)
	cost = models.IntegerField(verbose_name="Полная стоимость заказа", blank=True, null=True, default=None)
	status = models.CharField(verbose_name="Статус", max_length=2, choices=CHOICES, default=OPEN)


