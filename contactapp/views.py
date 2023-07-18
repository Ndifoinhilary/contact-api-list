from django.shortcuts import render
from .serializers import ContactSerializer
from rest_framework import generics
from rest_framework import permissions
from contactapp.models import Contact



class ContatList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated,]
    
    def perform_create(self, serializer): #creating an instance base on the currently login user that's the owner
        
        serializer.save(owner= self.request.user)
    
    
    def  get_queryset(self):#the user can only view his/her contacts 
        return Contact.objects.filter(owner = self.request.user)



class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    
    
    def  get_queryset(self):#the user can only view his/her contacts 
        return Contact.objects.filter(owner = self.request.user)