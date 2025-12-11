"""Data models for PWA product tests."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Product:
    """Model for e-commerce product."""

    name: str
    price: float
    description: Optional[str] = None
    sku: Optional[str] = None
    quantity: int = 1


@dataclass
class CartItem:
    """Model for item in shopping cart."""

    product: Product
    quantity: int = 1

    @property
    def total_price(self) -> float:
        """Calculate total price for this cart item."""
        return self.product.price * self.quantity
