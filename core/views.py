from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import (Food,
                         Wall,
                         Recommendation,
                         Compatibility,
                         Statistics)
from core.serializers import (FoodSerializer,
                              WallSerializer,
                              RecommendationSerializer,
                              CompatibilitySerializer,
                              StatisticsSerializer)


class FoodViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Food.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = FoodSerializer

    def perform_create(self, serializer):
        return serializer.save(name=self.request.data['name'],
                               type=self.request.data['type'],
                               quantity=self.request.data['quantity'])

    def get_queryset(self):
        queryset = self.queryset.all()
        return queryset


class WallViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Wall.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = WallSerializer

    # def perform_create(self, serializer):
    #     return serializer.save(food=self.request.data['food'],
    #                            water=self.request.data['water'],
    #                            recommendation=self.request.data['recommendation'],
    #                            compatibility=self.request.data['compatibility'])

    def get_queryset(self):
        queryset = self.queryset.all()
        return queryset


class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    http_method_names = ['get', 'post']
    serializer_class = RecommendationSerializer
    model = Recommendation

    def get_queryset(self):
        return self.queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        return Response({'station': serializer.data})


class CompatibilityViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = Compatibility.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CompatibilitySerializer

    def perform_create(self, serializer):
        return serializer.save(count=self.request.data['count'], )

    def get_queryset(self):
        queryset = self.queryset.all()
        return queryset


class StatisticsViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Statistics.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = StatisticsSerializer

    def perform_create(self, serializer):
        return serializer.save(day=self.request.data['day'],
                               food=Food.objects.get(id=self.request.data['food']),
                               amount=self.request.data['amount'])

    def get_queryset(self):
        queryset = self.queryset.all()
        return queryset
