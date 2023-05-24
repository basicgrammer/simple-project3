# # from django.db import transaction

# from ninja import Router, Schema
# from platform_app.Services import *


# router = Router()


# '''
# ## API 응답 스키마
# ## API의 응답값을 수정하려면 이곳에서 수정하시면 됩니다.
# '''


# ## Code 200
# class Success(Schema) :
#     pk : int
#     name : str
#     option_set : list
#     # option_set : Created[] --> 데이터베이스에서 직렬화로 읽어서 그대로 반환할 수 있는지 확인할 것 // 순서 문제에 대한 해결을 볼 수 있을것? // 시간 남으면 해결 예정
#     ## Nested Schema -> DB, 호출을 하는 과정이 붙어있더라고
#     ## 입력되는 스키마(DB구조) -> 내보낼때 스키마(DB) 이런 방식으로 동일할 경우 사용해야하나? 들어가고 재조합없이 내보내준다고 하면

#     tag_set : list

# ## 스키마 참고 시켜서 데이터 가져오게 하기


# ## Code 201
# class Created(Schema) :
#     message: dict

# ## Code 400
# class Error(Schema) :
#     message: dict

# ## Code 500
# class ServerError(Schema) :
#     message: dict



# '''
# ## API 입력 스키마
# ## API 입력값을 수정하시려면 이곳에서 수정하시면 됩니다.
# '''

# class InputData(Schema) :
#     name : str
#     option_set : list
#     tag_set : list


# ## 상품 리스트 요청 API

# # URL: /shop/products/
# # URL: /shop/products/<pk>/

# @router.get('/products', response={200:Success, 400:Error}, 
#     summary = "상품 데이터 요청 (모든 데이터 호출)"
# )
# def request_item(request) : ## 헤더 

#     # res_code, header, option_set_data, tag_set_data = PlatService.retrieve_item_data()
#     PlatService.retrieve_item_data()

#     message = {
#         "message": "API 완료"
#     }

#     return  400, {'message': message}



# @router.get('/products/{pk}', response={200:Success, 400:Error}, 
#     summary = "상품 데이터 요청 (특정 데이터 요청)"
# )
# def request_item(request, pk) : ## 헤더 

#     # pk = none이면 로직에서 다 불러주면 되고
#     # pk가 none이 아니라면 pk에 해당하는 데이터만 가져오면 되는데

#     PlatService.retrieve_item_data(pk)

#     pass

#     message = {
#         "message": "API 완료"
#     }

#     return  200, {'message': message}



# ## 상품 등록 API 
# @router.post('/products',response={200:Success, 400:Error}, summary = "상품 등록 API")
# # @transaction.atomic
# def create_item(request, data:InputData) :

#     res_code, header, option_set, tag_set = PlatService.insert_item_data(data.dict())

#     return  res_code, {'pk': header.id, 'name':header.name, 'option_set':option_set, 'tag_set':tag_set}



# ## 상품 수정 API
# @router.patch('/products/{pk_id}',response={200:Success, 400:Error})
# def modify_item(request, pk_id:int, data:InputData) :

#     print(data.dict())

#     message = {
#         "message": "API 완료"
#     }

#     return  200, {'message': message}





    



# ##  상품 추가 / 조회 / 수정 /삭제 API 