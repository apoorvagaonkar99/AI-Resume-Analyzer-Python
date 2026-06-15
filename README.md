# AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Flask, NLP, SQLite, and Bootstrap.

## Features

* ATS Score Calculation
* Resume Skill Extraction
* Job Description Matching
* Skill Gap Analysis
* Resume Completeness Check
* PDF Report Generation
* Resume Analysis History
* SQLite Database Integration

## Tech Stack

* Python
* Flask
* SQLite
* Bootstrap
* NLP
* PDF Processing
* Matplotlib

## Project Structure

```text
AI-Resume-Analyzer
│
├── app.py
├── ats_score.py
├── jd_matcher.py
├── database.py
├── skill_gap.py
├── report_generator.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── history.html
│
├── static/
├── uploads/
└── reports/
```

## Installation

```bash
git clone https://github.com/apoorvagaonkar99/AI-Resume-Analyzer-Python.git

cd AI-Resume-Analyzer-Python

pip install -r requirements.txt

python app.py
```

## Usage

1. Upload a Resume (PDF)
2. Paste a Job Description
3. Click **Analyze Resume**
4. View ATS Score, JD Match, Missing Skills, and Recommendations
5. Download PDF Report

## Key Features

### ATS Score

Evaluates resume quality and ATS compatibility.

### JD Matching

Compares resume skills against job requirements.

### Skill Gap Analysis

Identifies missing skills required for a target role.

### PDF Report Generation

Generates downloadable professional reports.

### Resume History

Stores previous analyses using SQLite.

## Author

**Apoorva D Gaonkar**

Bachelor of Engineering (Computer Science)

GitHub: https://github.com/apoorvagaonkar99
