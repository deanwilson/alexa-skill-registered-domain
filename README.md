# Registered Domain - Alexa Skill

I own too many domain names, thanks to this Alexa skill you can too!

This skill enhances Alexa so you can ask it if a domain name is available.
Luckily you can't, yet, purchase domains through the echo itself as that'd
be a little too dangerous.

This project uses the [Serverless framework](https://serverless.com) and is
written in python 3.

## Development docs

### Edit the config file

    vi serverless.yml

Here is my [config file](/serverless.yml) for this project.

### Deploy the app to AWS

I use a dedicated set of credentials for this but you don't have to.

    AWS_PROFILE=admin serverless deploy -v

### View the logs

It'll break and you'll want to know why.

    AWS_PROFILE=admin serverless logs -f registeredDomain

### Author

[Dean Wilson](https://www.unixdaemon.net)

### License

 * GPLv2
