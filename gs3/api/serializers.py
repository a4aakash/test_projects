from rest_framework import fields, serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError("Name must start with R")
    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name','roll','city']

    # Field Label Validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() =='kumar' and ct.lower() !='rajgir':
            raise serializers.ValidationError('City must Rajgir')
        return data