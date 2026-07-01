# Inventário de Componentes Eletrônicos

Uma aplicação desktop intuitiva desenvolvida para organizar, gerenciar e pesquisar componentes eletrônicos (como Resistores PTH/SMD, Capacitores, Transistores, Circuitos Integrados e mais). O sistema permite o mapeamento físico preciso em gavetas e cálculo dinâmico de parâmetros.

## Funcionalidades

- **Busca Paramétrica Avançada:** Encontre componentes rapidamente filtrando por categoria, localização física, valores exatos ou propriedades específicas.
- **Sincronização em Rede Local (LAN):** Projetado para ambientes de trabalho reais. O sistema possui arquitetura embutida para operar em modo **Servidor (Host)** ou **Cliente**, permitindo que múltiplos computadores no mesmo local compartilhem e atualizem o mesmo banco de dados em tempo real.
- **Calculadoras Integradas Bidirecionais:** Ferramentas nativas para decodificação rápida direto na bancada. Inclui calculadora bidirecional inteligente para Resistores PTH (Cores ↔ Valores) e decodificadores automáticos de códigos alfanuméricos para Resistores SMD e Capacitores SMD.
- **Subdivisões Dinâmicas de Gavetas:** Controle total sobre o seu armazenamento físico. Adicione, edite ou exclua gavetas com quantidades ilimitadas e flexíveis de subdivisões. O preenchimento automático sincroniza dados e cores nativamente ao editar.
- **Privacidade e Persistência de Dados:** Todo o inventário é salvo de forma segura (SQLite), operando de forma 100% offline no modo local ou centralizado com segurança na sua própria rede.
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
