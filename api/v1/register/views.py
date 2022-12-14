from functools import partial

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.v1.register.serializers import CreateSerializer, DeleteSerializer
from register.models import Create


@api_view(['GET'])
def register(request):
    instances = Create.objects.filter(is_deleted=False)
    serializer = CreateSerializer(instances, many=True)
    response_data = {
        "status_code": 6000,
        "data": serializer.data
    }

    return Response(response_data)


@api_view(['GET'])
def register_list(request, pk):
    if Create.objects.filter(pk=pk).exists():
        instance = Create.objects.get(pk=pk)

        context = {
            "request": request,
        }

        serializer = CreateSerializer(instance, context=context)
        response_data = {
            "status_code": 6000,
            "data": serializer.data
        }
        return Response(response_data)

    else:
        response_data = {
            'status_code': 6001,
            'messages': 'Not Found',
        }
        return Response(response_data)


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

        serializer = CreateSerializer(
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
