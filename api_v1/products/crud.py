# create
# read
# update
# delete
from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Product

from .schemas import ProductCreate, ProductUpdate


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()  # короче scalars надо
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product:
    product = Product(
        **product_in.model_dump()
    )  # kwagrs model_dump - преобразование в словарь
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def update_product(session: AsyncSession, product: Product, product_update: ProductUpdate) -> Product:
    for name, value in product_update.model_dump().items():
        setattr(product, name, value)
        await session.commit()
        return product



async def update_product_partial():
    pass