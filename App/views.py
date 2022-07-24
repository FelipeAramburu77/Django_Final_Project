from django.shortcuts import render, redirect
from django.http import HttpResponse
from App.models import *
from App.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def inicio(request):
      return render(request, "App/index.html")

def about_us(request):
      return render(request, "App/about_us.html")

def locales(request):
      locales = Locales.objects.all()
      return render(request, "App/locales.html", {"locales":locales})

def locales_formulario(request):
      if request.method == "POST":
            mi_formulario = Local_Formulario(request.POST) #aquí me llega toda la información del html
            print(mi_formulario)

            if mi_formulario.is_valid():  #Si pasó la validación de Django
                  informacion = mi_formulario.cleaned_data
                  print(informacion)
                  local = Locales (name=informacion['name'],city=informacion['city'],address=informacion['address'], mall_number=informacion['mall_number'],opening_hours=informacion['opening_hours'])
                  local.save()
                  return redirect("Locales") 
            else:
                  return render(request,"App/locales_formulario.html",{"mi_formulario":mi_formulario})
            
      else: 
            formulario_vacio = Local_Formulario()
            return render(request, "App/locales_formulario.html", {"mi_formulario":formulario_vacio})

def buscar_local(request):   
    if request.method == "POST":    
        mall_number = request.POST["mall_number"]    
        locales = Locales.objects.filter(mall_number__icontains=mall_number)
        return render(request,"App/buscar_local.html",{"locales":locales})
    
    else:
        locales = []     
        return render(request,"App/buscar_local.html",{"locales":locales})  




def vendedores(request):
      vendedores = Vendedores.objects.all()
      return render(request, "App/vendedores.html", {"vendedores":vendedores})

def vendedores_formulario(request):
      if request.method == "POST":
            mi_formulario = Vendedor_Formulario(request.POST) #aquí me llega toda la información del html
            print(mi_formulario)

            if mi_formulario.is_valid():  #Si pasó la validación de Django
                  informacion = mi_formulario.cleaned_data
                  print(informacion)
                  vendedor = Vendedores(name=informacion['name'], last_name=informacion['last_name'], email=informacion['email'], mall_number=informacion['mall_number'], birthday=informacion['birthday'])
                  vendedor.save()
                  return redirect("Vendedores") #Vuelvo al inicio o a donde quieran
            else:
                  return render(request, "App/vendedores_formulario.html", {"mi_formulario":mi_formulario})
      else: 
            formulario_vacio = Vendedor_Formulario()
            return render(request, "App/vendedores_formulario.html", {"mi_formulario":formulario_vacio})

def leer_vendedor(request):
      vendedores= Vendedores.objects.all()
      return render(request, "App/leer_vendedor.html",{"vendedores":vendedores})

def eliminar_vendedor(request, vendedor_nombre):
      vendedor= Vendedores.objects.get(name=vendedor_nombre)
      vendedor.delete()
      #vuelvo al menú
      vendedores= Vendedores.objects.all()
      return render(request, "App/vendedores.html", {"vendedores":vendedores})

def editar_vendedor(request, vendedor_nombre):
      #Recibe el nombre del vendedor que vamos a modificar
      vendedor = Vendedores.objects.get(name=vendedor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            mi_formulario = Vendedor_Formulario(request.POST) #aquí mellega toda la información del html
            print(mi_formulario)

            if mi_formulario.is_valid:   #Si pasó la validación de Django
                  informacion = mi_formulario.cleaned_data
                  vendedor.name = informacion['name']
                  vendedor.last_name = informacion['last_name']
                  vendedor.email = informacion['email']
                  vendedor.mall_number = informacion['mall_number']
                  vendedor.birthday = informacion['birthday']
                  vendedor.save()
                  return render(request, "App/index.html") 

      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            mi_formulario= Vendedor_Formulario(initial=
                                                {'name': vendedor.name, 
                                                'last_name':vendedor.last_name , 
                                                'email':vendedor.email, 
                                                'mall_number':vendedor.mall_number,
                                                'birthday': vendedor.birthday}
                                               ) 

      #Voy al html que me permite editar
      return render(request, "App/editar_vendedor.html", {"mi_formulario":mi_formulario, "vendedor_nombre":vendedor_nombre})





def productos(request):
      productos = Productos.objects.all
      return render(request, "App/productos.html", {"productos":productos})
    
def productos_formulario(request):
      if request.method == "POST":
            mi_formulario = Producto_Formulario(request.POST) #aquí me llega toda la información del html
            print(mi_formulario)

            if mi_formulario.is_valid():  #Si pasó la validación de Django
                  informacion = mi_formulario.cleaned_data
                  print(informacion)
                  producto = Productos (product=informacion['product'], prize=informacion['prize'], brand=informacion['brand'], stock=informacion['stock'])
                  producto.save()
                  return redirect("Productos") #Vuelvo al inicio o a donde quieran
            else:
                  return render(request,"App/productos_formulario.html",{"mi_formulario":mi_formulario})
      else:
            formulario_vacio = Producto_Formulario()     
            return render(request, "App/productos_formulario.html", {"mi_formulario":formulario_vacio})

def buscar_producto(request):   
    if request.method == "POST":    
        product = request.POST["product"]    
        productos = Productos.objects.filter(product__icontains=product)
        return render(request,"App/buscar_producto.html",{"productos":productos}) 

    else:
        productos = []     
        return render(request,"App/buscar_producto.html",{"productos":productos})  

def descripcion(request):
      return render(request, "App/descripcion.html")




#iniciamos el login
def login_request(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)     
            if form.is_valid():
                  user = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')   
                  user = authenticate(username = user , password = password)
                 
                  if user is not None:
                        login(request, user)
                        return render (request, "App/index.html", {"mensaje": f"Welcome {user}"})
                  else:    
                        return render (request, "App/index.html", {"mensaje":"Error!"})
            
            else:
                  return render(request, "App/index.html", {"mensaje":"Error!"})     

      form = AuthenticationForm()
      return render(request, "App/login.html", {'form': form})

def register(request):      
      if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request, "App/index.html", {"mensaje": "User created"})
      else: 
            form = UserRegisterForm()
      return render(request, "App/register.html", {"form": form})

