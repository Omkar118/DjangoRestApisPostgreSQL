from rest_framework import serializers
from userfiles.models import Userfiles


class UserfilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Userfiles
        fields = ('id',
                  'title',
                  'description',
                  'published')
