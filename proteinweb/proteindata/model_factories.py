import factory
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from .models import*


class TaxonomyFactory(factory.django.DjangoModelFactory):
    taxa_ID ='568076' # give sample data for each fields in the model
    clade = 'E'
    genus = 'Metarhizium'
    species = 'robertsii'

    class Meta: # telling the factory to use the Taxonomy model
        model = Taxonomy


class ProteinFactory(factory.django.DjangoModelFactory):
    protein_ID = 'protein1'
    sequence ='ABCDEFG'
    length = 123
    taxonomy = factory.SubFactory(TaxonomyFactory) # foreign key

    class Meta: # telling the factory to use the Protein model
        model = Protein


class PfamFactory(factory.django.DjangoModelFactory):
    domain_ID = 'PF02800'
    domain_description = 'Glyceraldehyde3-phosphatedehydrogenase: C-terminaldomain'

    class Meta: # using Pfam model
        model = Pfam
        

        
class DomainFactory(factory.django.DjangoModelFactory):
    pfam_ID = factory.SubFactory(PfamFactory) # using sub-factory for foreign key
    description = 'Glyceraldehyde 3-phosphate dehydrogenase catalytic domain'
    start = 157
    end = 314
    protein =factory.SubFactory(ProteinFactory) # using ProteinFactory class as the sub-factory

    class Meta: # using Domain model
        model = Domain


