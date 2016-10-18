from django.test import TestCase

from hello_world.models import StuffToRate, Rating


class TestHelloWorld(TestCase):
    def setUp(self):
        obj = StuffToRate(title='my_thing', color='blue')
        obj.save()

    def test_stuff_rating(self):
        obj = StuffToRate.objects.get(id=1)

        r1 = Rating(rating=3, stuff=obj)
        r1.save()
        self.assertEqual(obj.get_rating(), 3)

        r2 = Rating(rating=5, stuff=obj)
        r2.save()
        self.assertEqual(obj.get_rating(), 4)
        self.assertEqual(type(obj.get_rating()), int)

    def test_stuff_rating_invalid(self):
        obj = StuffToRate.objects.get(id=1)

        r1 = Rating(rating=500, stuff=obj)
        self.assertRaises(r1.save)
