from rest_framework import serializers
from .models import *



class PfamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pfam  # model from the Pfam class
        # specify the fields to be served to the user
        fields = ['id','domain_ID', 'domain_description']



class TaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxonomy  # model from the Taxonomy class
        # specify the fields
        fields = ['taxa_ID', 'clade',
                  'genus', 'species']



class ProteinSerializer(serializers.ModelSerializer):
    taxonomy = TaxonomySerializer()
    class Meta:
        model = Protein # Protein table
        fields = ['id','protein_ID', 'sequence',
                  'length', 'taxonomy']



class DomainSerializer(serializers.ModelSerializer):
    protein = ProteinSerializer()
    pfam_ID = PfamSerializer()
    class Meta:
        model = Domain  # Domain table
        fields = ['protein','pfam_ID', 'description',
                  'start', 'end']
        
    def create(self, validated_data):
        protein_data = self.initial_data.get('protein') 
        pfam_data = self.initial_data.get('pfam_ID') 
        domain = Domain(**{**validated_data, 
                        'protein': Protein.objects.get(pk=protein_data['id']), 
                        'pfam_ID': Pfam.objects.get(pk = pfam_data['id'])})
        domain.save()
        return domain


class TaxonomyProteinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['id','protein_ID']



class TaxonomyPfamSerializer(serializers.ModelSerializer):
   
   
    pfam_ID = PfamSerializer()

    class Meta:
         model = Domain
         fields = ['id', 'pfam_ID']





