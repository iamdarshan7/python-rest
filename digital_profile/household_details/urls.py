
from rest_framework import routers
from .api import HouseholdDetailsViewSets

router = routers.DefaultRouter()
router.register('api/household-details', HouseholdDetailsViewSets, 'household_details')

urlpatterns = router.urls