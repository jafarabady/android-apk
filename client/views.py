from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from client.models import Name
from client.serializers import NameSerializer


class Namee(APIView):
    permission_classes = (
        permissions.AllowAny,
    )

    def post(self, request):
        context = {}
        name = request.POST.get('name')
        family = request.POST.get('family')
        print(1)
        print(request.data)
        print(8245)
        mmd = Name(name=name)
        mmd.save()
        print(51554)
        context['msg'] = "ذخیره گردید"
        status_code = HTTP_200_OK

        # context['msg'] = 'فیلدنام  نمی‌تواند خالی باشد'
        # status_code = HTTP_400_BAD_REQUEST
        # context['msg'] = 'ذخیره نشد'
        # status_code = HTTP_404_NOT_FOUND

        return Response(context, status=status_code)


def get(self, request):
    context = {}
    try:
        mmd = Name.objects.get(id=1)
        context['name'] = NameSerializer(mmd, many=False).data
        context['msg'] = "ذخیره گردید"
        status_code = HTTP_200_OK
    except:
        context['msg'] = 'چیزی برای نمایش نیست'
        status_code = HTTP_404_NOT_FOUND
    return Response(context, status=status_code)
