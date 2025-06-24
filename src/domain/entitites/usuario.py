from dataclasses import dataclass, field
from typing import Optional
import uuid

@dataclass
class Usuario:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    nome: str = ""
    email: str = ""
    acessar: bool = False

    def __post_init__(self):
        self._validar_invariantes()

    def _validar_invariantes(self):
        if not self.nome or not self.nome.strip():
            raise ValueError("O nome do usuário não pode ser vazio. Ele é obrigatório.")
        if not self.email or not self.email.strip():
            raise ValueError("O e-mail do usuário não pode ser vazio. Ele é obrigatório.")

    def acesso(self):
        if self.acessar:
            raise ValueError(f"Usuário '{self.nome}' já está logado.")
        self.acessar = True
        print(f"Usuário '{self.nome}' logado com sucesso.")

    def atualizar_informacoes(self, nome: Optional[str] = None, email: Optional[str] = None) -> None:
        if nome:
            self.nome = nome
        if email:
            self.email = email
        self._validar_invariantes()
        print(f"Informações do usuário '{self.nome}' atualizadas com sucesso.")

    @property
    def informacoes_completas(self) -> bool:
        return all([
            bool(self.nome.strip()),
            bool(self.email.strip()),
            self.acessar
        ])

    def __eq__(self, other) -> bool:
        if not isinstance(other, Usuario):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __str__(self) -> str:
        return f"Usuário '{self.nome}' com e-mail '{self.email}'"

    def __repr__(self) -> str:
        return (
            f"Usuario(id='{self.id}', nome='{self.nome}', "
            f"email='{self.email}', acessar={self.acessar})"
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "acessar": self.acessar
        }