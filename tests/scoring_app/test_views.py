import pytest

from django.urls import reverse

pytestmark = pytest.mark.django_db



def test_view(client):
   url = reverse('game-list')
   response = client.get(url)
   assert response.status_code == 200
