from twilio.rest import Client


class Message:
    def __init__(self, body, to, account_sid, auth_token, from_number):
        """
        Send a message through Twilio.

        Parameters:
            body (str): The text of the message to be sent.
            to (str): The destination phone number in E.164 format (e.g., '+15558675310').
            account_sid (str): Your Twilio Account SID.
            auth_token (str): Your Twilio Auth Token.
            from_number (str): Your Twilio phone number in E.164 format (e.g., '+15017122661').
        """
        # Initialize the Twilio client with your credentials
        self.client = Client(account_sid, auth_token)

    # Create and send the message
    def send_message(self):
        return self.client.messages.create(
            body=body,
            from_=from_number,
            to=to
        )

        # Output the unique message SID to confirm sending
        print("Message sent with SID:", self.message.sid)


# Example usage:
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv


    load_dotenv(".env")

    # Replace these values with your actual Twilio credentials and numbers
    ACCOUNT_SID = os.environ.get("TWILIO_SID")
    AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
    FROM_NUMBER = os.environ.get("TWILIO_AUTH_TOKEN")
    TO_NUMBER = os.environ.get("TWILIO_TO_PHONE")
    MESSAGE_BODY = "Hello, this is a test message from Twilio!"

    msg = Message(MESSAGE_BODY, TO_NUMBER, ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER)
