from ..core.database import Base
from sqlalchemy import Integer, String, Column

class Setor(Base):
    __tablename__ = "setor"

    setor_id = Column(Integer, primary_key=True, index=True)
    setor_nome = Column(String, unique=True)
    setor_descricao = Column(String, nullable=True)

    def __str__(self):
        return self.setor_nome