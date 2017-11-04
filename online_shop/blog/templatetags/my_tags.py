from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter
@stringfilter
def cut_text(text, num):
	'''Returns cropped text of (num) characters in length'''
	if len(text) < num:
		return text
	else:
		return text[:num] + '...'



