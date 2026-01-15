# Postgres + pgvector + pgai

Documentacao linha a linha do Dockerfile e do docker-compose, com o motivo de cada instrucao.

## Conceitos-base
- Imagem: template imutavel gerado pelo Dockerfile (aqui vira postgres-ai:v1).
- Container: execucao da imagem; estado e dados ficam em volumes, nao na imagem.
- Entrypoint oficial do Postgres: script docker-entrypoint.sh que cria o cluster, roda scripts em /docker-entrypoint-initdb.d na primeira subida do volume e entao inicia o servidor.
- Script de init: qualquer arquivo mapeado em /docker-entrypoint-initdb.d roda apenas na primeira criacao do volume de dados.
- Volume: pasta montada fora do container para persistir dados (./postgres_data).
- Porta: host:container; 5432:5432 expoe o Postgres interno na porta 5432 do host.

## docker-compose.yml (explicado)
- version: "3" — usa sintaxe da especificacao do Compose v3.
- name: postgres-ai — prefixo para nomes de containers/redes/volumes criados.
- services — bloco dos servicos.
  - postgres — nome do servico (vira parte do nome do container).
    - build:
      - context: . — usa o diretorio atual como contexto (leva Dockerfile e arquivos citados).
      - dockerfile: Dockerfile — escolhe o arquivo Dockerfile local para construir.
    - image: postgres-ai:v1 — nome/tag atribuida a imagem resultante do build.
    - ports: "5432:5432" — mapeia porta 5432 do host para 5432 do container (porta padrao do Postgres).
    - volumes:
      - ./postgres_data:/var/lib/postgresql/data — volume persistente do cluster; evita perda ao recriar o container.
      - ./activate-extension.sql:/docker-entrypoint-initdb.d/0-activate_extension.sql — script de init executado na primeira inicializacao do volume; ativa extensoes.
    - environment:
      - POSTGRES_USER=postgres — usuario inicial criado pelo entrypoint.
      - POSTGRES_PASSWORD=postgres — senha do usuario inicial.
      - POSTGRES_DB=vectordb — banco inicial criado na primeira subida.

## Dockerfile (explicado)
- FROM postgres:16.3 — base oficial do Postgres 16.3.
- RUN apt-get update && apt-get install ... — instala toolchain e dependencias para compilar extensoes e PL/Python (build-essential, git, headers do Postgres, python3, postgresql-plpython3-16); limpa cache para reduzir tamanho.
- WORKDIR /tmp — define diretorio de trabalho temporario para builds.
- RUN git clone https://github.com/pgvector/pgvector.git — baixa o codigo-fonte do pgvector.
- RUN git clone https://github.com/timescale/pgai.git — baixa o codigo-fonte do pgai.
- WORKDIR /tmp/pgvector; RUN make; RUN make install — compila e instala a extensao pgvector no Postgres da imagem.
- WORKDIR /tmp/pgai; RUN make; RUN make install — compila e instala a extensao pgai e dependencias no Postgres da imagem.

## activate-extension.sql (explicado)
- Executado apenas na primeira criacao do volume de dados pelo entrypoint oficial.
- CREATE EXTENSION IF NOT EXISTS vector; — habilita pgvector.
- CREATE EXTENSION IF NOT EXISTS plpython3u; — habilita PL/Python nao-confiavel (requerido por pgai).
- CREATE EXTENSION IF NOT EXISTS ai CASCADE; — habilita pgai e dependencias.

## Passos de uso
```bash
# construir a imagem (usa o Dockerfile)
docker compose build

# subir o banco em background
docker compose up -d

# checar se esta rodando
docker ps

# conectar via psql
psql -h localhost -U postgres -d vectordb
```

## Limpeza
```bash
# parar e remover o container
docker compose down

# remover dados persistidos (destrutivo)
rm -rf postgres_data
```'