from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class primerx_field_model(models.Model):
    id = models.BigAutoField(primary_key=True)
    prime_form_id = models.IntegerField( null=True, blank =True )
    prime_patient_id = models.IntegerField( null=True, blank =True )
    prime_address_id = models.IntegerField( null=True, blank =True )
    prime_first_name = models.CharField(max_length=200, null=True, blank =True )
    prime_lst_name = models.CharField(max_length=200, null=True, blank =True )
    prime_middle_name = models.CharField(max_length=200, null=True, blank =True )
    prime_suffix_form = models.CharField(max_length=200, null=True, blank =True )
    prime_prefix_form = models.CharField(max_length=200, null=True, blank =True )
    prime_work_number = PhoneNumberField( null=True, blank =True )
    prime_Social_security_num = models.IntegerField( null=True, blank =True )

    prime_education = models.CharField(max_length=200, null=True, blank =True ) #checkbox

    prime_address_street = models.CharField(max_length=200, null=True, blank =True )
    prime_address_city = models.CharField(max_length=200, null=True, blank =True )
    prime_address_state = models.CharField(max_length=200, null=True, blank =True )
    
    prime_emergency_phone = PhoneNumberField( null=True, blank =True )
    prime_emergency_name = models.CharField(max_length=200, null=True, blank =True )
    prime_emergency_relation = models.CharField(max_length=200, null=True, blank =True )

    prime_sex = models.CharField(max_length=200, null=True, blank =True )  #checkbox

    objects = models.Manager()


