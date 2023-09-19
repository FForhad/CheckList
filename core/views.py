from django.shortcuts import render
from django.http import Http404
#from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from core.models import Checklist,CheckListItem
from core.serializers import ChecklistSerializer, ChecklistItemSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ChecklistAPIView(APIView):
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated,]

    def get(self, request, format=None):
        data = Checklist.objects.all()

        serializer = self.serializer_class(data, many=True)
        serialized_data =serializer.data

        return Response(serialized_data)
    
    def post(self, request, format=None):
        # print(request.data)
        serializer = self.serializer_class(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
        # serialized_data = None
            return Response(serialized_data)
        return Response(serializer.errors)
    
class ChecklistsAIPView(APIView):
    serializer_class = ChecklistSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self, pk):
        try:
            return Checklist.objects.get(pk=pk)
        except Checklist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data)
    
    def put(self, request, pk, format=None):
        Checklist = self.get_object(pk)
        serilaizer = self.serializer_class(Checklist, data = request.data, context={'request': request})
        if serilaizer.is_valid():
            serilaizer.save()
            serilaizer_data = serilaizer.data
            return Response(serilaizer_data)
        return Response(serilaizer.errors)
    def delete(self,request,pk, format =None):
        Checklist = self.get_object(pk)
        Checklist.delete()
        return Response(Http404)

class ChecklistItemCreateAPIView(APIView):
    serializer_class = ChecklistItemSerializer
    permission_classes = [IsAuthenticated,]

    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
        # serialized_data = None
            return Response(serialized_data)
        return Response(serializer.errors)

class ChecklistItemAPIView(APIView):
    serializer_class = ChecklistItemSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self, pk):
        try:
            return CheckListItem.objects.get(pk=pk)
        except CheckListItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Checklist_item = self.get_object(pk)
        serializer = self.serializer_class(Checklist_item)
        serialized_data = serializer.data
        return Response(serialized_data)
    
    def put(self, request, pk, format=None):
        Checklist_item = self.get_object(pk)
        serializer = self.serializer_class(Checklist_item, data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serilaizer_data = serializer.data
            return Response(serilaizer_data)
        return Response(serializer.errors)
    def delete(self,request,pk, format =None):
        Checklist_item = self.get_object(pk)
        Checklist_item.delete()
        return Response(Http404)


