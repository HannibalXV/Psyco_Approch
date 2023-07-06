
██████╗░░██████╗██╗░░░██╗░█████╗░░█████╗░
██╔══██╗██╔════╝╚██╗░██╔╝██╔══██╗██╔══██╗
██████╔╝╚█████╗░░╚████╔╝░██║░░╚═╝██║░░██║
██╔═══╝░░╚═══██╗░░╚██╔╝░░██║░░██╗██║░░██║
██║░░░░░██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝
╚═╝░░░░░╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░
                      
░█████╗░██████╗░██████╗░██████╗░░█████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░██║
███████║██████╔╝██████╔╝██████╔╝██║░░██║██║░░╚═╝███████║
██╔══██║██╔═══╝░██╔═══╝░██╔══██╗██║░░██║██║░░██╗██╔══██║
██║░░██║██║░░░░░██║░░░░░██║░░██║╚█████╔╝╚█████╔╝██║░░██║
╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝


# Summary
This code uses the OpenAI API to generate email and SMS message templates based on a given topic and language. It provides functions to generate emails and SMS messages, save the results to a file, and print the generated templates. The code makes use of the OpenAI Completion API to generate the text.

# Usage:
To use this code, follow these steps:

1-Make sure you have the OpenAI Python package installed. You can install it using pip install openai.

2-Obtain an API key from OpenAI and replace "Put-Open-Ai-Api-Key" in the code with your actual API key.

3-Set the user_topic variable to the desired topic for the emails and SMS messages.

4-Modify the languages list to include the languages you want to generate templates for.

5-Run the code. It will generate email and SMS message templates for each language and store them in a dictionary.

6-The generated templates will be saved in a file named "results.txt" with the email and SMS message templates for each language.

7-The results will also be printed to the console, showing the email and SMS message templates for each language.

Note: Ensure you have a valid subscription to the OpenAI API and that you comply with their terms of service and acceptable use policy.

# Required Packages:
The code requires the openai package, which can be installed using pip install openai. Make sure you have a valid API key from OpenAI to use their API services.
