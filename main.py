from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import sessionmaker, relationship, DeclarativeBase, Mapped, mapped_column

engine = create_engine('sqlite:///shop.db')
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user_table'

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(50))
    email : Mapped[str] = mapped_column(String(100), unique=True)

class Product(Base):
    __tablename__ = 'product_table'

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(100))
    price : Mapped[float] = mapped_column()

class Order(Base):
    __tablename__ = 'order_table'

    id : Mapped[int] = mapped_column(primary_key=True)
    user_id : Mapped[int] = mapped_column(ForeignKey('user_table.id'))
    product_id : Mapped[int] = mapped_column(ForeignKey('product_table.id'))
    quantity : Mapped[int] = mapped_column()

    user : Mapped['User'] = relationship('User', backref='orders')
    product : Mapped['Product'] = relationship('Product', backref='orders')

Base.metadata.create_all(engine)

user1 = session.query(User).filter_by(
    email="darwin@email.com"
).first()

if user1 is None:
    user1 = User(
        name="Darwin",
        email="darwin@email.com"
    )
    session.add(user1)

user2 = session.query(User).filter_by(
    email="victoria@email.com"
).first()

if user2 is None:
    user2 = User(
        name="Victoria",
        email="victoria@email.com"
    )
    session.add(user2)


product1 = session.query(Product).filter_by(
    name="Laptop"
).first()

if product1 is None:
    product1 = Product(
        name="Laptop",
        price=1200.00
    )
    session.add(product1)

product2 = session.query(Product).filter_by(
    name="Smartphone"
).first()

if product2 is None:
    product2 = Product(
        name="Smartphone",
        price=800.00
    )
    session.add(product2)

product3 = session.query(Product).filter_by(
    name="Headphones"
).first()

if product3 is None:
    product3 = Product(
        name="Headphones",
        price=150.00
    )
    session.add(product3)


if session.query(Order).count() == 0:
    order1 = Order(user=user1, product=product1, quantity=1)
    order2 = Order(user=user1, product=product2, quantity=2)
    order3 = Order(user=user2, product=product3, quantity=3)
    order4 = Order(user=user2, product=product1, quantity=1)

    session.add_all([order1, order2, order3, order4])
    session.commit()


users = session.query(User).all()
for user in users:
     print(f"User: {user.name}, Email: {user.email}")

products = session.query(Product).all()
for product in products:
    print(f"Product: {product.name}, Price: {product.price}")
    
orders = session.query(Order).all()
for order in orders:
    print(f"Order ID: {order.id}, User: {order.user.name}, Product: {order.product.name}, Quantity: {order.quantity}")

product_to_update = session.get(Product, 1)

if product_to_update:
     print(f"Old price: ${product_to_update.price:.2f}")

     product_to_update.price = 1000.00
     session.commit()

     print(f"New price: ${product_to_update.price:.2f}")
else:
     print("Product not found.")

user_id_to_delete = 2

user_to_delete = session.get(User, user_id_to_delete)

if user_to_delete:
     session.query(Order).filter_by(
         user_id=user_id_to_delete
     ).delete()

     session.delete(user_to_delete)
     session.commit()

     print(f"User with ID {user_id_to_delete} was deleted.")
else:
    print(f"User with ID {user_id_to_delete} was not found.")

remaining_users = session.query(User).all()
for user in remaining_users:
    print(f"Remaining User: {user.name}, Email: {user.email}")




