import streamlit as st
import pandas as pd
from PIL import Image #comando para importar imagem

#configuração da página
st.set_page_config(page_title="Quem é você?", layout="wide")
st.title("Apresentação")

#Importar imagem
imagem = st.file_uploader("Adicione uma imagem de perfil", type=["png", "jpng", "jpeg" ]) #Armazena o arquivo na variavel imagem: Adiciona o local para colocar a imagem e a mensagem, e o tipo de arquivo suportado
if imagem is not None:  #verifica se foi adicionada uma imagem
    img = Image.open(imagem)  #abre o arquivo de imagem usando a biblioteca PIL (Python Imaging Library).
    st.image(img, caption="Foto de perfil", use_container_width=True) #exibe a imagem na tela/ é a imagem que foi carregada./ adiciona uma legenda abaixo da imagem./ faz a imagem se ajustar automaticamente à largura da coluna da interface.
else:
    st.info("🚨 Faça o upload de uma imagem para começar.") #executa esse bloco se nenhum arquivo tiver sido carregado./ exibe uma mensagem informativa em azul, alertando o usuário.

    # Campos do formulário
with st.form("formulario_perfil"):
    nome = st.text_input("Nome completo") #Entrada de texto
    idade = st.number_input("Idade", min_value=0, max_value=150, step=1) #Entrada de número. Step1 ( diminui ou aumenta idade de 1 em 1)
    
    genero = st.selectbox("Gênero", ["Selecione", "Feminino", "Masculino", "Não binário", "Prefiro não dizer", "Outro"]) #Cria uma caixa de seleção
    pronomes = st.text_input("Pronomes (ex: ela/dela, ele/dele, elu/delu)")
    
    interesses = st.text_area("Interesses (separados por vírgula)", placeholder="Tecnologia, Arte, Viagens...")

    submit = st.form_submit_button("Enviar")

# Exibir resultado
if submit:
    st.markdown("---")
    st.image()
    st.subheader("📄 Resultado do Cadastro")
    st.write(f"**Nome:** {nome}")
    st.write(f"**Idade:** {idade}")
    st.write(f"**Gênero:** {genero}")
    st.write(f"**Pronomes:** {pronomes}")
    st.write(f"**Interesses:** {[i.strip() for i in interesses.split(',') if i.strip()]}")