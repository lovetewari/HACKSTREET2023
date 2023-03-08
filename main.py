# import numpy 
# import pandas
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# import warnings
# import pickle
# warnings.filterwarnings("ignore")
# import math
# Height=float(input("Enter your height in centimetres: "))
# Weight=float(input("Enter your Weight in Kg: "))
# Height = Height/100
# BMI=Weight/(Height*Height)
# print("your Body Mass Index is: ",BMI)
# if(BMI>0):
# 	if(BMI<=16):
# 		print("you are severely underweight")
# 	elif(BMI<=18.5):
# 		print("you are underweight")
# 	elif(BMI<=25):
# 		print("you are Healthy")
# 	elif(BMI<=30):
# 		print("you are overweight")
# 	else: print("you are severely overweight")
# else:("enter valid details")

















# # importing Flask and other modules
# from flask import Flask, request, render_template
# # Flask constructor
# app = Flask(__name__)
# # A decorator used to tell the application
# # which URL is associated function
# @app.route('/', methods =["GET", "POST"])
# def gfg():
# 	if request.method == "POST":
# 	# getting input with name = fname in HTML form
# 	first_name = request.form.get("fname")
# 	# getting input with name = lname in HTML form
# 	last_name = request.form.get("lname")
# 	return "Your name is "+first_name + last_name
# 	return render_template("form.html")

# if __name__=='__main__':
# app.run()





#pip install Py_edamam
from keys import edamam_id, edamam_key
e = PyEdamam(nutrition_applied=edamam_id,nutrition_appkey=edamam_key)
def bmr_calculation():
    weightInLbs =int(input("weight: "))
    heightInInches=int(input("height in inches: "))
    age = int(input("age :"))
    maleOrFemale = input("are you a (m)ale or (f)emale?").lower()
    weightInKgs = weightInLbs / 2.2
    heightInCentimeters = heightInInches * 2.54
    if maleOrFemale == "m":
        bmr = int((10 * weightInKgs) + (6.25 * heightInCentimeters) - (5 * age) + 5)
    elif maleOrFemale == "f":
        bmr = int((10 * weightInKgs) + (6.25 * heightInCentimeters) - (5 * age) -161)
    print("your basal metabolic rate is " + str(bmr) + ".")
    return bmr
def daily_caloric_needs(bmr):
    print(
        '''
        1 = sedentary
        2 = Excersise 1 - 3 times a week
        3 = Excersise 4 - 5 times a week
        4 = daily excersise or intense excersise 3-4 times in week 
        5 = Intense excersise 6 times a week 
        '''    
	)
    activitylevel=int(input("select your activity level: " ))
    if activitylevel == 1:
        activitylevelIndex = 1.2
    elif activitylevel == 2:
        activitylevelIndex = 1.375
    elif activitylevel == 3:
        activitylevelIndex == 1.46
    elif activitylevel == 4:
        activitylevelIndex == 1.725
    elif activitylevel == 5:
        activitylevelIndex == 1.9
    dailyCaloriesNeeded = int(bmr * activitylevelIndex)
    print("to maintain your currrent weight you need" + str(dailyCaloriesNeeded) + "calories a day.")
    return dailyCaloriesNeeded
def calculate_macros(calories):
    calories_from_protein = int(.4 * calories)
    calories_in_protein = int(calories_from_protein /4)
    calories_from_carbs = int(.4 * calories)
    calories_in_carbs = int(calories_from_carbs/4)
    calories_from_fat = int(.2 * calories)
    calories_in_fat = int(calories_from_fat/9)
    print("calories from protein:" + str(calories_from_protein) +" / " + str(calories_in_protein) + "grams of protein.")
    print("calories from carbs:" + str(calories_from_carbs) +" / " + str(calories_in_carbs) + "grams of carbs.")
    print("calories from fat: " + str(calories_from_fat) +" / " + str (calories_in_fat) + "grams of fat.")
    print("/n")
    haLFAPoundaweek_calories =int(calories - int((3500 /2 ) / 7))
    print("to lose .5 lb of fat a week, your daily caloric needs drops to " + str(haLFAPoundaweek_calories) + ".")
    calories_from_protein = int(.4 * haLFAPoundaweek_calories )
    calories_from_protein = int(calories_from_protein / 4)
    calories_from_carbs = int(.4 * haLFAPoundaweek_calories)
    calories_in_carbs = int(calories_from_carbs / 4)
    calories_from_fat = int(.2 * haLFAPoundaweek_calories)
    calories_in_fat = int(calories_from_fat /9)
    
    
    print("calories from protein : " + str(calories_from_protein) + " / " + str(calories_in_protein) + "grams of protein.")
    print("calories from carbs : " + str(calories_from_carbs) + " /  " + str(calories_in_carbs)+ "grams of carbs.")
    print("calories from fat : "  + str(calories_from_fat) + " / " + str(calories_in_fat)+ "grams of fat.")
    
    
    def get_nutrients_data():
        for nutrient_data in e.search_nutrient('3 egg whites and 2 whole eggs '):
            print(nutrient_data)
            print(nutrient_data.calories)
            print(nutrient_data.totalNuterients[1])
            
 #bmr = bmr_calculation()
 #dailyCaloriesNeeded = daily_caloric_needs(bmr)
#calculate_macros(dailycaloriesNeeded)
#get_nutrition_data()      