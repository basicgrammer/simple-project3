from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import json, copy

from platform_app.serializers import *
from platform_app.Services import *
from platform_app.models import *


class BasicViewSet(viewsets.ModelViewSet) :
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # @action(detail=False, methods=["POST"])
    @csrf_exempt    
    def create(self, request) :
        # 1. 데이터 파싱
        data = json.loads(request.body)
        
        # 2.시리얼 라이저 데이터 주입
        serializer_class = ProductSerializer(data=data)
        serializer_class.is_valid(raise_exception=True)

        print(serializer_class.validated_data)

        product = serializer_class.save()

        new_serializer = ProductSerializer(instance = product)

        print(new_serializer.data)

        return Response(new_serializer.data, status=201)

    @csrf_exempt
    def retrieve(self, request, pk=None) :

        # data = json.loads(request.body)

        if pk is not None : 

            queryset = Product.objects.filter(id = pk)
            serializer = ProductSerializer(queryset[0])

        else : 

            serializer = ProductSerializer(queryset[0])

        return Response(serializer.data, status=200)

    ## 부분 데이터 수정 (Patch)
    @csrf_exempt
    def partial_update(self, request, pk) -> "Json Data":

        ## 업데이트 로직에서 2가지를 분리해서 수행해야할듯함
        ## 1. 존재하지 않는 데이터의 생성
        ## 2. 기존 데이터 업데이트
        ## 3. option_set 및 tag_set 길이를 비교하여 기존 데이터 업데이트 과정에서 삭제해야함

        data = json.loads(request.body)

        # 생성 및 업데이트 데이터 분리 작업 수행 -> 그러면 다시 병합하는 과정이 필요한거 아닌가? --> 아니지 그냥 새로 불러오면 되니까 굳이 찾을 필요가 없는것
        # c_data, u_data = PlatService().seperated_data(data)
        # PlatService().seperated_data(data)


        ## 데이터 구분이 애시당초 필요하지 않다고 생각이 든다.

        ## 생성 및 수정 단계는 원활하게 들어갔으나, 이제 삭제하는 과정이 필요하다. 
        
        # data = data['tag_set']


        # print(data)

        # for index in data :

        #     # print(index.pk)
        #     if index.get('pk') is not None :

        #         tag_query = Tag.objects.filter(id = index['pk'])[0]


            
        #         tag_query.name = index['name']
        #         tag_query.save()

        #     else : 
                
        #         new_query = Tag()
        #         new_query.name = index['name']
        #         new_query.save()


        # serializer = ProductSerializer(data = data)

        # serializer_class.is_valid(raise_exception=True)

        # product = serializer_class.save()

        queryset = Product.objects.filter(id = pk)

        serializer_class = ProductSerializer(queryset[0], data=data, partial = True)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()

        # print(serializer_class.data)

        product = serializer_class.save()




        new_serializer = ProductSerializer(instance = product)

        PlatService().sync_option_set(new_serializer.data['option_set'], pk)


        # print("complete data")
        # print(new_serializer.data)


        return Response(new_serializer.data, status=200)




