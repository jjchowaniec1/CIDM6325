import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum
from django.db.models.aggregates import Avg, Min
from django.db.models.expressions import Func

from . models import MarketData

# Rounds to the nearest person for averages
class RoundInt(Func): 
    function = 'ROUND' 
    template='%(function)s(%(expressions)s, 0)'

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_opax=Sum('passengers')) \
                        .order_by('-total_opax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_dpax=Sum('passengers')) \
                                 .order_by('-total_dpax')[0:5]
    template_name="rankorder_list_destination.html"

# What are the top 5 airports in terms of: Total freight by origin
class Top5AirportsFreightByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_ofreight=Sum('freight')) \
                        .order_by('-total_ofreight')[0:5]
    template_name="rankorder_list_origin_freight.html"

# What are the top 5 airports in terms of: Total freight by destination
class Top5AirportsFreightByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_dfreight=Sum('freight')) \
                                 .order_by('-total_dfreight')[0:5]
    template_name="rankorder_list_destination_freight.html"
    
# What are the top 5 airports in terms of: Total mail by origin
class Top5AirportsMailByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_omail=Sum('mail')) \
                        .order_by('-total_omail')[0:5]
    template_name="rankorder_list_origin_mail.html"

# What are the top 5 airports in terms of: Total mail by destination
class Top5AirportsMailByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_dmail=Sum('mail')) \
                                 .order_by('-total_dmail')[0:5]
    template_name="rankorder_list_destination_mail.html"

# What are the top 5 airports in terms of: Total distance by origin
class Top5AirportsDistanceByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_odistance=Sum('distance')) \
                        .order_by('-total_odistance')[0:5]
    template_name="rankorder_list_origin_distance.html"

# What are the top 5 airports in terms of: Total distance by destination
class Top5AirportsDistanceByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_ddistance=Sum('distance')) \
                                 .order_by('-total_ddistance')[0:5]
    template_name="rankorder_list_destination_distance.html"

# Which airport reported the most passengers by month?
class TopPaxByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pax_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,8):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_mpax=Max('passengers')) \
                .order_by('-total_mpax')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list


# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []

        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,8):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_mdistance=Max('distance')) \
                .order_by('-total_mdistance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Which airline reported the most freight carried?
class TopFreight(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_id','carrier_name','freight') \
                                .annotate(top_freight=Sum('freight')) \
                                .order_by('-top_freight')[:1]
    template_name="rankorder_list_origin_top_freight.html"
    

# Which airline reported the most passengers carried?
class TopPax(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_id','carrier_name','passengers') \
                                .annotate(top_pax=Sum('passengers')) \
                                .order_by('-top_pax')[:1]
    template_name="rankorder_list_origin_top_pax.html"

# Which airline reported the most mail carried?
class TopMail(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_id','carrier_name','mail') \
                                .annotate(top_mail=Sum('mail')) \
                                .order_by('-top_mail')[:1]
    template_name="rankorder_list_origin_top_mail.html"

# Which airline reported the longest flight distance?
class TopDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('carrier_name','carrier_id') \
                                .annotate(max_distance=Max('distance')) \
                                .order_by('-max_distance')[:1]
    template_name="rankorder_list_origin_max_distance.html"

# Rank order passengers carried, by month, for these airlines:
#     AA (American Airlines)
#     AS (Alaska Airlines)
#     DL (Delta Airlines)
#     UA (United Airlines)
#     WN (Southwest Airlines)

#  January
class OrderPaxJanuary(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pax_january.html"

    def get_queryset(self):

        month_list = []

        queryset = MarketData.objects \
            .values('month','carrier_id','carrier_name') \
            .filter(month__exact=1,carrier_id__in=['AA','AS','DL','UA','WN']) \
            .annotate(total_jan_pax=Sum('passengers')) \
            .order_by('-total_jan_pax')[0:5]
        
        month_list.append(queryset)

        # return list
        return month_list

# February
class OrderPaxFebruary(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pax_february.html"

    def get_queryset(self):

        month_list = []

        queryset = MarketData.objects \
            .values('month','carrier_id','carrier_name') \
            .filter(month__exact=2,carrier_id__in=['AA','AS','DL','UA','WN']) \
            .annotate(total_feb_pax=Sum('passengers')) \
            .order_by('-total_feb_pax')[0:5]
        
        month_list.append(queryset)

        # return list
        return month_list

# March
class OrderPaxMarch(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pax_march.html"

    def get_queryset(self):

        month_list = []

        queryset = MarketData.objects \
            .values('month','carrier_id','carrier_name') \
            .filter(month__exact=3,carrier_id__in=['AA','AS','DL','UA','WN']) \
            .annotate(total_mar_pax=Sum('passengers')) \
            .order_by('-total_mar_pax')[0:5]
        
        month_list.append(queryset)

        # return list
        return month_list

# April
class OrderPaxApril(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pax_april.html"

    def get_queryset(self):

        month_list = []

        queryset = MarketData.objects \
            .values('month','carrier_id','carrier_name') \
            .filter(month__exact=4,carrier_id__in=['AA','AS','DL','UA','WN']) \
            .annotate(total_apr_pax=Sum('passengers')) \
            .order_by('-total_apr_pax')[0:5]
        
        month_list.append(queryset)

        # return list
        return month_list

# May
class OrderPaxMay(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pax_may.html"

    def get_queryset(self):

        month_list = []

        queryset = MarketData.objects \
            .values('month','carrier_id','carrier_name') \
            .filter(month__exact=5,carrier_id__in=['AA','AS','DL','UA','WN']) \
            .annotate(total_may_pax=Sum('passengers')) \
            .order_by('-total_may_pax')[0:5]
        
        month_list.append(queryset)

        # return list
        return month_list

# June
class OrderPaxJune(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pax_june.html"

    def get_queryset(self):

        month_list = []

        queryset = MarketData.objects \
            .values('month','carrier_id','carrier_name') \
            .filter(month__exact=6,carrier_id__in=['AA','AS','DL','UA','WN']) \
            .annotate(total_jun_pax=Sum('passengers')) \
            .order_by('-total_jun_pax')[0:5]
        
        month_list.append(queryset)

        # return list
        return month_list

# July - not asked but in the data
class OrderPaxJuly(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pax_july.html"

    def get_queryset(self):

        month_list = []

        queryset = MarketData.objects \
            .values('month','carrier_id','carrier_name') \
            .filter(month__exact=7,carrier_id__in=['AA','AS','DL','UA','WN']) \
            .annotate(total_jul_pax=Sum('passengers')) \
            .order_by('-total_jul_pax')[0:5]
        
        month_list.append(queryset)

        # return list
        return month_list

# All months
class OrderPaxAll(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pax_all.html"

    def get_queryset(self):

        month_list = []

        queryset = MarketData.objects \
            .values('month','carrier_id','carrier_name') \
            .filter(carrier_id__in=['AA','AS','DL','UA','WN']) \
            .annotate(total_all_pax=Sum('passengers')) \
            .order_by('-total_all_pax')[0:5]
        
        month_list.append(queryset)

        # return list
        return month_list

# Find the average number of passengers for flights into:
#     LAX (Los Angeles)
#     SFO (San Francisco)
#     DFW (Dallas-Fort Worth)
#     ATL (Atlanta)
#     ORD (Chicago)


    
class AvgPax(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code', 'dest_city_name') \
                                .filter(dest_iata_code__in=['LAX','SFO','DFW','ATL','ORD']) \
                                .annotate(avg_pax= RoundInt(Avg('passengers'))) \
                                .order_by('-avg_pax')[:]
    template_name="rankorder_list_origin_avg_pax.html"

# Find the average volume of freight for flights departing:
#     MIA (Miami)
#     MEM (Memphis)
#     JFK (New York JFK)
#     ANC (Anchorage)
#     SDF (Louisville)

class AvgFreight(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code', 'orig_city_name') \
                                .filter(orig_iata_code__in=['MIA','MEM','JFK','ANC','SDF']) \
                                .annotate(avg_freight=RoundInt(Avg('freight'))) \
                                .order_by('-avg_freight')[:]
    template_name="rankorder_list_origin_avg_freight.html"

# What city pairs represent the most freight carried for the longest distance?
class LongFreight(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code', 'orig_city_name', 'dest_iata_code', \
                                         'dest_city_name') \
                                    .annotate(max_freight=Max('freight'),
                                            longest_distance=Max('distance')) \
                                    .order_by('-max_freight', '-longest_distance')[:1]
    template_name="rankorder_list_long_freight.html"

# What city pairs represent the most mail carried for the shortest distance?
class ShortFreight(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code', 'orig_city_name',
                                            'dest_iata_code', 'dest_city_name') \
                                    .annotate(max_mail=Max('mail'),
                                            shortest_distance=Min('distance')) \
                                    .order_by('-max_mail', '-shortest_distance')[:1]
    template_name="rankorder_list_short_freight.html"