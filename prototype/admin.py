from django.contrib import admin
from .models import Field, FieldConstraint, Key, Table, TableConstraint

# Register your models here.
admin.site.register(Field)
admin.site.register(FieldConstraint)
admin.site.register(Key)
admin.site.register(Table)
admin.site.register(TableConstraint)