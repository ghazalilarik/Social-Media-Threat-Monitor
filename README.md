### Social Media Threat Monitor

#### Introduction
This Social Media Threat Monitor is a tool that continuously monitors social media channels such as Twitter and Reddit for mentions of data breaches, cyber threats, or vulnerabilities. It uses natural language processing (NLP) to categorize the types of threats and provides a mechanism for ongoing monitoring.

#### Features
- **Social Media Monitoring**: Collects public posts and mentions related to cybersecurity on platforms like Twitter and Reddit.
- **NLP-Based Threat Categorization**: Uses natural language processing to classify mentions into categories such as "Data Breach", "Vulnerability", and "General Threat".
- **Automated Monitoring**: Runs continuously and saves the results for further analysis.

#### Usage Instructions
1. **Setup Dependencies**: Install necessary packages using `pip`.
    ```sh
    pip install tweepy praw requests pandas scikit-learn textblob schedule
    ```
2. **Configure API Keys**: Replace the placeholders with your actual API keys for Twitter and Reddit.
   - `twitter_api_key`, `twitter_api_secret`, `twitter_access_token`, `twitter_access_secret`
   - `reddit_client_id`, `reddit_client_secret`, `reddit_user_agent`
3. **Run the Tool**: Use the following command to start the monitoring service.
    ```sh
    python social_media_threat_monitor.py
    ```

#### Prerequisites
- **Python 3.6 or above**: Ensure you have Python installed in your system.
- **Twitter API Keys**: You need API credentials to access Twitter data.
- **Reddit API Keys**: Reddit client ID, client secret, and user agent are required.

#### How It Works
1. **Set Up APIs**: The tool sets up connections to the Twitter and Reddit APIs using the provided credentials.
2. **Monitor Social Media**: It continuously monitors posts for specific keywords related to cybersecurity threats.
3. **Categorize Threats**: Natural language processing is used to categorize the threats into pre-defined types.
4. **Schedule Task**: Monitoring runs every hour and saves results in a CSV file.

#### Implementation Steps
1. **Clone Repository**: Clone this repository from GitHub.
2. **Install Dependencies**: Run the command `pip install -r requirements.txt` to install dependencies.
3. **Run the Tool**: Execute the Python script to start monitoring social media channels.

#### Contributing
If you find bugs or have suggestions for improvements, feel free to contribute by opening an issue or making a pull request.

#### License
This project is open-source and licensed under the MIT License.

#### Disclaimer
This tool is intended for educational purposes only. Users are responsible for ensuring they comply with applicable laws and regulations regarding data scraping and API usage.
