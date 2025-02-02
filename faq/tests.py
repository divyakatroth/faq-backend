from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a web framework.",
            language="en"
        )
        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.language, "en")