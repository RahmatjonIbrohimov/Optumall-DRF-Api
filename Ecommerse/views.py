from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from .models import Products
from .serializers import OnlyAdminSerializer


# Create your views here.
class HomeApiViews(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = OnlyAdminSerializer


# class DetailBlog(RetrieveAPIView):

class DetailApiViews(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = OnlyAdminSerializer
    lookup_field = "id"


class UpdateApiViews(generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = OnlyAdminSerializer
    lookup_field = 'id'


class CreateApiViews(generics.CreateAPIView):
    serializer_class = OnlyAdminSerializer
    queryset = Products.objects.all()


class DeleteApiViews(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = OnlyAdminSerializer
    lookup_field = "id"


class ForwardUsersViews(generics.ListAPIView):
    ...


class OnlyAuthUsersViews(generics.ListAPIView):
    ...


class CategoryProductsViews(generics.ListAPIView):
    ...


class SearchProductTitleViews(generics.ListAPIView):
    ...
