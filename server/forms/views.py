# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Forms
from .serializers import FormsSerializer
from django.shortcuts import render


class FormsList(APIView):

    def get(self, request):
        forms = Forms.objects.all()
        serializer = FormsSerializer(forms, many=True)
        return Response(serializer.data)


