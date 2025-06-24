from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
import uuid

@dataclass
class Emprestimo:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    id_livro: str = ""
    id_usuario: str = ""
    dt_emprestimo: datetime = field(default_factory=datetime.now)
    dt_devolucao: Optional[datetime] = None
    disponivel: bool = True

    def __post_init__(self):
        if not self.id_livro:
            raise ValueError("Identificador do livro é obrigatório")
        if not self.id_usuario:
            raise ValueError("Identificador do usuário é obrigatório")

    def emprestar(self):
        if not self.disponivel:
            raise ValueError(f"O livro com ID '{self.id_livro}' já está emprestado.")
        self.dt_emprestimo = datetime.now()
        self.disponivel = False
        print(f"Livro com ID '{self.id_livro}' emprestado com sucesso para o usuário '{self.id_usuario}'.")

    def devolver(self):
        if self.disponivel:
            raise ValueError(f"O livro com ID '{self.id_livro}' já está disponível (não está emprestado).")
        self.dt_devolucao = datetime.now()
        self.disponivel = True
        print(f"Livro com ID '{self.id_livro}' devolvido com sucesso.")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Emprestimo):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)