# browser-use-agent-project

## Overview
The `browser-use-agent-project` is a Python-based application designed for browser automation tasks using a language model interface. The project allows users to automate interactions with web applications, such as logging in, searching for products, and managing shopping carts.

## Project Structure
```
browser-use-agent-project
├── browser_use_agent
│   ├── __init__.py
│   ├── agent.py
│   └── llm.py
├── .env
├── requirements.txt
├── browser.py
└── README.md
```

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd browser-use-agent-project
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure your environment variables in the `.env` file. This file should include sensitive information such as API keys and credentials.

## Usage
To run the application, execute the following command:
```
python browser.py
```

The application will perform the following tasks:
1. Open the Zepto website.
2. Log in using saved credentials.
3. Search for 'yogurt'.
4. Add the first available yogurt to the cart.
5. Proceed to checkout, stopping before payment.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.