#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BMI Calculator

def bmi_cal():
    print(" My BMI calculator!")
    print("I can tell you your weight and height")
    print("I can tell you your Body Mass Index")
    print("Let's Go!\n")
    
    
def main():
    bmi_cal()
    
    get_height = 0.0
    get_weight = 0.0
    body_mass_index = 0.0

    get_height = float(input("Please enter your height in inches. "))
    get_weight = float(input("Please enter your weight in pounds. "))
    body_mass_index = (get_weight * 703) / (get_height ** 2)


    if body_mass_index < 16.5:
        print(" BMI of a person " + str(body_mass_index ) + " is underweight ")
    
    elif body_mass_index < 26.6:
        print(" BMI of a person " + str(body_mass_index ) + " is healthy ")
    
    elif body_mass_index < 29.9:
        print(" BMI of a person " + str(body_mass_index ) + " is normal weight ")
    
    elif body_mass_index < 32.3:
        print(" BMI of a person " + str(body_mass_index ) + " is overweight ")    
    
    elif body_mass_index < 35.6:
        print(" BMI of a person " + str(body_mass_index ) + " is moderatelyobese ")
    
    elif body_mass_index < 35.6:
        print(" BMI of a person " + str(body_mass_index ) + " is severelyobese ")     
    
    else:
         print(" BMI of a person " + str(body_mass_index ) + " is severe obese ")

main()


# In[ ]:




