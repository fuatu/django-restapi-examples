from django.contrib.auth.models import Group
from django.db import models


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=20, blank=True)
    file = models.FileField(blank=False, null=False, validators=[validate_file_extension])
    groups = models.ManyToManyField(Group)
    def __str__(self):
        return self.file.name
