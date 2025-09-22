# Transliteration Telegram Bot

This Telegram bot is designed to transcribe Cyrillic characters into Latin script. The bot transliterates characters in accordance with the Russian Foreign Ministry Order No. 2113, ensuring proper transliteration.

This Telegram bot uses a Docker container solution with a Dockerfile included in the repository. It can also be run locally on your machine using the bot.py script.

## Docker Container Launch Instructions:

1. Clone the Git repository into your folder.
2. Ensure Docker is installed. If not, follow the official Docker installation guide to install the Docker engine.
3. Open the Dockerfile and insert your Telegram bot token into:

    ```dockerfile
    ENV TOKEN='YOUR_BOT_TOKEN_HERE'
    ```

4. Open an SSH terminal in the folder where the Dockerfile, script, and requirements files are located.
5. Run the command: `docker build -t your_docker_image_name.`
6. Run the command: `docker run -d -p 80:80 your_docker_image_name`

## Notes:

* Logs are stored in the `logs.log` file, which is created automatically when you launch the Docker container.
* To extract the logs file, use the command:

    ```bash
    docker cp Your_docker_container_name:/app/logs.log Your_local_path
    ```

## Additional Recommendations:

* Verify that all required dependencies are installed.
* Check the permissions for file access.
* Ensure the bot token is correctly set in the environment variables.

