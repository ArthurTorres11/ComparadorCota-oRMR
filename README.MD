# Comparador de Cotações RMR  

![Logo da RMR Company Auto Peças](assets/logo-rmr.png)  

## 🔧 Sobre o Projeto  
O **Comparador de Cotações RMR** é uma aplicação desenvolvida para facilitar a análise e comparação de cotações de peças automotivas. Ele permite o upload de planilhas, processa os dados e retorna uma tabela com os melhores preços por peça, otimizando o processo de decisão.  

## 📚 Tecnologias Utilizadas  
- **Python**: Linguagem principal do projeto.  
- **Streamlit**: Framework para criação de interfaces web interativas.  
- **Pandas**: Biblioteca para manipulação e análise de dados.  
- **openpyxl**: Para leitura e escrita de arquivos Excel.  
- **python-dotenv**: Gerenciamento de variáveis de ambiente.  

## 🔐 Login  
O acesso à aplicação é protegido por autenticação via variáveis de ambiente armazenadas em um arquivo `.env`. As variáveis necessárias são:  
- `USERNAME`: Nome de usuário.  
- `SENHA`: Senha de acesso.  

## 📄 Funcionalidades  
1. **Upload de Planilhas**: Suporte para até 5 arquivos no formato `.xlsx`.  
    - Os dados devem começar a partir da linha 8.  
    - Colunas obrigatórias: `Quantidade`, `Peça`, `Preço`, `Marca`.  
2. **Processamento de Dados**: Identificação dos melhores preços por peça.  
3. **Exportação**: Geração de uma tabela consolidada com opção de exportar para Excel.  

## 📁 Estrutura de Pastas  
```plaintext  
ComparadorRMR/  
├── assets/  
│   └── logo-rmr.png  
├── app.py 
├── utils/  
│   ├── auth.py  
│   ├── process.py    
├── .env  
├── requirements.txt  
└── README.md  
```  

## 🚀 Como Executar o Projeto  
1. **Clone o repositório**:  
    ```bash  
    git clone https://github.com/seu-usuario/ComparadorRMR.git  
    cd ComparadorRMR  
    ```  

2. **Crie um ambiente virtual e instale as dependências**:  
    ```bash  
    python -m venv venv  
    source venv/bin/activate  # No Windows: venv\Scripts\activate  
    pip install -r requirements.txt  
    ```  

3. **Configure o arquivo `.env`**:  
    Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:  
    ```plaintext  
    USERNAME=seu_usuario  
    SENHA=sua_senha  
    ```  

4. **Execute a aplicação**:  
    ```bash  
    streamlit run src/app.py  
    ```  

5. **Acesse no navegador**:  
    Acesse a aplicação em `http://localhost:8501`.  

## 📤 Exportação de Resultados  
Após o processamento, clique no botão **Exportar para Excel** para baixar a tabela consolidada com os melhores preços.  

## 🤝 Contribuições  
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.  

## 📄 Licença  
Este projeto está licenciado sob a [MIT License](LICENSE).  

---  
Desenvolvido com ❤️ pela equipe da **RMR Company Auto Peças**.  