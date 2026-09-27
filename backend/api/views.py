import json
from django.http import JsonResponse
from products.models import Product
def api_home(request, *args, **kwargs):
    data = {}
    model_data = Product.objects.all().order_by("?").first()
    if model_data:
        data = {
            "id": model_data.id,
            "title": model_data.title,
            "content": model_data.content,
            "price": str(model_data.price),
        }
    return JsonResponse(data)