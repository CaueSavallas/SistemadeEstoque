import streamlit as st
from crud import inserir_produto, listar_produtos, atualizar_produto, excluir_produto

st.set_page_config(page_title="Sistema de Estoque", layout="wide")

st.title("Sistema de Estoque de Produtos")

menu = st.sidebar.selectbox("Menu", ["Inserir Produto", "Ver Produtos", "Atualizar Produto", "Excluir Produto"])

if menu == "Inserir Produto":
    st.subheader("Inserir Produto")
    nome = st.text_input("Nome do Produto")
    categoria = st.text_input("Categoria")
    preco = st.number_input("Preço")
    quantidade = st.text_input("Quantidade")
    fornecedor = st.text_input("Fornecedor")
    if st.button("Salvar"):
        if nome:
            inserir_produto(nome, categoria, preco, quantidade, fornecedor)
            st.success("Produto inserido com sucesso!")

        else:
            st.waring("Nome do produto é obrigatorio.")

elif menu == "Ver Produtos":
    st.subheader("Todos os Produtos no Estoque")
    dados = listar_produtos()
    st.dataframe(dados,  use_container_width=True)

elif menu == "Atualizar Produto":
    st.subheader("Atualizar Produtos")

    dados = listar_produtos()

    if not dados:
        st.warning("Nenhum produto cadastrado.")
    else:
        produtos = {f"{p[0]} - {p[1]}": p for p in dados}

        escolhido = st.selectbox("Escolha um produto", list(produtos.keys()))
        p = produtos[escolhido]

        novo_nome = st.text_input("Nome", value=p[1])
        nova_categoria = st.text_input("Categoria", value=p[2])
        novo_preco = st.number_input("Preço", value=float(p[3]), format="%.2f")
        nova_quantidade = st.number_input("Quantidade", value=p[4])
        novo_fornecedor = st.text_input("Fornecedor", value=p[5])

    if st.button("Atualizar"):
        atualizar_produto(p[0], novo_nome, nova_categoria, novo_preco, nova_quantidade, novo_fornecedor)
        st.success("Produto atualizado.")

elif menu == "Excluir Produto":
    st.subheader("Excluir Produtos")
    dados = listar_produtos()
    produtos = {f"{p[0]} - {p[1]}": p[0] for p in dados}
    escolhido = st.selectbox("Escolha o produto para excluir", list(produtos.keys()))
    if st.button("Excluir Produto"):
        excluir_produto(produtos[escolhido])
        st.success("Produto excluído.")