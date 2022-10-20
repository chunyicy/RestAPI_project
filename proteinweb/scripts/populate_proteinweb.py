import os
import sys
import django
import csv
from collections import defaultdict
sys.path.append("/Users/user/Desktop/advanced web dev/project/awd_midterm/proteinweb")

os.environ.setdefault('DJANGO_SETTINGS_MODULE','proteinweb.settings')

django.setup()

from proteindata.models import *

pfam_file = '/Users/user/Desktop/advanced web dev/project/awd_midterm/pfam_descriptions.csv'
data_file = '/Users/user/Desktop/advanced web dev/project/awd_midterm/assignment_data_set.csv'
proteinSeq_file = '/Users/user/Desktop/advanced web dev/project/awd_midterm/assignment_data_sequences.csv'


pfam_set = defaultdict(set)
proteinseq_set = defaultdict(set)
taxonomy_dict = defaultdict(dict)
protein_dict = defaultdict(dict)
domain_dict = defaultdict(dict)

with open(pfam_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        # domain_ID - row 0
        # domain_description - row 1
        pfam_set[row[0]] = row[1]


with open(proteinSeq_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        # protein_ID - row 0
        # sequence - row 1
        proteinseq_set[row[0]] = row[1]


with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader :

        # taxa_ID - row 1
        # clade - row 2
        # taxonomy_scientific_name ("Genus Species") - row 3
        # genus - taxonomy_scientific_name[0]
        # species - taxonomy_scientific_name[1]
        taxonomy_scientific_name = row[3].split(' ')
        if len(taxonomy_scientific_name)>2:
            taxonomy_dict[row[1]]= {
                                    "clade":row[2], 
                                    "genus":taxonomy_scientific_name[0], 
                                    "species":taxonomy_scientific_name[1:len(taxonomy_scientific_name)]
                                    }
        else:
            taxonomy_dict[row[1]]= {
                                    "clade":row[2], 
                                    "genus":taxonomy_scientific_name[0], 
                                    "species":taxonomy_scientific_name[1]
                                    }
        
        # protein_ID - row 0
        # sequence
        # length - row 8
        # taxonomy - row 1
        protein_dict[row[0]] = {"sequence":proteinseq_set[row[0]],"length":row[8],
                                "taxonomy":row[1]}


        # pfam_ID - row 5
        # description - row 4
        # start - row 6
        # end - row 7
        # protein - row[0]
       
        domain_dict[row[5], row[6], row[7],row[0]] = { "description":row[4]}

Pfam.objects.all().delete()
Taxonomy.objects.all().delete()
Protein.objects.all().delete()
Domain.objects.all().delete()

# stroing foreign key
pfam_rows={}
taxonomy_rows = {} 
protein_rows = {}
domain_rows = {}

# insert data into Pfam table
for data in pfam_set:
    row = Pfam.objects.create(domain_ID = data,
                              domain_description = pfam_set[data])

    row.save()
    pfam_rows[data] = row



# insert data into Taxonomy table
for taxa_ID, data in taxonomy_dict.items():
    row = Taxonomy.objects.create(taxa_ID=taxa_ID,
                                  clade=data['clade'],
                                  genus=data['genus'],
                                  species=data['species'])
    row.save()
    taxonomy_rows[taxa_ID] = row



# insert data into Protein table
for protein_ID,data in protein_dict.items():
    row = Protein.objects.create(protein_ID=protein_ID,
                                 sequence=data['sequence'],
                                 length=data['length'],
                                 taxonomy=taxonomy_rows[data['taxonomy']]
                                 )
    row.save()
    protein_rows[protein_ID] = row


# insert data into Domain table
for (pfam_ID, start, end,protein), data in domain_dict.items():
    row = Domain.objects.create( pfam_ID=pfam_rows[pfam_ID],
                                 description = data['description'],
                                 start=start,
                                 end = end,
                                 protein=protein_rows[protein])
                                
    row.save()
    domain_rows[pfam_ID, start, end,protein] = row




