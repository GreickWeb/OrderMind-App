from sqlalchemy import create_engine, Column, String, Boolean, Integer, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime


db = create_engine("sqlite:///meubanco2.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "Usuarios"

    user_id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    name_user = Column(String, unique=True, nullable=True)
    email = Column(String, unique=True, nullable=True)
    datanascimento = Column(DateTime, nullable=True)
    senha = Column(String)
    nacionalidade = Column(String, nullable=True)
    pontos = Column(Integer, ForeignKey("Ranking.pontuacao"))  # Ajuste necessário para evitar erro de FK

    def __init__(self, name_user, email, datanascimento, senha, nacionalidade, pontos=0):
        self.name_user = name_user
        self.email = email
        self.datanascimento = datanascimento
        self.senha = senha
        self.nacionalidade = nacionalidade
        self.pontos = pontos

class Tarefa(Base):
    __tablename__ = "tarefas"

    task_id = Column(Integer, autoincrement=True, primary_key=True)
    usuarioid = Column(Integer, ForeignKey("Usuarios.user_id"))
    nometarefa = Column(String)
    tipo_tarefa = Column(String)
    desc_tarefa = Column(String)
    data_tarefa = Column(DateTime)

    def __init__(self, usuarioid, nometarefa, tipo_tarefa, desc_tarefa, data_tarefa):
        self.usuarioid = usuarioid
        self.nometarefa = nometarefa
        self.tipo_tarefa = tipo_tarefa
        self.desc_tarefa = desc_tarefa
        self.data_tarefa = data_tarefa

class Ranking(Base):
    __tablename__ = "Ranking"

    id = Column(Integer, autoincrement=True, primary_key=True)
    pontuacao = Column(Integer)
    posicao = Column(Integer)
    nacao = Column(String, ForeignKey("Usuarios.nacionalidade"))
    nome_usuario = Column(String, ForeignKey("Usuarios.name_user"))

    def __init__(self, pontuacao, posicao, nacao, nome_usuario):
        self.pontuacao = pontuacao
        self.posicao = posicao
        self.nacao = nacao
        self.nome_usuario = nome_usuario

class Agenda(Base):
    __tablename__ = "Agenda"
    id_agenda = Column(Integer, autoincrement=True, primary_key=True)  # Adicionando chave primária
    prazo = Column(DateTime, ForeignKey("tarefas.data_tarefa"))
    tipo_da_tarefa = Column(String, ForeignKey("tarefas.tipo_tarefa"))
    descricao = Column(String, ForeignKey("tarefas.desc_tarefa"))
    id_task = Column(Integer, ForeignKey("tarefas.task_id"))

    def __init__ (self, prazo, tipo_da_tarefa, descricao, id_task):
        self.prazo = prazo
        self.tipo_da_tarefa = tipo_da_tarefa
        self.descricao = descricao
        self.id_task = id_task

class Friend(Base):
    __tablename__ = "Friends"

    friend_id = Column(Integer, autoincrement=True, primary_key=True)
    nomeamigo = Column(String, ForeignKey("Usuarios.name_user"))
    idamigo = Column(Integer, ForeignKey("Usuarios.user_id"))
    status = Column(Boolean, default=False)
    start_friend = Column(DateTime)

    def __init__(self, nomeamigo, idamigo, start_friend, status=False):
        self.nomeamigo = nomeamigo
        self.idamigo = idamigo
        self.status = status
        self.start_friend = start_friend

Base.metadata.create_all(bind=db)

#Read - Filtrando, buscando e lendo dados pelo python
# lista_usuarios = session.query(Usuario).filter_by(email= "johndoe@example.com").first()
# print(lista_usuarios)
# print(lista_usuarios.name_user)
# print(lista_usuarios.email )



# session.add(novo_usuario3)
# session.commit()
# session.close()
# print("Instância 3 executada!")


# # Adicionando o novo usuário à sessão
# session.add(novo_usuario)

# # Confirmando a transação
# session.commit()
# session.close()

# novo_usuario = Usuario(
#     name_user="John Doe",
#     email="johndoe@example.com",
#     datanascimento=datetime.strptime("18/12/2002", "%d/%m/%Y"),  # Convertendo string para datetime
#     senha="senha_secreta",
#     nacionalidade="Brasileiro",
#     pontos=10
# )

# session.commit()
# session.close()


# Adicionando o usuário
#CRUD = Create, Read, Update and delete

#Create - Criando dados
# user = Usuario(name_user= "greick", email= "Greickguilherme@gmail.com", datanascimento= "07/09/2006", senha= 1231, nacionalidade= "Brasileiro")
# session.add(user)
# session.commit()


# Create 2 - criando tarefa e aplicando a foreing key
# tarefa = Tarefa(nometarefa= "organizar os livros", tipo_tarefa= "Alta importância", desc_tarefa="Tirar os livros da cama e da mesa, para colocar eles na prateleira adequada.", data_tarefa= "15/11/24", usuarioid=usergreick.user_id)

#Read - Filtrando, buscando e lendo dados pelo python
# usergreick = session.query(Usuario).all()
# usergreick = session.query(Usuario).filter_by(nacionalidade = "Brasileiro").all()
# print(usergreick)
# print(usergreick.nacionalidade)
# print(usergreick.email)
#Updadte - Atualizando o nome do usuário para Guilherme Greick

# usergreick.name_user = Guilherme Greick
# session.add(usergreick)
# session.commit()

# lista_usuarios.pontos = 20
# session.add(lista_usuarios)
# session.commit()

# Delete - Deletando o usuário 2
# userd = session.query(Usuario).filter_by(name_user = "John greick").first()
# print(userd)
# print(userd.name_user)
# session.delete(userd)
# session.commit()



