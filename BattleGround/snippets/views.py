from .models import Cube, Rectangle
from requests import Response
from django.conf import settings
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect
import json
import os
# Create your views here.
@api_view()
def index(request):
    cubes = Cube.objects.all()
    rectangles = Rectangle.objects.all()
    data = []
    cube_data = []
    rectangle_data = []
    for cube in cubes:
        cube_data.append({"name":cube.name,
                          "length":cube.length,
                          "x_coordinate":cube.x_coordinate,
                          "y_coordinate":cube.y_coordinate,
                          "z_coordinate":cube.z_coordinate,
                          "texID":cube.texID,
                          "mass":cube.mass})
    for rectangle in rectangles:
        rectangle_data.append({"name": rectangle.name,
                               "length": rectangle.length,
                               "breadth":rectangle.breadth,
                                "x_coordintate": rectangle.x_coordinate,
                                "y_coordinate": rectangle.y_coordinate,
                                "z_coordinate": rectangle.z_coordinate,
                                "texID": rectangle.texID,
                                "mass": rectangle.mass,
                                "orientation":rectangle.orientation})
    data = [{"cube": [cube_data],"rectangle": [rectangle_data]}]
    return Response(data)

def download(request):
    cubes = Cube.objects.all()
    rectangles = Rectangle.objects.all()
    data = []
    cube_data = []
    rectangle_data = []
    for cube in cubes:
        cube_data.append({"name": cube.name,
                          "length": cube.length,
                          "x_coordinate": cube.x_coordinate,
                          "y_coordinate": cube.y_coordinate,
                          "z_coordinate": cube.z_coordinate,
                          "texID": cube.texID,
                          "mass": cube.mass})
    for rectangle in rectangles:
        rectangle_data.append({"name": rectangle.name,
                               "length": rectangle.length,
                               "breadth": rectangle.breadth,
                               "x_coordintate": rectangle.x_coordinate,
                               "y_coordinate": rectangle.y_coordinate,
                               "z_coordinate": rectangle.z_coordinate,
                               "texID": rectangle.texID,
                               "mass": rectangle.mass,
                               "orientation": rectangle.orientation})
    data = [{"cube": [cube_data], "rectangle": [rectangle_data]}]
    file_path =  os.path.join(settings.MEDIA_ROOT, "res.json")
    with open(file_path, "w") as f:
        f.write(json.dumps(data))
    return HttpResponseRedirect('/')


def home(request):
    return render(request,'snippets/index.html')