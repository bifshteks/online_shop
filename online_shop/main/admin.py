# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Feedback
# Register your models here.
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from ckeditor.widgets import CKEditorWidget
from django.db import models


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }




admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)
admin.site.register(Feedback)