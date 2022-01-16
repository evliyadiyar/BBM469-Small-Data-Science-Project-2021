import joblib
import numpy as np
from django.http import  HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import modelForm


file = joblib.load("model.joblib") #Import our ml model and model's features list

class Pred(View):




    def get(self, request):
        form = modelForm(features = file["features"])
        context = {"form" : form }
        return render(request, "home.html",context)




 
    def post(self, request):

        data = request.POST.dict()
      
        feature_values = []
        for keys,values in data.items():
            if keys[0:2] == 'Fe': # If column is 'Fe'atures
                feature_values.append(values)


        model = file.get('model')
        result = model.predict_proba([feature_values])
        for i in range (0,len(result[0])):
            np.round(result[0][i],2)
        result = result.tolist()
        
        new_result = [x*100 for x in result[0]] # get % ratio 
      
        for i in range (0,len(new_result)):
            new_result[i] = float("%0.2f"%new_result[i]) # get 2 decimal places
            print(new_result[i])
            
           
        
             
        return render(request, "result.html",{'result1':new_result[0],'result2':new_result[1],'result3':new_result[2],'result4':new_result[3]})



