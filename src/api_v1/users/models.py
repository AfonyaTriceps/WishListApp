# from src.db import Base
# from datetime import datetime
# from sqlalchemy.orm import Mapped, relationship, mapped_column
# from sqlalchemy import String, Integer, Enum
# from src.users.constants import Gender
#
#
# class User(Base):
#     first_name: Mapped[str] = mapped_column(String(50))
#     last_name: Mapped[str]
#     email: Mapped[str] = mapped_column(String(150))
#     birth_date: Mapped[datetime]
#     gender: Mapped[str] = mapped_column(Enum(Gender))
