RPN Calculator
==============

A simple Reverse Polish Notation (RPN) calculator implemented in Python. This calculator supports basic arithmetic operations and handles errors gracefully.

# Getting started

To run the RPN calculator, you need to have Python 3 installed on your machine, along with `uv`.

1. Clone the repository

2. Navigate to the project directory:
   ```bash
   cd rpn
   ```
3. Install the required dependencies:
   ```bash
   uv sync
   ```
4. Run the application:
   ```bash
   uv run uvicorn rpn.main:app
   ```