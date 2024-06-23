## Weekend project
weekend project to pass time

## Overview

Ai agent to check pros and cons of a bussiness idea and it's chance of profitablity

## Prerequisites

- Python
- API key from OpenAI (stored in .env file)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/achmad-dev/ai-agent.git
    cd ai-agent
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the OpenAI API key:

    - Add your OpenAI API key to `.env file`:

        ```
        OPEN_AI_API_KEY=your_secret_key
        ```

## Usage

1. Run the app:

    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to the provided URL. http://localhost:8501

3. Enter your bussiness idea.

## Configuration

- Adjust the `temperature` parameter in the OpenAI language model initialization for different levels of creativity and randomness in the generated content.


## Acknowledgments

- This project uses the [Streamlit](https://www.streamlit.io/) library for creating the web interface.
- [OpenAI](https://openai.com/) provides the GPT language model used for content generation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.