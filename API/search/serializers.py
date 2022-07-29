from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Data

class SearchSerializer(serializers.ModelSerializer):
    # ent_seq = serializers.IntegerField()
    # keb = serializers.CharField()
    # reb = serializers.CharField()
    # name_type = serializers.CharField()
    # trans_det = serializers.CharField()
    class Meta:
        model = Data
        fields = ['ent_seq','keb','reb','name_type','trans_det']

