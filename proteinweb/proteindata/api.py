from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework import generics


@api_view(['GET']) 
def pfam_detail(request, type):
    try: 
        # to get pfam detail from the database based on the domain_ID
        pfam = Pfam.objects.get(domain_ID__exact=type)
        
    except Pfam.DoesNotExist:
        return HttpResponse(status=404) # return 404 response for missing data
    if request.method == 'GET': 
        serializer = PfamSerializer(pfam) 
        return Response(serializer.data) # return serializer data




@api_view(['GET']) # implementing get
def taxonomyProtein_detail(request, type):
    try:
        proteins = Protein.objects.filter(taxonomy__taxa_ID__exact=type)
    except Protein.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = TaxonomyProteinSerializer(proteins, many=True)
        return Response(serializer.data)



@api_view(['GET'])

def taxonomyPfam_detail(request, type):
    try:
        pfams = Domain.objects.filter(protein__taxonomy__taxa_ID__exact=type)
        
    except Domain.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = TaxonomyPfamSerializer(pfams, many=True) # many lists
        return Response(serializer.data)



# implement the GET POST HTTP methods
@api_view(['GET', 'POST'])

def protein_detail(request, type):# request object and string type from user
    if request.method == 'POST': 
        serializer = DomainSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        protein = Domain.objects.filter(protein__protein_ID__exact=type)
        
    except Domain.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET': # successfully get the protein data
        serializer = DomainSerializer(protein, many=True)  # called the Domain serializer
        return Response(serializer.data) # return the serialize data





