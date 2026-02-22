from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import Category, Service
from django.db.models import Q



class IndexView(TemplateView):
    
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categories'] = Category.objects.all()
        
        services = Service.objects.all().order_by('-created_at')
        
        category_slug = self.request.GET.get('category')
        if category_slug:
            services = services.filter(category__slug=category_slug)
            context['selected_category'] = category_slug
        
        query = self.request.GET.get('q', '')
        if query:
            services = services.filter(
                Q(name__icontains=query) | 
                Q(description__icontains=query)
            )
            context['search_query'] = query
        
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        
        if min_price:
            services = services.filter(price__gte=min_price)
            context['min_price'] = min_price
        
        if max_price:
            services = services.filter(price__lte=max_price)
            context['max_price'] = max_price
        
        context['services'] = services
        
        return context


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'main/service_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.get_object()
        context['categories'] = Category.objects.all()
        context['related_services'] = Service.objects.filter(
            category=service.category
        ).exclude(id=service.id)[:4]
        context['current_category'] = service.category.slug
        return context
    


    