import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from django.core.files import File
from django.utils import timezone
from urllib.request import urlretrieve
from django.contrib.auth.models import User
from info.models import DailyUpdate
from datetime import date
from urllib.request import urlretrieve, urlcleanup

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token="xoxb-2023650115936-3329529215958-FhifEdVEIBv7uOonfXqU5DmA")
logger = logging.getLogger(__name__)
# Store conversation history
conversation_history = []
# ID of the channel you want to send the message to
channel_id = "C0275PBD99R"

try:
    # Call the conversations.history method using the WebClient
    # conversations.history returns the first 100 messages by default
    # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
    result = client.conversations_history(channel=channel_id)

    conversation_history = result["messages"]

    # Print results
    logger.info("{} messages found in {}".format(len(conversation_history), id))

except SlackApiError as e:
    logger.error("Error creating conversation: {}".format(e))


# ID of user you watch to fetch information for
user_id = "U031K38TAA1"

def get_user(user_id):
    try:
        # Call the users.info method using the WebClient
        result = client.users_info(
            user=user_id
        )
        logger.info(result)
        return result
    except SlackApiError as e:
        logger.error("Error fetching conversations: {}".format(e))


def save_profile_image(url, profile):
  try:
    name, _ = urlretrieve(url)
    profile.image.save("{timestamp}.jpg".format(timestamp=timezone.now().strftime('%Y-%m-%d%/%H-%M-%S')), File(open(name, 'rb')))
  finally:
    urlcleanup()

for x in conversation_history:
    result = get_user(x['user'])
    if result.data['user']['profile'].get('bot_id'): continue
    user, created = User.objects.get_or_create(
        email=result.data['user']['profile']['email'],
        username=result.data['user']['profile']['email']
        )
    name = result.data['user']['profile']['display_name_normalized'].split()
    try:
        user.first_name =  name[0]
        user.last_name =  name[1]
    except IndexError: ...
    user.set_password("Now@12345")
    user.save()
    profile = user.userinformation 
    save_profile_image(result.data['user']['profile']['image_24'], profile)

    daily_update, created = DailyUpdate.objects.get_or_create(
        chat_id = x["client_msg_id"]
        )
    daily_update.date=date.fromtimestamp(float(x['ts']))
    daily_update.user = user
    daily_update.detail = x['text']
    daily_update.save()