import django_tables2 as tables 
from django_tables2 import  TemplateColumn
from .models import Table, Field

class FieldsTable(tables.Table):
    buttons = TemplateColumn(template_name='prototype/edit_field.html', 
        orderable=False, verbose_name='', 
        attrs={
            "td": {"align": "right"}
        })

    class Meta:
        model = Field
        template_name = "django_tables2/bootstrap5.html"

        row_attrs = {
            "data-id": lambda record: record.name
        }

        # fields = ("name", "type", "subtype", "distribution", "example", "description", "constraints.min_length", "buttons")
        fields = ("name", "subtype", "distribution", "example", "description", "buttons")


class TablesTable(tables.Table):

    # create a column that will hold the buttons used to modify tables.
    # these are defined externally in a template file.
    buttons = TemplateColumn(template_name='prototype/edit_table.html', 
        orderable=False, verbose_name='', 
        attrs={
            "td": {"align": "right"}
        })
    
    class Meta:
        model = Table
        template_name = "django_tables2/bootstrap5.html"

        # assign these attributes to each row.  
        row_attrs = {
            "data-id": lambda record: record.name
        }

        fields = ("name", "description", "buttons" )


