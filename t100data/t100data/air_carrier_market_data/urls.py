# urls.py
from django.urls import path
from . views import MarketDataList, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    Top5AirportsFreightByOrigin, \
                    Top5AirportsFreightByDestination, \
                    Top5AirportsMailByOrigin, \
                    Top5AirportsMailByDestination, \
                    Top5AirportsDistanceByOrigin, \
                    Top5AirportsDistanceByDestination, \
                    TopPaxByMonth, \
                    TopDistanceByMonth , \
                    TopFreight, \
                    TopPax, \
                    TopMail, \
                    TopDistance, \
                    OrderPaxJanuary, \
                    OrderPaxFebruary,\
                    OrderPaxMarch, \
                    OrderPaxApril, \
                    OrderPaxMay, \
                    OrderPaxJune, \
                    OrderPaxJuly, \
                    OrderPaxAll,\
                    AvgPax, \
                    AvgFreight, \
                    LongFreight, \
                    ShortFreight
                                   

urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),

    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}),
        name="top5paxorigin"),

    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}), 
        name="top5paxdestination"),

    path('top5freightorigin/',
        Top5AirportsFreightByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Origin Airport"}),
        name="top5freightorigin"),
    
    path('top5freightdestination/',
        Top5AirportsFreightByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Destination Airport"}),
        name="top5freightdestination"),
    
    path('top5mailorigin/',
        Top5AirportsMailByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Origin Airport"}),
        name="top5mailorigin"),
    
    path('top5maildestination/',
        Top5AirportsMailByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Destination Airport"}),
        name="top5maildestination"),
    
    path('top5distanceorigin/',
        Top5AirportsDistanceByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Origin Airport"}),
        name="top5distanceorigin"),
    
    path('top5distancedestination/',
        Top5AirportsDistanceByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Destination Airport"}),
        name="top5distancedestination"),
    
    path('toppax_month/',  
        TopPaxByMonth.as_view(
            extra_context={'title': "Top Passengers by Month"}), 
        name="toppax_month"),
    
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}), 
        name="topdistance_month"),
    
    path('top_freight/',  
        TopFreight.as_view(
            extra_context={'title': "Airline with most freight carried"}), 
        name="top_freight"),
    
    path('top_pax/',  
        TopPax.as_view(
            extra_context={'title': "Airline with most passengers carried"}), 
        name="top_pax"),
    
    path('top_mail/',  
        TopMail.as_view(
            extra_context={'title': "Airline with most mail carried"}), 
        name="top_mail"),

    path('max_distance/',  
        TopDistance.as_view(
            extra_context={'title': "Airline with longest flight distance"}), 
        name="max_distance"),

    path('pax_january/',  
        OrderPaxJanuary.as_view(
            extra_context={'title': "January passenger rank order for AA, AS, DL, UA, WN"}), 
        name="pax_january"),

    path('pax_february/',  
        OrderPaxFebruary.as_view(
            extra_context={'title': "February passenger rank order for AA, AS, DL, UA, WN"}), 
        name="pax_february"),

    path('pax_march/',  
        OrderPaxMarch.as_view(
            extra_context={'title': "March passenger rank order for AA, AS, DL, UA, WN"}), 
        name="pax_march"),

    path('pax_april/',  
        OrderPaxApril.as_view(
            extra_context={'title': "April passenger rank order for AA, AS, DL, UA, WN"}), 
        name="pax_april"),

    path('pax_may/',  
        OrderPaxMay.as_view(
            extra_context={'title': "May passenger rank order for AA, AS, DL, UA, WN"}), 
        name="pax_may"),

    path('pax_june/',  
        OrderPaxJune.as_view(
            extra_context={'title': "June passenger rank order for AA, AS, DL, UA, WN"}), 
        name="pax_june"),
    
      path('pax_july/',  
        OrderPaxJuly.as_view(
            extra_context={'title': "June passenger rank order for AA, AS, DL, UA, WN"}), 
        name="pax_july"),

    path('pax_all/',  
        OrderPaxAll.as_view(
            extra_context={'title': "All months together passenger rank order for AA, AS, DL, UA, WN"}), 
        name="pax_all"),

    path('avg_pax/',  
        AvgPax.as_view(
            extra_context={'title': "Average number of passengers for flights into LAX, SFO, DFW, ATL, ORD"}), 
        name="avg_pax"),

    path('avg_freight/',  
        AvgFreight.as_view(
            extra_context={'title': "Average volume of freight for flights departing MIA, MEM, JFK, ANC, SDF"}), 
        name="avg_freight"),

    path('long_freight/',  
        LongFreight.as_view(
            extra_context={'title': "City pairs that represent the most freight carried for the longest distance"}), 
        name="long_freight"),

    path('short_freight/',  
        ShortFreight.as_view(
            extra_context={'title': "City pairs that represent the most freight carried for the shortest distance"}), 
        name="short_freight"),
]