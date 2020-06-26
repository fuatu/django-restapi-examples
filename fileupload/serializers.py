from rest_framework import serializers
from fileupload.models import File
from django.contrib.auth.models import Group


class FileSerializer(serializers.ModelSerializer):
    # SlugRelatedField can be used to add the groups from their names
    groups = serializers.SlugRelatedField(
        many=True,
        queryset=Group.objects.all(),
        slug_field='name',
        read_only=False
    )
    class Meta:
        model = File
        fields = "__all__"
