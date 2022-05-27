
from multiprocessing import context
from django.shortcuts import render, redirect
from django.db.models import Q, F
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView,CreateView,View
from product.forms import ProductForm,CategoryForm
from product.models import CartModel, ProductModel , CategoryModel 

# Product Views
# class ProductCreateView(CreateView):
#     template_name = "product/create.html"
#     model = ProductModel
#     form_class = ProductForm
#     success_url = reverse_lazy('product_list')

class ProductCreateView(View):
    template_name = 'product/create.html'
    model = ProductModel
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    
    def get(self, request):
        context={ 
            'form' : self.form_class()
            }
        return render(request,self.template_name,context)

    def post(self, request):
        files = self.request.FILES
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            self.form_valid(form)
        else:
            return self.form_invalid(form)
        return self.get_success_url()

    def form_valid(self, form):
        form.save()

    def form_invalid(self, form):
        context={ 
            'form' : self.form_class(form)
            }
        return render(self.request,self.template_name,context)

    def get_success_url(self):
        return redirect(self.success_url)
        
    
class ProductListView(ListView):
    template_name = "product/list.html"
    model = ProductModel

class ProductDetailView(DetailView):
    template_name = "product/detail.html"
    model = ProductModel

class ProductUpdateView(UpdateView):
    template_name = 'product/update.html'
    model = ProductModel
    # fields = ['name','price','image','category','description','unit']
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    template_name = 'product/detail.html'
    model = ProductModel
    success_url = reverse_lazy('product_list')



# Category Views



class CategoryListView(ListView):
    template_name = "product/category/list.html"
    model = CategoryModel


class CategoryDetailView(DetailView):
    template_name = "product/category/detail.html"
    model = CategoryModel


class CategoryCreateView(CreateView):
    template_name = "product/category/create.html"
    model = CategoryModel
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')




class CategoryUpdateView(UpdateView):
    template_name = 'product/category/update.html'
    model = CategoryModel
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')


class CategoryDeleteView(DeleteView):
    template_name = 'product/category/detail.html'
    model = CategoryModel
    success_url = reverse_lazy('category_list')


class ProductListByCategory(View):
    template_name = 'product/search_list.html'

    def get(self,request,pk):
        context = {'products': ProductModel.objects.filter(category_id =pk)}
        return render(request,self.template_name,context)


class SearchView(View):
    template_name = 'product/search_list.html'
    def get(self, request):
        query = request.GET.get('query')
        products = ProductModel.objects.filter(
            Q(name__icontains=query) | Q(category__name__icontains=query)
        )
        context = {
            'products': products
        }
        return render(request, self.template_name, context)


# Add to cart
class AddToCart(View):
    def get(self, request):
        pass

    def post(self, request):
        product_id = request.POST.get('product_id')
        product = ProductModel.objects.get(id=product_id)
        cart = CartModel.objects.get_or_create(
            user = request.user,
            products = (product_id, )
        )
        cart[0].products.add(product)

        return redirect(reverse_lazy('home'))