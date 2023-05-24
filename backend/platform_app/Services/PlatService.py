from django.db import transaction
from platform_app.models import *
import copy

class PlatService :
    

    ## PK가 있는 데이터 및 없는 데이터를 분리하는 로직
    def seperated_data(self, data:dict) -> "None PK in Data, PK in Data" :

        ## PK 가 없는 데이터는 created_data2에 남김
        ## PK 가 있는 데이터는 updated_data2에 남김

        ## 참조용
        created_data = copy.deepcopy(data)
        updated_data = copy.deepcopy(data)
        
        ## 데이터 재조합용
        created_data2 = copy.deepcopy(data)
        updated_data2 = copy.deepcopy(data)

        count, count1, count2, count3 = 0,0,0,0
        

        for index1, index2 in zip(created_data['option_set'], updated_data['option_set']) :

            ## PK가 있다고 하면 업데이트를 진행해야하는 데이터
            if index1.get('pk') is not None :

                del created_data2['option_set'][count]
                count -= 1
                

            ## PK가 없다고 하는 경우 생성해야하는 데이터이므로, 
            if index2.get('pk') is None :    

                del updated_data2['option_set'][count1]
                count1 -= 1
                

            count += 1
            count1 += 1




        for index1, index2 in zip(created_data['tag_set'], updated_data['tag_set']) :

            if index1.get('pk') is not None : 

                del created_data2['tag_set'][count2]
                count2 -= 1

            if index2.get('pk') is None :

                del updated_data2['tag_set'][count3]
                count3 -= 1

            count2 += 1
            count3 += 1


        return created_data2, updated_data2


    ## 여기서는 삭제할 option_set의 pk 값을 찾아서 내보내주면 된다.
    def sync_option_set(self, data:dict, product_pk) -> "Delete option_set PK_id" :

        delete_id = []

        compare_query = ProductOption.objects.filter(product_id = product_pk)

        for index in compare_query :

            print(index.id)

            



        return True



            



        