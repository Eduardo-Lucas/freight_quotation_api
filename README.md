# freight_quotation_api

## Overview

This project is a Python application that uses Pydantic for settings management. The application is designed to be easily configurable and maintainable.

## Features

- Configuration management using Pydantic's `BaseSettings`
- Easy to extend and customize
- Follows best practices for Python development

## Requirements

- Python 3.7+
- `pydantic-settings` package

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/freight_quotation_api.git
   cd freight_quotation_api
   ```

2. Create a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Install the `pydantic-settings` package:
   ```sh
   pip install pydantic-settings
   ```

## Usage

1. Configure your settings in a `.env` file or directly in the code.

2. Run the application:
   ```sh
   uvicorn app.main:app --reload
   ```
