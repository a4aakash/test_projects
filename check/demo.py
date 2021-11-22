import logging

from dateutil.relativedelta import relativedelta
from django.db.models import Q, Count
from django.utils import timezone

# from accounts.enums import OnBoardingProgress, VerificationStatus
# from accounts.models.user import User
from django.conf import settings

# from connections.models import Connection
# from recommendations.utils.queries.base_query import get_base_query_for_on_boarding_completed_user
import json
from django.core.serializers import serialize
# from accounts.models.location import *
# from elastic_search_population import *
from .es_client import *

logger = logging.getLogger(__name__)

from elasticsearch import Elasticsearch
es = Elasticsearch(
    ['search-eltest-ukevwwpseamydksckn5zd6fy34.ap-south-1.es.amazonaws.com'],
    port=9200
)

def process():
    print("start the process")
    start_point = 0
    offset = 3
    end_point = start_point + offset
    es = ESClient()
    index = "metros"
    val = es.create_index(index)
    # es.insert_data(index)
    location_map = {}
    count = 0
    while(True):
        print("start_point : ", start_point)
        count += 1
        print("iteration : ", count)
        location_queryset = Location.objects.all()[start_point:end_point]
        print("len : ", len(location_queryset))
        query_size = len(location_queryset)
        if query_size == 0:
            break
        coordinates_json = json.loads(serialize('geojson', location_queryset, geometry_field='point', fields=('name',)))
        print("coordinates_json : ", coordinates_json)
        all_coordinates = coordinates_json["features"]
        print("all_coordinates : ", all_coordinates)
        for i in range(0, query_size):
            location = {}
            # print("location query : ", location_queryset[i].city)
            location["city"] = location_queryset[i].city.lower()
            print("city : ", location["city"])
            location["state"] = location_queryset[i].state
            location["country"] = location_queryset[i].country
            if all_coordinates is None:
                continue
            temp = all_coordinates[i].get("geometry", None)
            if temp is None:
                continue

            coordinates = temp.get("coordinates", None)
            if coordinates is not None:
                location["latitude"] = coordinates[0]
                location["longitude"] = coordinates[1]

            # print("location : ", location)
            # es.insert_data(index, location)
            location_map[location["city"]] = location
        start_point = end_point
        end_point = start_point + offset

    locations = []
    for key in location_map.keys():
        locations.append(location_map[key])

    print("total data need to populate : ", len(locations))
    # query = {}
    # result = es.search_by_index_and_query(index, "", query)

    # for location in locations:
    #     es.insert_data(index, location)


    # print("result : ", result)

    # print( coordinates_json["features"])