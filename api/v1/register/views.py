from functools import partial
from rest_framework.response import Response
from rest_framework.decorators import api_view

from register.models import Create
from api.v1.register.serializers import CreateSerializer, DeleteSerializer


@api_view(['GET'])
def register(request):
    instances = Create.objects.filter(is_deleted=False)
    serializer = CreateSerializer(instances, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def create_data(request):
    serializer = CreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        response_data = {
            'status_code': 6000,
            'messages': 'success',
        }

        return Response(response_data)

    else:
        response_data = {
            'status_code': 6001,
            'messages': 'register failed',
            'data': serializer.errors
        }

        return Response(response_data)


@api_view(['POST'])
def update_data(request, pk):
    if Create.objects.filter(pk=pk).exists():
        register = Create.objects.get(pk=pk)

        serializer = CreateSerializer(
            instance=register, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            response_data = {
                'status_code': 6000,
                'messages': 'success',
            }
            return Response(response_data)

        else:
            response_data = {
                'status_code': 6001,
                'messages': 'register failed',
                'data': serializer.errors
            }
            return Response(response_data)

    else:
        response_data = {
            'status_code': 6001,
            'messages': 'Not Found',
        }
        return Response(response_data)


@api_view(['POST'])
def delete_data(request, pk):
    if Create.objects.filter(pk=pk).exists():
        register = Create.objects.get(pk=pk)

        serializer = DeleteSerializer(
            instance=register, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            response_data = {
                'status_code': 6000,
                'messages': 'Successfully deleted',
            }
            return Response(response_data)

        else:
            response_data = {
                'status_code': 6001,
                'messages': 'Delete failed',
                'data': serializer.errors
            }
            return Response(response_data)

    else:
        response_data = {
            'status_code': 6001,
            'messages': 'Not Found',
        }
        return Response(response_data)
