
#   to insert data and get what we need , just run Final_per_building
#from start import app as app1

class Building():
     
    '''

    Each project contains number of buildings .
    Each building has some features :

    name                ( name of building )
    group               ( group number) 
    repetation          ( number of reapetation of that building)
    area                ( area of buiding )
    cost                ( cost of buiding per meter)
    initial estimate    ( direct cost , inserted by customer )
    
    note that cost = initial estimate


    map of code -----
                    |
                    |
                    |
                   \ /


                 Building
                    |
                    |
        ------------------------------------------------------------------
        |          |                     |                               |
        |          |                     |                               |
       \ /        \ /                   \ /                             \ / 
      Final  Step_based_fees   Repeatition_coefficient    Percentage_of_reduction_in_fees

(calculate                          درصد کاهش حق الزحمه             ضریب تکرار                    
    answer)


    '''
    
    name = None     #  building name not proj. name 
    group = None
    repetition = None
    area = None
    cost = None # قیمت هر متر زمین است اما در اخر به براورد نهایی تبدیل میشود
    initial_estimate = None

    counter = 0

    def __init__(self , name= None , group= None  , repetition= None , area = None , cost = None , initial_estimate = None  ):
        
        '''
        
        collect whatever is needed
        
        '''

       
        def answer () :

            final=Final_per_building()


# -----------------------------------------------------------------------------

class Step_based_fees (Building) :

    '''
    
    درصد حق ازحمه خدمات مراحل 1و2و3
    
    '''

    def step_based_fees(self,group) :
        
        step_one_second_part = None
        step_one_first_part = None
        step_two = None
        step_three = None
        final = None
        if group == 1 :
        
            step_one_second_part,step_one_first_part = 0.85 , 0.85    # step 1 
        
            step_two = 3.41 
        
            step_three = 1.71
        
            final = 6.82

        elif group == 2 :
        
            step_one_second_part,step_one_first_part = 1.03 , 1.03  # step 1   
        
            step_two = 4.11
        
            step_three = 2.05

            final = 8.22

        elif group == 3 :
        
            step_one_second_part,step_one_first_part = 1.24 , 1.24  # step 1 
        
            step_two = 4.98
        
            step_three = 2.49

            final = 9.95

        elif group == 4 :
        
            step_one_second_part,step_one_first_part = 1.51 , 1.51  # step 1 
        
            step_two = 6.04
        
            step_three = 3.02

            final = 12.08


        return step_one_first_part , step_one_second_part , step_two , step_three , final


# -----------------------------------------------------------------------------

