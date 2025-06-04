# Site Database Leak Scanner

## Overview

This is a simple Python-based tool designed to scan websites for exposed database backup files. It attempts to locate common database backup paths on a given website and checks if these files contain sensitive SQL data such as table creation commands or passwords.

The tool helps security researchers and penetration testers quickly identify exposed database files that may lead to data leaks.

## How It Was Made

- Written in Python 3  
- Uses `requests` library to make HTTP requests to target URLs  
- Uses `concurrent.futures.ThreadPoolExecutor` to perform concurrent scanning for faster results  
- Loads paths dynamically from a file named `Tomas.txt` which contains a list of common database backup file paths  
- Uses colored console output via ANSI escape codes without any external library dependencies  
- Handles HTTP and HTTPS URLs and ignores SSL certificate warnings for flexibility during testing  

## Installation

Make sure you have Python 3 installed. You also need to install the `requests` library:

```bash
pip install requests
```

Download the script and the Tomas.txt file to your working directory. Tomas.txt should contain a list of paths to check, one per line.

Alternatively, you can clone the repository:
```bash
git clone https://github.com/Toma1264git0hub/Site-databases-.git
```
```bash
cd Site-databases-
```

Usage

Run the Python script:
```bash
python3 Adol.py
```

You will be prompted to enter the target site URL (e.g., http://example.com). The script will then scan the site for exposed database backup files listed in Tomas.txt.

Output

Results will be printed to the console with found files in green and not found files in red.

Found database URLs are saved in db_leaks.txt.


Notes

The tool ignores SSL certificate verification to work with sites having self-signed or invalid certs.

Make sure you have permission to scan the target sites to avoid legal issues.

Customize Tomas.txt to add more paths or tailor the scan to specific targets.



---

Programmer

TELEGRAM: @K_DKP

TIKTOK: @.html.1

GITHUB: @toma1264git0hub
