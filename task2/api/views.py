from django.shortcuts import render


# Temporary server-side storage
users_data = []


def home(request):

    message = ""
    message_type = ""

    if request.method == "POST":

        # Form data receive karna
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        age = request.POST.get("age", "").strip()
        course = request.POST.get("course", "").strip()
        message_text = request.POST.get("message", "").strip()


        # ================= SERVER-SIDE VALIDATION =================

        if not name:
            message = "Name is required."
            message_type = "danger"

        elif len(name) < 3:
            message = "Name must contain at least 3 characters."
            message_type = "danger"

        elif not email:
            message = "Email is required."
            message_type = "danger"

        elif "@" not in email:
            message = "Please enter a valid email."
            message_type = "danger"

        elif not age:
            message = "Age is required."
            message_type = "danger"

        else:

            # Age ko integer mein convert karna
            try:
                age_number = int(age)

                if age_number < 18 or age_number > 100:
                    message = "Age must be between 18 and 100."
                    message_type = "danger"

                elif not course:
                    message = "Please select a course."
                    message_type = "danger"

                elif not message_text:
                    message = "Message is required."
                    message_type = "danger"

                elif len(message_text) < 10:
                    message = "Message must contain at least 10 characters."
                    message_type = "danger"

                else:

                    # ================= TEMPORARY STORAGE =================

                    user = {
                        "name": name,
                        "email": email,
                        "age": age_number,
                        "course": course,
                        "message": message_text
                    }

                    users_data.append(user)

                    message = "Form submitted successfully!"
                    message_type = "success"

            except ValueError:

                message = "Age must be a valid number."
                message_type = "danger"


    return render(
        request,
        "home.html",
        {
            "message": message,
            "message_type": message_type,
            "users": users_data
        }
    )

def result(request):
    return render(request, 'result.html') 