class Repeatition_coefficient (Building):
    
    '''
    
    ضریب تکرار
    
    '''

    @staticmethod
    def interpolation(x1,x2,y1,y2,x) :

    # intertpolation way of calculate Percentage of reduction in fees

        a = (y2-y1)/(x2-x1)
        b = y1-(a*x1)

        percentage = round((a*x + b),2)


        return percentage


    def repeatition_coefficient(self):

        if self.repetition == 2 :
            repeatition_coefficient = 67.5

        elif self.repetition == 3 :
            repeatition_coefficient = 53.52

        elif self.repetition == 4 :
            repeatition_coefficient = 47.47

        elif self.repetition == 5 :
            repeatition_coefficient = 42.89

        elif self.repetition == 6 :
            repeatition_coefficient = 39.63

        elif self.repetition == 7 :
            repeatition_coefficient = 37.16

        elif self.repetition == 8 :
            repeatition_coefficient = 35.22

        elif self.repetition == 9 :
            repeatition_coefficient = 33.64

        elif self.repetition == 10 :
            repeatition_coefficient = 32.33

        elif self.repetition == 11 :
            repeatition_coefficient = 31.23

        elif self.repetition == 12 :
            repeatition_coefficient = 30.27

        elif self.repetition == 13 :
            repeatition_coefficient = 29.43

        elif self.repetition == 14 :
            repeatition_coefficient = 28.19

        elif self.repetition == 15 :
            repeatition_coefficient = 28.03

        elif self.repetition == 16 :
            repeatition_coefficient = 27.25

        elif self.repetition == 17 :
            repeatition_coefficient = 26.92

        elif self.repetition == 18 :
            repeatition_coefficient = 26.44

        elif self.repetition == 19 :
            repeatition_coefficient = 26.00

        elif self.repetition == 20 :
            repeatition_coefficient = 25.6

        elif self.repetition == 25 :
            repeatition_coefficient = 23.99

        elif self.repetition == 30 :
            repeatition_coefficient = 22.83

        elif self.repetition == 35 :
            repeatition_coefficient = 21.97

        elif self.repetition == 40 :
            repeatition_coefficient = 21.29

        elif self.repetition == 45 :
            repeatition_coefficient = 20.74

        elif self.repetition == 50 :
            repeatition_coefficient = 20.28

        elif self.repetition == 60 :
            repeatition_coefficient = 19.56

        elif self.repetition == 70 :
            repeatition_coefficient = 19.02

        elif self.repetition == 80 :
            repeatition_coefficient = 18.6

        elif self.repetition == 90 :
            repeatition_coefficient = 18.27

        elif self.repetition == 100 :
            repeatition_coefficient = 18.00
    # Intermediate values
        else:
            if 20< self.repetition <25 :
                repeatition_coefficient = self.interpolation(20,25,25.6,23.99,self.repetition)

            elif 25< self.repetition <30 :
                repeatition_coefficient = self.interpolation(25,30,23.99,22.83,self.repetition)

            elif 30< self.repetition <35 :
                repeatition_coefficient = self.interpolation(30,35,22.83,21.97,self.repetition)

            elif 35< self.repetition <40 :
                repeatition_coefficient = self.interpolation(35,40,21.97,21.29,self.repetition)

            elif 40< self.repetition <45 :
                repeatition_coefficient = self.interpolation(40,45,21.29,20.74,self.repetition)

            elif 45< self.repetition <50 :
                repeatition_coefficient = self.interpolation(45,50 ,20.74, 20.28,self.repetition)

            elif 50< self.repetition <60 :
                repeatition_coefficient = self.interpolation(50,60,20.28,19.56,self.repetition)

            elif 60< self.repetition <70 :
                repeatition_coefficient = self.interpolation(60,70,19.56,19.02,self.repetition)

            elif 70< self.repetition <80 :
                repeatition_coefficient = self.interpolation(70,80,19.02,18.6,self.repetition)

            elif 80< self.repetition <90 :
                repeatition_coefficient = self.interpolation(80,90,18.6,18.27,self.repetition)

            elif 90< self.repetition <100 :
                repeatition_coefficient = self.interpolation(90,100,18.27,18,self.repetition)    



        return float(repeatition_coefficient)  #turn coefficient number to percent

# -----------------------------------------------------------------------------

