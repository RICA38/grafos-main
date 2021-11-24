from django.shortcuts import render, HttpResponse
from .models import Tejido
import pandas as pd
from scipy.spatial import distance
tejidos = Tejido.objects.all()

# Create your views here.
def grafo(request):
    # lol = pd.read_csv('grafo_app/db.csv')
    # for i in range(200):
    #     newTejido = Tejido(
    #         temperatura = lol['temperatura'][i],
    #         color = lol['color'][i],
    #         inflammation = lol['inflammation'][i],
    #     )
    #     newTejido.save()
    id = []
    for i in range(200):
        id.append(i+1)

    return render(request, 'grafo.html' , {'tejidos': tejidos, 'euclidea':euclidea(tejidos) , 'id':id})

def euclidea(tejidos):
    tejidosTotal = []
    for i in tejidos:
        tejido = []
        tejido.append(i.temperatura)
        tejido.append(i.color)
        tejido.append(i.inflammation)
        tejidosTotal.append(tejido)      

    mEuclidea = []
    for i in range(len(tejidosTotal)):
        f = []
        for j in range(len(tejidosTotal)):
            f.append(round(distance.euclidean(tejidosTotal[i],tejidosTotal[j], 6 )))
        mEuclidea.append(f)
    # print(mEuclidea)
    return mEuclidea

def procesa(request):
    if(request.method == 'POST'):
        #umbral =forms.IntegerField(min_value=1,max_value=100)
        umbral = int(request.POST['umbral'])
        
            
        
    return render(request, 'grafo.html' , {'tejidos': tejidos, 'euclidea':euclidea(tejidos) , 'umbral':umbral})



    
    
    
    
    
