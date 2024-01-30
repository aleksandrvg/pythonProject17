from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def FirstGet(request):
    if request.method == "GET":
        return Response({"message": "My first get request"})
@api_view(["POST"])
def FirstPost(request):
    if request.method == "POST":
        level = ['B3', 'B4']
        data = request.data
        print(data)
        if int(data["age"]) > 25 and data["language"] in level:
            return Response(f"{data["name"]} вы подходите")
        else:
            return Response(f"{data["name"]} вы не подходите")