import os
import shutil
from winotify import Notification, audio 

def copiar_arquivo( destino_pasta):
    try:
        pasta_origem_rel = os.path.join(destino_pasta, "../interno")
        origem_arquivo = os.path.abspath(os.path.join(pasta_origem_rel, 'estoque.db'))

        # Verifica se a pasta de destino existe, caso contrário, cria-a
        if not os.path.exists(destino_pasta):
            os.makedirs(destino_pasta)

        # Extrai o nome do arquivo a partir do caminho de origem
        nome_arquivo = os.path.basename(origem_arquivo)
        
        # Cria o caminho completo para o arquivo de destino
        caminho_destino = os.path.join(destino_pasta, nome_arquivo)
        
        # Copia o arquivo de origem para o destino
        shutil.copy2(origem_arquivo, caminho_destino)

        # Nome do arquivo PNG
        nome_arquivo_png = 'icon.png'
        # Nome da pasta onde o arquivo está localizado
        pasta_icones = 'icones'

        # Obtendo o caminho absoluto do arquivo PNG
        caminho_absoluto = os.path.abspath(os.path.join(pasta_icones, nome_arquivo_png))

        notificacao = Notification(app_id= 'ArmazenaTi Backups', title='Backup concluído', msg='Espero que tenha um ótimo dia!', duration='short',icon=caminho_absoluto)
        
        notificacao.set_audio(audio.Mail, loop=False)
        notificacao.show()

    except Exception as e:

        # Nome do arquivo PNG
        nome_arquivo_png = 'icon2.png'
        # Nome da pasta onde o arquivo está localizado
        pasta_icones = 'icones'

        # Obtendo o caminho absoluto do arquivo PNG
        caminho_absoluto = os.path.abspath(os.path.join(pasta_icones, nome_arquivo_png))

        notificacao = Notification(app_id= 'ArmazenaTi Backups', title='Erro ao fazer o backup', msg='Algo de insperado aconteceu', duration='short',icon=caminho_absoluto)
        
        notificacao.set_audio(audio.Mail, loop=False)
        notificacao.show()


pasta_destino = r"\\SAC0005\SUPORTE\Ladislau Scripts\Controle patrimonio\Backup"
copiar_arquivo(pasta_destino)




