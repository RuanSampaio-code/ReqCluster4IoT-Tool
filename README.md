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
- `docker-compose.yml` (MongoDB container setup)
- [Accepted Article (PDF)](./CBSoft___SBES_2025_Uma_ferramenta_para_apoiar_a_análise_de_requisitos_de_software_de_IoT_utilizando_técnicas_de_agrupamento.pdf.pdf)

## Requirements

- **Software**
  - Python 3.10+
  - Docker & Docker Compose (for MongoDB database)
  - Django 5.x
- **Hardware**
  - **Processor:** Intel Core i7 (12th Gen) or equivalent
  - **Minimum Memory (RAM):** 16 GB
  - **Graphics Card (GPU):** NVIDIA GTX 1660 with 6 GB GDDR5 memory (or equivalent)
  - **Free Disk Space:** At least 500 MB
- **Environment**
  - Operating System: Linux, Windows, or MacOS
  - Internet access to download NLP models (if needed)
- **Dependencies**
  - All dependencies are listed in [requirements.txt](projeto/requirements.txt)
- **AI Models**
  - You must request access to the Google Drive folder containing the AI models: [Google Drive link](https://drive.google.com/drive/u/3/folders/1YwLZWSpjo-6yfBtOU5MUOuCS04TX3Ni3). After access is granted, download the folders `modelo_classificacao` and `modelo_similaridade` and place them inside the `requisitos` folder before running the system.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/RuanSampaio-code/ReqCluster4IoT-Tool.git
   cd ReqCluster4IoT-Tool
   ```

2. **Start MongoDB with Docker:**
   ```sh
   docker compose up -d
   ```

3. **Create and activate a virtual environment (recommended):**

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

4. **Navigate to the project directory:**
   ```sh
   cd projeto
   ```

5. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

6. **Download AI models:**
   - Request access to the Google Drive folder: [Google Drive](https://drive.google.com/drive/u/3/folders/1YwLZWSpjo-6yfBtOU5MUOuCS04TX3Ni3).
   - After access is granted, download the folders `modelo_classificacao` and `modelo_similaridade`.
   - Place both folders inside the `projeto/requisitos/` directory.

7. **Run Django migrations:**
   ```sh
   python manage.py migrate
   ```

8. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

9. **Access the system:**
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Docker Commands

- **Start MongoDB:** `docker compose up -d`
- **Stop MongoDB:** `docker compose down`
- **View MongoDB logs:** `docker compose logs db`
- **Remove containers and volumes:** `docker compose down -v`

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
- `docker-compose.yml` (configuração do container MongoDB)
- [Artigo Aceito (PDF)](./11218_Artigo_f4PlF73.pdf)

## Requisitos

- **Software**
  - Python 3.10+
  - Docker & Docker Compose (para banco de dados MongoDB)
  - Django 5.x
- **Hardware**
  - **Processador:** Intel Core i7 (12ª Geração) ou equivalente
  - **Memória Mínima (RAM):** 16 GB
  - **Placa Gráfica (GPU):** NVIDIA GTX 1660 com 6 GB de memória GDDR5 (ou equivalente)
  - **Espaço Livre em Disco:** Pelo menos 500 MB
- **Ambiente**
  - Sistema Operacional: Linux, Windows ou MacOS
  - Acesso à internet para baixar modelos de PLN (se necessário)
- **Dependências**
  - Todas as dependências estão especificadas em [requirements.txt](projeto/requirements.txt)
- **Modelos de IA**
  - É necessário solicitar acesso à pasta do Google Drive que contém os modelos de IA: [Link do Google Drive](https://drive.google.com/drive/u/3/folders/1YwLZWSpjo-6yfBtOU5MUOuCS04TX3Ni3). Após o acesso ser concedido, baixe as pastas `modelo_classificacao` e `modelo_similaridade` e coloque-as dentro da pasta `requisitos` antes de executar o sistema.

## Instalação

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/RuanSampaio-code/ReqCluster4IoT-Tool.git
   cd ReqCluster4IoT-Tool
   ```

2. **Inicie o MongoDB com Docker:**
   ```sh
   docker compose up -d
   ```

3. **Crie e ative um ambiente virtual (recomendado):**

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

4. **Navegue para o diretório do projeto:**
   ```sh
   cd projeto
   ```

5. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

6. **Baixe os modelos de IA:**
   - Solicite acesso à pasta do Google Drive: [Google Drive](https://drive.google.com/drive/u/3/folders/1YwLZWSpjo-6yfBtOU5MUOuCS04TX3Ni3).
   - Após o acesso ser concedido, baixe as pastas `modelo_classificacao` e `modelo_similaridade`.
   - Coloque ambas as pastas dentro do diretório `projeto/requisitos/`.

7. **Execute as migrações do Django:**
   ```sh
   python manage.py migrate
   ```

8. **Inicie o servidor de desenvolvimento:**
   ```sh
   python manage.py runserver
   ```

9. **Acesse o sistema:**
   - Abra [http://127.0.0.1:8000/](http://127.0.0.1:8000/) no navegador.

## Comandos Docker

- **Iniciar MongoDB:** `docker compose up -d`
- **Parar MongoDB:** `docker compose down`
- **Ver logs do MongoDB:** `docker compose logs db`
- **Remover containers e volumes:** `docker compose down -v`

## Teste da Instalação

Após iniciar o servidor, acesse `/` e verifique se a página inicial é exibida. Para testar o agrupamento, crie um projeto e adicione requisitos, depois acesse a funcionalidade de agrupamento. A saída esperada é a visualização dos requisitos agrupados em um mapa mental.

## Requisitos de Armazenamento e Declarações Éticas/Legais

- Os dados são armazenados localmente em MongoDB e SQLite.
- Não armazene dados pessoais sensíveis sem consentimento.
- O uso do sistema deve respeitar as leis de proteção de dados aplicáveis.

## Licença

Este projeto está sob a [MIT License](LICENSE).