class Percentage_of_reduction_in_fees(Building) :
    
    '''
    
    (درصد کاهش حق الزحمه)
    cost = The cost of each building (هزینه هر ساختمان)(in million Rial)
    percentage = Percentage of reduction in fees  (درصد کاهش حق الزحمه)

    '''

    @staticmethod
    def interpolation(x1,x2,y1,y2,x) :

    # intertpolation way of calculate Percentage of reduction in fees

        a = (y2-y1)/(x2-x1)
        b = y1-(a*x1)

        percentage = round((a*x + b),2)


        return float(percentage)

    
    def percentage_of_reduction_in_fees(self,cost) :
        percentage = None

        if cost <= 50 :
            percentage = 100 

        elif cost == 100 :
            percentage = 87.28


        elif cost == 200 :
            percentage = 81.71


        elif cost == 300 :
            percentage = 78.14


        elif cost == 400 :
            percentage = 75.51


        elif cost == 500 :
            percentage = 73.42


        elif cost == 600 :
            percentage = 71.68


        elif cost == 700 :
            percentage = 70.2


        elif cost ==  800:
            percentage = 68.9


        elif cost == 900 :
            percentage =67.75


        elif cost == 1000 :
            percentage = 66.71


        elif cost == 1500 :
            percentage = 62.7


        elif cost == 2000 :
            percentage = 59.85


        elif cost == 2500 :
            percentage = 57.44


        elif cost == 3000 :
            percentage = 55.85


        elif cost == 3500 :
            percentage = 54.3


        elif cost == 4000 :
            percentage = 53.02


        elif cost == 4500 :
            percentage = 51.87


        elif cost == 5000 :
            percentage = 50.84


        elif cost == 6000 :
            percentage = 49.09


        elif cost == 7000 :
            percentage = 47.62


        elif cost == 8000 :
            percentage = 46.36


        elif cost == 9000 :
            percentage = 45.26


        elif cost == 10000 :
            percentage = 44.28


        elif cost == 11000 :
            percentage = 43.4


        elif cost == 12000 :
            percentage = 42.61


        elif cost == 13000 :
            percentage = 41.88


        elif cost == 14000 :
            percentage = 41.22


        elif cost == 15000 :
            percentage = 40.6


        elif cost == 20000 :
            percentage = 38.07


        elif cost == 25000 :
            percentage = 36.17


        elif cost == 30000 :
            percentage = 34.65


        elif cost == 35000 :
            percentage = 33.39


        elif cost == 40000 :
            percentage = 32.32


        elif cost == 45000 :
            percentage = 31.39


        elif cost == 50000 :
            percentage = 30.57


        elif cost == 60000 :
            percentage = 29.19


        elif cost == 70000 :
            percentage = 28.05


        elif cost == 80000 :
            percentage = 27.08


        elif cost == 90000 :
            percentage = 26.25


        elif cost == 100000 :
            percentage = 25.52

    # cost is between two Specified value

        else:
            if 50 < cost <100 :
                percentage = self.interpolation(50,100,100,87.28,cost)

            if 100 < cost <200 :
                percentage = self.interpolation(100,200,87.28,81.71,cost)


            if 200 < cost <300 :
                percentage = self.interpolation(200,300,81.71,78.14,cost)


            if 300 < cost < 400:
                percentage = self.interpolation(300,400,78.14,75.51,cost)


            if 400 < cost < 500:
                percentage = self.interpolation(400,500,75.51,73.42,cost)


            if 500 < cost <600 :
                percentage = self.interpolation(500,600,73.42,71.68,cost)


            if 600 < cost <700 :
                percentage = self.interpolation(600,700,71.68,70.2,cost)


            if 700 < cost < 800:
                percentage = self.interpolation(700,800,70.2,68.9,cost)


            if 800 < cost <900 :
                percentage = self.interpolation(800,900,68.9,67.75,cost)


            if 900 < cost <1000 :
                percentage = self.interpolation(900,1000,67.75,66.71,cost)


            if 1000 < cost <1500 :
                percentage = self.interpolation(1000,1500,66.71,62.7,cost)


            if 1500 < cost <2000 :
                percentage = self.interpolation(1500,2000,62.7,59.85,cost)


            if 2000 < cost <2500 :
                percentage = self.interpolation(2000,2500,59.85,57.44,cost)


            if 2500 < cost <3000 :
                percentage = self.interpolation(2500,3000,36.17,34.65,cost)


            if 3000 < cost <3500 :
                percentage = self.interpolation(3000,3500,55.85,54.3,cost)


            if 3500 < cost <4000 :
                percentage = self.interpolation(3500,4000,54.3,53.02,cost)


            if 4000 < cost <4500 :
                percentage = self.interpolation(4000,4500,53.02,51.87,cost)


            if 4500 < cost <5000 :
                percentage = self.interpolation(4500,5000,51.87,50.84,cost)


            if 5000 < cost <6000 :
                percentage = self.interpolation(5000,6000,50.84,49.09,cost)


            if 6000 < cost <7000 :
                percentage = self.interpolation(6000,7000,49.09,47.62,cost)


            if 7000 < cost <8000 :
                percentage = self.interpolation(7000,8000,47.62,46.36,cost)


            if 8000 < cost <9000 :
                percentage = self.interpolation(8000,9000,46.36,45.26,cost)


            if 9000 < cost <10000 :
                percentage = self.interpolation(9000,10000,45.26,44.28,cost)


            if 10000 < cost <11000 :
                percentage = self.interpolation(10000,11000,44.28,43.4,cost)


            if 11000 < cost <12000 :
                percentage = self.interpolation(11000,12000,43.4,42.61,cost)


            if 12000 < cost <13000 :
                percentage = self.interpolation(12000,13000,42.61,41.88,cost)


            if 13000 < cost <14000 :
                percentage = self.interpolation(13000,14000,41.88,41.22,cost)


            if 14000 < cost <15000 :
                percentage = self.interpolation(14000,15000,41.22,40.6,cost)


            if 15000 < cost <20000 :
                percentage = self.interpolation(15000,20000,40.6,38.07,cost)


            if 20000 < cost <25000 :
                percentage = self.interpolation(20000,25000,38.07,36.17,cost)


            if 25000 < cost <30000 :
                percentage = self.interpolation(25000,30000,36.17,34.65,cost)


            if 30000 < cost <35000 :
                percentage = self.interpolation(30000,35000,34.65,33.39,cost)


            if 35000 < cost <40000 :
                percentage = self.interpolation(35000,40000,33.39,32.32,cost)


            if 40000 < cost <45000 :
                percentage = self.interpolation(40000,45000,32.32,31.39,cost)


            if 45000 < cost <50000 :
                percentage = self.interpolation(45000,50000,31.39,30.57,cost)


            if 50000 < cost <60000 :
                percentage = self.interpolation(50000,60000,30.57,29.19,cost)


            if 60000 < cost <70000 :
                percentage = self.interpolation(60000,70000,29.19,28.05,cost)


            if 70000 < cost <80000 :
                percentage = self.interpolation(70000,80000,28.05,27.08,cost)


            if 80000 < cost <90000 :
                percentage = self.interpolation(80000,90000,27.08,26.25,cost)


            if 90000 < cost <100000 :
                percentage = self.interpolation(90000,100000,26.25,25.52,cost)


            if 11000 < cost <12000 :
                percentage = self.interpolation(11000,12000,43.4,42.61,cost)


            if 11000 < cost <12000 :
                percentage = self.interpolation(11000,12000,43.4,42.61,cost)


        return float(percentage)



