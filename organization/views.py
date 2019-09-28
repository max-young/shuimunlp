from rest_framework.views import APIView
from rest_framework.response import Response
from snownlp import SnowNLP


class TextAnalysisView(APIView):

    def post(self, request):
        file = request.data.get('file')
        text = file.read().decode('utf-8')
        s = SnowNLP(text)
        keywords = s.keywords(5)
        #  summary = s.summary(3)
        #  sentences = s.sentences
        sentiments = "{:.0%}".format(s.sentiments)
        return Response({'positive_probability': sentiments, 'keywords': keywords})
