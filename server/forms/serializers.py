from rest_framework import serializers
from .models import Forms


class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forms
        ProfilePicture = serializers.CharField(max_length=1000)
        Name = serializers.CharField(max_length=100)
        Email = serializers.EmailField(max_length=500)
        Mobile = serializers.CharField(max_length=12)
        National_ID = serializers.CharField(max_length=40)
        University = serializers.CharField(max_length=100)
        Faculty = serializers.CharField(max_length=100)
        Major = serializers.CharField(max_length=100)
        Minor = serializers.CharField(max_length=100)
        Expected_GraduationYear = serializers.CharField(max_length=4)

        def validate_email(self, value):

            if '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$' not in value:
                raise serializers.ValidationError("Your Email is invalid")
            return value


        def validate_mobile(self, value):

            if '^(\+\d{1,2}\s)?\(?\d{4}\)?[\s.-]\d{4}[\s.-]\d{4}$' not in value:
                raise serializers.ValidationError("Please Enter 12 digits")
            return value