from django.db import models


# Pfam table
class Pfam(models.Model):
    domain_ID = models.CharField(max_length=256, null=False,blank=False, db_index=True)
    domain_description = models.CharField(max_length=256, null=False,blank=False)

    def __str__(self):
            return self.domain_ID 


# Taxonomy table
class Taxonomy(models.Model):
    taxa_ID = models.IntegerField(null=False,blank=False, db_index=True)
    clade = models.CharField(max_length=1, default = "E")
    genus = models.CharField(max_length=256, null=False, blank=False)
    species = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return str(self.taxa_ID)



# Protein table 
class Protein(models.Model):
    protein_ID =models.CharField(max_length=256, null=False,blank=False,db_index=True)
    sequence =models.CharField(max_length=700, null=False,blank=True)
    length = models.IntegerField(null=False, blank=False)
    taxonomy = models.ForeignKey(Taxonomy, on_delete=models.DO_NOTHING) 
    
    def __str__(self):
        return self.protein_ID


# Domain table
class Domain(models.Model):
    pfam_ID = models.ForeignKey(Pfam, on_delete=models.DO_NOTHING, db_index=True)
    description = models.CharField(max_length=256, null=False,blank=False)
    start = models.IntegerField(null=False, blank=False) 
    end = models.IntegerField(null=False, blank=False)
    protein = models.ForeignKey(Protein, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.pfam_ID

