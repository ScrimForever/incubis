from ..core.database import Base
from sqlalchemy import Integer, String, ForeignKey, Column


class Equipe(Base):
    __tablename__ = "equipe"
    equipe_id = Column(Integer, primary_key=True, index=True)
    equipe_nome = Column(String, unique=True, nullable=True)

    def __str__(self):
        return str(self.equipe_id)
