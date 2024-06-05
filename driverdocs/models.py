from django.db import models

# Create your models here.

class Drivers(models.Model):
    dr_id = models.AutoField(primary_key=True, verbose_name="ID")
    dr_name = models.CharField(max_length=15, verbose_name="სახელი")
    dr_surname = models.CharField(max_length=25, verbose_name="გვარი")
    dr_email = models.EmailField(max_length=60, blank=True, null=True, verbose_name="ელ-ფოსტა")
    birth_date = models.DateField(blank=True, null=True, verbose_name="დაბადების თარიღი")
    dr_personal = models.CharField(max_length=11, null=True, verbose_name="პირადი ნომერი")
    dr_phone = models.CharField(max_length=12, null=True, verbose_name="ტელეფონი")

    def __str__(self):
        return str(self.dr_name) + " " + str(self.dr_surname)

    def display_time(self):
        time1 = self.birth_date.strftime("%d.%m.%Y")
        return time1

    class Meta:
        managed = True
        verbose_name_plural = "მძღოლები"


class DriverDocCategories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=45, verbose_name="კატეგორია")


    def __str__(self):
        return str(self.cat_name)


    class Meta:
        managed = True
        verbose_name_plural = "მძღოლის საბუთების კატეგორიები"

class Documents(models.Model):
    doc_id = models.AutoField(primary_key=True)
    dr_id = models.ForeignKey(Drivers, null=True, on_delete=models.CASCADE, verbose_name="მძღოლი")
    doc_number = models.CharField(max_length=12, default="", verbose_name="დოკუმენტის ნომერი")
    doc_category = models.ForeignKey(DriverDocCategories, on_delete=models.PROTECT, verbose_name="დოკუმენტის კატეგორია")
    doc_given = models.DateField(verbose_name="გაცემის თარიღი")
    doc_expire = models.DateField(verbose_name="Expire date")
    relevance = models.BooleanField(default=True, verbose_name="აქტუალურობა")
    doc_path = models.FileField(upload_to="uploads/docs", verbose_name="ფაილი")

    class Meta:
        managed = True
        verbose_name_plural = "მძღოლის საბუთები"

    def display_given_day(self):
        time0 = self.doc_given.strftime("%d.%m.%Y")
        return time0

    def display_day(self):
        time1 = self.doc_expire.strftime("%d.%m.%Y")
        return time1