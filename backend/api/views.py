import json
from django.shortcuts import render
from django.forms.models import model_to_dict
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields = ['id', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price
#         data = model_to_dict(model_data, fields = ['id', 'title', 'price'])
#     return JsonResponse(data)


# def api_home(request, *args, **kwargs):
#     body = request.body     #byte string of JSON data OR stringified version of JSON object
#     # print(body)
#     print(request.GET)
#     print(request.POST)
#     data = {}
#     try:
#         data = json.loads(body)     # string of JSON data -> Python Dict
#     except:
#         pass
#     print(data)
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     # return JsonResponse({"message":"Hi there, this is your Django API response!!"})
#     return JsonResponse(data)