from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class TestImage(TestCase):
    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

        self.category = Category(name='nature')
        self.category.save_category()

        self.image_pic = Image(id=1, title='image', description='This is photo gallery test',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_pic, Image))    

    def test_save_image(self):
        self.image_pic.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_pic.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)   

    def test_update_image(self):
        self.image_pic.save_image()
        self.image_pic.update_image(self.image_pic.id, 'images/photo1.jpg')
        updated_image = Image.objects.filter(image='images/photo2.jpg')
        self.assertFalse(len(updated_image) > 0)

    def test_get_image_by_id(self):
        found_image = self.image_pic.get_image_by_id(self.image_pic.id)
        images = Image.objects.filter(id=self.image_pic.id)
        self.assertFalse(found_image, images)    

    def test_search_by_category(self):
        category = 'technology'
        found_img = self.image_pic.search_by_category(category)
        self.assertFalse(len(found_img) > 1)  
    
    def test_view_location(self):
        self.image_pic.save()
        location = Image.view_location(self.location)
        self.assertTrue(len(location) > 0) 

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(name='food')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))