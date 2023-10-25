from rest_framework.routers import DefaultRouter
from apps.api.views import UsersModelViewSet, BlogModelViewSet


router: DefaultRouter = DefaultRouter()

router.register(r'users', UsersModelViewSet)
router.register(r'posts', BlogModelViewSet)