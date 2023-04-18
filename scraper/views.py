from django.shortcuts import render

from .scraping_logic import run_scraper
from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SearchResult
from .serializers import SearchResultSerializer

from datetime import datetime


#GET API for displaying scraped results
class SearchResultList(generics.ListAPIView):
    serializer_class = SearchResultSerializer

    def get_queryset(self):
        queryset = SearchResult.objects.all()
        keyword = self.request.query_params.get('keyword', None) #parameter for keyword input
        search_date = self.request.query_params.get('date', None) #paramter for date input

        if keyword is not None and search_date is not None: # if both keword and date provided then filter by both
            try:
                search_date_obj = datetime.strptime(search_date, '%Y-%m-%d').date()
                queryset = queryset.filter(keyword__keyword__icontains=keyword,search_date=search_date_obj)
            except ValueError:
                pass
        elif search_date is not None: # if only date provided then filter by date
            try:
                search_date_obj = datetime.strptime(search_date, '%Y-%m-%d').date()
                queryset = queryset.filter(search_date=search_date_obj)
            except ValueError:
                pass
        elif keyword is not None: # if only keyword provided then filter by keyword
            try:
                queryset = queryset.filter(keyword__keyword__icontains=keyword)
            except ValueError:
                pass
        return queryset


# POST Api for triggering the scraper
@api_view(['POST'])
def trigger_scraper(request):
    try:
        run_scraper()  # call the runscraper function
        return Response({"message": "Scraper triggered successfully"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)