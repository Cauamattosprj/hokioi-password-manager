# Hokioi Password Manager

Este projeto tem o principal intuito de servir como fonte de estudos na área de desenvolvimento, banco de dados, python, consumo e integração de API's, criptografia e cibersegurança. **Não é um software desenvolvido por profissionais experientes.**

## 1. Definição do Projeto

**Objetivo:** 

O Hokioi será um software de gerenciamento de senhas fácil de ser usado, que contará com um tutorial de introdução para que o usuário entenda as funcionalidades e a importância de um sistema de gerenciamento de senhas para a sua segurança.  

O Hokioi irá introduzir o usuário de forma fácil aos conceitos de segurança e dentro do software poderá armazenar suas senhas, garantir que elas serão trocadas periodicamente, ser lembrado de suas senhas memoráveis periodicamente, receber ideias de senhas memoráveis, saber se foi vítima de vazamento de dados e futuramente poderá usar o software para colocar bloqueio por senha em outros aplicativos.

## 2. Análise de Requisitos

**Objetivo:** Identifique e documente todos os requisitos do seu software.

**Funcionais:** 
- Armazenar senhas de forma criptografada, 
- gerar senhas fortes (memoráveis e aleatórias), 
- opção de dicionário para que a pessoa possa escolher em qual idioma será criada a senha memorável, 
- criação de senhas memoráveis customizadas (usando frases como exemplo),
- verificar em banco de vazamentos se a senha foi prejudicada

### 001. Armazenamento de Senhas Criptografadas Feito em Banco de Dados

O software deve ser capaz de armazenar senhas do usuário de maneira criptografada e armazena-las em um banco de dados, exigindo uma senha mestre para descriptografia dos dados.

### 01. Criptografia dos Dados em Trânsito e em Repouso

O software deve ser capaz de realizar a total criptografia dos dados em todos os momentos da operação. Na consulta, na criação e no armazenamento das senhas e dados.
### 1. Verificação de Senhas Vazadas

**Problema:** As senhas dos usuários podem ser comprometidas em vazamentos de dados. **Funcionalidade:** Integre uma API que verifica as senhas dos usuários em bancos de dados de senhas vazadas, como o "Have I Been Pwned". Informe os usuários imediatamente se suas senhas estão comprometidas e sugira uma alteração.

### 2. Detecção de Reutilização de Senhas

**Problema:** Reutilizar senhas em múltiplos serviços aumenta o risco de comprometimento. **Funcionalidade:** Monitore a reutilização de senhas e alerte os usuários quando uma senha é reutilizada, sugerindo a criação de uma senha única para cada serviço.

### 3. Avaliação da Força da Senha

**Problema:** Usuários frequentemente criam senhas fracas. **Funcionalidade:** Avalie a força das senhas em tempo real enquanto os usuários as digitam, fornecendo feedback sobre a segurança e sugestões para torná-las mais robustas.

### 4. Autenticação de Múltiplos Fatores (MFA)

**Problema:** Apenas uma senha pode não ser suficiente para proteger contas importantes. **Funcionalidade:** Integre opções de MFA, como autenticadores de dois fatores (2FA), biometria, e autenticação via dispositivos móveis.

### 5. Gerenciamento de Senhas Compartilhadas

**Problema:** Compartilhar senhas entre membros de uma equipe ou família pode ser inseguro. **Funcionalidade:** Permita o compartilhamento seguro de senhas entre usuários autorizados, mantendo um log de auditoria de quem acessou quais senhas e quando.

### 6. Monitoramento de Atividade Suspeita

**Problema:** Atividades não autorizadas podem passar despercebidas. **Funcionalidade:** Monitore e alerte os usuários sobre atividades suspeitas, como tentativas de login em locais não reconhecidos ou em horários atípicos.

### 7. Gerenciamento de Senhas de Aplicativos

