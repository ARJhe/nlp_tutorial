from django.shortcuts import render
from django.http import JsonResponse
from gensim import models
from . import seman
import jieba



def home(request):
    return render(request, 'seman/home.html')


def semantic_output(request):
    if request.is_ajax and request.method == "GET":
        query = request.GET.get("input", None)
        output = str(jieba.lcut(query))
        # output = seman.analysis(query)
        return JsonResponse({"output": output}, status=200)