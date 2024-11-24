from django.shortcuts import render, get_object_or_404
from .models import PostProduct, Review

def buy_tshirt(request):
    posted_products = PostProduct.objects.all()
    return render(request, 'BuyT-Shirts.html', {'posted_products': posted_products})

def men(request):
    men_products = PostProduct.objects.all()
    return render(request, 'Men.html', {'men_products': men_products})

def women(request):
    women_products = PostProduct.objects.all()
    return render(request, 'Women.html', {'women_products': women_products})

def shopping_cart(request):
    return render(request, 'ShoppingCart.html')

def product_details(request, post_id):
    posted_product = get_object_or_404(PostProduct, pk=post_id)
    customer_comment = request.POST.get('customer-comment')
    customer_name = request.POST.get('customer-name')
    customer_email = request.POST.get('customer-email')
    customer_review = Review(customer_comment=customer_comment, customer_name=customer_name, customer_email=customer_email, product_name=posted_product.name)
    if request.method == "POST":
        customer_review.save()
    return render(request, 'Product.html', {'posted_product':posted_product})