**Problema:** Muitas senhas são salvas diretamente nos navegadores, onde podem ser menos seguras. **Funcionalidade:** Desenvolva uma extensão de navegador que armazene senhas de forma segura no gerenciador em vez de no navegador, oferecendo preenchimento automático seguro.

### 8. Rotação Automática de Senhas

**Problema:** Senhas antigas são menos seguras. **Funcionalidade:** Configure a rotação automática de senhas para contas importantes, alterando-as periodicamente e notificando o usuário das mudanças.

### 9. Armazenamento Segurizado com Criptografia Avançada

**Problema:** Senhas armazenadas podem ser alvo de ataques. **Funcionalidade:** Utilize criptografia de ponta a ponta (end-to-end encryption) para armazenar senhas, garantindo que apenas o usuário possa descriptografá-las.

### 10. Recuperação Segura de Conta

**Problema:** Perder acesso a uma conta pode ser complicado e inseguro. **Funcionalidade:** Desenvolva métodos seguros de recuperação de conta que não dependam apenas de questões de segurança, como recuperação por MFA ou através de contatos de confiança pré-configurados.

### 11. Identificação de Vulnerabilidades em Contas Vinculadas

**Problema:** Contas vinculadas a serviços vulneráveis podem comprometer a segurança. **Funcionalidade:** Verifique periodicamente as contas vinculadas a serviços de terceiros e alerte os usuários sobre quaisquer vulnerabilidades conhecidas nesses serviços.

### 12. Sugestões de Senhas Baseadas em Padrões Pessoais

**Problema:** Criar senhas que sejam ao mesmo tempo seguras e memoráveis pode ser difícil. **Funcionalidade:** Utilize inteligência artificial para sugerir senhas seguras que ainda sejam fáceis de lembrar para os usuários, baseadas em padrões pessoais (sem comprometer a segurança).

### 13. Backup e Sincronização Segura

**Problema:** Perder o acesso a senhas pode ser desastroso. **Funcionalidade:** Ofereça backup e sincronização seguros entre dispositivos, garantindo que os usuários sempre tenham acesso às suas senhas, mesmo em caso de falha de dispositivo.

### 14. Análise de Segurança de Sites

**Problema:** Usuários podem não estar cientes dos riscos de segurança dos sites que utilizam. **Funcionalidade:** Analise a segurança dos sites onde as senhas são usadas e informe os usuários sobre quaisquer riscos ou vulnerabilidades encontradas.

### 15. Treinamento e Conscientização em Segurança

**Problema:** Usuários frequentemente desconhecem as melhores práticas de segurança. **Funcionalidade:** Ofereça módulos de treinamento e conscientização sobre segurança cibernética, educando os usuários sobre como criar e manter senhas seguras e evitar ataques comuns.

**Não Funcionais:** Requisitos de desempenho, segurança, usabilidade, etc.

**Ferramentas:** Use um documento de especificação de requisitos ou uma ferramenta como Trello ou Jira para organizar suas tarefas e requisitos.

## 3. Planejamento do Projeto

**Objetivo:** Crie um plano detalhado de como o software será desenvolvido.

- **Cronograma:** 1 ano (15/05/2025).
- **Recursos:** 
	Back-end: Python com Django
	Database: PostgreSQL

### 1. Segurança

- **Hashing de Senhas:** Argon2 ou bcrypt para hashing de senhas.
- **Criptografia de Dados:**  AES-256 para criptografar dados sensíveis.

### 2. Integração de Serviços e APIs

- **Have I Been Pwned API:** Para verificar se as senhas dos usuários foram comprometidas em vazamentos.
- **OAuth2/OpenID Connect:** Para autenticação segura e integração com outros serviços.

### 5. Arquitetura e Design

- Monolithic

### 6. Ferramentas e Tecnologias Adicionais

#### Controle de Versão

Git

# Marcos: 
1. Salvar as senhas em um banco de dados
2. Criptografar as senhas no banco de dados, realizando a descriptografia ao utilizar a senha-mestra
3. Criação de interface funcional
4. Implementação de outras funcionalidades...