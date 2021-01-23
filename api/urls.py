from restApi.views import LobbyViewSet, LotteryViewSet, UserViewSet
from rest_framework import routers
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'lobby', LobbyViewSet)
router.register(r'lottery', LotteryViewSet)
# router.register(r'branches/autcomplete', BranchesAutoCompleteViewSet)
# router.register(r'branches', BranchesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(
        url='/static/favicon.ico')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
