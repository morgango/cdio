from django.contrib import admin
from .models import Field, FieldConstraint, Key, Table, TableConstraint
from guardian.admin import GuardedModelAdmin

class TableAdmin(GuardedModelAdmin):
    search_fields=('name', 'slug')

# Register your models here.
admin.site.register(Field)
admin.site.register(FieldConstraint)
admin.site.register(Key)
admin.site.register(Table, TableAdmin)
admin.site.register(TableConstraint)