from rest_framework import serializers
from .models import Forms


class FormsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forms
        fields = "__all__"
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

    def validate_Name(self, value):
        if "^\[a-zA-Z ]\$*" not in value:
            raise serializers.ValidationError("Your name is invalid")
        return value

    def validate_Email(self, value):
        if "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$" not in value:
            raise serializers.ValidationError("Your email is invalid")
        return value

    def validate_Mobile(self, value):
        if "^([9]{1})([234789]{1})([0-9]{8})$" not in value:
            raise serializers.ValidationError("Your mobile number is invalid")
        return value

    def validate_University(self, value):
        if "^\[a-zA-Z ]\$*" not in value:
            raise serializers.ValidationError("Your University name is invalid")
        return value


    def validate_Faculty(self, value):
        if "^\[a-zA-Z ]\$*" not in value:
            raise serializers.ValidationError("Your Minor is invalid")
        return value

    def validate_Major(self, value):
        if "^\[a-zA-Z ]\$*" not in value:
            raise serializers.ValidationError("Your Major is invalid")
        return value

