# 🚀 Guia Completo: Como Subir o Projeto no GitHub

Este guia foi criado para ajudar iniciantes a subir um projeto local para o GitHub utilizando o GitHub Desktop.

---

## 📌 Pré-requisitos

Antes de começar, verifique:
  
* Git instalado no computador
* GitHub Desktop instalado
* Conta no GitHub
* Projeto salvo no computador

---

## 📁 Estrutura esperada do projeto

```bash
clima_rn/
├── scripts/
├── dags/
├── README.md
├── requirements.txt
├── .env
├── .gitignore
```

---

## 🧭 PASSO A PASSO

### 1. Abrir o GitHub Desktop

* Vá em:

  * **File → Add local repository**

---

### 2. Selecionar o projeto

Escolha a pasta:

```text
C:\Users\SeuUsuario\Desktop\clima_rn
```

Se aparecer:

> “This directory does not appear to be a Git repository”

👉 Clique em:

**Create a repository here**

---

### 3. Verificar arquivos

Você deverá ver:

* README.md
* scripts
* outros arquivos do projeto

---

### 4. Fazer o commit

Na parte inferior:

Mensagem:

```text
Primeiro commit do projeto
```

Clique em:

👉 **Commit to main**

---

### 5. Publicar no GitHub

Clique em:

👉 **Publish repository**

Escolha:

* Public (recomendado para portfólio)

---

### 6. Confirmar no GitHub

Acesse o site do GitHub e verifique se o repositório foi criado.

---

## 🔁 Como atualizar o projeto depois

Sempre que fizer mudanças:

1. Editar arquivos
2. Abrir GitHub Desktop
3. Escrever mensagem
4. Clicar em **Commit**
5. Clicar em **Push origin**

---

## ❗ Problemas Comuns e Soluções

---

### 🔴 Git não reconhecido

Erro:

```text
git não é reconhecido
```

✔ Solução:

* Instalar o Git
* Reiniciar o terminal

---

### 🔴 Nenhum arquivo aparece

✔ Possíveis causas:

* Pasta errada
* Git não inicializado

✔ Solução:

```bash
git init
git add .
```

---

### 🔴 Erro ao conectar no MySQL

Erro:

```text
ConnectionRefusedError
```

✔ Solução:

* Verificar se Docker está rodando
* Subir containers:

```bash
docker compose up -d
```

---

### 🔴 API não funciona (erro 401)

✔ Causa:

* API inválida ou não carregada

✔ Solução:

* Verificar arquivo `.env`
* Confirmar variável:

```env
API_KEY=sua_chave
```

---

### 🔴 Imagem não aparece no README

✔ Verificar:

* Nome correto do arquivo
* Caminho correto:

```markdown
![Arquitetura](./arquitetura_clima_rn.png)
```

---

## 🔐 Boas Práticas

✔ Nunca subir `.env`
✔ Usar `.gitignore`
✔ Commits com mensagens claras
✔ Um projeto = um repositório

---

## 🎯 Objetivo deste guia

Este material foi criado para auxiliar iniciantes a entender o fluxo de versionamento de código e publicação de projetos no GitHub.

---

## 👨‍💻 Autor

Lúcio Fábio Barbosa de Lima
📧 [engenheirodedados.luciofabio@gmail.com](mailto:engenheirodedados.luciofabio@gmail.com)
