import openai

openai.api_key = "Your-Open-Ai-Api-Key"

def generate_email(topic, language):
    if language == 'fr':
        prompt = f"Thème: {topic}\n\nCorps de l'email:"
    elif language == 'en':
        prompt = f"Topic: {topic}\n\nEmail Body:"
    elif language == 'ar':
        prompt = f"الموضوع: {topic}\n\nنص البريد الإلكتروني:"
    elif language == 'es':
        prompt = f"Tema: {topic}\n\nCuerpo del correo electrónico:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=100,
        n=1,
        stop=None
    )
    email_body = response.choices[0].text.strip()

    if language == 'fr':
        email_subject = f"À propos de {topic}"
    elif language == 'en':
        email_subject = f"Regarding {topic}"
    elif language == 'ar':
        email_subject = f"بخصوص {topic}"
    elif language == 'es':
        email_subject = f"Respecto a {topic}"

    email = f"Subject: {email_subject}\n\n{email_body}"

    return email


def generate_sms(topic, language):
    if language == 'fr':
        prompt = f"Thème: {topic}\n\nMessage SMS:"
    elif language == 'en':
        prompt = f"Topic: {topic}\n\nSMS Message:"
    elif language == 'ar':
        prompt = f"الموضوع: {topic}\n\nرسالة SMS:"
    elif language == 'es':
        prompt = f"Tema: {topic}\n\nMensaje SMS:"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=50,
        n=1,
        stop=None
    )
    sms_message = response.choices[0].text.strip()

    return sms_message


def save_results(emails, sms_messages):
    with open('results.txt', 'w', encoding='utf-8') as file:
        for language in emails:
            file.write(f"{language.upper()}:\n")
            file.write(f"Email:\n{emails[language]}\n\nSMS Message:\n{sms_messages[language]}\n\n")


# Example usage:
user_topic = "football"  # Provide the user's desired topic

languages = ['fr', 'en', 'ar', 'es']

emails = {}
sms_messages = {}

for language in languages:
    email = generate_email(user_topic, language)
    sms = generate_sms(user_topic, language)

    emails[language] = email
    sms_messages[language] = sms

save_results(emails, sms_messages)

# Print the results
for language in emails:
    print(f"{language.upper()} Email:")
    print(emails[language])
    print("\nSMS Message:")
    print(sms_messages[language])
    print("\n---\n")
