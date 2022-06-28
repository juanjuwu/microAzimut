from django.shortcuts import render, HttpResponse
from django.http import request
from calculos import salida
from calculos import df_salida
from django.shortcuts import redirect
##from microAzimut.forms import Calculo
from .forms import MyForm
# from calculos import getLista
##def index(request):
##    form= Calculo(request.POST)
##
##
##    return render(request, "microAzimut/index.html", {'form':form})
a = df_salida()
def writeList(lista):
    file = open("lista.txt","w")
    for x in range(len(lista)):
        if x != len(lista) - 1:
            file.write(lista[x]+",")
        else:file.write(lista[x])
    file.close()
def calculo(request):


    # data_frame = calculos.df_salida()
    # #print (data_frame)
    # data_frame = data_frame.to_html()
    context = {
        "data_frame" : df_salida()
    }
    return render(request,'microAzimut/calculo.html',context)

def index(request):
   
    form = MyForm()
    
    if request.method == 'POST':
        fruits = request.POST.getlist('display_type')
        #print(fruits)
        
        #print(a)
        writeList(fruits)   
        return redirect("/calculo/")
    return render(request, 'microAzimut/index.html', {'form': form})

# def index(request):
    
#     form = MyForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             if request.POST["something_truthy"]:
#                print('hola')

#     return render(request, 'microAzimut/index.html', {'form': form})