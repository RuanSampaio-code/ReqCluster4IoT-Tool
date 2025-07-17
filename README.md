# Tool4IoTReq

Tool4IoTReq is an intelligent platform for managing, classifying, and grouping requirements in Internet of Things (IoT) projects, using Natural Language Processing (NLP) and Machine Learning techniques.

## Repository Organization

- `projeto/`  
  - `manage.py`  
  - `project/` (Django settings)
  - `projetos/` (project logic)
  - `requisitos/` (requirements classification and grouping, models, ML)
    - `modelo_classificacao/` (AI model for classification)
    - `modelo_similaridade/` (AI model for similarity)
  - `usuarios/` (user management)
  - `static/` (static files)
  - `templates/` (HTML templates)
  - `requirements.txt` (Python dependencies)
  - `README.md` (this file)
- [Accepted Article (PDF)](https://arxiv.org/abs/xxxx.xxxxx) <!-- Replace with actual link or local path -->

## Requirements

- **Software**
  - Python 3.10+
  - MongoDB 4.0+ (requirements database)
  - Django 5.x
  - Docker (optional, for isolated environment)
- **Hardware**
  - 8GB RAM (minimum recommended)
  - 500MB free space for database and models
- **Environment**
  - Operating System: Linux, Windows, or MacOS
  - Internet access to download NLP models (if needed)
- **Dependencies**
  - All dependencies are listed in [requirements.txt](projeto/requirements.txt)
- **AI Models**
  - Download the folders `modelo_classificacao` and `modelo_similaridade` from [Google Drive](https://drive.google.com/drive/u/3/folders/1YwLZWSpjo-6yfBtOU5MUOuCS04TX3Ni3) and place them inside the `requisitos` folder before running the system.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/RuanSampaio-code/ReqCluster4IoT-Tool.git
   cd tool4iotreq/projeto
   ```

2. **Create and activate a virtual environment (recommended):**

   * **Windows:**
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```

   * **Linux/macOS:**
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Download AI models:**
   - Request access to the Google Drive folder: [Google Drive](https://drive.google.com/drive/u/3/folders/1YwLZWSpjo-6yfBtOU5MUOuCS04TX3Ni3).
   - Download the folders `modelo_classificacao` and `modelo_similaridade` from [Google Drive](https://drive.google.com/drive/u/3/folders/1YwLZWSpjo-6yfBtOU5MUOuCS04TX3Ni3).
   - Place both folders inside the `projeto/requisitos/` directory.

5. **Configure MongoDB database:**
   - Make sure MongoDB service is running locally on the default port (27017).

6. **Run Django migrations:**
   ```sh
   python manage.py migrate
   ```

7. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

8. **Access the system:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Installation Test

After starting the server, access `/` and check if the home page is displayed. To test grouping, create a project and add requirements, then access the grouping feature. The expected output is the visualization of requirements grouped in a mind map.

## Storage Requirements and Ethical/Legal Statements

- Data is stored locally in MongoDB and SQLite.
- Do not store sensitive personal data without consent.
- System usage must comply with applicable data protection laws.

## License

This project is licensed under the [MIT License](LICENSE).

---

# Tool4IoTReq (Português)

Tool4IoTReq é uma plataforma inteligente para gestão, classificação e agrupamento de requisitos em projetos de Internet das Coisas (IoT), utilizando técnicas de Processamento de Linguagem Natural (PLN) e Aprendizado de Máquina.

## Organização do Repositório

- `projeto/`  
  - `manage.py`  
  - `project/` (configurações Django)
  - `projetos/` (lógica de projetos)
  - `requisitos/` (classificação e agrupamento de requisitos, modelos, ML)
    - `modelo_classificacao/` (modelo de IA para classificação)
    - `modelo_similaridade/` (modelo de IA para similaridade)
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
- **Modelos de IA**
  - Baixe as pastas `modelo_classificacao` e `modelo_similaridade` do [Google Drive](https://drive.google.com/drive/u/3/folders/1YwLZWSpjo-6yfBtOU5MUOuCS04TX3Ni3) e coloque-as dentro da pasta `requisitos` antes de executar o sistema.

## Instalação

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/RuanSampaio-code/ReqCluster4IoT-Tool.git
   cd tool4iotreq/projeto
   ```

2. **Crie e ative um ambiente virtual (recomendado):**

   * **Windows:**
     ```sh
     python -m venv venv
     venv\Scripts\activate
     ```

   * **Linux/macOS:**
     ```sh
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Baixe os modelos de IA:**
   - Primeiro solicite acesso ao drive do link: [Google Drive](https://drive.google.com/drive/u/3/folders/1YwLZWSpjo-6yfBtOU5MUOuCS04TX3Ni3).
   - Baixe as pastas `modelo_classificacao` e `modelo_similaridade` do [Google Drive](https://drive.google.com/drive/u/3/folders/1YwLZWSpjo-6yfBtOU5MUOuCS04TX3Ni3).
   - Coloque ambas as pastas dentro do diretório `projeto/requisitos/`.

5. **Configure o banco de dados MongoDB:**
   - Certifique-se que o serviço MongoDB está rodando localmente na porta padrão (27017).

6. **Execute as migrações do Django:**
   ```sh
   python manage.py migrate
   ```

7. **Inicie o servidor de desenvolvimento:**
   ```sh
   python manage.py runserver
   ```

8. **Acesse o sistema:**
   - Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador.

## Teste da Instalação

Após iniciar o servidor, acesse `/` e verifique se a página inicial é exibida. Para testar o agrupamento, crie um projeto e adicione requisitos, depois acesse a funcionalidade de agrupamento. A saída esperada é a visualização dos requisitos agrupados em um mapa mental.

## Requisitos de Armazenamento e Declarações Éticas/Legais

- Os dados são armazenados localmente em MongoDB e SQLite.
- Não armazene dados pessoais sensíveis sem consentimento.
- O uso do sistema deve respeitar as leis de proteção de dados aplicáveis.

## Licença

Este projeto está sob a [MIT License](LICENSE).