from django.urls import path
from .views import candleSticks,LineChart,BarChart,PieChart

urlpatterns = [
    path('api/candlestick-data/',candleSticks.as_view(),name='candlestick=data'),
    path('api/line-chart-data/',LineChart.as_view(),name='line-chart-data'),
    path('api/bar-chart-data/',BarChart.as_view(),name='bar-chart-data'),
    path('api/pie-chart-data/',PieChart.as_view(),name='line-chart-data'),
]