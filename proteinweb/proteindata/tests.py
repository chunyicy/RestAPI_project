import json
from django.http import response
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from .model_factories import *
from .serializers import*


class PfamTest(APITestCase):

    def test_pfamDetailReturnSuccess(self):
        pfam = PfamFactory.create(pk=1,domain_ID = "CoiledCoil")
        url = reverse('pfam_api', kwargs={'type': 'CoiledCoil'})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200) # return 200 response

    def test_pfamDetailReturnFailOnBadType(self):
        pfam = PfamFactory.create(pk=2, domain_ID='LowComplexity')
        url = '/api/pfam/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,404) # return 404 response



class PfamSerialiserTest(APITestCase): # to test that the pfam serializer perform correctly
    pfam3=None
    pfamSerializer = None

    def setUp(self):
        self.pfam3 = PfamFactory.create(pk=3, domain_ID='mobidb-lite')
        self.pfamSerializer = PfamSerializer(instance = self.pfam3)

    def tearDown(self):
        Pfam.objects.all().delete()
        PfamFactory.reset_sequence(0)
        
    def test_pfamSerializer(self):
        data=self.pfamSerializer.data
        self.assertEqual(data['domain_ID'], 'mobidb-lite')




class ProteinTest(APITestCase):

    def test_proteinDetailReturnSuccess(self):
        # protein is a foreign key in the Domain model
        # using protein__protein_ID to reference another field in another model
        protein = DomainFactory.create(pk=1,protein__protein_ID = "A0A014PQC0")
        url = reverse('protein_api', kwargs={'type': 'A0A014PQC0'})
        response = self.client.get(url)
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_proteinDetailReturnFailOnBadType(self):
        protein = DomainFactory.create(pk=2, protein__protein_ID='A0A016S8J7')
        url = '/api/protein/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)




