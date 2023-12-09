from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, TemplateView
from .models import Category, Image, MenuItem
# Create your views here.

class HomePage(TemplateView):
    template_name = 'cafemenu/main_page.html'
    
class Contact(TemplateView):
    template_name = 'cafemenu/contact.html'

class CategoryView(ListView):
    model = Category
    template_name = 'cafemenu/catrgory.html'
    context_object_name = 'category'
    queryset = Category.objects.values('category_name')

class CategoryDetailView(ListView):
    model = MenuItem
    template_name = 'cafemenu/menuitem_list.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['category_slug'])
        return MenuItem.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
    
class ItemsView(ListView):
    model = MenuItem
    template_name = 'cafemenu/items_list.html'
    context_object_name = 'items'
    queryset = MenuItem.objects.values('item_name')

class ItemsDetailView(ListView):
    model = MenuItem
    template_name = 'cafemenu/item_detail_list.html'
    context_object_name = 'details'

    def get_queryset(self):
        self.item = MenuItem.objects.get(slug=self.kwargs['item_slug'])
        return MenuItem.objects.filter(item_name=self.item)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_name'] = self.item
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_images'] = self.item.image.all()
        return context



# def home_page(request):
#     return render(request, 'cafemenu/main_page.html')

# def contact(request):
#     return render(request, 'cafemenu/contact.html')