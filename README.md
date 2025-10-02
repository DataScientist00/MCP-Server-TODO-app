# MCP Server for Todo App

## Watch the Video 📺

[![YouTube Video](https://img.shields.io/badge/YouTube-Watch%20Video-red?logo=youtube\&logoColor=white\&style=for-the-badge)](https://youtu.be/jG_mxYPmqgk)

## Overview

This project demonstrates a **local MCP server for a Todo application** using **FastMCP**, along with **uv** for project management and **Inspector** to verify that the local stdio server is working correctly. The goal is to provide an interactive command-based tool to **add, list, and remove todos** while persisting data in a JSON file.


<img width="1280" height="720" alt="Image" src="https://github.com/user-attachments/assets/1c0886c0-75b8-4a7e-8e71-71059c537c73" />
---

## Table of Contents

1. [Introduction](#introduction)
2. [Project Files](#project-files)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Features](#features)
7. [Results](#results)
8. [Contributing](#contributing)
9. [License](#license)

---

## Introduction

Building a local MCP server allows you to manage tasks efficiently via Python scripts. This project leverages **FastMCP** to define tools for CRUD operations on todos and uses **uv** and **Inspector** for monitoring project workflow and server health.

### Objectives

* Build a local MCP server for task management.
* Add, list, and remove todos with a simple CLI interface.
* Persist todo data in a JSON file.
* Monitor server status using **Inspector**.
* Use **uv** for project management tasks.

---

## Project Files

### Input

* `todos.json` - Stores all todo items persistently.
* `main.py` - Main MCP server script.

You can start fresh by deleting `todos.json`; the server will recreate it automatically.

---

## Technologies Used

* **Python**: Core programming language.
* **FastMCP**: Framework to define tools and run MCP servers.
* **Inspector**: Check local stdio server functionality.
* **uv**: Project management tool for Python workflow.
* **JSON**: Persistent storage for todos.

---

## Installation

### Prerequisites

Ensure Python (>= 3.10) is installed on your system.

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/DataScientist00/MCP-Server-TODO-app.git
   cd todo-mcp-server
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the MCP server using:

```bash
uv run fastmcp run main.py
```

The server will:

* Load or create `todos.json`.
* Provide CLI tools to **add**, **list**, and **remove todos**.
* Allow you to monitor the local stdio server via **Inspector**.
* Use **uv** to organize and manage project workflow.

---

## Features

* **Local MCP Server**: Run a command-based server for todos.
* **Persistent Storage**: All tasks saved in `todos.json`.
* **Add/List/Remove Todos**: CRUD operations via simple CLI tools.
* **Server Monitoring**: Verify server status with Inspector.
* **Project Management**: Organize workflow with **uv**.
* **Lightweight & Fast**: Simple Python script, no heavy dependencies.

---

## Results

* **Efficient Task Management**: Add, view, and delete tasks in real-time.
* **Data Persistence**: Todos remain stored across server restarts.
* **Project Monitoring**: Ensure the local MCP server is running correctly.
* **Applications**:

  * Personal task management
  * Learning MCP server setup
  * Python-based workflow experiments

---

## Contributing

We welcome contributions to improve this project! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Create a pull request.

---

## Acknowledgements

* Thanks to **FastMCP** for enabling easy tool-based server creation.
* **Inspector** for monitoring local stdio servers.
* Python open-source community for support and inspiration.

---

## Contact

For questions or support, please reach out:

* **Email**: [nikzmishra@gmail.com](mailto:nikzmishra@gmail.com)
* **YouTube**: [NeuralArc00](https://www.youtube.com/@NeuralArc00/videos)


