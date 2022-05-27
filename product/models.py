from django.db import models
from django.contrib.auth.models import User

# Create your models here.   (database data)


class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class UnitModel(models.Model):
    base_unit = models.CharField(max_length=100)
    secondary_unit = models.CharField(max_length=100)
    conversion_ratio = models.FloatField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.base_unit


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(
        upload_to="image/product/",
        blank=True, null=True,
        default="default/product.png"
    )

    description = models.TextField(max_length=200,
                                   blank=True, null=True)

    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.SET_NULL,null=True,blank=True)
    unit = models.ForeignKey(UnitModel,
                             on_delete=models.SET_NULL,null=True,blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class ReviewModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    rating = models.FloatField()
    rated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.rating)

class CartModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  
    products = models.ManyToManyField(ProductModel, blank=True)
    total =  models.FloatField(default=0)
    updated_on = models.DateTimeField(auto_now=True)
    status =   models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.total = self.get_total()

    def __str__(self) -> str:
        return str(self.total)

    # def get_total(self):
    #     total = 0
    #     for product in self.products:
    #         total += product.price * self.products.count(product)

    #     return float(total)