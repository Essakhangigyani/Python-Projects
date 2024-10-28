# import smtplib as s
# ob=s.SMTP('smtp.gmail.com',587)
# ob.ehlo()
# ob.starttls()
# ob.login('essakhanofficial1@gmail.com', 'official54321')


# subject="test python"
# body='i love python'
# massage="subjest:{}\n\n{}".format(subject,body)
# listadd=["messakhan23232323@gmail.com",
#          "essakhanoffim)cial1@gmial.com"]
# obsendmail=("messakhan23232323@gmail.com",listadd,massage)
# print("sendmail")
# ob.quit

import smtplib as s

try:
    ob = s.SMTP('smtp.gmail.com', 587)
    ob.ehlo()
    ob.starttls()

    # Replace 'your_app_password' with the generated app password
    ob.login('essakhanofficial1@gmail.com', 'official54321')  

    subject = "Test Python"
    body = 'I love Python'
    message = "Subject: {}\n\n{}".format(subject, body)
    listadd = [
        "messakhan23232323@gmail.com",
        "essakhanofficial1@gmail.com"  # Ensure this email is valid
    ]

    ob.sendmail('essakhanofficial1@gmail.com', listadd, message)
    print("Email sent successfully!")

except s.SMTPAuthenticationError:
    print("Failed to login: check your email and app password.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    ob.quit()
