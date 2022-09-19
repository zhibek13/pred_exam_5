from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from account.models import Profile
from .models import Category, Item, Order
from .serializers import CategorySerializer, ItemSerializer, OrderSerializer
from .permissions import IsSenderPermission, IsSenderFalsePermission, IsAuthorPermission


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsSenderPermission, ]

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.filter()


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsSenderPermission, ]


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsSenderPermission, ]

    def get_queryset(self):
        return self.queryset.filter(category_id=self.kwargs['category_id'])

    def perform_create(self, serializer):
        serializer.save()


class ItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthorPermission, ]


# class OrderItems(APIView):
#     def get(self, request, pk):
#         item = get_object_or_404(Item, id=pk)
#         try:
#             order = Order.objects.create(item=item, user=request.user.profile)
#         except IntegrityError:
#             order = Order.objects.get(item=item, user=request.user.profile)
#             order.save()
#             return Response(data, status=status.HTTP_200_OK)
#         else:
#             data = {'message': f"you've ordered this {pk} item"}
#             return Response(data, status=status.HTTP_201_CREATED)

class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsSenderFalsePermission, ]

    def get_queryset(self):
        return self.queryset.filter(pk=self.kwargs['pk'])

    def perform_create(self, serializer):
        serializer.save(profile=get_object_or_404(Profile, pk=self.kwargs['pk']))


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsSenderFalsePermission, ]

