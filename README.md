# Spotify Analyzer

## Visão Geral
O Spotify Analyzer é uma aplicação em Python que utiliza a API Web do Spotify para analisar os hábitos musicais de um usuário. Ele fornece informações sobre os artistas, faixas e gêneros musicais mais ouvidos em diferentes períodos de tempo (últimas 4 semanas, 6 meses ou 1 ano). A aplicação gera visualizações, usando a matplotlib e pandas, para ajudar os usuários a entenderem suas preferências musicais.

## Funcionalidades
- **Análise de Gêneros com Base em Artistas**: Exibe um gráfico de pizza com os 10 gêneros musicais mais comuns entre os artistas favoritos do usuário.
- **Análise de Gêneros com Base em Faixas**: Exibe um gráfico de pizza com os 10 gêneros musicais derivados dos artistas das faixas mais ouvidas do usuário.
- **Faixas Mais Ouvidas**: Lista as 10 faixas mais ouvidas com detalhes como nome da faixa, artista, álbum, popularidade e duração.
- **Artistas Mais Ouvidos**: Lista os 10 artistas mais ouvidos com seus nomes e pontuações de popularidade.
- **Seleção de Período de Tempo**: Permite aos usuários analisar dados em três períodos: últimas 4 semanas, últimos 6 meses ou último ano.

## Bibliotecas utilizadas
- Spotipy
- Pandas
- Matplotlib
- Python-dotenv

## Configuração
**Configurar Variáveis de Ambiente**:
   - Crie um arquivo `.env` na raiz do projeto.
   - Adicione as seguintes variáveis com suas credenciais da API do Spotify:
     ```plaintext
     CLIENT_ID=seu_client_id
     CLIENT_SECRET=seu_client_secret
     REDIRECT_URI=seu_redirect_uri
     ```
   - Obtenha essas credenciais criando um aplicativo no [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).

## Estrutura do Projeto
- **`main.py`**: Script principal que contém o menu interativo.
- **`analysis.py`**: Contém funções para análise de dados.
- **`auth.py`**: Gerencia a autenticação com a API do Spotify.
- **`.env`**: Arquivo para armazenar credenciais da API (não incluído no repositório).
