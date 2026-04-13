from django.shortcuts import render
from .models import Category, Tag, Product

def product_list(request):
    products = Product.objects.all()

    description = request.GET.get("description")
    category = request.GET.get("category")
    tag = request.GET.getlist("tag")

    if description:
        products = products.filter(
            description__icontains=description
        )
    if category:
        products = products.filter(
            category_id = category
        )
    if tag:
        for tag_id in tag:
            products = products.filter(
                tag__id=tag_id
            )

    # Pass the data to the template
    context = {
        "products": products,
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),

        # Keeping the value after user submitted
        "selected_tag": tag,
        "selected_category": category,
        "description": description or "",

    }

    return render(request, "products/product_list.html", context)

