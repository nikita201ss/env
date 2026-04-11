import pytest
from django.test import TestCase
from .models import Service, Category

class ServiceModelTest(TestCase):
    def test_service_creation(self):

        pass


@pytest.mark.django_db
def test_service_slug():

    pass