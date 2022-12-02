from django.db import models

# # see https://specs.frictionlessdata.io/table-schema/#constraints for more info
class FieldConstraint(models.Model):
    CONSTRAINT_TYPES = (
        ('String', 'string'),
        ('Numeric', 'numeric'),
        ('Collection', 'collection'),
        ('Temporal', 'temporal'),
        ('Expression', 'expression'),
        ('Any', 'any')
    )
    name = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=20, choices=CONSTRAINT_TYPES)
    required = models.BooleanField(blank=True)
    unique = models.BooleanField(blank=True)
    min_length = models.BigIntegerField(blank=True)
    max_length = models.BigIntegerField(blank=True)
    minimum = models.BigIntegerField(blank=True)
    maximum = models.BigIntegerField(blank=True)
    pattern = models.CharField(max_length=100, null=True, blank=True)
    enum = models.CharField(max_length=500, null=True, blank=True)
    expression = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.type)

class TableConstraint(models.Model):
    CONSTRAINT_TYPES = (
        ('Expression', 'expression'),
        ('Any', 'any'),
    )
    name = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=20, choices=CONSTRAINT_TYPES, null=True, blank=True)
    expression = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.type)

# see  https://specs.frictionlessdata.io/table-schema/#field-descriptors for more info
class Field(models.Model):
    FIELD_TYPES = (
        ('String', 'string'),
        ('Number', 'number'),
        ('Integer', 'integer'),
        ('Boolean', 'boolean'),
        ('Object', 'object'),
        ('Array', 'array'),
        ('Date', 'date'),
        ('Time', 'time'),
        ('Datetime', 'datetime'),
        ('Year', 'year'),
        ('Duration', 'duration'),
        ('Geopoint', 'geopoint'),
        ('Expression', 'expression'),
        ('Any', 'any'),
    )
    FIELD_SUBTYPES = (
        ('Email', 'email'),
        ('First Name', 'first name'),
        ('Last Name', 'last name'),
        ('Full Name', 'full name'),
        ('Postal Code', 'postal code'),
        ('Positive Integer', 'positive integer'),
        ('Negative Integer', 'negative integer'),
        ('None', 'none'),
    )
    DISTRIBUTION_TYPES = (
        ('Normal', 'normal'),
        ('Uniform', 'uniform'),
        ('Exponential', 'exponential'),
        ('Binomial', 'binomial'),
        ('Bernoulli', 'bernoulli'),
        ('Poisson', 'poisson'),
        ('Custom', 'custom'),
        ('None', 'none'),
    )
    name = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    distribution = models.CharField(max_length=20, choices=DISTRIBUTION_TYPES, null=True)
    type = models.CharField(max_length=20, choices=FIELD_TYPES, null=True)
    subtype = models.CharField(max_length=50, choices=FIELD_SUBTYPES, null=True)
    format = models.CharField(max_length=100, null=True, blank=True)
    example = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    expression = models.CharField(max_length=500, null=True, blank=True)
    constraints = models.ForeignKey(FieldConstraint, on_delete=models.CASCADE, null=True, blank=True)    

    def __str__(self):
        return "{} - {} - {} - {}".format(self.name, self.type, self.subtype, self.distribution)

class Key(models.Model):
    KEY_TYPES = (
        ('Primary', 'primary'),
        ('Foreign', 'foreign'),
        ('Set', 'set'),
    )
    name = models.CharField(max_length=30, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=20, choices=KEY_TYPES, null=True)
    #fields = models.ForeignKey(Field, on_delete=models.CASCADE, blank=True)    
    fields = models.ManyToManyField(Field, blank=True)
    # TODO: figure out how to implement a link to a foreign table
    # foreign_table = models.OneToOneField(
    #     'prototype.Table',
    #     on_delete=models.CASCADE,
    #     primary_key=False,
    #     blank=True) 

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.type, self.fields)

# see https://specs.frictionlessdata.io/table-schema/#descriptor for more details.
class Table(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    #keys = models.ForeignKey(Key, on_delete=models.CASCADE, null=True, blank=True)
    #fields = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, blank=True)
    #constraints = models.ForeignKey(TableConstraint, on_delete=models.CASCADE, null=True, blank=True)
    keys = models.ManyToManyField(Key, blank=True)
    fields = models.ManyToManyField(Field, blank=True)
    constraints = models.ManyToManyField(TableConstraint, blank=True)

    def __str__(self):
        return self.name
