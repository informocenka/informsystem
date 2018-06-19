from django.contrib import admin
from .models import ObjectFlat, Table
from .resources import TableAdmin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(ObjectFlat)
admin.site.register(Table, TableAdmin)

