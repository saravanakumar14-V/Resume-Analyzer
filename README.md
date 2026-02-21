 📄 Resume Analyzer

A beginner-friendly full-stack web application that allows users to upload resumes and analyze them using a FastAPI backend and a Next.js frontend.

This project was built as my first complete full-stack project to understand how frontend, backend, APIs, and GitHub work together.

---

🚀 Features

- Upload resumes in PDF or DOCX format
- Extract text content from resumes
- Analyze resume text
- Backend API built with FastAPI
- Frontend built with Next.js
- Simple and clean user interface

---

🏗️ Project Structure

```
Resume-Analyzer/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── app/
│   ├── public/
│   ├── package.json
│
└── README.md
```

---

🛠️ Tech Stack

# Backend
- Python
- FastAPI
- Uvicorn
- pdfplumber
- python-docx

# Frontend
- Next.js
- React
- TypeScript
- CSS

---

 ⚙️ How to Run the Project

 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Resume-Analyzer.git
cd Resume-Analyzer
```

---

 2️⃣ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at:
http://127.0.0.1:8000

---

 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:
http://localhost:3000

---

🔄 How the Application Works

1. User uploads a resume from the frontend
2. Resume file is sent to the FastAPI backend
3. Backend extracts text from the file
4. Processed data is returned as JSON
5. Frontend displays the result

---

🎯 Purpose of This Project

This project was built to:

- Learn full-stack development
- Understand frontend–backend communication
- Practice REST APIs
- Learn file uploads and text extraction
- Gain experience using Git and GitHub

---

🔮 Future Improvements

- Add database support
- Add authentication
- Improve resume analysis logic
- Deploy backend and frontend online
- Add AI-based scoring

---

👨‍💻 Author

Saravana Kumar  
Second-year Computer Science Student  

---

 ✅ Notes

- This project is built for learning purposes
- No paid tools were used
- Created as a beginner full-stack project
