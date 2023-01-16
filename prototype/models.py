from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from guardian.models import GroupObjectPermissionBase, UserObjectPermissionBase

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
    slug = models.SlugField(max_length=30, null=True)
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
    code = models.TextField(null=True, blank=True)
    expression = models.TextField(null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        default=0,
    )

    def __str__(self):
        return "{} - {}".format(self.name, self.type)

    def _generate_unique_slug(self):
        unique_slug = slugify(self.name)
        num = 1
        while FieldConstraint.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug    
        
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = self._generate_unique_slug(self.name)
        return super().save(*args, **kwargs)

class TableConstraint(models.Model):
    CONSTRAINT_TYPES = (
        ('Expression', 'expression'),
        ('Any', 'any'),
    )
    name = models.CharField(max_length=30, null=True)
    slug = models.SlugField(max_length=30, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=20, choices=CONSTRAINT_TYPES, null=True, blank=True)
    expression = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        default=0,
    )

    def __str__(self):
        return "{} - {}".format(self.name, self.type)
        
    def _generate_unique_slug(self):
        unique_slug = slugify(self.name)
        num = 1
        while TableConstraint.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug    
        
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = self._generate_unique_slug(self.name)
        return super().save(*args, **kwargs)

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
    slug = models.SlugField(max_length=30, null=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    distribution = models.CharField(max_length=20, choices=DISTRIBUTION_TYPES, null=True)
    type = models.CharField(max_length=20, choices=FIELD_TYPES, null=True)
    subtype = models.CharField(max_length=50, choices=FIELD_SUBTYPES, null=True)
    format = models.CharField(max_length=100, null=True, blank=True)
    example = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    expression = models.CharField(max_length=500, null=True, blank=True)
    constraints = models.ForeignKey(FieldConstraint, on_delete=models.CASCADE, null=True, blank=True)    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        default=0,
    )

    def __str__(self):
        return "{} - {} - {} - {}".format(self.name, self.type, self.subtype, self.distribution)
        
    def _generate_unique_slug(self):
        unique_slug = slugify(self.name)
        num = 1
        while Field.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug    
        
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = self._generate_unique_slug(self.name)
        return super().save(*args, **kwargs)

class Key(models.Model):
    KEY_TYPES = (
        ('Primary', 'primary'),
        ('Foreign', 'foreign'),
        ('Group', 'group'),
    )
    name = models.CharField(max_length=30, null=True)
    slug = models.SlugField(max_length=30, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=20, choices=KEY_TYPES, null=True)
    fields = models.ManyToManyField(Field, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        default=0,
    )

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.type, self.fields)
        
    def _generate_unique_slug(self):
        unique_slug = slugify(self.name)
        num = 1
        while Key.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug    
        
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = self._generate_unique_slug(self.name)
        return super().save(*args, **kwargs)

# see https://specs.frictionlessdata.io/table-schema/#descriptor for more details.
class Table(models.Model):
    name = models.CharField(max_length=30, null=True)
    slug = models.SlugField(max_length=30, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    keys = models.ManyToManyField(Key, blank=True)
    fields = models.ManyToManyField(Field, blank=True)
    constraints = models.ManyToManyField(TableConstraint, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        default=0,
    )

    class Meta:
        default_permissions = ('add', 'change', 'delete')
        permissions = (
            ('view_table', 'Can view table'),
        )

    def __str__(self):
        return self.name

    # TODO: Set a path so that we can have tables and fields accessed by author and slug
    # See https://wellfire.co/learn/fast-and-beautiful-urls-with-django/
    def get_absolute_url(self):
        return reverse('table-slug', kwargs={'author': self.author, 'slug': self.slug})
        
    def _generate_unique_slug(self):
        unique_slug = slugify(self.name)
        num = 1
        while Table.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(unique_slug, num)
            num += 1
        return unique_slug    
        
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = self._generate_unique_slug()
        return super().save(*args, **kwargs)
