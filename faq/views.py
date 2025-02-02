from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from googletrans import Translator

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')  # Default to English
        translator = Translator()
        faqs = self.get_queryset()
        translated_faqs = []

        for faq in faqs:
            try:
                # Translate question and answer
                translated_question = translator.translate(faq.question, dest=lang).text
                translated_answer = translator.translate(faq.answer, dest=lang).text
            except:
                # Fallback to original text if translation fails
                translated_question = faq.question
                translated_answer = faq.answer

            translated_faqs.append({
                'id': faq.id,
                'question': translated_question,
                'answer': translated_answer,
                'language': lang,
            })

        return Response(translated_faqs)