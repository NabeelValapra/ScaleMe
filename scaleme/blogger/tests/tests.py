import pytest

@pytest.mark.django_db
class TestBlog:

    def test_url(self, client):
        response = client.get('/blogger/api/')
        assert response.status_code == 200
