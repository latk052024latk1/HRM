from django.db import models
from driverdocs.models import Drivers
# Create your models here.

class DocCategories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=45, verbose_name="კატეგორია")

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name_plural = "დოკუმენტების კატეგორიები"

class Cars(models.Model):
    car_id = models.AutoField(primary_key=True, verbose_name="ID")
    car_reg_number = models.CharField(max_length=8, verbose_name="სახელმწიფო ნომერი")
    car_vin = models.CharField(max_length=17, verbose_name="VIN")
    car_photo = models.ImageField(upload_to="uploads/car_photo", null=True, blank=True, verbose_name="ფაილი")
    driver = models.OneToOneField(Drivers, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.car_reg_number

    class Meta:
        verbose_name_plural = "მანქანები"

class CarDocuments(models.Model):
    car_doc_id = models.AutoField(primary_key=True)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, verbose_name="მანქანის ID")
    car_doc_number = models.CharField(max_length=22, verbose_name="დოკუმენტის ნომერი")
    car_doc_category = models.ForeignKey(DocCategories, on_delete=models.PROTECT, verbose_name="კატეგორია")
    car_doc_given = models.DateField(verbose_name="გაცემის თარიღი")
    car_doc_expire = models.DateField(verbose_name="მოქმედების ვადა")
    relevance = models.BooleanField(default=True, verbose_name="აქტუალურობა")
    car_doc_path = models.FileField(upload_to="uploads/car_docs", verbose_name="ფაილი")

    class Meta:
        verbose_name_plural = "მანქანის დოკუმენტები"

    def display_given_day(self):
        time0 = self.car_doc_given.strftime("%d.%m.%Y")
        return time0

    def display_expire_day(self):
        time1 = self.car_doc_expire.strftime("%d.%m.%Y")
        return time1

class Trailers(models.Model):
    trailer_id = models.AutoField(primary_key=True, verbose_name="ID")
    trailer_reg_number = models.CharField(max_length=8, verbose_name="სახელმწიფო ნომერი")
    trailer_vin = models.CharField(max_length=17, verbose_name="VIN")
    trailer_photo = models.ImageField(upload_to="uploads/trailer_photo", null=True, blank=True, verbose_name="ფაილი")
    car = models.OneToOneField(Cars, on_delete=models.CASCADE)

    def __str__(self):
        return self.trailer_reg_number


    class Meta:
        verbose_name_plural = "ტრეილერები"

class TrailerDocuments(models.Model):
    trailer_doc_id = models.AutoField(primary_key=True)
    trailer = models.ForeignKey(Trailers, on_delete=models.CASCADE, verbose_name="ტრეილერის ID")
    trailer_doc_number = models.CharField(max_length=22, verbose_name="დოკუმენტის ნომერი")
    trailer_doc_category = models.ForeignKey(DocCategories, on_delete=models.PROTECT, verbose_name="კატეგორია")
    trailer_doc_given = models.DateField(verbose_name="გაცემის თარიღი")
    trailer_doc_expire = models.DateField(verbose_name="მოქმედების ვადა")
    relevance = models.BooleanField(default=True, verbose_name="აქტუალურობა")
    trailer_doc_path = models.FileField(upload_to="uploads/trailer_docs", verbose_name="ფაილი")

    class Meta:
        verbose_name_plural = "ტრეილერის დოკუმენტები"
