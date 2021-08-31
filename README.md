# SlackTaskManager
A simple task manager for Slack. You can create and assign tasks to people in your workspace.
## Installation
    pip install apscheduler
## Features
* Create and manage tasks
* Be able to create recurring tasks
* Assign tasks to other people
* Tasks can have due date
## Usage
First, look up how to build and run a Slack app, go through the basics of building a Slack app. A recommended guide is: [Guide to build Slack app](https://www.digitalocean.com/community/tutorials/how-to-build-a-slackbot-in-python-on-ubuntu-20-04)

After you are done with setting up a Slack app, export necessary tokens

    export SLACK_SIGN="your signin secret token"
    
    export SLACK_BOT_TOKEN="your oauth bot token"

Run the Slack app with

    python3 app.py
    
### Remove a buggy task
If a task is still being reminded after deleted, use the command `/removesched [Task ID]` to completely remove the task.
