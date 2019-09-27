from rest_framework.views import APIView
from rest_framework.response import Response


class TextAnalysisView(APIView):

    def post(self, request):
        import pdb
        pdb.set_trace()
        return Response({'message': 'hello world'})
