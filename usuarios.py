from Banco import Banco

# ao tipo de sistema que 
# cria um elemento -> insert
#remove um elemento -> delete
#update de um elemento -> update
# busca um elemento -> select
# dá-se o nome de CRUD

class Usuario:

    def __init__(self, idusuario=0, nome="",telefone="",email="", usuario="",senha=""):
        self.info = {}
        self.idusuario=idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha
    
    def insertUser(self):

        banco = Banco()

        c = banco.conexao.cursor()
        comando = "insert into usuarios(nome, telefone,email,usuario, senha) values('"+ self.nome +"', '"+ self.telefone + "','"+ self.email +"','"+ self.usuario +"','"+ self.senha +"')"
        c.execute(comando)
        banco.conexao.commit()
        c.close()
    
    def deleteUser(self):
        banco = Banco()

        c = banco.conexao.cursor()
        comando = "delete from usuarios where idusuario = "+self.idusuario+ " "
        c.execute(comando)
        banco.conexao.commit()
        c.close()

    def selectUser(self, id):
        banco = Banco()

        c = banco.conexao.cursor()
        comando = "select * from usuarios where idusuario = " + str(id) + " "
        c.execute(comando)

        # c recebe uma lista com os atributos
        #exemplo ["2","claudio","1111","claudio@ufrj.br","claudio","123456"]

        print (c) #só para debug depois

        for elemento in c:
            self.idusuario = elemento[0]
            print(elemento[0])
            self.nome = elemento[1]
            print(elemento[1])
            self.telefone = elemento[2]
            print(elemento[2])
            self.email = elemento[3]
            print(elemento[3])
            self.usuario = elemento[4]
            print(elemento[4])
            self.senha = elemento[5]
            print(elemento[5])


        c.close()

    def updateUser(self):
        banco = Banco()

        c = banco.conexao.cursor()
        comando = "update usuarios set nome = '" + self.nome +"', telefone = '" + self.telefone +"', email = '"+self.email+"', usuario = '" +self.usuario+"',senha = '"+self.senha+"'where idusuario = "+self.idusuario+""
        c.execute(comando)
        banco.conexao.commit()
        c.close()