import pymysql

def conectar():
    return pymysql.connect(
        host="localhost",
        user="root",
        database="EstoqueDb",
        charset="utf8mb4",
        port=3306,
        autocommit=True
    )

conexao = conectar()
conexao.close()

def inserir_produto(nome, categoria, preco, quantidade, fornecedor):
    with conectar() .cursor() as cursor:
        cursor.execute("""
            INSERT INTO PRODUTO (nome, categoria, preco, quantidade, fornecedor)           
            VALUES (%s, %s, %s, %s, %s)
    """, (nome, categoria, preco, quantidade, fornecedor))
        
def listar_produtos():
    conexao = conectar()
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM produtos")
        dados = cursor.fetchall()
    conexao.close()
    return dados
def atualizar_produto(id_produto, nome, categoria, preco, quantidade, fornecedor):
    with conectar().cursor() as cursor:
        cursor.execute("""
            UPDATE PRODUTO
        SET nome=%s, categoria=%s, preco=%s, quantidade=%s, fornecedor=%s
        WHERE id_produto=%s
    """, (nome, categoria, preco, quantidade, fornecedor, id_produto))
def excluir_produto(id_produto):
    with conectar().cursor() as cursor:
        cursor.execute("DELETE FROM PRODUTO WHERE id_produto=%s", (id_produto,))