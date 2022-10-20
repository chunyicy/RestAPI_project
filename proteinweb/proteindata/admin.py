from django.contrib import admin
from .models import*

# use ModelAdmin objects to add display columns
class PfamAdmin(admin.ModelAdmin):
    list_display = ('domain_ID','domain_description')


class TaxonomyAdmin(admin.ModelAdmin):
    list_display = ('taxa_ID', 'clade','genus', 
                    'species')


class ProteinAdmin(admin.ModelAdmin):
    list_display = ('protein_ID','sequence','length','taxonomy')


class DomainAdmin(admin.ModelAdmin):
    list_display = ('pfam_ID','description', 'start', 'end', 'protein')


# register the model class
admin.site.register(Pfam, PfamAdmin)
admin.site.register(Taxonomy, TaxonomyAdmin)
admin.site.register(Protein, ProteinAdmin)
admin.site.register(Domain, DomainAdmin)

