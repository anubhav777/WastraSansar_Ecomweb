from unittest import TestCase
from _pytest.mark import param
from django.test import Client
import pytest
import json
from django.conf import settings
from products.models import Product,Brand
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from products.files import allowed_image
from fixtures import time_tracker
#Unit Test



# @pytest.mark.django_db
# class ParentTest(TestCase):
#     def setUp(self) -> None:
#         self.client = APIClient()



# class TestProducts(ParentTest):
#     def test_all_product(self)->None:
#         prod = Product.objects.create(name='New prod',brand='nike',price = 90,category='Men',subcategory='Men',size='L',discription='fck',status='Instock',discount=0,picture={
#     "1": "Men_4.jpg"
# },specs = {})
#         product_url = 'http://127.0.0.1:8000/pages/getproduct/'
#         response = self.client.get(product_url)
        
#         response_content = json.loads(response.content)['data'][0]
#         self.assertEqual(response.status_code,200)
#         self.assertEqual(response_content.get('name'),'New prod')

# class TestPostBrand(ParentTest):
#     def test_empty_post(self)-> None:
#         user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom',is_superuser=True)
#         refresh = RefreshToken.for_user(user)
#         self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
#         new_response = self.client.post(path='http://127.0.0.1:8000/pages/brandat/')
#         new_response_content = json.loads(new_response.content)
#         print(new_response_content)
#         self.assertEqual(new_response.status_code,200)
#         self.assertEqual(new_response_content.get('status'),'data are invalid')

#     def test_staff_insert(self)->None:
#         user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom')
#         refresh = RefreshToken.for_user(user)
#         self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
#         new_response = self.client.post(path='http://127.0.0.1:8000/pages/brandat/',data={'brandname':'levis','category':'men'})
#         new_response_content = json.loads(new_response.content)
#         print(new_response_content)
#         self.assertEqual(new_response.status_code,200)
#         self.assertEqual(new_response_content.get('status'),'user not permitted')
    
#     def test_post_branch(self)->None:
#         user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom',is_superuser=True)
#         refresh = RefreshToken.for_user(user)
#         self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
#         new_response = self.client.post(path='http://127.0.0.1:8000/pages/brandat/',data={'brandname':'levis','category':'men'})
#         new_response_content = json.loads(new_response.content)
#         self.assertEqual(new_response.status_code,200)
#         self.assertEqual(new_response_content.get('status'),'sucess')

# class TestDeleteBrand(ParentTest):
#     def test_delete_brand_empty_id(self)->None:
#         user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom',is_superuser=True)
#         refresh = RefreshToken.for_user(user)
#         new_brand=Brand.objects.create(brandname = 'levis',category='men')
#         self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
#         response = self.client.delete('http://127.0.0.1:8000/pages/brandat/')
#         new_response_content = json.loads(response.content)
#         self.assertEqual(response.status_code,200)
#         self.assertEqual(new_response_content.get('status'),'id not provided')

#     def test_delet_not_admin(self)->None:
#         user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom')
#         refresh = RefreshToken.for_user(user)
#         new_brand=Brand.objects.create(brandname = 'levis',category='men')
#         self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
#         response = self.client.delete('http://127.0.0.1:8000/pages/brandat/')
#         new_response_content = json.loads(response.content)
#         self.assertEqual(response.status_code,200)
#         self.assertEqual(new_response_content.get('status'),'you do not provide privilege')
    
#     def test_delet_admin(self)->None:
#         user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom',is_superuser=True)
#         refresh = RefreshToken.for_user(user)
#         new_brand=Brand.objects.create(brandname = 'levis',category='men',id=1)
#         self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}',)
#         response = self.client.delete('http://127.0.0.1:8000/pages/brandat/',param=None,HTTP_ID=1)
#         new_response_content = json.loads(response.content)
#         self.assertEqual(response.status_code,200)
#         self.assertEqual(new_response_content.get('status'),'success')




#Pytest

@pytest.fixture
def api_client():
    client = APIClient()
    return client

pytestmark = pytest.mark.django_db


def test_all_product(api_client)->None:
        prod = Product.objects.create(name='New prod',brand='nike',price = 90,category='Men',subcategory='Men',size='L',discription='fck',status='Instock',discount=0,picture={
    "1": "Men_4.jpg"
},specs = {})
        product_url = 'http://127.0.0.1:8000/pages/getproduct/'
        response = api_client.get(product_url)
        
        response_content = json.loads(response.content)['data'][0]
        assert response.status_code == 200
        assert response_content.get('name') =='New prod'


def test_empty_post(api_client)-> None:
        user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom',is_superuser=True)
        refresh = RefreshToken.for_user(user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        new_response = api_client.post(path='http://127.0.0.1:8000/pages/brandat/')
        new_response_content = json.loads(new_response.content)
        print(new_response_content)
        assert new_response.status_code == 200
        assert new_response_content.get('status') == 'data are invalid'


def test_staff_insert(api_client)->None:
        user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom')
        refresh = RefreshToken.for_user(user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        new_response = api_client.post(path='http://127.0.0.1:8000/pages/brandat/',data={'brandname':'levis','category':'men'})
        new_response_content = json.loads(new_response.content)
        print(new_response_content)
        assert new_response.status_code == 200
        assert new_response_content.get('status')=='user not permitted'

 
def test_post_branch(api_client)->None:
        user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom',is_superuser=True)
        refresh = RefreshToken.for_user(user)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        new_response = api_client.post(path='http://127.0.0.1:8000/pages/brandat/',data={'brandname':'levis','category':'men'})
        new_response_content = json.loads(new_response.content)
        assert new_response.status_code==200
        assert new_response_content.get('status')=='sucess'


def test_delete_brand_empty_id(api_client)->None:
        user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom',is_superuser=True)
        refresh = RefreshToken.for_user(user)
        new_brand=Brand.objects.create(brandname = 'levis',category='men')
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.delete('http://127.0.0.1:8000/pages/brandat/')
        new_response_content = json.loads(response.content)
        assert response.status_code == 200
        assert new_response_content.get('status')== 'id not provided'

def test_delet_not_admin(api_client)->None:
        user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom')
        refresh = RefreshToken.for_user(user)
        new_brand=Brand.objects.create(brandname = 'levis',category='men')
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = api_client.delete('http://127.0.0.1:8000/pages/brandat/')
        new_response_content = json.loads(response.content)
        assert response.status_code == 200
        assert new_response_content.get('status') == 'you do not provide privilege'


def test_delet_admin(api_client)->None:
        user = User.objects.create_user(email='genji@gmail.com',username='magaranub', password='tom',is_superuser=True)
        refresh = RefreshToken.for_user(user)
        new_brand=Brand.objects.create(brandname = 'levis',category='men',id=1)
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}',)
        response = api_client.delete('http://127.0.0.1:8000/pages/brandat/',param=None,HTTP_ID=1)
        new_response_content = json.loads(response.content)
        assert response.status_code == 200
        assert new_response_content.get('status') == 'success'



##function testing
@pytest.mark.parametrize('name,expected',[('pic.png',True),('pic.mp4',False),('noextension',False)])
def test_image_extension(time_tracker,name:str, expected:bool):
        res = allowed_image(name)
        assert res == expected