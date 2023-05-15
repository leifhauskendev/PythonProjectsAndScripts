import win32com.client

def add_appointment(subject, start_time, end_time, location, description, reminder_minutes):
    outlook_app = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook_app.GetNamespace("MAPI")
    calendar = namespace.GetDefaultFolder(9)  # 9 represents the calendar folder

    appointment = calendar.Items.Add()
    appointment.Subject = subject
    appointment.Start = start_time
    appointment.End = end_time
    appointment.Location = location
    appointment.Body = description
    appointment.ReminderSet = True
    appointment.ReminderMinutesBeforeStart = reminder_minutes
    appointment.Save()

    print("Appointment added successfully!")

# Example usage
subject = "Go to bed"
start_time = "2023-05-16 :00"
end_time = "2023-05-16 23:00"
location = ""
description = ""
reminder_minutes = 15

add_appointment(subject, start_time, end_time, location, description, reminder_minutes)
