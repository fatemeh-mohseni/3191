from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.TextField()
    def __str__(self) :
        return self.project_name


class Subproject(models.Model):
    
    '''
    Make a note of the related_field = “subproject" attribute.
    This is required for the serializer for Product to get access to the related subproject.
    In fact, when defining serializer, you will need to use the same exact name as 
    related_field in your serializer field
    '''
    
    project = models.ForeignKey(Project , on_delete=models.CASCADE ,
    related_name='subprojects')  # **** #
# raw info
    #user_id = models.IntegerField()
    subproject_name = models.CharField(max_length=100 , null=False , blank=False)
    group = models.IntegerField()
    repetition = models.IntegerField()
    cost_per_meter = models.FloatField(null=True)
    area = models.FloatField(null=True)
    initial_estimate = models.FloatField(null=True)
# calinfo
    fee_step_one_first_part = models.CharField(max_length=20)
    fee_step_one_second_part = models.CharField(max_length=20)
    fee_step_two = models.CharField(max_length=20)
    fee_step_three = models.CharField(max_length=20)
    fee_final = models.CharField(max_length=20)