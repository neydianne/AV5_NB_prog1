import os
from dotenv import load_dotenv
from sqlalchemy import ForeignKey, create_engine, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import List

class Base(DeclarativeBase):
    pass


class Gato(Base):
    __tablename__ = "tabela_gato"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(40))
    raca: Mapped[str] = mapped_column(String(30))
    cor: Mapped[str] = mapped_column(String(15))
    vacinas: Mapped[List["Vacina"]] = relationship(back_populates="gato", cascade="all, delete-orphan")
    #Deleta as vacinas do gato quando o gato for deletado, pra não ficar vacinas órfãs no banco kkkkk ;P

class Vacina(Base):
    __tablename__ = "tabela_vacina"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    fornecedor: Mapped[str] = mapped_column(String(70))
    ml: Mapped[float] = mapped_column(Float)
    gato_id: Mapped[int] = mapped_column(ForeignKey("tabela_gato.id"))
    gato: Mapped["Gato"] = relationship(back_populates="vacinas")

#fiz uma função pra conectar no banco, se for mysql ele pega os dados do .env, se for sqlite ele conecta no arquivo local
def  conectar_db(escolha_db):
    if escolha_db == 1:
        load_dotenv()
        #Pega tudo os dados do arquivo .env
        host = os.getenv("MYSQL_HOST")
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        port = os.getenv("MYSQL_PORT")
        db = os.getenv("MYSQL_DATABASE")
        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        print("-> Conectando ao MySQL...")
        return create_engine(url)
    if escolha_db == 2:
        print("||-> Conectando ao SQLite local...||")
        return create_engine("sqlite:///vacinar_gato.db")
    else:
        print("Não sabe ler?")
        return 0 

print("||ESCOLHA O BANCO DE DADOS||\n" \
      "||1 - MySql               ||\n" \
      "||2 - SQLite              ||")
db = int(input("Insira sua escolha: "))

engine = conectar_db(db)
Base.metadata.create_all(engine)

while True:
    #Loop pra ficar repetindo bonitinho
    print("==============================")
    print("||           MENU           ||")
    print("|| 1 - INSERIR GATO         ||")
    print("|| 2 - INSERIR VACINA       ||")
    print("|| 3 - LISTAR DADOS         ||")
    print("|| 4 - EXCLUIR GATO         ||")
    print("|| 5 - EXCLUIR VACINA       ||")
    print("|| 6 - ALTERAR CONEXÃO      ||")
    print("|| 0 - SAIR                 ||")
    print("==============================")
    
    opcao = int(input("Insira sua escolha: "))
    #Auto-explicativo, se a opção for 0, ele sai do loop e encerra o programa
    if opcao == 0:
        print("Tchau Tchau")
        break
    #CAso ele queira trocar de banco
    elif opcao == 6:
        print("\n||1 - MySql | 2 - SQLite||")
        db = int(input("Qual banco deseja usar agora? "))
        engine = conectar_db(db)
        Base.metadata.create_all(engine)
        continue

    with Session(engine) as session:
        #Preenche os dados do gato e da commit no db
        if opcao == 1:
            nome = input("Nome do gato: ")
            raca = input("Raça: ")
            cor = input("Cor: ")
            novo_gato = Gato(nome=nome, raca=raca, cor=cor)
            session.add(novo_gato)
            session.commit()
            print(f"Gato '{nome}' registrado com sucesso! id = {id} :P")

        elif opcao == 2:
            #Escolhe gato, preenche vacina e faz commit no db
            gato_id = int(input("ID do gato que receberá a vacina: "))
            gato = session.get(Gato, gato_id)
            #O if gato ta ai pra garantir que o gato existe, se não existir ele não vai tentar registrar a vacina ai n dá erro
            if gato:
                nome_vac = input("Nome da Vacina: ")
                fornecedor = input("Fornecedor: ")
                ml = float(input("Quantidade (ml): "))
                nova_vacina = Vacina(nome=nome_vac, fornecedor=fornecedor, ml=ml, gato_id=gato.id)
                session.add(nova_vacina)
                session.commit()
                print("Vacina registrada com sucesso!")
            else:
                print("Gato não encontrado!")

        elif opcao == 3:
            #Cata tudo os gatos e suas vacinas e printa bonitinho
            #O query é tipo SELECT * FROM tabela_gato, e o .all() é pra pegar tudo mesmo
            gatos = session.query(Gato).all()
            print("\n||--- LISTA DE GATOS E VACINAS ---||")
            for g in gatos:
                print(f"[{g.id}] Gato: {g.nome} | Raça: {g.raca} | Cor: {g.cor}")
                if g.vacinas:
                    for v in g.vacinas:
                        print(f"   -> Vacina [{v.id}]: {v.nome} ({v.ml}ml) - {v.fornecedor}")
                else:
                    print("   -> Nenhuma vacina registrada.")

        elif opcao == 4:
            #Exclui o gato, se existir
            gato_id = int(input("Informe o ID do gato para excluir: "))
            gato = session.get(Gato, gato_id)
            if gato:
                session.delete(gato)
                session.commit()
                print("Gato excluído com sucesso!")
            else:
                print("Gato não encontrado.")

        elif opcao == 5:
            #Exclui a vacina, se existir
            vacina_id = int(input("Informe o ID da vacina para excluir: "))
            vacina = session.get(Vacina, vacina_id)
            if vacina:
                session.delete(vacina)
                session.commit()
                print("Vacina excluída com sucesso!")
            else:
                print("Vacina não encontrada.")
        
        else:
            print("Betinha não sabe ler ou não tem capacidade de digitar certo, tente novamente.")