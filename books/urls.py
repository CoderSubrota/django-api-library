from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet, AuthorViewSet, MemberViewSet, BorrowRecordViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'members', MemberViewSet)
router.register(r'borrow', BorrowRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
