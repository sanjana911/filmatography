from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from actors.models import Actors
# Create your views here.

@method_decorator(csrf_exempt, name="dispatch")
class ActorView(View):

    def get(self,request):

        qs = Actors.objects.all().values()

        response_data = list(qs)

        return JsonResponse(response_data,safe=False)

    def post(self,request):

        form_data =loads(request.body)

        Actors.objects.create(**form_data)

        response_data ={"message":"created.."}

        return JsonResponse(response_data)


@method_decorator(csrf_exempt, name="dispatch")
class ActorRetrieveUpdateDeleteView(View):

    def get(self,request, pk = None):

        instance = Actors.objects.filter(id= pk).values()

        response_data = list(instance)

        return JsonResponse(response_data ,safe=False)

    def put(self,request, pk = id):

        form_data = loads(request.body)

        Actors.objects.filter(id = pk).update(**form_data)

        response_data ={"message":"update actor.."}

        return JsonResponse(response_data)

    def delete(self,request, pk = None):

        Actors.objects.get(id = pk).delete()

        response_data = {"message":"actor deleted.."}

        return JsonResponse(response_data)

