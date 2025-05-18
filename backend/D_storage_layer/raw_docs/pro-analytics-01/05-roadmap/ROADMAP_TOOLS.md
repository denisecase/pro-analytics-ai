# ROADMAP: Tools to Know

For Python Data Analytics, Business Intelligence, Machine Learning, and more.

All tools listed are **free** unless noted. Check the boxes as you add skills. 

---

## Core Setup

- [ ] **Visual Studio Code (VS Code)** - Modern IDE with Python, Markdown, and Git support. Use to edit code, run notebooks, and manage projects.
- [ ] **Python** - Primary programming language for scripting, data analysis, and BI automation.
- [ ] **Markdown** - Simple formatting language for README files, documentation, and Jupyter notes.
- [ ] **Jupyter Notebooks / JupyterLab** - Interactive notebooks that combine code, output, and formatted text. Essential for data exploration and storytelling.
- [ ] **VS Code Jupyter Extension** - Rich notebook editing in VS Code, with support for Markdown, plots, and cell output.

---

## Version Control and Project Management

- [ ] **Git + GitHub** - Version control and collaboration platform.  Track changes, share code, and publish projects.
- [ ] **.gitignore / requirements.txt / virtual environments** - Tools to manage dependencies and keep projects clean and reproducible.
- [ ] **GitHub Actions** - Automate testing, notebooks, or deployments from GitHub.
- [ ] [**TortoiseGit**](https://tortoisegit.org/) - Windows only, integrates Git with Windows File Explorer. 
---

## Terminals  

- [ ] [**PowerShell**](https://learn.microsoft.com/en-us/powershell/) - Use on Windows Machines. Also a very popular cross-platform automation tool for Mac/Linux.  
- [ ] [**Windows Subsystem for Linux (WSL/WSL2)**](https://learn.microsoft.com/en-us/windows/wsl/about) - Linux environment on Windows machines. Strongly recommended or required when testing advanced Apache and open-source data tools.  
- [ ] [**bash / zsh / Git Bash**](https://www.gnu.org/software/bash/) - Common terminal interfaces for Mac/Linux. Git Bash provides a bash shell for Windows.  

---

## Data Manipulation & In-Memory Processing

- [ ] [**Pandas**](https://pandas.pydata.org/) - Core library for tabular data manipulation and analysis in Python.
- [ ] [**Dask**](https://www.dask.org/) - Parallel processing for Python, scalable alternative to Pandas. Handles larger-than-memory data with parallel computing.
- [ ] [**Polars**](https://pola.rs/) - High-performance DataFrame library (written in Rust). Fast and efficient, especially for large datasets.

---

## Modern Analytics Data Engineering Tools

- [ ] [**dbt**](https://www.getdbt.com/) - Transform and test SQL-based analytics workflows in a modular way.
- [ ] [**SQLMesh**](https://sqlmesh.com/) - Modern data transformation and version control for SQL-based workflows. Allows modular and repeatable ETL development.

---

## In-Process SQL & Columnar Data

- [ ] [**DuckDB**](https://duckdb.org/) - In-process SQL engine. Run fast queries directly on CSVs and Parquet files.
- [ ] **Apache Arrow** - Columnar data format that improves performance across tools like DuckDB and Polars.

---

## Distributed Computing & Big Data Processing

- [ ] [**Apache Spark**](https://spark.apache.org/) - Distributed processing engine for big data and analytics. Uses micro-batching, good for iterative machine learning tasks, mature ecosystem with extensive community support.
- [ ] [**PySpark**](https://spark.apache.org/docs/latest/api/python/) - Python API for working with Apache Spark.
- [ ] [**Apache Flink**](https://flink.apache.org/) - Highly scalable stream processing engine for exactly once event processing, real-time analytics, and complex events.

---

## Data Lakehouse & Table Formats

- [ ] [**Delta Lake**](https://delta.io/) - open source framework for data lakes
- [ ] [**Apache Iceberg**](https://iceberg.apache.org/) - High-performance table format for huge analytic datasets, enabling fast data lake queries and ACID transactions.  
- [ ] [**Apache Hudi**](https://hudi.apache.org/) - Real-time data lake platform for incremental data processing and streaming ingestion.  
- [ ] [**Apache XTable**](https://xtable.apache.org/) - Multi-format table abstraction layer, enabling seamless conversion between Iceberg, Delta Lake, and Hudi.  

---

## Data Pipelines & Quality

- [ ] [**Apache NiFi**](https://nifi.apache.org/) - Visual tool to build and manage automated data flows.
- [ ] [**Prefect**](https://www.prefect.io/) - Orchestrate and schedule ETL pipelines. Great for managing dependencies and retries in production environments. See also [Apache Airflow](https://airflow.apache.org/). 
- [ ] [**Pandera**](https://pandera.readthedocs.io/) - open source DataFrame validator tool 
- [ ] [**Tableau Prep**](https://www.tableau.com/products/prep) - *(Paid, but free for students via Tableau for Students)* Visual tool to clean, shape, and join data before loading into Tableau dashboards.
- [ ] [**Great Expectations, GX Cloud**](https://greatexpectations.io/) - Tool for validating and testing data quality in pipelines or notebooks. Used in enterprise-grade pipelines to ensure data reliability.

---

## Streaming & Real-Time Processing

- [ ] [**WebSockets**](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) - Real-time communication in dashboards and live apps.
- [ ] Python [**socket.io**](https://python-socketio.readthedocs.io/) - real-time bidirectional event-based communication between clients (e.g., web browsers) and a server.
- [ ] [**Apache Kafka**](https://kafka.apache.org/) - High-throughput distributed messaging system for real-time data.
- [ ] [**Apache Pulsar**](https://pulsar.apache.org/) - Cloud-native distributed messaging and event streaming platform for high-throughput, low-latency real-time processing.

---

## Web Scraping & APIs

- [ ] [**requests**](https://requests.readthedocs.io/) - Simple HTTP library for making API calls.
- [ ] [**BeautifulSoup**](https://beautiful-soup-4.readthedocs.io/) - HTML parser for web scraping and structured data extraction.
- [ ] [**Scrapy**](https://www.scrapy.org/) - Open-source scraping and extraction framework.
- [ ] [**FastAPI**](https://fastapi.tiangolo.com/) - High-performance web framework for building APIs in Python.
- [ ] [**Flask**](https://flask.palletsprojects.com/) - Lightweight microframework for building web apps and data services.

---

## Data Visualization: Core

- [ ] [**Matplotlib**](https://matplotlib.org/) - Core plotting library for Python.
- [ ] [**Seaborn**](https://seaborn.pydata.org/) - Statistical data visualization built on top of Matplotlib.
- [ ] [**Plotly**](https://plotly.com/) - Interactive charts and graphs, browser-based.

---

## Data Visualization: Interactive Web Apps

- [ ] [**Streamlit**](https://streamlit.io/) - Create interactive web apps directly from Python scripts.
- [ ] [**Plotly Dash**](https://dash.plotly.com/) - Build analytical web applications with no front-end experience required.

---

## Data Visualization: Interactive and Dashboarding Tools

- [ ] [**PyShiny**](https://shiny.posit.co/py/) - Reactive Python dashboard framework (inspired by the popular R Shiny).
- [ ]  [**Apache Superset**](https://superset.apache.org/) - Open-source BI tool for building interactive dashboards and data exploration.
- [ ] [**Power BI**](https://www.microsoft.com/en-us/power-platform/products/power-bi) - *(Free for students and basic use)* - Professional Windows-only dashboarding tool used widely in business.
- [ ] [**Tableau**](https://www.tableau.com/) - *(Paid, but free for students via Tableau for Students)* - Leading BI dashboard platform used in many companies.

---

## Cloud Tools & Deployment

- [ ] [**Google Colab**](https://colab.research.google.com/) - Free hosted Jupyter notebooks with built-in libraries and GPU support.
- [ ] [**ShinyLive**](https://shinylive.io/py/examples/) - Host interactive Shiny applications directly in the browser without servers.
- [ ] [**Streamlit Cloud**](https://streamlit.io/cloud) - Host Streamlit dashboards and apps online with a free account.
- [ ] [**Render**](https://render.com/) - Platform for deploying FastAPI, Flask, and Python web apps easily.
- [ ] [**Railway**](https://railway.com/) - Platform for deploying web apps and microservices easily.
- [ ] [**AWS Lambda**](https://aws.amazon.com/pm/lambda/) - Run Python functions in the cloud without managing servers. Free tier available.
- [ ] [**Microsoft Azure Functions**](https://learn.microsoft.com/en-us/azure/azure-functions/) - Cloud-based serverless function execution from Microsoft. Free tier available.

---

## AI & Semantic Tools (Advanced or Optional)

- [ ] [**Chroma (ChromaDB)**](https://www.trychroma.com/) - Open-source vector database for storing and searching embeddings (semantic search). Used in AI pipelines for tasks like document search, RAG apps, and chatbots.


---

[🏠 Back to Home](https://github.com/denisecase/pro-analytics-01)
