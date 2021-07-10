from django.test import TestCase
from .models import HappyIndexTable
from django.test import Client
import unittest

# testing to check whether the object created correctly or not
class HappyIndexTableTestCase1(TestCase):
    def setUp(self):
        # create new objects
        self.testobj1 = HappyIndexTable.objects.create(countryName="test1", ladderScore=1.1, healthyLifeExpectancy=1.1, generosity=1.1, gdp=1.1)
        self.testobj2 = HappyIndexTable.objects.create(countryName="test2", ladderScore=2.1, healthyLifeExpectancy=2.1, generosity=2.1, gdp=2.1)
       
    def test_happyindex1case1(self):
        self.assertEqual(self.testobj1.countryName, "test1")
        self.assertEqual(self.testobj1.gdp, 1.1)

    def test_happyindex1case2(self):
        self.assertNotEqual(self.testobj1.countryName, "wrong name")
        self.assertNotEqual(self.testobj1.gdp, 0.1)

    def test_happyindex2case1(self):
        self.assertEqual(self.testobj2.countryName, "test2")
        self.assertEqual(self.testobj2.ladderScore, 2.1)

    def test_happyindex2case2(self):
        self.assertNotEqual(self.testobj2.countryName, "wrong name")
        self.assertNotEqual(self.testobj2.ladderScore, 0.1)


# testing for the server request and response for first-endpoint
class HappyIndexByCountryName(unittest.TestCase):
    def setUp(self):
        # create new objects
        self.client = Client()  
        
    def test_details(self):
        # Make a GET request.
        response = self.client.get('/v1/country?country=Finland')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

# testing for the server request and response for the second end-point
class HappyIndexByLadderRange(unittest.TestCase):
    def setUp(self):
        # create new objects
        self.client = Client()  
        
    def test_details(self):
        # Make a GET request.
        response = self.client.get('/v1/score-range?from=1&to=10')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


