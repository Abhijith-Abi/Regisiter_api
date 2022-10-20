from rest_framework.serializers import ModelSerializer

from register.models import Create


class CreateSerializer(ModelSerializer):
    class Meta:
        model = Create
        fields = ('id', 'first_name', 'last_name', 'image', 'phone',
                  'email', 'address', 'company_name', 'date',)


class DeleteSerializer(ModelSerializer):
    class Meta:
        model = Create
        fields = ('id', 'is_deleted')
