# bible-gpt3-commentary
A OpenAI GPT powered commentary to the daily readings of Bible.


# Installation

1. Install requirements

```bash
pip install -r requirements.txt
```

2. Use env template to create your own env file. Add OpenAI API key to the env file.

```bash
cp .env.template .env
```

# Usage - Run the script

```bash
python main.py
```

# How it works?

1. The script will fetch the daily readings from [Polish] Deon.pl
2. Text of readings will be passed to OpenAI GPT API
3. The response will be saved to the file
4. The file will be uploaded to the Facebook site.

# How to contribute?

Fork the repo and create a pull request.
