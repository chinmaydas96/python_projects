import smtplib
content="Subject:TEMPERTURE ALERT\n\nhello mr B4T\nyour temperature is too high.check your room please."
mail = smtplib.SMTP_SSL("smtp.gmail.com")
mail.login("chinmaydasbat@gmail.com","chinmayee123")
mail.sendmail("chinmaydasbat@gmail.com","chinmaydasbat@gmail.com",content)
mail.quit()

