from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Forms
from .serializers import FormsSerializer


# any view concerning general or all data
class FormsList(APIView):
    def get(self, request):
        forms = Forms.objects.all()
        serializer = FormsSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request):
        formEntry = FormsSerializer(data=request.data)
        if formEntry.is_valid():
            formEntry.save()
            return Response(formEntry.data, status=status.HTTP_201_CREATED)
        return Response(formEntry.errors, status=status.HTTP_400_BAD_REQUEST)


# any view concerning details
class FormsDetail(APIView):
    def getObject(self, id):
        try:
            return Forms.objects.filter(id=id)
        except Forms.DoesNotExist:
            raise Http404("Not Found")

    def get(self, request, id):
        forms = self.getObject(id=id)
        serializer = FormsSerializer(forms, many=True)
        return Response(serializer.data)

    def put(self, request, id):
        curr_form = self.getObject(id=id)
        form_entry = FormsSerializer(curr_form, data=request.data)
        if form_entry.is_valid():
            form_entry.save()
            return Response(form_entry.data, status=status.HTTP_201_CREATED)
        return Response(form_entry.errors, status=status.HTTP_400_BAD_REQUEST)
