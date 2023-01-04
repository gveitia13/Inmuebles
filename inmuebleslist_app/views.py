# from django.forms import model_to_dict
# from django.http import HttpRequest, JsonResponse
# from django.shortcuts import render
#
# from inmuebleslist_app.models import Inmueble
#
#
# def inmueble_list(request: HttpRequest):
#     inmuebles = Inmueble.objects.all()
#     data = {
#         'inmuebles': list(inmuebles.values()),
#     }
#     return JsonResponse(data)
#
#
# def inmueble_details(request: HttpRequest, pk: int):
#     inmueble = Inmueble.objects.get(pk=pk)
#     data = model_to_dict(inmueble)
#     return JsonResponse(data)
