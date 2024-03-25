import pytest
from app.schemas.product import Product


def test_product_schema():
    product = Product(
        name="Product Name",
        slug="product-name",
        price=22.99,
        stock=22,
    )

    assert product.dict() == {
        "name": "Product Name",
        "slug": "product-name",
        "price": 22.99,
        "stock": 22,
    }


def test_product_schema_invalid_slug():
    with pytest.raises(ValueError):
        Product(
            name="Produto de Cama",
            slug="produto de cama",
            price=22.99,
            stock=22,
        )

    with pytest.raises(ValueError):
        Product(
            name="Produto",
            slug="cão",
            price=22.99,
            stock=22,
        )

    with pytest.raises(ValueError):
        Product(
            name="Produto",
            slug="Produto",
            price=22.99,
            stock=22,
        )


def test_product_schema_invalid_price():
    with pytest.raises(ValueError):
        Product(
            name="Produto",
            slug="Produto",
            price=0,
            stock=22,
        )
