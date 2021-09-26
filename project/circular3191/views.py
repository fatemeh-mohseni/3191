from typing import final
from django.db.models.expressions import Value
from django.http import request, response
from django.shortcuts import redirect, render
from .calculate import Final ,Percentage_of_reduction_in_fees,Step_based_fees
from .models import Project,Subproject
from .forms import Input_form



# store raw data collected from input
rawstorage={}  # store raw data
calstorage={}  # store calculated data



#def circular3191(request):
def circular3191():     
    finalfinal = None


    #   render the  main circular page
    #   connect to right function

    #if request.method == 'POST':
    #   create a form instance and populate it with data from the request:    
        #global form
        #form = Input_form(request.POST or None)
    
        #if form.is_valid():
           
    global project_name,building_name,group,repetition,cost_per_meter,area,initial_estimate

        #project_name = form.cleaned_data['project_name']
        #building_name = form.cleaned_data['building_name']
        #group = form.cleaned_data['group']
        #repetition = form.cleaned_data['repetition']
        #cost_per_meter = form.cleaned_data['cost_per_meter']
        #area = form.cleaned_data['area']
        #initial_estimate = form.cleaned_data['initial_estimate']

    project_name = Project.objects.last()
    building_name = Subproject.objects.last().subproject_name
    group = Subproject.objects.last().group
    repetition = Subproject.objects.last().repetition
    cost_per_meter = Subproject.objects.last().cost_per_meter
    area = Subproject.objects.last().area
    initial_estimate =Subproject.objects.last().initial_estimate





    # select wich function should be called 

        #if len(request.POST.getlist('calculate')) == 0 : # new subproject has been called # 'calculate is the name of input tag
        #        calculate()              
        #        new_subproject()
    # select calculate funcrion             
        #else:
        #        calculate()
        #        finalfinal = Fee()
        #        finalfinal=str(finalfinal.Cal_Fee())
        #        print('finalfinal @@@@@@@@@@@@',finalfinal)


    #else:
    #    form = Input_form()
    
    calculate()
    finalfinal = Fee()
    finalfinal=str(finalfinal.Cal_Fee())
    store_in_db(calstorage)

    return (calstorage , finalfinal)
    #return render(request, 'circulars3191/main1.html',{'form':form , 'rawstorage':rawstorage , 'calstorage':calstorage , 'finalfinal':finalfinal})

# ---------------------------



class collect_store_raw_input():

    def __init__(self) :
        
        input_info = {                  
                'building_name': building_name ,                   
                'project_name':project_name ,                   
                'group':group,                  
                'repetition':repetition ,                     
                'initial_estimate':initial_estimate ,                   
                'area':area ,                   
                'cost':cost_per_meter                     
        }

        collect_store_raw_input.store(input_info)

# store locally
    @staticmethod
    def store(input_info):
        key = input_info['building_name']
        rawstorage[key] = input_info


# ---------------------------

def store_calculated_data(caldata):
    # store data based on subproject names
    # each caldata or calculated data is a dict of calculated datas just for one building based on its group
    name = caldata['building_name'] 
    calstorage[name] = caldata

# ---------------------------

def store_in_db(calstorage) :
    for key,value in calstorage.items() :
        record = Subproject.objects.get(subproject_name=key)
        record.fee_step_one_first_part = value['fee_step_one_first_part']
        record.fee_step_one_second_part = value['fee_step_one_second_part']
        record.fee_step_two = value['fee_step_two']
        record.fee_step_three = value['fee_step_three']
        record.fee_final = value['fee_final']
        record.save()
# ---------------------------
def new_subproject():
    
    collect_store_raw_input()

# ---------------------------


def calculate():

    collect_store_raw_input()  #locally stored

    # lets start calculate
    # first send data of each building to be calculated 
    for key,value in rawstorage.items():
        final = Final(value) 
        output = Final.for_return()
    # second send calculated data to be stored
        store_calculated_data(output)


   # show_tables(request)      
        #store_calculated_data(output)


#This is a restriction of HTTP that POST data cannot go with redirects.
   
  

#def show_tables(request):
#
#    return render(request,'circulars3191/show.html',calstorage)
#    




#  ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
#                                     whole                                    #   



class Fee():


    def Average_orif(self):
        soorat = 0
        cost_sum = 0
        for key , value in calstorage.items() :
            

            p=Percentage_of_reduction_in_fees()
            soorat+=float(value['building_cost'])*float(p.percentage_of_reduction_in_fees(float(value['building_cost'])))
            cost_sum+=float(value['building_cost'])
        
        try:
            final = float( 0.5 * ((soorat/cost_sum)+float(p.percentage_of_reduction_in_fees(float(cost_sum)))) )
            return final
        except:
            pass

        


    def Cal_Fee(self):
        
        '''
        lets cal formula NO.2 here

        '''
        
    # first sort building base on group            
        group1 = {}
        group2 = {}
        group3 = {}
        group4 = {}

        for key , value in calstorage.items() :
            if value['building_group'] == 1:
                group1[key] = value

            elif value['building_group'] == 2:
                group2[key] = value


            elif value['building_group'] == 3:
                group3[key] = value


            elif value['building_group'] == 4:
                group4[key] = value


        cost1 , cost2 , cost3 , cost4 = 0,0,0,0    
        for key , value in group1.items() :
            cost1 += float(value['building_cost'])
        for key , value in group2.items() :
            cost2 += float(value['building_cost'])
        for key , value in group3.items() :
            cost3 += float(value['building_cost'])
        for key , value in group4.items() :
            cost4 += float(value['building_cost'])

        mini_final = 0

        mini1=float(Step_based_fees.step_based_fees(self,1)[0]) * cost1
        mini2=float(Step_based_fees.step_based_fees(self,2)[1]) * cost2
        mini3=float(Step_based_fees.step_based_fees(self,3)[2]) * cost3
        mini4=float(Step_based_fees.step_based_fees(self,4)[3]) * cost4

        mini_final = mini1 + mini3 + mini2 + mini4

        finalfinal = mini_final * self.Average_orif()
        return finalfinal

    
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------              
