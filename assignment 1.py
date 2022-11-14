''' This program calculates user's iron deficiency based on user's age, 
weight and gender for user's last 4 lab results of  hg levels using 
'Ganzoni equation' and guesses the number of days the user should take
iron supplement to treat defiency. '''

def iron_deficiency(age, weight,gender, hgLevel):
    # This for loop iterate through user's last 4 lab result of hg Level
    for i in hgLevel:
        #this if statement checks if the user's hg level is less than 119 g/L
        #nested if-statements
        if i < 119: # 119 considered  low iron deficiency  for children under 18 years old
            
            if  weight < 35: # based on Ganzoni's equation if weight is under 35 kg
                             # calculation for iron stores differs.
                target = 140 # this value is avreage target hg level for children under 18
                iron_stores = 15 * weight
                # Ganzoni's Equation
                deficiency = int(weight * (target - i) * 0.24 +  iron_stores) 
                print( 'If your hg level is',i,',you have iron deficiency of' ,deficiency , 'mg')
                
            else: # if user weighs more than 35 kg, the iron store amount is fixed.
                target = 140
                iron_stores = 500
                deficiency = int(weight * (target - i) * 0.24 +  iron_stores)
                print( 'If your hg level is',i,',you have iron deficiency of' ,deficiency , 'mg')
                   
        elif 119 < i <135: # 135 g/L is considered iron deficiency for people older than 18 years old
            if age < 18: #if the user is younger than 18, anything more than 119 g/l iron is adaquent
                         #regardless of their gender.
                deficiency = 0
                print('If your hg level is',i,',you have adequate iron in your blood.')
            else:
                #this condition checks whether the user is female or male
                if gender == 'female': #the target hg Level differs between female and male if they're older than 18 
                    target =160 #average target hg level for females in g/L
                    iron_stores = 500
                    deficiency = int(weight * (target - i) * 0.24 +  iron_stores)
                    print( 'If your hg level is',i,',you have iron defiency of' ,deficiency , 'mg')
                    
                else: #condition is not met, so user's gender is male
                    target = 170 #average target hg level for males in g/L
                    iron_stores = 500
                    deficiency = int(weight * (target - i) * 0.24 +  iron_stores)
                    print( 'If your hg level is',i,',you have iron deficiency of' ,deficiency , 'mg')
        
        # this else statement is for hg levels greater than 135 g/L            
        else: 
            deficiency = 0 #any hg level greater than 135 is enough for adults
            print ('If your hg level is',i,',you have adequate iron in your blood.')
        # this adds all deficiency values to list called 'value'
        value.append(deficiency) 
    # prints the value list
    print (value) 
    # this for loop calculates iterate through value list and calculates 
    #the number of days the user should take iron supplement to treat deficiency.
    for a in value:
        # this condition makes sure the computer only calculates for if user
        # has deficiency
        if a > 0:
            # the prescribed amount will vary based on many different factors
            #however the average amount for daily oral intake is 18 mg tablet
            print('For deficiency of',a,'mg you need to take one 18 mg tablet iron for', a//18 , 'days. ')
        



if __name__ == "__main__":
    value =[] #empty now, but append funtion will add all deficiency values
    age = int(input ('Please enter your age: ')) #convert string ex. to integer
    weight = int(input('Please enter your weight in kg : '))
    gender = input('Please enter your gender: ').lower 
    # lower function will make user's input lower so we don't have to worry
    # about capitalization
    hgL_1 = int(input('Please enter your hgLevel in first lab result: '))
    hgL_2 = int(input('Please enter your hgLevel in second lab result: '))
    hgL_3 = int(input('Please enter your hgLevel in third lab result: '))
    hgL_4 = int(input('Please enter your hgLevel in fourth lab result: '))
    hgLevel = [hgL_1 ,hgL_2, hgL_3, hgL_4] 
    #list of hg levels that first for loop iterate through
    #finally we are calling the function with 4 parameters age,weight,gender, hgLevel
    iron_deficiency (age,weight,gender, hgLevel )
    



