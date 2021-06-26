from django.contrib import admin

import navapp.models as models

# Register your models here.

admin.site.register(models.NavTemplate)
admin.site.register(models.NavItem)