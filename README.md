# CodeLogic 🧠💻  
An AI-powered tutoring app that helps users learn **coding and math** through a conversational chat interface — built with **FastAPI**, **vanilla JavaScript**, and fully deployed using **Render** and **GitHub Pages**.

## 🔗 Live Demo

- 🌐 Frontend: [https://nscook19.github.io/CodeLogic/](https://nscook19.github.io/CodeLogic/)  
- 🚀 Backend API: [https://codelogic-backend.onrender.com](https://codelogic-backend.onrender.com)

---

## 🛠️ Tech Stack

| Layer        | Tools Used                                |
|--------------|--------------------------------------------|
| Frontend     | HTML, CSS, JavaScript                      |
| Backend      | Python, FastAPI                            |
| AI API       | OpenAI API (via secure backend proxy)      |
| Deployment   | GitHub Pages (Frontend), Render (Backend)  |
| Version Control | Git + GitHub (multi-branch workflow)    |
| Security     | Environment Variables (.env), API proxying |

---

## 📌 Features

- 🧠 Real-time AI tutoring for coding & math problems  
- 📄 Clean chat-style interface with timestamps and animations  
- ⚙️ Custom backend logic to detect confusion levels and handle OpenAI API securely  
- 🔒 API key protected on server-side using environment variables  
- 🌍 Fully deployed using free-tier infrastructure (Render + GitHub Pages)

---

## 💡 Key Technical Highlights

- 🔧 Built and deployed a full-stack chatbot using open-source tools and cloud hosting (no frameworks)
- 🌐 Configured secure API proxy on the backend to protect OpenAI keys with `python-dotenv` and `.env` files
- ⚙️ Diagnosed and fixed production deployment issues including backend sleep/wake cycles, 404 routing errors, and CORS misconfigurations
- 🔒 Used Git branches and history rewriting to remove exposed secrets and enforce secure DevOps practices
- 🧪 Created a clean, interactive UI with chat-style animations and real-time user interaction (via fetch API)

---

## ✍️ What I Learned

- ☁️ How to deploy and manage **cloud-hosted web applications**
- 🔍 Real-world debugging of issues across **frontend, backend, and network layers**
- 🧰 Best practices in **environment config, version control, and API security**
- 📋 The importance of **clear documentation and problem-solving** in multi-layer systems
