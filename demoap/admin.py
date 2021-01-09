from django.contrib import admin
from demoap.models import DemoDB


class DemoDBAdmin(admin.ModelAdmin):
    list_display = ('username', 'real_name')
    ordering = ("id",)


admin.site.register(DemoDB, DemoDBAdmin)