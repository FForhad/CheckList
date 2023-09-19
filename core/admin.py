from django.contrib import admin
from core.models import Checklist,CheckListItem
# Register your models here.

admin.site.register(Checklist)
admin.site.register(CheckListItem)