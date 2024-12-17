from rest_framework import serializers
from .models import Student, LibraryHistory, FeesHistory, User
from django.contrib.auth.hashers import make_password

class StudentSerializer(serializers.ModelSerializer):
    total_books_borrowed = serializers.SerializerMethodField()

    def get_total_books_borrowed(self, obj):
        return obj.library_records.count()

    def validate_age(self, value):
        if value < 5 or value > 25:
            raise serializers.ValidationError("Age must be between 5 and 25.")
        return value

    class Meta:
        model = Student
        fields = '__all__'


class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = '__all__'


class FeesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesHistory
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
