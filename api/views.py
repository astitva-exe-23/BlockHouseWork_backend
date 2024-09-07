from rest_framework.views import APIView    
from rest_framework.response import Response
from rest_framework import status

class candleSticks(APIView):
    def get(set,request):
        data = {
            "data": [
                {"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
                {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
                {"x": "2023-01-03", "open": 40, "high": 50, "low": 35, "close": 45},
                {"x": "2023-01-04", "open": 45, "high": 55, "low": 40, "close": 50},
                {"x": "2023-01-05", "open": 50, "high": 60, "low": 45, "close": 55},
                {"x": "2023-01-06", "open": 55, "high": 65, "low": 50, "close": 60}
            ]
        }
        return Response(data,status=status.HTTP_200_OK)
    


#API VIEW FOR LINECHART
class LineChart(APIView):
    def get(self,request):
        data = {
            "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
            "data": [10, 20, 80, 40, 30, 60, 50, 90]
        }
        return Response(data,status=status.HTTP_200_OK)

#API VIEW FOR BAR CHART  
class BarChart(APIView):
    def get(self,request):
        data = {
            "labels": [" A", " B", " C", " D", " E"],
            "data": [100, 150, 200, 250, 300]
        }
        return Response(data,status=status.HTTP_200_OK)
    
#API VIEW FOR PIE CHART
class PieChart(APIView):
    def get(self,request):
        data = {
            "labels": ["Red", "Blue", "Yellow", "Green", "Purple"],
            "data": [300, 50, 100, 200, 150]
        }
        return Response(data,status=status.HTTP_200_OK)
    
