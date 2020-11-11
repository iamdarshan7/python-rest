from django.db import models

# Create your models here.
class HouseholdDetails(models.Model):
    owner_name = models.CharField(max_length=100)
    spouse_name = models.CharField(max_length=100, blank=True)
    total_family_members = models.IntegerField()
    total_male_members = models.IntegerField()
    no_of_children = models.IntegerField()
    literate_members =  models.IntegerField()
    no_of_members_eligible_to_caste_vote = models.IntegerField()
    members_above_sixty_years = models.IntegerField()
    ward_no = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=9)
    longitude = models.DecimalField(max_digits=9, decimal_places=9)
    created_at = models.DateTimeField(auto_now_add=True)  