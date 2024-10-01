from django.db import models


class Banner(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='banner_images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return settings.API_URL + self.image.url
        else:
            return ''