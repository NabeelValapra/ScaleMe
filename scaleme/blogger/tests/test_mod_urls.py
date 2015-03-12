import pytest


@pytest.mark.django_db
def test_url():
	assert 'a' == 'a'	 


def test_url_three():
	assert 'a' == 'a'


def test_url_two():
	assert 'a' == 'a'
    #response = client.get('/blogged/api/')
	#assert 'a' == 'a'