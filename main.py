# Programmer: Leif LaBianca
# Course:  CS151, Prof. Zelalem
# Due Date: Wednesday, September 18, 23:00
# Programming Assignment:  00
# Problem Statement:  Takes the amount of sent, read, and clicked emails and calculates open, click, and clickthrough rates
# Data In: Total sent email count, total read email count, total clicked email count
# Data Out:  Data in + Email open rate, click rate, and clickthrough rate expressed in percentages
# Credits: All original code

# each of the below input statements are converted to an integer to serve as the value of the amount of sent, read, and clicked emails per the users input
sent_emails = int(input('Provide the number of sent emails: '))
read_emails = int(input('Provide the number of read emails: '))
clicked_emails = int(input('Provide the number of clicked emails: '))

# the above variables are fed into these division problems that solve for the relevant rates. these are assigned new variables
email_open_rate = float(read_emails/sent_emails)
email_click_rate = float(clicked_emails/sent_emails)
email_clickthrough_rate = float(clicked_emails/read_emails)

# each rate variable is multiplied by 100 and rounded to the nearest whole number to express themselves as a percent. each are once again assigned a new variable.
email_open_rate_percent = round(email_open_rate * 100)
email_click_rate_percent = round(email_click_rate * 100)
email_clickthrough_rate_percent = round(email_clickthrough_rate * 100)

# this statement prints the user inputted counts as well as the relevant rates expressed as percentages. all are on their own individual line
print('Email statistics\nTotal emails:', sent_emails,'\nRead emails:', read_emails,'\nClicked emails:', clicked_emails,'\nEmail open rate:', email_open_rate_percent,'%\nEmail click rate:', email_click_rate_percent,'%\nEmail clickthrough rate:', email_clickthrough_rate_percent,'%')