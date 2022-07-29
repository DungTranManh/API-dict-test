from django.db import models

# Create your models here.
class Data(models.Model):
    ent_seq = models.IntegerField()
    keb = models.TextField()
    reb = models.TextField()
    name_type = models.TextField()
    trans_det = models.TextField()

    def __str__(self):
        return self.ent_seq
    
