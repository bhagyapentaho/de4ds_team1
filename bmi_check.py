__author__ = "Vijayasree Ravulapati"

'''
Class to calculate BMI based on height(in mts) & weight (in kgs)
'''
class BMICheck:
    def __init__(self):
        pass

    def bmi_intro(self):
        print("Welcome to my BMI calculator!")
        print("If you can tell me your weight and height")
        print("I can tell you your Body Mass Index")
        print("Let's Go!\n")

    def start_bmi(self):
        
        height = float(input("Please enter your height in inches. "))
        weight = float(input("Please enter your weight in pounds. "))

        bmi_ = self.calculate_bmi(height, weight)
        print("Your BMI: %s" % bmi_)

    def calculate_bmi(self, height, weight):
        height_in_meter = height
        weight_in_kg = weight
        bmi = round((weight_in_kg/(height_in_meter * height_in_meter)))
        self.bmi_category(bmi)
        return bmi
    
    def bmi_category(self, bmi):
        if bmi < 15.0:
            return 'Very severely underweight'
        elif bmi < 16.0:
            return 'Severely underweight'
        elif bmi < 18.5:
            return 'Underweight'
        elif bmi < 25:
            return 'Great shape!'
        elif bmi < 30:
            return 'Overweight'
        elif bmi < 35:
            return 'Obese Class I Moderately obese'
        elif bmi <= 40:
            return 'Obese Class II Severely obese'
        elif bmi > 40:
            return 'Very severely obese'
            
# bmi_check = BMICheck()
# bmi_check.bmi_intro()
# bmi_check.start_bmi()
