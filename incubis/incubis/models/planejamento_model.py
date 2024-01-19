from ..core.database import Base
from sqlalchemy import Integer, Text, Column, ForeignKey


class Planejamento(Base):
    __tablename__ = "planejamento"
    planejamento_id = Column(Integer, primary_key=True, index=True)
    planejamento_texto = Column(Text, unique=True)

    def __str__(self):
        return self.planejamento_texto