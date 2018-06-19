from import_export import resources
from .models import Table
from import_export.admin import ImportExportModelAdmin


class TableResource(resources.ModelResource):

    class Meta:
        model = Table

class TableAdmin(ImportExportModelAdmin):
    resources_class = TableResource




