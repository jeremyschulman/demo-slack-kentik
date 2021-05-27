# Demo Kentik Image Cache with Slack

As a User of Kentik and Slack I would like to include data visualizations from
the Kentik Portal into my Slack application.

Kentik has created an open-source app, [Kentik Image
Cache](https://github.com/kentik/kentik_image_cache), that is used to execute
Kentik TopN chart queries to the Kentik API and locally store the images.
Application that want to display images by URL refernce, Slack for example, can
then access these images from the Kentik Image Cache REST API.

You can find a short demo video on YouTube [here](https://youtu.be/oqmKLYzG9MU).

# Setup

## Running the Kentik Image Cache Container

You will need to build the Kentik Image Cache docker container image, as
described in that project
[README](https://github.com/kentik/kentik_image_cache/blob/master/README.md)
file.  When you build the image set the tag name to **kentik-fotomat**. 
Alternatively you can change the image name in the
[docker-compose.yaml](docker-compose.yaml) file.  The compose file defines a
few environment variables that you need to export, or you can change this file
directly:

* `KT_AUTH_EMAIL` - Your Kentik portal login email address
* `KT_AUTH_TOKEN` - Your Kentik portal token value
* `KENTIK_FOTOMAT_PORT` - The HTTP port number you want to expose for the container

You can then use `docker-compose` or `docker compose` to start the Kentik Image Cache service.

## Running the Demo Slack Application

The [fotomat](fotomat) directory contains a demo Slack application that will
interact with the Kentik Image Cache app.  You will need to define a Slack App
in the Slack Platform portal.  Configure your app to use [Socket
Mode](https://api.slack.com/apis/connections/socket).  For Slack app setup
help, refer to this
[documentation](https://slack.dev/bolt-python/tutorial/getting-started).

If you want to use the provided `start.sh` and `kill.sh` scripts, you will need
to export the environment variable `SLACK_APP_PORT` value for running the demo
app on your laptop.

You **MUST** make a few changes to the
code directly to suit your needs.  I could make the demo app a bit more
configurable; perhaps in time, but for now you need to make the following code
changes.

1. You need to change the `FOTOMAT_URL` value in the
[command_fotomat.py](fotomat/command_fotomat.py) file.  This value must be the
value that is reachable via the Slack Platform; meaning it must be publically
reachable.  The current value is `https://fotomat.ngrok.io` as I am using ngrok
for dev-testing forwarding. You **CANNOT** use the same value.

2.  The demo commands in the `command_format.py` are bound to specific Kentik
data explorer queries; specific to your Kentik portal.  You cannot use these. 
But you can see how the demo app is using them.  You will need to substitute
your own.