@login_required
def editar_perfil(request):
      #se instancia el Login; 
      user = request.user   
      if request.method == 'POST':
            mi_formulario = UserEditForm(request.POST)
            if mi_formulario.is_valid(): #si pasa la validación Django
                  informacion = mi_formulario.cleaned_data                 
                  #datos que modificaríamos
                  user.email = informacion['email']
                  user.password1 = informacion['password1']
                  user.password2 = informacion['password2']
                  user.save()
                  return render(request, "App/index.html") 

      else:
            #creo el formulario con los datos que voy a modificar
            mi_formulario = UserEditForm(initial={'email':user.email})
      
      #voy al HTML que me permite editar
      return render(request, "App/editar_perfil.html", {"mi_formulario": mi_formulario, "user": user})






@login_required
def nuevos_productos(request):
      nuevos_productos = Nuevos_Productos.objects.all
      return render(request, "App/nuevos_productos.html", {"nuevos_productos":nuevos_productos})

def nuevos_productos_formulario(request):
      if request.method == "POST":
            mi_formulario = Nuevos_Productos_Formulario(request.POST) #aquí me llega toda la información del html
            print(mi_formulario)

            if mi_formulario.is_valid():  #Si pasó la validación de Django
                  informacion = mi_formulario.cleaned_data
                  print(informacion)
                  nuevo_producto = Nuevos_Productos(product=informacion['product'], brand=informacion['brand'], release_date=informacion['release_date'])
                  nuevo_producto.save()
                  return redirect("Nuevos_Productos") #Vuelvo al inicio o a donde quieran
            else:
                  return render(request, "App/nuevos_productos_formulario.html", {"mi_formulario":mi_formulario})
      else: 
            formulario_vacio = Nuevos_Productos_Formulario()
            return render(request, "App/nuevos_productos_formulario.html", {"mi_formulario":formulario_vacio})

def info_nuevos_productos(request):
      nuevos_productos= Nuevos_Productos.objects.all()
      return render(request, "App/nuevos_productos_detalle.html",{"nuevos_productos":nuevos_productos})

def editar_nuevo_producto(request, nuevo_producto_nombre):
      #Recibe el nombre del vendedor que vamos a modificar
      nuevo_producto = Nuevos_Productos.objects.get(product=nuevo_producto_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            mi_formulario = Nuevos_Productos_Formulario(request.POST) #aquí mellega toda la información del html
            print(mi_formulario)

            if mi_formulario.is_valid:   #Si pasó la validación de Django
                  informacion = mi_formulario.cleaned_data
                  nuevo_producto.product = informacion['product']
                  nuevo_producto.brand = informacion['brand']
                  nuevo_producto.release_date = informacion['release_date']
                  nuevo_producto.save()
                  return render(request, "App/index.html") 

      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            mi_formulario= Nuevos_Productos_Formulario(initial=
                                                {'product': nuevo_producto.product, 
                                                'brand':nuevo_producto.brand , 
                                                'release_date':nuevo_producto.release_date}
                                               ) 

      #Voy al html que me permite editar
      return render(request, "App/editar_nuevo_producto.html", {"mi_formulario":mi_formulario, "nuevo_producto_nombre":nuevo_producto_nombre})

def eliminar_nuevo_producto(request, nuevo_producto_nombre):
      nuevo_producto= Nuevos_Productos.objects.get(product=nuevo_producto_nombre)
      nuevo_producto.delete()
      #vuelvo al menú
      nuevos_productos= Nuevos_Productos.objects.all()
      return render(request, "App/nuevos_productos.html", {"nuevos_productos":nuevos_productos})