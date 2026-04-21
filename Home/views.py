from django.shortcuts import render, HttpResponse
from django.db import connections
from django.db.models import Q
from .models import NNPTable1
#from .models import NutrientStudy

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Welcome to Home page, Kanika")

def Search(request):
    query = request.GET.get('q', '').strip()  # Get user input and remove extra spaces
    results = []    #results = NNPTable1.objects.all()  # Default: Get all results

    if query:
        # Use `icontains` instead of `iregex` for MSSQL
        results = NNPTable1.objects.filter(
            Q(data_type__icontains=query) |
            Q(platform_seq__icontains=query) |
            Q(NCBI_ID__icontains=query) |
            Q(studied_nutrient__icontains=query) |
            Q(growing_seasons__icontains=query) |
            Q(Plant_tissue_Bacterial_strain_Fungal_strain__icontains=query) |
            Q(Genotype_name__icontains=query) |
            Q(trait_studied__icontains=query) |
            Q(study__icontains=query)
            
        )
    # Split NCBI_ID field (if exists) into a list using "; " as separator
    for result in results:
        if result.NCBI_ID:
            result.NCBI_ID_list =  [item.strip() for item in result.NCBI_ID.split(";")]  #result.NCBI_ID.split("; ")  # Create a new list attribute   

    return render(request, 'search.html', {'results': results, 'query': query})



def Team(request):
    return render(request, 'Team.html')
    #return HttpResponse("Welcome to Team page, Kanika")
