from django.db import models

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def url_field(self, field_name, default=''):
        field = getattr(self, field_name)
        if field and hasattr(field, 'url'):
            return field.url
        return default