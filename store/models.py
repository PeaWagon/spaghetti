from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class Promotion(models.Model):
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    percent_discount = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=100),
        ],
        null=True,
    )


class Collection(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # if the Product class changes, also update this foreign key relationship
    # using + as the related_name means the reverse relationship to Product
    # for collection is not made
    # the related_name must be specified in any case, since collection is
    # already an attribute of the Product model (and attributes must be unique)
    featured_product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, related_name="+"
    )


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True)
    promotions = models.ManyToManyField(Promotion)


class MembershipTier(models.TextChoices):
    BRONZE = "B", _("bronze")
    SILVER = "S", _("silver")
    GOLD = "G", _("gold")


class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(unique=True, max_length=64)
    phone = models.PositiveBigIntegerField(
        validators=[
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
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    # association class to facilitate the many-to-many relationship between Product and Order
    quantity = models.PositiveSmallIntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    # since product prices can change, we want to save the price of the product
    # at the time it was ordered
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip_code = models.PositiveIntegerField(
        validators=[MinValueValidator(501), MaxValueValidator(999999999)]
    )


class Cart(models.Model):
    # cart creation datetime can be used to set an expiry datetime
    # auto_now_add was chosen over auto_now (only set created at instead
    # of last updated), because products should not be held indefinitely
    # in a cart
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    # association class to facilitate the many-to-many relationship between Product and Cart
    quantity = models.PositiveSmallIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
