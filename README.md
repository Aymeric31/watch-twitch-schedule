# Watch-twitch-schedule
Welcome to the Watch twitch schedule project!

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)

## Introduction

The Twitch Schedule Update Detector project is designed to monitor a Twitch streamer's schedule page and automatically detect updates or changes to their schedule. Once an update is detected, the system sends a tweet to the streamer's Twitter account and discord channel to inform their followers.

## Features

- Weekly monitoring of the Twitch schedule page with a cron.
- Automatic detection of schedule updates. ( using github action )
- Automatic tweet notifications to the streamer's Twitter account and discord channel.
- Automatic push on the branch the data of the twitch schedule week, and replaced by the new one if the schedule has been updated

## Getting Started
These instructions will help you set up and run the project on Github Action.

### Prerequisites

Before you begin, make sure you have the following:
- **Discord Webhook:** You need to create a Discord Webhook to receive notifications and send the message. You can create one from your Discord server by following the Discord documentation on setting up webhooks.
- **GitHub Repository with GitHub Actions Enabled:** You should have a GitHub repository where you intend to use this project. Ensure that GitHub Actions is enabled for your repository. You can check and enable it in the "Actions" tab of the repository.

### Creating Developer Applications

Before you can use this tool to check the twitch schedule and publish message on twitter and discord, you need to create developer applications on Twitter and Twitch. Follow these steps:

**Twitter Developer Application**

  - Go to the Twitter Developer Portal.

  - Click on the "Create an App" button and follow the instructions to create a Twitter developer application.

  - Once your Twitter app is created, obtain the API keys and access tokens, and add them to your project's configuration file.

**Twitch Developer Application**

  - Go to the Twitch Developer Portal.

  - Click on the "Create an App" button and follow the instructions to create a Twitch developer application.

  - After creating your Twitch app, obtain the Client ID and Client Secret, and add them to your project's configuration file.


## Usage

This project is configured to be used with GitHub Actions for automated monitoring. Here's how to set it up:

1. **Fork this Repository:** Start by forking this repository to your GitHub account.

2. **Configure Secrets:** In your forked repository, go to "Settings" > "Secrets" and add the following secrets:

   - `TWITCH_CLIENT_ID`: Your Twitch Client ID.
   - `TWITCH_BROADCASTER_ID`: Your Twitch Broadcaster ID.
   - `TWITCH_ACCESS_TOKEN`: Your Twitch Access Token.
   - `TWITTER_CONSUMER_KEY`: Your Twitter Consumer Key.
   - `TWITTER_CONSUMER_SECRET`: Your Twitter Consumer Secret.
   - `TWITTER_ACCESS_TOKEN`: Your Twitter Access Token.
   - `TWITTER_ACCESS_TOKEN_SECRET`: Your Twitter Access Token Secret.
   - `TWITTER_BEARER_TOKEN`: Your Twitter Bearer Token.
   - `TWITCH_USERNAME`: Your Twitch Username.
   - `GIT_EMAIL`: Your Git email address.
   - `GIT_USERNAME`: Your Git username.

3. **GitHub Actions Workflow:** This repository includes a GitHub Actions workflow (`.github/workflows/main.yml`) that is scheduled to run at specific times. You can customize the schedule by modifying the cron expression in the workflow file.

4. **Run the Workflow:** The GitHub Actions workflow will automatically run at the scheduled times, check for updates on your Twitch schedule, and send a tweet & discord message if a change is detected.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Technologies Used

- Python (lib: tweepy, dotenv)
- Twitch API
- Twitter API
