from django import template
from django.template.defaultfilters import stringfilter
import re

register = template.Library()

@register.filter
@stringfilter
def cut_text(text, num):
	'''Returns cropped text of (num) characters in length without tags and styles'''
	clean_text = re.sub(r'(\<(/?[^>]+)>)', '', text)

	if len(clean_text) < num:
		return clean_text
	else:
		return clean_text[:num] + '...'



