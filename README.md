## Q3 Project Cybersecurity

## Automated Web Scraping and Email Report Script

## Write Up

Our exploration into web development began as a research project, driven by our lack of prior knowledge on the topic and coding in general. Several days ago, we embarked on a mission to understand the basics of HTML and CSS, starting from scratch.

We immersed ourselves in tutorials and documentation, absorbing the fundamental concepts of web design one step at a time. Despite the initial challenges, each new lesson bolstered our understanding and propelled us forward.

Motivated to put our learning into practice, we conceived the idea of creating a simulated login system. Starting with a basic static website, we gradually built a simple login form. Though rudimentary, this initial achievement marked a significant milestone in our journey.

Eager to expand our skills, we delved deeper into backend development. Through further research and experimentation, we learned about Node.js and MySQL, essential technologies for creating dynamic web applications.

The process was challenging, requiring dedication and perseverance. However, with persistence, we successfully transformed the static login form into a dynamic interface capable of user authentication and registration.


## How it works
This Python script automates the process of scraping product information from a list of URLs and emailing the results to a specified recipient. Here's a simplified overview of how it works:

Importing Necessary Libraries:

The script imports urlopen and Request from urllib.request, BeautifulSoup from bs4, smtplib, and sys.
Main Function (main(email="")):

Clears the content of the draft.txt file.
Reads URLs from links.txt, extracts product information from each URL, and appends it to draft.txt.
If no email address is provided, prompts the user to input one.
Establishes a connection to Gmail's SMTP server, logs in using provided credentials, constructs an email message with the scraped data, sends the email, and prints a confirmation message.
Scraping Function (check(link)):

Takes a URL as input.
Creates a request to the URL, mimicking a web browser user-agent to avoid blocking.
Parses the HTML content using BeautifulSoup.
Extracts product title and price from specific HTML elements using class identifiers.
Prints the extracted information and appends it to draft.txt.
Script Execution:

Checks if it's being run as the main program.
If no command-line arguments are provided, calls the main function without an email address.
If an email address is provided as a command-line argument, calls the main function with that email address.
Displays an error message if more than one command-line argument is provided.
Execution from Command Line:

Users can execute the script from the command line by running python script_name.py recipient_email.
If no recipient email is provided, the script prompts the user to enter one during execution.
This script simplifies the process of scraping and emailing product information, making it suitable for users who want a straightforward solution without complex features. Users can customize it further according to their needs, such as adding error handling or expanding the scope of information scraped.

## Sources
- https://github.com/judz5/PyCrack
- https://www.codecademy.com
- https://www.youtube.com/watch?v=e9oOj5jRHrM
- https://www.youtube.com/channel/UCaKqU7lmR4wQ5Bj9F9E9i_Q
- https://www.w3schools.com/nodejs/nodejs_mysql_insert.asp
