from rest_framework import routers

from core.views import FoodViewSet, WallViewSet, RecommendationViewSet, CompatibilityViewSet, StatisticsViewSet

router = routers.DefaultRouter()
router.register(r'food', FoodViewSet, base_name='core')
router.register(r'walls', WallViewSet, base_name='core')
router.register(r'recommendations', RecommendationViewSet, base_name='core')
router.register(r'compatibilities', CompatibilityViewSet, base_name='core')
router.register(r'statistics', StatisticsViewSet, base_name='core')

urlpatterns = router.urls
