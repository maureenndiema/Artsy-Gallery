from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
       return self.name

    def save_location(self):
        self.save()

    @classmethod
    def get_location(cls):
        location = Location.objects.all()
        return location    
    
    @classmethod
    def upt_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
    
    def del_location(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete() 

class Image(models.Model):
    image = models.ImageField(upload_to='images/',default='SOMETHING STRONG')
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=30,null=False,blank=False)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    update = models.DateTimeField(auto_now_add=False,auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE) 
    location = models.ForeignKey(Location,on_delete=models.CASCADE,default=1)  


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']

    def save_image(self):
        self.save() 

    def delete_image(self):
        self.delete()   

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)        

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image      


        
        

