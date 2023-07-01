from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (IngredientViewSet, MeUserViewSet, RecipeViewSet,
                       TagViewSet)

router = DefaultRouter()
app_name = 'api'

router.register('users', MeUserViewSet)
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)
router.register('recipes', RecipeViewSet)
# router.register('users', MeUserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    # path('', include('djoser.urls')),
    # path('', include('djoser.urls.jwt')),
]