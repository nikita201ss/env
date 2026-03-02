from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Category, Service, ServiceImage
from django.db.models import Q
from django.contrib import messages
from .forms import ServiceForm

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
    


class AboutView(TemplateView):
    template_name = 'main/about.html'



def service_create_view(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        
        if form.is_valid():
            service = form.save(commit=False)
            
            from django.utils.text import slugify
            service.slug = slugify(service.name)
            
            original_slug = service.slug
            counter = 1
            while Service.objects.filter(slug=service.slug).exists():
                service.slug = f"{original_slug}-{counter}"
                counter += 1
            
            service.save()
            
            form.save_m2m()
            
            images = request.FILES.getlist('extra_images')
            for image in images:
                ServiceImage.objects.create(service=service, image=image)
            
            messages.success(request, 'Услуга успешно добавлена!')
            return redirect('main:index')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = ServiceForm()
    
    categories = Category.objects.all()
    
    return render(request, 'main/service_create.html', {
        'form': form,
        'categories': categories,
    })


