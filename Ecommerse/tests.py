from django.test import TestCase
from .models import User, Profile, Photo, Product

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name="Erkin", last_name="Amirov", email="erkinamirov008@example.com", password="erkin008")

    def test_user_str(self):
        user = User.objects.get(first_name="Erkin")
        self.assertEqual(str(user), "Erkin")



class ProfileTestCase(TestCase):
    def setUp(self):
        Profile.objects.create(phone_number=935559988, who="customer", telegram_username="erkin")

    def test_profile_creation(self):
        profile = Profile.objects.get(telegram_username="erkin")
        self.assertEqual(profile.phone_number, 935559988)
        self.assertEqual(profile.who, "customer")
        self.assertEqual(profile.telegram_username, "erkin")

class ProductTestCase(TestCase):
    def setUp(self):
        photo = Photo.objects.create(image="test_image.jpg")
        Product.objects.create(title="Test Image", price="21", description="This is test image", availability=True, category="category1", size="M")
        product = Product.objects.get(title="Test Image")
        product.photos.add(photo)

    def test_product_str(self):
        product = Product.objects.get(title="Test Image")
        self.assertEqual(str(product), "Test Image")

class PhotoTestCase(TestCase):
    def setUp(self):
        Photo.objects.create(image="test_image.jpg")

    def test_photo_str(self):
        photo = Photo.objects.get(image="test_image.jpg")
        self.assertEqual(str(photo), "test_image.jpg")


