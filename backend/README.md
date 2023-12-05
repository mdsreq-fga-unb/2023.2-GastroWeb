# Passo a passo da inicialização do Docker para desenvolvimento:

### 1. Clonando o repositório

```
git clone https://github.com/mdsreq-fga-unb/2023.2-GastroWeb.git
```

### 2. Ir para a Branch Dev

```
git checkout dev
```

### 3. Inicializar o Docker

Você precisa ter o docker baixado!

```
sudo docker-compose up --build
```

### 4. Caso precise subir o banco de dados manualmente

- 1. Entre no container do backend

```
sudo docker exec -it gastro-backend bash
```

- 2. Execute 

```
python3 database/start.py
```

### 5. Saindo do Docker

- Apenas dê um Ctrl + C no terminal em que ele está rodando.


#### Comandos para verificar as tabelas no postgresql

1. Entrar no container
```
sudo docker exec -it postgresql bash
```

2. Entrar no sql

```
psql -U admin -d fastapi
```

3. Verificar se as tabelas foram carregadas

```
\dt
```

4. Verificar os dados da tabela

```
SELECT * FROM receitas;
```
