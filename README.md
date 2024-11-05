# SnapBot - Snapchat Brute Force Tool

## Project Status
🚧 **Work In Progress (WIP)** 🚧  
An advanced brute-forcing No not really im just learing might become something though. tool designed specifically for Snapchat. SnapBot combines asynchronous requests, proxy support, CAPTCHA handling, and Tor integration to bypass detection and maximize efficiency.

## Features
- **Asynchronous Requests** with AIOHTTP for efficient brute-force attempts.
- **CAPTCHA Handling** with OpenCV, Tesseract OCR, and Selenium for text-based and interactive CAPTCHAs.
- **Proxy Support** for HTTP, HTTPS, SOCKS4, and SOCKS5 proxies, with automatic rotation to avoid rate limits.
- **Tor Network Integration** for continuous free IP rotation.
- **Logging** for tracking each login attempt, including errors and successes.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Password List](#password-list)
- [To-Do List](#to-do-list)
- [Legal Disclaimer](#legal-disclaimer)
- [Contributing](#contributing)

## Installation

### Clone the Repository:
```bash
git clone https://github.com/your-username/SnapBot.git
cd SnapBot
```
#### Install Required Dependencies
Ensure Python 3.8+ is installed, then install dependencies:

```bash
pip install -r requirements.txt
```
#### Install and Configure Tor (optional)
Install Tor for IP rotation:
```bash
sudo apt install tor
```
#### Start the Tor Service:
```bash
sudo service tor start
```
#### Download a Password List
Save a password list as passwords.txt in the SnapBot directory (see the Password List section below for sources). editors note I got lazy
