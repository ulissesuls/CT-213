# 📘 Comandos Básicos do Git – Explicação Detalhada

## 📌 1. `git status`

- Mostra o estado atual do repositório.
- Informa quais arquivos foram modificados, quais estão prontos para commit e quais ainda não foram adicionados.

**Exemplo de uso:**

```bash
git status
```


## 📌 2. `git add`

* Adiciona arquivos ao  *staging area* , ou seja, prepara os arquivos para o commit.
* Pode adicionar arquivos específicos ou todos os arquivos modificados.

**Exemplos de uso:**

```bash
git add nome-do-arquivo.txt
git add .   # Adiciona todos os arquivos modificados
```


## 📌 3. `git commit`

* Registra as mudanças no histórico do repositório (cria um snapshot).
* É necessário passar uma mensagem descritiva com `-m`.

**Exemplo de uso:**

```git
git commit -m "Mensagem descritiva explicando as alterações"
```


## 📌 4. `git push`

* Envia os commits locais para o repositório remoto (ex: GitHub).
* Garante que suas alterações fiquem disponíveis na nuvem.

**Exemplo de uso:**

```
git push origin main
```


## 📌 5. `git pull`

* Atualiza seu repositório local com as mudanças feitas por outras pessoas no repositório remoto.
* Equivale a `git fetch` + `git merge`.

**Exemplo de uso:**

```
git pull origin main
```


## 📌 6. `git branch`

* Lista todas as branches existentes no repositório.
* Pode ser usado para criar (`-b`) ou mudar de branch (`checkout`).

**Exemplos de uso:**

```
git branch           # Lista branches
git branch nova-branch  # Cria uma nova branch
git checkout nova-branch # Alterna para a nova branch
```

## 🔁 Comandos Complementares

### 📥 `git clone`

* Clona um repositório remoto para sua máquina local.
  ```
  git clone https://github.com/usuario/repositorio.git
  ```

### 📜 `git log`

* Exibe o histórico de commits.

  ```
  git log
  ```

## 💡 Dicas Finais

* 🔍 Sempre faça um `git status` antes de qualquer coisa para saber onde você está no fluxo do Git.
* 🧹 Para remover arquivos do controle do Git, sem apagar do disco:

  ```
  git rm --cached nome-do-arquivo
  ```
* 🚨 Se cometeu um erro no commit e precisa corrigir a mensagem:

  ```
  git commit --amend -m "Nova mensagem"
  ```
* 🛠️ Se quiser restaurar um arquivo modificado ao último commit:

  ```
  git checkout -- nome-do-arquivo
  ```
