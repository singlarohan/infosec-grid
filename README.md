# LogLama

LogLama is a Python script that utilizes a Language Model (LLM) to check logs for compliance and other security breaches. It identifies security breaches in logs and generates reports based on a given ruleset.

## Features

- Automates the process of checking logs for security breaches and compliance violations.
- Utilizes a Language Model to provide explanations and suggestions for fixing breaches.
- Generates breach reports for identified breaches and non-compliant logs.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/singlarohan/infosec-grid.git
   cd infosec-grid
## Execution

1. Run the script:
    ```sh
    python main.py

2. Enter the path to the log file (PDF, CSV, or TXT) when prompted.
3. Enter the path to the ruleset file (PDF, CSV, TXT, or JSON) when prompted
4. After some time, the script will analyze the logs using the provided ruleset and generate breach reports if any breaches are detected. Breach details, including log number, user_id, and suggested fixes, will be outputted in a file under comp/breaches.txt.


<!-- CONTACT -->
## Contact
- [Pragati Arora](mailto:pragatiarora314@gmail.com)
- [Rohan Singla](mailto:rohansingla2003@gmail.com)

Project Link: [https://github.com/singlarohan/infosec-grid](https://github.com/singlarohan/infosec-grid)
