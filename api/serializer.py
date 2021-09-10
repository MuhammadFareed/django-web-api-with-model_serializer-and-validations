from django.db.models import fields
from api.models import Student
from rest_framework import serializers



# Validaion by validators (This def remains outside the serializer class)
def is_name_starts_with_s(value):
    if value[0].lower() != 's':
            raise serializers.ValidationError('Name should start with the letter S')


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=50, validators=[is_name_starts_with_s])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name']
        # extra_kwargs = {'name': {'read_only': True}}

    
    #########################################
    #                                       #
    #               Validations             #
    #                                       #
    #########################################



    # Field level validaion
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Roll number must be less than 200')
        return value

    # Object level validaion
    def validate(self, data):
        name = data.get('name')
        roll = data.get('roll')
        city = data.get('city')
        if name.lower() == 'fareed':
            raise serializers.ValidationError('User with this name already exist')
        if roll >= 200:
            raise serializers.ValidationError('Roll number must be less than 200')
        return data