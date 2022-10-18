from rest_framework.serializers import ModelSerializer
from register.models import Create


class CreateSerializer(ModelSerializer):
    class Meta:
        model = Create
        fields = ('id', 'first_name', 'last_name',
                  'email', 'password', 'phone', 'company_name', 'date', 'education')
