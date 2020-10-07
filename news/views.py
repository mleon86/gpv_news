from django.shortcuts import render
from django.shortcuts import get_object_or_404 #hace validación de datos, en vez de hacer el try con el raise
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Post, Categoria

from django.views.generic import View

# Create your views here.

#vistas basadas en clases
class Inicio(View):
	def get(self, request, *args, **kwargs):
		queryset = request.GET.get("buscar")
		posteos = Post.objects.filter(estado = True)
		if queryset:
			posteos = Post.objects.filter(
				Q(titulo__icontains = queryset) |
				Q(descripcion__icontains = queryset) |
				Q(contenido__icontains = queryset)
			).distinct()
		#paginacion
		paginator = Paginator(posteos, 10)#instancia de la clase Paginator, recibe dos parametros, lista de objetos y la cantidad de paginas
		page = request.GET.get('page')#guarda la pagina actual en la que se encuentra navegando
		posteos = paginator.get_page(page)#vuelve a definir post entonces, carga en poestos los restantes
		return render(request,'index.html',{'posteos':posteos})



#vistas basadas en funciones
def home(request):
	queryset = request.GET.get("buscar")
	posteos = Post.objects.filter(estado = True)
	if queryset:
		posteos = Post.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset) |
			Q(contenido__icontains = queryset)
		).distinct()

	#paginacion
	paginator = Paginator(posteos, 2)#instancia de la clase Paginator, recibe dos parametros, lista de objetos y la cantidad de paginas
	page = request.GET.get('page')#guarda la pagina actual en la que se encuentra navegando
	posteos = paginator.get_page(page)#vuelve a definir post entonces, carga en poestos los restantes

	return render(request,'index.html',{'posteos':posteos})

def noticias(request):
	posteos = Post.objects.filter(
		estado = True,
		categoria = Categoria.objects.get(nombre = 'Noticias')
	)
	return render (request, 'noticias.html', {'posteos': posteos})

def eventos (request):
	queryset = request.GET.get("buscar")
	posteos = Post.objects.filter(
		estado = True,
		categoria = Categoria.objects.get(nombre__iexact = 'Eventos')#iexact hace que ignore las mayusculas ni minusculas
	)
	if queryset:
		posteos = Post.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(descripcion__icontains = queryset) |
			Q(contenido__icontains = queryset),
			estado = True,
			categoria = Categoria.objects.get(nombre__iexact = 'Eventos')#iexact hace que ignore las mayusculas ni minusculas
		).distinct()
	
	#paginacion
	paginator = Paginator(posteos, 2)#instancia de la clase Paginator, recibe dos parametros, lista de objetos y la cantidad de paginas
	page = request.GET.get('page')#guarda la pagina actual en la que se encuentra navegando
	posteos = paginator.get_page(page)#vuelve a definir post entonces, carga en poestos los restantes
	
	return render (request, 'eventos.html', {'posteos': posteos})

def legion (request):
	return render (request, 'legion.html')

def recursos (request):
	return render (request, 'recursos.html')

def contacto (request):
	return render(request, 'contacto.html')

def detallePost(request, slug):
	post = get_object_or_404(Post, slug = slug) #utilizando el metodo get_object_or_404

	return render(request, 'post.html', {'detalle_post':post})