Secure Cloud Authentication (0-RTT Key Agreement)

This repository contains the implementation of a Secure Cloud Authentication system based on a certificateless key agreement protocol with 0-RTT (Zero Round Trip Time) session establishment.

The project demonstrates a fast, anonymous, and secure login mechanism with replay attack prevention using nonces and cryptographic techniques. It was developed as a self-initiated learning project to understand secure authentication workflows used in modern cloud environments.

Project Overview

Traditional authentication systems often require multiple communication rounds and rely on certificates or passwords, which can introduce latency and potential security risks.

This project implements:

Anonymous user authentication

Certificateless key agreement with 0-RTT session key derivation

Replay attack prevention using unique nonces

Secure session data storage using SQLite

A lightweight web interface built with Flask

The focus is on practical secure authentication, session key management, and database logging.

Features

Anonymous Login: User identities are anonymized using SHA-256 hashing.

0-RTT Session Keys: Session keys are derived with minimal handshake.

Nonce-Based Replay Protection: Unique nonces prevent repeated authentication attempts.

Certificateless Key Agreement: Avoids certificate management overhead.

Secure Storage: Stores anonymous user IDs, secret keys, and nonces in SQLite.

Web UI: Simple login and dashboard interfaces.

Technologies Used

Python 3.9+

Flask – Web framework

SQLite – Lightweight relational database

HTML / CSS / JavaScript

hashlib, hmac, secrets – Cryptographic modules

Visual Studio Code – Development environment

Google Chrome – Testing browser

Project Structure
secure-cloud-authentication-0rtt/
├── app.py
├── security.db
├── templates/
│   ├── index.html
│   └── dashboard.html
├── static/
│   └── style.css
└── README.md

Setup Instructions

Clone the repository

git clone https://github.com/Gayathri-Nandakumar16/secure-cloud-authentication-0rtt.git


Navigate into the project folder

cd secure-cloud-authentication-0rtt


Install dependencies

pip install flask


Run the application

python app.py


Open your browser and visit:

http://127.0.0.1:5000

Demo Video

Watch the demo here:
Google Drive Link:

<PASTE YOUR DEMO LINK HERE>


(Replace the above line with your actual video link.)

Learning Outcomes

This project provided hands-on experience with:

Web application security

0-RTT key agreement concepts

Cryptographic hashing and session key derivation

Replay attack prevention

Frontend–backend integration with Flask

Author

Gayathri Nandakumar
Self-Initiated Secure Cloud Authentication Project
January 2026

License

This project is provided for educational and learning purposes only.
