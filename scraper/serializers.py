from rest_framework import serializers
from .models import  SearchResult

from rest_framework import serializers
from .models import SearchResult

# seriliazer to to convert queryset into renderable content
class SearchResultSerializer(serializers.ModelSerializer):
    keyword = serializers.StringRelatedField()

    class Meta:
        model = SearchResult
        fields = ['id', 'keyword', 'title', 'description', 'price', 'rating', 'is_sponsored', 'search_date']
