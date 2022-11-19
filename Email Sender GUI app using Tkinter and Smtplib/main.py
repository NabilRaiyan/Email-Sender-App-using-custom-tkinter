import customtkinter
import tkinter
import smtplib
import messagebox

# Setup main window
window = customtkinter.CTk()
customtkinter.set_default_color_theme("dark-blue")
window.title("Email Sender")
window.geometry("700x550")
window.configure(fg_color="#D8D8D8", padx=50, pady=50)

# Setting label and entry box to get user input
user_email = customtkinter.CTkLabel(text="From: ", text_color="black", text_font=("Courier", 12, "bold"))
user_email.grid(column=0, row=0, padx=5, pady=5)
user_entry = customtkinter.CTkEntry(border_color="black", border_width=2, corner_radius=8)
user_entry.grid(column=1, row=0)

to_email = customtkinter.CTkLabel(text="Recipient: ", text_color="black", text_font=("Courier", 12, "bold"))
to_email.grid(column=0, row=1, padx=5, pady=5)
to_email_entry = customtkinter.CTkEntry(border_color="black", border_width=2, corner_radius=8)
to_email_entry.grid(column=1, row=1)

subject = customtkinter.CTkLabel(text="Subject: ", text_color="black", text_font=("Courier", 12, "bold"))
subject.grid(column=0, row=2, padx=2, pady=20)
subject_entry = customtkinter.CTkEntry(border_color="black", border_width=2, corner_radius=8)
subject_entry.grid(column=1, row=2)

email_body = customtkinter.CTkLabel(window, text="Enter email body: ", text_color="black",
                                    text_font=("Courier", 12, "bold"))
email_body.grid(column=0, row=3, padx=2, pady=2)
email_body_entry = tkinter.Text(width=40, height=8)

email_body_entry.grid(column=1, row=4, padx=20, pady=20)


def send_email():
    # Smtplib for sending email
    email = user_entry.get()
    password = "btcysemavltmdbef"

    recipient_email = to_email_entry.get()
    subjects = subject_entry.get()
    body = email_body_entry.get("1.0", "end")
    if len(email) == 0 or len(recipient_email) == 0 or len(subjects) == 0 or len(body) == 0:
        messagebox.showinfo(title="Oops", message="Please enter all the information to send the email.")

    else:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=recipient_email, msg=f"Subject:{subjects}\n\n"
                                                                               f"{body}")
            user_entry.delete(0, customtkinter.END)
            to_email_entry.delete(0, customtkinter.END)
            subject_entry.delete(0, customtkinter.END)
            email_body_entry.delete("1.1", customtkinter.END)
            email_body_entry.insert("0.0", "Email sent successfully.")


# Send Button
send_button = customtkinter.CTkButton(text="Send", text_color="white", bg_color="#D8D8D8",
                                      fg_color="black", text_font=("Courier", 10, "bold"),
                                      corner_radius=8, border_width=0, hover_color="#2C3333", command=send_email)
send_button.grid(column=1, row=5)

window.mainloop()
