# Tool4IoTReq

Tool4IoTReq é uma plataforma inteligente para gestão, classificação e agrupamento de requisitos em projetos de Internet das Coisas (IoT), utilizando técnicas de Processamento de Linguagem Natural (PLN) e Aprendizado de Máquina.

## Organização do Repositório

- `projeto/`  
  - `manage.py`  
  - `project/` (configurações Django)
  - `projetos/` (lógica de projetos)
  - `requisitos/` (classificação e agrupamento de requisitos, modelos, ML)
  - `usuarios/` (gestão de usuários)
  - `static/` (arquivos estáticos)
  - `templates/` (templates HTML)
  - `requirements.txt` (dependências do Python)
  - `README.md` (este arquivo)
- [Artigo Aceito (PDF)](https://arxiv.org/abs/xxxx.xxxxx) <!-- Troque pelo link real ou caminho local -->

## Requisitos

- **Software**
  - Python 3.10+
  - MongoDB 4.0+ (banco de requisitos)
  - Django 5.x
  - Docker (opcional, para ambiente isolado)
- **Hardware**
  - 8GB RAM (mínimo recomendado)
  - 500MB de espaço livre para base de dados e modelos
- **Ambiente**
  - Sistema Operacional: Linux, Windows ou MacOS
  - Acesso à internet para baixar modelos de PLN (se necessário)
- **Dependências**
  - Todas as dependências estão especificadas em [requirements.txt](projeto/requirements.txt)

## Instalação

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/RuanSampaio-code/ReqCluster4IoT-Tool.git
   cd tool4iotreq/projeto
   ```

2. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure o banco de dados MongoDB:**
   - Certifique-se que o serviço MongoDB está rodando localmente na porta padrão (27017).

4. **Execute as migrações do Django:**
   ```sh
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```sh
   python manage.py runserver
   ```

6. **Acesse o sistema:**
   - Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador.

## Teste da Instalação

Após iniciar o servidor, acesse `/` e verifique se a página inicial é exibida. Para testar o agrupamento, crie um projeto e adicione requisitos, depois acesse a funcionalidade de agrupamento. A saída esperada é a visualização dos requisitos agrupados em um mapa mental.

## Requisitos de Armazenamento e Declarações Éticas/Legais

- Os dados são armazenados localmente em MongoDB e SQLite.
- Não armazene dados pessoais sensíveis sem consentimento.
- O uso do sistema deve respeitar as leis de proteção de dados aplicáveis.

## Licença

Este projeto está sob a [MIT License](LICENSE).


