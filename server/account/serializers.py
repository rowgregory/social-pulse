from rest_framework import serializers
# serializers are used to convert complex data types, such as Django models, into Python data types that can be easily rendered into JSON

from .models import User, FriendshipRequest


class UserSerializer(serializers.ModelSerializer):
  # allows you to define certain properties about how the serialization process should be handled
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'friends_count',)


class FriendshipRequestSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = FriendshipRequest
        fields = ('id', 'created_by',)
