from ..core.database import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class Avaliacao(Base):
    __tablename__ = "avaliacao"
    avaliacao_id = Column(Integer, primary_key=True, index=True)
    avaliacao_escala = Column(String, unique=True, nullable=True)

    def __str__(self):
        return self.avaliacao_nome