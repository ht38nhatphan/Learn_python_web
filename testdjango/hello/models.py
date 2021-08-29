from django.db import models

# Create your models here.
#class link
class link(models.Model):
    linkfb = models.CharField(max_length=300)
    linktwitter = models.CharField(max_length=300)
    phone = models.CharField(max_length=30)
    mail = models.CharField(max_length=200,null=True)
    def __str__(self):
        return f"id : {self.id}"
#class hero
class hero(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return f"id : {self.id}"
#class about 
class about(models.Model):
    about_title = models.CharField(max_length=200)
    about_content = models.TextField()
#class process
class process(models.Model):
    process_title = models.CharField(max_length=200)
    process_content = models.TextField()
#class team
class team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    linkfb_team = models.CharField(max_length=300)
    linktwitter_team = models.CharField(max_length=300)
    phone_team = models.CharField(max_length=20)
    image_team = models.ImageField(null=True)
#class solutions
class solutions(models.Model):
    solutions_title = models.TextField()
    solutions_main_title = models.CharField(max_length=200)
    solutions_content = models.TextField()
    solutions_image = models.ImageField(null=True)
#class possibilities
class possibilities(models.Model):
    possibilities_title = models.TextField()
    possibilities_main_title = models.CharField(max_length=200)
    possibilities_content = models.TextField()
    possibilities_img1 = models.ImageField(null=True)
    possibilities_img2 = models.ImageField(null=True)
    possibilities_img3 = models.ImageField(null=True)
    possibilities_img4 = models.ImageField(null=True)
#class services
class services(models.Model):
    services_title = models.CharField(max_length=200)
    services_main_title = models.CharField(max_length=100)
    services_content = models.TextField()
    services_title_feature1 = models.CharField(max_length=200)
    services_content_feature1 = models.TextField()
    services_title_feature2 = models.CharField(max_length=200)
    services_content_feature2 = models.TextField()
    services_title_feature3 = models.CharField(max_length=200)
    services_content_feature3 = models.TextField()
    services_title_feature4 = models.CharField(max_length=200)
    services_content_feature4 = models.TextField(null=True)
#class footer
class footer(models.Model):
    footer_content = models.TextField()
    footer_title_tw = models.CharField(max_length=200)
    footer_main_title_tw = models.CharField(max_length=100)
    footer_main1_title_tw = models.CharField(max_length=200)
    footer_content_tw = models.TextField()
    footer_title_into = models.CharField(max_length=200)
    footer_content_into = models.TextField()