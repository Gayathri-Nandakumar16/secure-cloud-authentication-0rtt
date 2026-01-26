# Secure Cloud Authentication (0-RTT Based)

This repository contains a web-based Secure Cloud Authentication system designed to demonstrate 0-RTT (Zero Round Trip Time) session establishment, anonymous authentication, and replay attack prevention.

The project is developed as a self-initiated academic learning project to understand secure authentication workflows in cloud-based applications without relying on traditional password-based or certificate-heavy mechanisms.

---

## Project Overview

Modern cloud applications require authentication mechanisms that are fast, secure, and efficient. Traditional authentication systems often introduce additional communication delays and depend on certificates or static credentials.

This project focuses on implementing a lightweight secure authentication workflow that demonstrates:
- Anonymous login
- 0-RTT-style session establishment
- Replay attack prevention
- Secure session logging
- Web-based authentication flow

The implementation emphasizes conceptual clarity and practical understanding rather than enterprise-level cryptographic complexity.

---

## Key Features

- Anonymous user authentication  
- 0-RTT session establishment for faster authentication  
- Replay attack prevention using unique nonces  
- Secure session data storage using SQLite  
- Simple and clean web-based interface  

---

## Technologies Used

- Python  
- Flask  
- SQLite  
- HTML, CSS, JavaScript  
- Visual Studio Code  
- Google Chrome  

---

## Project Structure

secure-cloud-authentication-0rtt/
├── app.py
├── security.db
├── templates/
│ ├── index.html
│ └── dashboard.html
├── static/
 └── style.css


## Setup Instructions

1. Download the repository as a ZIP file from GitHub and extract it to a folder.  
2. Open the folder in **Visual Studio Code** or your preferred IDE.  
3. Install Flask if not already installed:
pip install flask
Run the application:
python app.py
Open your browser and go to:
http://127.0.0.1:5000



**Demo Video**
Google Drive link to project demo:
https://drive.google.com/file/d/10wtoz-g-1pF46tsE8rvFjHiysmlU3hGV/view?usp=drive_link


**Learning Outcomes**
Understanding secure cloud authentication workflows

Practical exposure to 0-RTT session concepts

Replay attack prevention using nonces

Flask-based backend development

Frontend and backend integration

Session data storage using SQLite

Author
Gayathri Nandakumar
Secure Cloud Authentication – Self-Initiated Project
January 2026

License
This project is intended for academic and educational purposes.


