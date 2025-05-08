from django.views.generic import TemplateView
from producto.models import Producto, Categoria

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        context['categorias'] = Categoria.objects.all()
        return context
