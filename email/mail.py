import smtplib
content="Subject:TEMPERTURE ALERT\n\nhello mr B4T\nyour temperature is too high.check your room please."
mail = smtplib.SMTP_SSL("smtp.gmail.com")
mail.login("user@gmail.com","******")
mail.sendmail(user@gmail.com","sender@gmail.com",content)
mail.quit()