# -----------------------------------------------------------------------------


class Final_per_building (Building) :

    global fee_step_one_first_part , fee_step_one_second_part , fee_step_two , fee_step_three , fee_final
    fee_step_one_first_part = None
    fee_step_one_second_part = None
    fee_step_two = None
    fee_step_three = None
    fee_final = None

    def __init__(self, name, group, repetition, cost):
        
        global name1 ,cost1,group1
        name1 = name
        cost1 = cost
        group1 = group

        #   porinf stands for Percentage_of_reduction_in_fees
        porinf=Percentage_of_reduction_in_fees(name , group , repetition  , cost )
        porinf=porinf.percentage_of_reduction_in_fees(cost) ###########
        
        
        #    درصد حق ازحمه خدمات مراحل 1و2و3

        step_based_fees=Step_based_fees(name , group , repetition )
        step_based_fees=list(step_based_fees.step_based_fees(group)) ##############

        # ----------------------------------------------------- #

        self.fee_step_one_first_part = cost * porinf * float(step_based_fees[0])
        self.fee_step_one_second_part = cost * porinf * float(step_based_fees[1])
        self.fee_step_two = cost * porinf * float(step_based_fees[2])
        self.fee_step_three = cost * porinf * float(step_based_fees[3])
        self.fee_final = cost * porinf * float(step_based_fees[4])

        # round up to 5 digits after comma
        self.fee_step_one_first_part = "{:,.5f}".format(self.fee_step_one_first_part)
        self.fee_step_one_second_part = "{:,.5f}".format(self.fee_step_one_second_part)
        self.fee_step_two = "{:,.5f}".format(self.fee_step_two)
        self.fee_step_three = "{:,.5f}".format(self.fee_step_three)
        self.fee_final = "{:,.5f}".format(self.fee_final)



    def information(self,name) :

        '''
        
finall fee for each group
ready to insert in table
        
        '''


        info = 'information of building '+ name1

        info={
            'building_name':name1 ,
        'building_group':group1 ,
        'building_cost':cost1 ,
        'fee_step_one_first_part':self.fee_step_one_first_part , 
        'fee_step_one_second_part':self.fee_step_one_second_part ,
        'fee_step_two':self.fee_step_two ,
        'fee_step_three':self.fee_step_three , 
        'fee_final':self.fee_final
        }

        
        return info


# -----------------------------------------------------------------------------

    

class Final():
    
    
    def __init__(self,dict_info):

        global name , group , reapetation , cost


        name = dict_info['building_name']
        group = int(str(dict_info['group'])[-1])
        reapetation = int(dict_info['repetition'])

        try :    
            initial_estimate = float(dict_info['initial_estimate'])
            self.initial_estimate = initial_estimate
            cost = initial_estimate

        except :
            initial_estimate = None
        try :
            area = float(dict_info['area'])
            self.area = area
        except :
            area = None
        try :
            cost = float(dict_info['cost'])
            cost = cost * area 
            self.cost = cost

        except :
            pass


        self.name = name
        self.group = group
        self.repetition = reapetation
        

    @staticmethod
    def for_return():
        
        final_per_building = Final_per_building(name, group, reapetation, cost)
        output=( final_per_building.information(name))
        
        return output

    



# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
#input_info = {                  
#            'building_name':'hhhhhhhh' ,                   
#            'project_name':'gtfdhdgtht' ,                   
#            'group':3,                  
#            'repetition':1 ,                     
#            'initial_estimate':350 ,                   
#            'area':None ,                   
#            'cost':None                     
#    }                       
#final=Final(input_info)
#print(Final.for_return())
#       
#