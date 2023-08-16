from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):
    def get(self, request):
        name = "Algunos methodos necesitan login"
        return Response({"success": f"API Legal Bot is alive but '{name}'"})
