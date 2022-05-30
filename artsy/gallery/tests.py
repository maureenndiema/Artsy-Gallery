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