
---

# Site Quadros - Post-its Interativos

Projeto de mural interativo com post-its, desenvolvido com **React** (frontend) e **Django** (backend).  
Permite criar, mover, editar e deletar post-its, com cores aleatórias e persistência no backend.

---

## 📁 Estrutura do projeto


site_quadros/
├── frontend/ # React
│ ├── package.json
│ ├── src/
│ └── public/
├── backend/ # Django
│ ├── manage.py
│ ├── requirements.txt
│ └── ...resto do projeto Django...
└── README.md

<img width="269" height="240" alt="image" src="https://github.com/user-attachments/assets/8ca75db1-b956-4e0d-b2ac-8a36724ec9ef" />


<img width="1329" height="728" alt="image" src="https://github.com/user-attachments/assets/c7a1275e-0a73-4e29-9995-c615c591d888" />

update 2 escolha cores, icone excluir, editar e sem erros deletar... salva em banco
<img width="1335" height="730" alt="image" src="https://github.com/user-attachments/assets/6f5fda50-ccf3-4130-af7e-e129469ccab8" />

---

## 🚀 Tecnologias usadas

- Frontend: React, React-Draggable, Axios  
- Backend: Django, Django REST Framework  
- Banco de dados: SQLite (padrão, pode ser substituído por PostgreSQL)  

---

## ⚙️ Configuração e execução local

### 1. Backend (Django)

1. Entrar na pasta `backend`:

```bash
cd backend
Criar e ativar virtualenv (se ainda não tiver):
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
Instalar dependências:
pip install -r requirements.txt
Rodar servidor:
python manage.py runserver

Backend estará disponível em http://127.0.0.1:8000/.

2. Frontend (React)
Entrar na pasta frontend:
cd frontend
Instalar dependências:
npm install
Rodar servidor de desenvolvimento:
npm start

Frontend estará disponível em http://localhost:3000 e se conecta automaticamente ao backend.

🎨 Funcionalidades
Criar novos post-its com cores aleatórias
Arrastar post-its pelo mural
Editar texto clicando no post-it
Deletar post-its
Salvar posição e texto no backend automaticamente
🔮 Futuros aprimoramentos
Sistema de login e usuários
Salvar histórico de notas por usuário
Integração com VPS ou nuvem para deploy real
Layout responsivo e design aprimorado com cores pastel e animações
Sistema de coins / recompensas ou gamificação
Links de download do projeto ou páginas de demonstração
Integração com Twitch/Discord para compartilhar post-its em tempo real
💻 Deploy sugerido
Backend Django: VPS ou Heroku, configurando variáveis de ambiente e banco de dados PostgreSQL
Frontend React: Vercel, Netlify ou mesmo servido pelo backend Django via build/
Configurar proxy no React (package.json) para produção ou usar variáveis de ambiente
📌 Observações
O projeto é totalmente modular: frontend e backend podem ser hospedados separadamente
É necessário rodar backend antes do frontend para que as requisições funcionem
Banco de dados atual: SQLite (fácil para testes), mas recomenda-se PostgreSQL para produção
