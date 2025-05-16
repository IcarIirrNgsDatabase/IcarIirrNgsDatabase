from django.db import models

# Create your models here.
class NNPTable1(models.Model):
    ID = models.AutoField(primary_key=True)
    data_type = models.CharField(max_length=255)
    platform_seq = models.CharField(max_length=255)
    NCBI_ID = models.CharField(max_length=255)
    studied_nutrient = models.CharField(max_length=255)
    growing_seasons = models.CharField(max_length=255)
    Plant_tissue_Bacterial_strain_Fungal_strain = models.CharField(max_length=255)
    Genotype_name = models.CharField(max_length=255)
    trait_studied = models.CharField(max_length=255)
    study = models.CharField(max_length=255)
    summary_abstract = models.TextField()

    class Meta:
        db_table = "NNPTable1"
        managed = False

    def __str__(self):
        return f"{self.Genotype_name} - {self.trait_studied}"