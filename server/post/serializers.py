from rest_framework import serializers
# serializers are used to convert complex data types, such as Django models, into Python data types that can be easily rendered into JSON
from account.serializers import UserSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    # allows you to define certain properties about how the serialization process should be handled

    class Meta:
        model = Post
        fields = ('id', 'body', 'created_by', 'created_at_formatted',)
