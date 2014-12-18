from builtins import object
from rest_framework import serializers
from .models import Group, Permission, User


class PermissionSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Permission


class GroupSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Group


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
