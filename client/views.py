from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from client.models import Name


class Namee(APIView):
    permission_classes = (
        permissions.AllowAny,
    )

    def post(self, request):
        context = {}
        try:

            salam = request.POST.get('name')
            mmd = Name(name=salam)
            mmd.save()
            context['msg'] = "ذخیره گردید"
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'Not Found'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    def get(self, request):
        context = {}
        try:
            mmd = Name.objects.all()
            context['mmd'] = mmd.name
            context['msg'] = "ذخیره گردید"
            status_code = HTTP_200_OK
        except:
            context['msg'] = 'Not Found'
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)
