from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

import requests
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!!")


def show(request):
    # api_url = request.build_absolute_uri(reverse("graphql",))
    api_url = "http://127.0.0.1:8000/graphql"

    graphql_query = """
    {
     allIngredients {
         id
         name
     }   
    }
    """
    payload = {"query": graphql_query}
    response = requests.post(api_url, json=payload)
    data = response.json()

    print("===" * 10)
    print(data["data"]["allIngredients"][0]["name"])

    return HttpResponse(data)


"""
query {
  allIngredients {
    id
    name
    category {
      id
      name
    }
  }
}

"""
