from django.urls import path

from .import api


urlpatterns = [

    path('api/pfam/<str:type>', api.pfam_detail, name='pfam_api'),
    path('api/proteins/<str:type>', api.taxonomyProtein_detail),
    path('api/pfams/<str:type>', api.taxonomyPfam_detail),
    path('api/protein/<str:type>',api.protein_detail, name='protein_api'),


]

