from rest_framework.response import Response
from rest_framework.decorators import api_view

from register.models import Create
from api.v1.register.serializers import CreateSerializer


@api_view(['GET'])
def register(request):
    instances = Create.objects.filter(is_deleted=False)
    serializer = CreateSerializer(instances, many=True)

    return Response(serializer.data)
