from django.shortcuts import render
from .models import Biome,Tree
from django.db.models import Q



def home(request):
    return render(request,'app/home.html')

def list_biomes(request):
    biomes = Biome.objects.all() 
    return render(request, 'app/biomes.html', {'biomes': biomes})

def catalog_view(request):
    trees = Tree.objects.all()
    biomes = Biome.objects.all() 

    return render(request, 'app/catalog.html', {'trees': trees,'biomes': biomes})

def catalog_register(request):

    if request.method == "POST":
        common_name = request.POST.get('common_name')
        scientific_name = request.POST.get('scientific_name')
        description = request.POST.get('description')
        biomes_ids = request.POST.getlist('biomes')  # muitos biomas

        tree = Tree.objects.create(
            common_name=common_name,
            scientific_name=scientific_name,
            description=description
        )

        if biomes_ids:
            tree.biomes.set(biomes_ids)  

    trees = Tree.objects.all()
    biomes = Biome.objects.all()

    return render(request, 'app/catalog.html', {'trees': trees, 'biomes': biomes})

def catalog_view(request):
    query = request.GET.get("q", "")  

    if query:
        trees = Tree.objects.filter(
            Q(common_name__icontains=query) |
            Q(scientific_name__icontains=query)
        )
    else:
        trees = Tree.objects.all()

    biomes = Biome.objects.all()

    return render(request, "app/catalog.html", {
        "trees": trees,
        "biomes": biomes,
        "query": query,
    })