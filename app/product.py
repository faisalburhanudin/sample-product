from collections import namedtuple
from typing import Optional

from app.exception import ProductNotFound
from app.model import Product, db


def create(name: str, price: int) -> Product:
    """Create product

    Args:
        name: name of product
        price: price of product

    Returns:
        Product object
    """
    p = Product(name, price)
    db.session.add(p)
    db.session.commit()
    return p


def get_by_id(product_id: int) -> Optional[Product]:
    """Get product by id

    Args:
        product_id: id product

    Returns:
        Product object
    """
    return Product.query.filter_by(id=product_id).first()


def delete(product_id: int):
    """Delete product by id"""
    p = get_by_id(product_id)
    if not p:
        raise ProductNotFound

    db.session.delete(p)
    db.session.commit()


def update(product_id: int, name: str = None, price: int = None) -> Product:
    """Update product

    Args:
        product_id: id product will be update
        name: new name product
        price: new price product

    Returns:
        new Product object
    """
    p = get_by_id(product_id)
    if not p:
        raise ProductNotFound

    if name is not None:
        p.name = name

    if price is not None:
        p.price = price

    db.session.add(p)
    db.session.commit()
    return p


ListProduct = namedtuple("ListProduct", "items has_next has_prev")


def list_product(page=1, per_page=10) -> ListProduct:
    """Get list pof product

    Args:
        page: get on page
        per_page: item per page

    Returns:
        List of product
    """
    paginate = Product.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return ListProduct(
        items=paginate.items,
        has_next=paginate.has_next,
        has_prev=paginate.has_prev
    )
