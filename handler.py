
def alexa_handler(event, context):
    request = event['request']

    # called when invoked with no values - early exit
    if request['type'] == 'LaunchRequest':
        return get_welcome_response()

    if request['type'] == 'IntentRequest':
        intent = request['intent']

        if intent['name'] == 'RegisteredDomain':
            return make_response(
                get_domainname_status(intent),
                card_title='Lookup'
            )
        elif intent['name'] == 'AMAZON.HelpIntent':
            return get_welcome_response()
        elif intent['name'] in ('AMAZON.StopIntent', 'AMAZON.CancelIntent'):
            return make_response(
                'Thank you for using Registered Domain',
                card_title='Goodbye',
            )

    # default catch all in case nothing else matches
    return make_response("Sorry, I didn't understand that request")


def get_welcome_response():

    welcome = """
              Welcome to the Alexa DomainNameChecker skill.
              You can ask me check if a domainname has been registered
              or is currently available

              """
    return make_response(
        welcome,
        card_title='Welcome',
        reprompt_text=welcome,
        should_end_session=False
    )


def get_domainname_status(intent):
    slots = intent.get('slots')
    speech_output = None

    if slots:
        domain_name = slots['DomainName'].get('value')

        if domain_name:
            status = _check_domainname(domain_name)
            speech_output = 'Domain name ' + domain_name + ' is ' + status
        else:
            speech_output = 'I need to be provided a domain name to check'

    return speech_output


def _check_domainname(name):
    import whois

    status = 'unknown'

    try:
        w = whois.whois(name)

        if 'expiration_date' in w:
            status = 'registered'

    except whois.parser.PywhoisError as e:
        # print str(e) # full debug

        first = str(e).split('\n')[0]
        if 'No match for' in first:
            status = 'not registered'
    except:
        status = 'a failed lookup'

    return status


def make_response(text, card_title='Thanks', should_end_session=True,
                  reprompt_text=None):

    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': text,
            },
            'card': {
                'type': 'Simple',
                'title': card_title,
                'content': text
            },
            'shouldEndSession': should_end_session
        }
    }

    if reprompt_text:
        response['reprompt'] = {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        }

    return response
