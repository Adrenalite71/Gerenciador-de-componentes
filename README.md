# Gerenciador de Componentes Eletrônicos 🚀

Um sistema desktop moderno, leve e offline para gerenciamento de estoque de componentes eletrônicos. Desenvolvido em Python com interface CustomTkinter e banco de dados SQLite, focado na velocidade e precisão para laboratórios e assistências técnicas.

## ✨ Principais Funcionalidades

*   **Interface Moderna (Dark Mode):** Construída com CustomTkinter para uma experiência limpa e fluida.
*   **Banco de Dados Offline (SQLite):** Sem necessidade de configurar servidores. Seus dados rodam localmente com máxima velocidade.
*   **Gestão por Localização:** Controle absoluto de onde cada peça está guardada (Gatetas e Divisões).
*   **Lojinha Dinâmica de Packs:** O sistema possui uma integração direta com a API do GitHub. Novos "Packs de Conhecimento" (bancos de dados de componentes JSON) criados pela comunidade aparecem automaticamente no aplicativo para download, sem precisar de atualizações de software.
*   **Categorização Paramétrica:** Campos inteligentes que se adaptam se o componente é um IGBT, um Microcontrolador (DSP), Resistor ou Capacitor.

## 📦 Como Usar

### Usando o Executável (Versão Estável)
1. Acesse a aba [Releases](https://github.com/Adrenalite71/Gerenciador-de-Componentes/releases).
2. Baixe a versão `.exe` mais recente.
3. Execute o programa (não requer instalação).

### Rodando pelo Código Fonte
Certifique-se de ter o Python instalado e rode os seguintes comandos no terminal:

```bash
# Clonar o repositório
git clone [https://github.com/Adrenalite71/Gerenciador-de-Componentes.git](https://github.com/Adrenalite71/Gerenciador-de-Componentes.git)

# Entrar na pasta do projeto
cd Gerenciador-de-Componentes

# Instalar as dependências
pip install -r requirements.txt

# Iniciar o aplicativo
python app.py
- <img width="1404" height="833" alt="image" src="https://github.com/user-attachments/assets/2254f7af-661a-43fa-936a-f5f6c3b4220e" />
- <img width="1399" height="830" alt="image" src="https://github.com/user-attachments/assets/86f3d4c7-056b-4e34-9f81-81367776c420" />
- <img width="558" height="434" alt="image" src="https://github.com/user-attachments/assets/912be76f-58cc-4855-bfdd-deda0e7b1bd6" />
- <img width="1403" height="837" alt="image" src="https://github.com/user-attachments/assets/57f42ab6-517a-435b-8439-cc06483a5d4e" />




## Como Baixar e Usar

1. Acesse a aba **[Releases](https://github.com/Adrenalite71/component-inventory-app/releases)** localizada no lado direito desta página do GitHub.
2. Baixe o arquivo `.exe` da versão mais recente.
3. Este aplicativo é um executável **standalone (portátil)**. Não é necessária nenhuma instalação complexa — basta dar um duplo clique no arquivo baixado e começar a gerenciar seu inventário!

> [!WARNING]
> ### Aviso Importante - Windows SmartScreen
> 
> Como esta é uma ferramenta independente, de código aberto e construída sem um certificado digital pago, o **Windows Defender SmartScreen** poderá bloqueá-la em sua primeira execução, exibindo um aviso de "Aplicativo não reconhecido" ou "Inseguro".
> 
> Para utilizar o aplicativo com segurança, siga os seguintes passos:
> 1. Na tela azul do *Windows Protect*, clique no texto **"Mais informações"** (More info).
> 2. Em seguida, clique no botão **"Executar assim mesmo"** (Run anyway).

🧠 Como funcionam os Packs de Conhecimento?
O aplicativo não vem com milhares de componentes pré-cadastrados para não pesar. Em vez disso, você pode acessar a Lojinha de Packs dentro da engrenagem do app e baixar nichos específicos (ex: "Pack de Inversores de Potência", "Pack Arduino", etc.).

Para aprender a criar o seu próprio Pack em JSON e contribuir com a comunidade, acesse a nossa Wiki.
