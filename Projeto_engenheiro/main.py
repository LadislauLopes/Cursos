import streamlit as st
import  streamlit_toggle as tog
from laudos import Laudos
from texts import textos
from PIL import Image
import io


st.set_page_config("Projeto Laudos", layout='wide')
st.title('Bem vindo')
with open(r"css\styles.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)
laudo_a_ser_gerado= Laudos()
with st.container():
    coluna1, coluna2 = st.columns([2,3])

    with coluna1:
        laudo_a_ser_gerado.nome = st.selectbox('Gerar laudo',['---------------','Guindaste', 'teste1','teste2'])
    
    if laudo_a_ser_gerado.nome == 'Guindaste':
        with st.container():
            with st.expander('Indentificação do profissional'):
                coluna1,coluna2= st.columns(2)
                with coluna1:
                    laudo_a_ser_gerado.proprietario= st.text_input('Nome Completo')
                    laudo_a_ser_gerado.crea = st.text_input('Crea')
                    laudo_a_ser_gerado.crea = st.text_input('Contato',placeholder="Telefone/Email")
                with coluna2:
                    laudo_a_ser_gerado.resposavel = st.text_input('Responsável')
                    laudo_a_ser_gerado.cpf = st.text_input('CPF')

        with st.container():
            with st.expander('Indentificação da empresa'):
                coluna1_,coluna2_, coluna3_, coluna4_,coluna5_, coluna6_ = st.columns(6)
            
                with coluna1_:
                    laudo_a_ser_gerado.num_do_laudo=  st.text_input('Numero do Laudo')
                with coluna2_:
                    laudo_a_ser_gerado.num_do_artigo = st.text_input('Numero do Art')
                with coluna3_:
                    laudo_a_ser_gerado.cnpj =st.text_input('CNPJ')


        with st.container():
            with st.expander('Indentificação do Veiculo'):
                coluna1_,coluna2_, coluna3_, coluna4_,coluna5_, coluna6_ = st.columns(6)
            
                with coluna1_:
                    laudo_a_ser_gerado.equipamento = st.text_input('Equipamentos')
                    laudo_a_ser_gerado.veiculo_de_transporte=  st.text_input('Verculo de trasporte')
                with coluna2_:
                    laudo_a_ser_gerado.placa=st.text_input('Placa')
                    laudo_a_ser_gerado.alcance_max_vertical= st.text_input('Alcance máximo vertical, em metros')
                    
                with coluna3_:
                    laudo_a_ser_gerado.placa_de_sinalizacao = st.text_input('Placa de Sinalização')
                    laudo_a_ser_gerado.data_de_fabricacao= st.date_input('Data de Fabricação')
                with coluna4_:
                    laudo_a_ser_gerado.veiculo_de_transporte= st.text_input('Veiculo de Transporte')
                    laudo_a_ser_gerado.tabela_capacidade_transporte = st.text_input('Tabela de capacidade para transporte')
                with coluna5_:
                    laudo_a_ser_gerado.capacidade_nominal_de_carga= st.text_input('Capacidade nominal de carga KGFM')
                    laudo_a_ser_gerado.modelo_tipo= st.text_input('Modelo e/ou tipo')
                coluna1__, coluna2__,coluna3__, _= st.columns(4)
                with coluna1__:
                    laudo_a_ser_gerado.nome_do_fabricante_e_marca = st.text_input('Nome do fabricante e marca')
                with coluna2__:
                    laudo_a_ser_gerado.max_rotacao_da_coluna= st.text_input('Rotação maxima em graus')
                with coluna3__:
                    laudo_a_ser_gerado.altura_maxima_para_transporte = st.text_input('Altura maxima para transporte')

        with st.container():
            
            if 'checkbox_values' not in st.session_state:
                st.session_state.checkbox_values = {texto: False for texto in textos}

            with st.expander('Checklist de verificação'):
                for texto in textos:
                    st.session_state.checkbox_values[texto] = st.toggle(f'{texto}', value=False)

        with st.container():
            
            with st.expander('Registros Fotográficos'):
                # Criar o campo de upload de múltiplos arquivos
                arquivos_enviados = st.file_uploader("Escolha as imagens", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

                # Verificar se arquivos foram carregados
                if arquivos_enviados:
                    descricoes = []
                    
                    # Exibir a imagem e coletar descrições
                    for arquivo_enviado in arquivos_enviados:
                        # Ler a imagem
                        imagem = Image.open(arquivo_enviado)
                        
                        # Exibir a imagem
                        st.image(imagem, caption=f'Imagem: {arquivo_enviado.name}')
                        
                        # Coletar descrição para a imagem
                        descricao = st.text_input(f"Descrição para {arquivo_enviado.name}", key=arquivo_enviado.name)
                        descricoes.append({
                            'nome': arquivo_enviado.name,
                            'descricao': descricao
                        })

                if st.button('Mostrar Descrições'):
                    for desc in descricoes:
                        st.write(f"Imagem: {desc['nome']}")
                        st.write(f"Descrição: {desc['descricao']}")

    #         st.button('Gerar Laudo',on_click=laudo_a_ser_gerado.gerar_guindaste)


