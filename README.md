Linux AI Monitoring Dashboard
Project Overview

Linux AI Monitor is a system monitoring tool built using Python and FastAPI.
It collects real-time Linux system information such as CPU usage, memory usage, and disk usage, and exposes the data through an API.

The project also includes a simple web dashboard to visualize system metrics.

This project demonstrates how to build a Linux monitoring system using Python APIs and web dashboards.

Project Architecture
Linux System
     │
     │
monitor.py (collect system data)
     │
     │
FastAPI Backend (api.py)
     │
     │
Dashboard (dashboard.html)
     │
     │
User Browser
Project Structure
linux-ai-monitor
│
├── api.py
├── monitor.py
├── dashboard.html
├── requirements.txt
└── README.md
Features

Linux system monitoring

CPU usage monitoring

Memory usage monitoring

Disk usage monitoring

FastAPI REST API

Web-based dashboard

Real-time system data display

Technologies Used

Linux

Python

FastAPI

HTML

System Monitoring Libraries

Git & GitHub

API Endpoints
Root Endpoint
GET /

Response:

{
  "message": "Linux AI Monitoring API"
}
System Monitoring Endpoint
GET /system

Returns system metrics such as:

CPU usage

Memory usage

Disk usage

Example Response:

{
  "cpu_usage": "25%",
  "memory_usage": "40%",
  "disk_usage": "60%"
}
Installation

Clone the repository:

git clone https://github.com/vishnuvp-codes/linux-ai-monitor.git

Navigate to project folder:

cd linux-ai-monitor

Install dependencies:

pip install -r requirements.txt
Running the Application

Start the FastAPI server:

uvicorn api:app --reload

Server will run on:

http://127.0.0.1:8000
API Documentation

FastAPI automatically provides interactive API documentation.

Open in browser:

http://localhost:8000/docs
Dashboard

Open the dashboard file in browser:

dashboard.html

This page displays system monitoring information from the API.

Use Cases

Linux system monitoring

DevOps learning project

Infrastructure monitoring

Backend API development practice



Author

Vishnu Priya
DevOps & Linux Enthusiast



