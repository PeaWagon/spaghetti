from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class MembershipTier(models.TextChoices):
    BRONZE = "B", _("bronze")
    SILVER = "S", _("silver")
    GOLD = "G", _("gold")


class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(unique=True, max_length=64)
    phone = models.BigIntegerField(
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=int("9" * 15)),
        ]
    )
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MembershipTier.choices, default=MembershipTier.BRONZE
    )


class PaymentStatus(models.TextChoices):
    PENDING = "P", _("pending")
    COMPLETE = "C", _("complete")
    FAILED = "F", _("failed")


class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PaymentStatus.choices, default=PaymentStatus.PENDING
    )


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer, on_delete=models.CASCADE, primary_key=True
    )
