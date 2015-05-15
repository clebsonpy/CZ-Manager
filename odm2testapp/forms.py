#from __future__ import unicode_literals
from django.forms import ModelForm
from django.contrib import admin
from django.db import models
from odm2testapp.models import Variables
from odm2testapp.models import CvVariabletype
from odm2testapp.models import CvVariablename
from odm2testapp.models import CvSpeciation


from django.forms import ModelChoiceField

class VariableModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s"%(obj.term)

class VariablesAdminForm(ModelForm):
    variabletypecv= VariableModelChoiceField(CvVariabletype.objects.all().order_by('term'))
    variablenamecv= VariableModelChoiceField(CvVariablename.objects.all().order_by('term'))
    speciationcv= VariableModelChoiceField(CvSpeciation.objects.all().order_by('term'))
    class Meta:
        model=Variables
       
class VariablesAdmin(admin.ModelAdmin):
    form=VariablesAdminForm