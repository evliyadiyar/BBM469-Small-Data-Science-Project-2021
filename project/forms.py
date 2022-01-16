from django import forms
from . import views


class modelForm(forms.Form):

    def __init__(self, *args, **kwargs): #constructor
        features = kwargs.pop('features', 0) #get features from dict
        super(modelForm,self).__init__(*args, **kwargs) #error exception

        for i in features: #create fields from my model's features
            
            if i != 'Disease':
                self.fields[i] = forms.CharField()
