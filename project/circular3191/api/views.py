# import models and serializers
from .serializer import ProjectCreateSerializer , SubprojectCreateSerializer , ProjectViewSerializer , SubprojectViewSerializer
from circular3191.models import Project , Subproject
from rest_framework import generics, serializers
from ..views import circular3191




class ProjectCreateAPIView (generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    
  

class SubprojectCreateAPIView (generics.ListCreateAPIView):
    queryset = Subproject.objects.all()
    serializer_class = SubprojectCreateSerializer

   
# -------------------------------------------------------------------------

class ProjectListAPIView (generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectViewSerializer


class SubprojectListAPIView (generics.ListAPIView):

    def __init__(self) :
        circ = circular3191()
        print('calstorage',circ[0])
        print('finalfinal',circ[1])


    queryset = Subproject.objects.all()
    serializer_class = SubprojectViewSerializer





