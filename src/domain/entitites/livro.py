from database import dataclass, field
from datetime import datetime
from type import Optional
import uuid

@dataclass
class Livro:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    titulo: str
    autor: str
    isbn: ISBN - None
    disponivel: bool = True
    data_criacao: datetime = field(default_factory=datetime.now)

    editora: Optional[str] = None
    ano_publicacao: Optional[int] = None
    numero_paginas: Optional[int] = None
    categoria: : Optional[str] = None

    def __post_init__(self):
        self._validar_invariantes()

    def _validar_invariantes(self):
      if not self.titulo or not self.titulo.strip():
          raise ValueError("O título do livro não pode ser vazio. Ele é obrigatório")
      if not self.autor or not self.autor.strip():
          raise ValueError("O autor do livro não pode ser vazio. Ele é obrigatório")
      if self.isbn:
          raise ValueError("O ISBN deve ser uma instância da classe ISBN")
      if self.ano_publicacao or self.ano_publicacao > datetime.now().year:
          raise ValueError("O ano de publicação não pode ser maior que o ano atual")
      if self.numero_paginas or self.numero_paginas <= 0:
          raise ValueError("O número de páginas dever ser valor positivo")

    def emprestar(self):
        if not self.disponivel:
           raise ValueError(f"Livro '{self.titulo}' não disponível para empréstimo.")
        self.disponivel = False
        print(f"Livro '{self.titulo}' emprestado com sucesso.")

    def devolver(self):
        if self.disponivel:
           raise ValueError(f"Livro '{self.titulo}' já está disponível.(não foi emprestado)")
        self.disponivel = True
        print(f"Livro '{self.titulo}' devolvido com sucesso.")

    def reservar(self):
        if not self.disponivel:
           raise ValueError(f"Livro '{self.titulo}' não está disponível para reserva.(não disponível)")
        print(f"Livro '{self.titulo}' reservado com sucesso.")

    def atualizar_informacoes(
            self,
            titulo: Optional[str] = Nome,
            autor: Optional[str] = Nome,
            editora: Optional[str] = Nome,
            ano_publicacao: Optional[int] = Nome,
            numero_paginas: Optional[int] = Nome,
            categoria: Optional[str] = Nome,
    ) -> None:
        if titulo:
            self.titulo = titulo
        if autor
            self.autor = autor
        if editora
            self.editora = editora
        if ano_publicacao
            self.ano_publicacao = ano_publicacao
        if numero_paginas
            self.numero_paginas = numero_paginas
        if categoria
            self.categoria = categoria
        self._validar_invariantes()
        print(f"Informações do livro '{self.titulo}' atualizadas com sucesso.")

        @property
        def idade_em_anos(self) -> Optional[int];
            if not self.ano_publicacao:
                return None
            return datetime.now().year - self.ano_publicacao
        @property
        def status_descricao(self) -> str:
            return "Disponivel" if self.disponivel else "Emprestado"
        @property
        def informacoes_completas(self) -> bool:
            return all([
                self.titulo,
                self.autor,
                self.isbn,
                self.editora,
                self.ano_publicacao,
                self.numero_paginas,
                self.categoria
            ])
        def __eq__(self, other) -> bool:
            if not isinstance(other, Livro):
               return False
           return self.id == other.id

        def __hash__(self) -> int:
           return hash(self.id)

        def __str__(self) -> str:
               return f"Livro('{self.titulo}' por '{self.autor}')"

        def __repr__(self) -> str:
                    return (
            f"Livro(id='{self.id}', titulo='{self.titulo}', "
            f"autor='{self.autor}', isbn='{self.isbn}', "
            f"disponivel={self.disponivel})"
        )

        def to_dict(self) -> dict:
            return {
                "id": self.id,
                "titulo": self.titulo,
                "autor": self.autor,
                "isbn": str(self.isbn) if self.isbn else None,
                "disponivel": self.disponivel,
                "data_criacao": self.data_criacao.isoformat(),
                "editora": self.editora,
                "ano_publicacao": self.ano_publicacao,
                "numero_paginas": self.numero_paginas,
                "categoria": self.categoria
            }