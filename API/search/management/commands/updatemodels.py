from django.core.management.base import BaseCommand
import pandas as pd
from search.models import Data
class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('data.csv')
        for ENT_SEQ,KEB,REB,NAME_TYPE,TRANS_DET in zip(df.ent_seq,df.keb,df.reb,df.name_type,df.trans_det):
            models = Data(ent_seq = ENT_SEQ, keb = KEB, reb = REB, name_type = NAME_TYPE, trans_det = TRANS_DET)
            models.save()
        