from typing import get_args
from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer , RelatedField
from circular3191.models import Project , Subproject
from django.contrib.sessions.models import Session


# -------------------------------------------------------------------------
# API for catch data
class SubprojectCreateSerializer (ModelSerializer):
    class Meta :
        model = Subproject 
        fields = ('project', 'subproject_name','group', 'repetition' , 'cost_per_meter' , 'area' , 'initial_estimate')


class ProjectCreateSerializer (ModelSerializer):
  
    subprojects = RelatedField(many=True , read_only=True)
    class Meta :
        model = Project 
        fields = '__all__' 
   
# -------------------------------------------------------------------------
# API for show data
class SubprojectViewSerializer (ModelSerializer) :
    class Meta :
        model = Subproject
        fields = ('subproject_name' , 'fee_step_one_first_part' , 'fee_step_one_second_part' , 'fee_step_two' , 'fee_step_three' , 'fee_final')

class ProjectViewSerializer (ModelSerializer) :
    class Meta :
        model = Project
        fields = '__all__'
# -------------------------------------------------------------------------






