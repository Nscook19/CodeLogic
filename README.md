# CodeLogic: AI Tutoring Meets Data Science

A full-stack AI-powered tutoring system that helps users learn **coding and math** through interactive conversation. Built with **FastAPI**, **vanilla JavaScript**, and a focus on **data-driven prompt analysis** using Python and Jupyter notebooks.

---

## Live Demos

- **Frontend**: [https://nscook19.github.io/CodeLogic/](https://nscook19.github.io/CodeLogic/)
- **Backend API**: [https://codelogic-backend.onrender.com](https://codelogic-backend.onrender.com)

---

## Project Overview

CodeLogic is more than a chatbot — it’s a **data science-backed platform** designed to personalize tutoring based on prompt complexity, user intent, and historical data patterns. Using **OpenAI's API**, the system generates dynamic responses to coding and math questions, while also being able to collect and analyze usage data to improve performance and topic relevance.

---

## Data Science & Analysis

The backend logs user prompts and AI responses to a structured CSV format. Using **pandas**, **scikit-learn**, **matplotlib**, and **seaborn** in **Jupyter Notebooks**, I performed an in-depth analysis on 100 user queries:

- Clustered prompts using **TF-IDF vectorization** and **KMeans** to categorize question types
- Identified key topic trends such as dominant interest in **calculus** and **Python programming**
- Measured question and response complexity via word counts and response length distributions
- Visualized semantic similarity between topics using **cosine similarity heatmaps**
- Extracted top TF-IDF terms per cluster to uncover key user vocabulary
- Built a full Markdown report summarizing all findings, trends, and interpretations

This analysis allowed me to **better understand user behavior** and informed how I designed both the interface and backend logic.

---

## Tech Stack

| Layer        | Tools Used                                |
|--------------|--------------------------------------------|
| Frontend     | HTML, CSS, JavaScript (no frameworks)      |
| Backend      | Python, FastAPI                            |
| AI Logic     | OpenAI API (proxied securely)              |
| Data Analysis| Jupyter Notebooks, pandas, sklearn, seaborn|
| Deployment   | GitHub Pages (Frontend), Render (Backend)  |
| Security     | `.env` for secrets, GitHub + dotenv        |

---

## Key Features

- Chat-style interface for math/coding help with animated responses
- Secure API proxying to keep OpenAI keys off the frontend
- CSV logging of user queries for real-time data capture
- Hint-level detection and prompt filtering logic (Python)
- Exploratory Data Analysis pipeline built from scratch

---

## Technical Achievements

- Built a RESTful API using **FastAPI** for managing OpenAI prompts and user logging
- Designed a **Jupyter notebook-based pipeline** to analyze educational query patterns
- Debugged and deployed a production backend with fixes for:
  - Sleep/wake delays on Render
  - CORS misconfigurations
  - Static file routing for GitHub Pages
- Applied **DevOps practices**:
  - Removed exposed secrets using git history rewriting
  - Organized development via feature branches and version control

---

## What I Learned

- How to build, deploy, and maintain a cloud-hosted AI application
- How to leverage **data science** to inform design decisions
- Best practices in API security, proxy architecture, and backend logging
- Real-world debugging across frontend, backend, and network layers
- Importance of clean visualization and **data storytelling** using Python

---

