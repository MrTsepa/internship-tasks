from django.contrib import admin

from models import *


class RoundAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cup', 'name')}


admin.site.register(Round, RoundAdmin)
admin.site.register(Cup)
