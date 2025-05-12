# CodeLogic 🧠💻  
An AI-powered tutoring app that helps users learn **coding and math** through a conversational chat interface — built with FastAPI, vanilla JS, and fully deployed on **Render** and **GitHub Pages**.

## 🔗 Live Demo

🌐 Frontend: [https://nscook19.github.io/CodeLogic/](https://nscook19.github.io/CodeLogic/)  
🚀 Backend API: [https://codelogic-backend.onrender.com](https://codelogic-backend.onrender.com)

---

## 🛠️ Tech Stack

| Layer        | Tools Used                                |
|--------------|--------------------------------------------|
| Frontend     | HTML, CSS, JavaScript                      |
| Backend      | Python, FastAPI                            |
| AI API       | OpenAI API (via secure backend proxy)      |
| Deployment   | GitHub Pages (Frontend), Render (Backend)  |
| Version Control | Git + GitHub                            |

---

## 📌 Features

- 🧠 Real-time AI tutoring for coding & math problems
- 📄 Clean chat-style interface with timestamps and animations
- ⚙️ Custom backend logic to detect confusion levels and handle OpenAI API securely
- 🔒 API key protected on server-side using environment variables
- 🌍 Fully deployed using free-tier infrastructure (Render + GitHub Pages)

---

## ✨ What I Learned

> “This project was a deep dive into **frontend/backend integration**, and deploying a **real-world, user-facing AI application**.”

### 🧱 Core Lessons:
- **Frontend Dev**: Creating responsive interfaces using HTML/CSS/JS without frameworks
- **Backend Dev**: Building API endpoints with FastAPI and structuring Python logic for response generation
- **Environment Config**: Using `.env` securely, and loading API keys with `python-dotenv`
- **Deployment**:
  - Deploying static frontend to **GitHub Pages**
  - Hosting a Python web service on **Render**
  - Diagnosing production errors (e.g. 404, backend sleep/wake, incorrect paths)
- **DevOps Workflow**: Using Git branches (`main` and `gh-pages`), force-pushes, and history rewriting to remove secrets from Git history

---

## 🚧 Future Plans

- Save and reload chat history using localStorage or backend DB
- Add topic filtering (e.g. Python vs Algebra vs JavaScript)
- Display smarter AI suggestions based on hint levels
