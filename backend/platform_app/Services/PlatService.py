import copy
from django.db import transaction

from platform_app.models import *



class PlatService :
    
    ## PK가 있는 데이터 및 없는 데이터를 분리하는 로직
    def seperated_data(self, data:dict) -> "None PK in Data, PK in Data" :

        ## 참조용
        created_data = copy.deepcopy(data)  # PK 가 없는 데이터는 created_data2에 남김
        updated_data = copy.deepcopy(data)  # PK 가 있는 데이터는 updated_data2에 남김
        
        ## 데이터 재조합용
        created_data2 = copy.deepcopy(data) 
        updated_data2 = copy.deepcopy(data)

        COUNT, COUNT1, COUNT2, COUNT3 = 0,0,0,0
        

        for index1, index2 in zip(created_data['option_set'], updated_data['option_set']) :

            ## PK가 있다고 하면 업데이트를 진행해야하는 데이터
            if index1.get('pk') is not None :

                del created_data2['option_set'][COUNT]
                COUNT -= 1
                

            ## PK가 없다고 하는 경우 생성해야하는 데이터이므로, 
            if index2.get('pk') is None :    

                del updated_data2['option_set'][COUNT1]
                COUNT1 -= 1
            COUNT += 1
            COUNT1 += 1

        for index1, index2 in zip(created_data['tag_set'], updated_data['tag_set']) :

            if index1.get('pk') is not None : 

                del created_data2['tag_set'][COUNT2]
                COUNT2 -= 1

            if index2.get('pk') is None :

                del updated_data2['tag_set'][COUNT3]
                COUNT3 -= 1

            COUNT2 += 1
            COUNT3 += 1

        return created_data2, updated_data2


            



        