from abc import ABC, abstractmethod

# Interface base para exames
class Exame(ABC):
    @abstractmethod
    def aprovar(self):
        pass


# Exame de sangue
class ExameSangue(Exame):
    def aprovar(self):
        # Aqui você coloca a lógica de aprovação específica
        print("Exame de sangue aprovado!")


# Exame de raio-x
class ExameRaioX(Exame):
    def aprovar(self):
        # Aqui você coloca a lógica de aprovação específica
        print("Exame de raio-x aprovado!")


# Classe que processa a aprovação (sem precisar conhecer os tipos)
class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: Exame):
        exame.aprovar()


# Exemplo de uso
if __name__ == "__main__":
    aprovador = AprovaExame()

    exame_sangue = ExameSangue()
    exame_raio_x = ExameRaioX()

    aprovador.aprovar_solicitacao_exame(exame_sangue)
    aprovador.aprovar_solicitacao_exame(exame_raio_x)
