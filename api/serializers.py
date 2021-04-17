
from rest_framework import serializers
from .models import primerx_field_model

class PrimerxSerializer(serializers.ModelSerializer):
    class Meta:
        model = primerx_field_model
        fields = ['id','prime_patient_id','prime_address_id','prime_first_name','prime_lst_name', 'prime_middle_name', 'prime_suffix_form', 'prime_prefix_form',
                    'prime_work_number', 'prime_Social_security_num', 'prime_education', 'prime_address_street', 'prime_address_city', 
                    'prime_address_state', 'prime_emergency_phone', 'prime_emergency_name', 'prime_emergency_relation',
                    'prime_sex' ]