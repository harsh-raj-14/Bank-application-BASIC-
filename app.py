import gradio as gr
from hello import Bank

# ---------- Functions ----------
def create_account(name, age, email, pin):
    if not name or not email or not pin:
        return "❌ Please fill all fields"

    try:
        age = int(age)
        pin = int(pin)
    except ValueError:
        return "❌ Age and PIN must be numbers"

    user, msg = Bank.create_account(name, age, email, pin)

    if user:
        return f"✅ {msg}\nAccount No: {user['account_No']}"
    return msg


def deposit(acc_no, pin, amount):
    if not acc_no or not pin or not amount:
        return "❌ Please fill all fields"

    try:
        pin = int(pin)
        amount = int(amount)
    except ValueError:
        return "❌ PIN and Amount must be numbers"

    success, msg = Bank.deposit(acc_no, pin, amount)
    return msg


def withdraw(acc_no, pin, amount):
    if not acc_no or not pin or not amount:
        return "❌ Please fill all fields"

    try:
        pin = int(pin)
        amount = int(amount)
    except ValueError:
        return "❌ PIN and Amount must be numbers"

    success, msg = Bank.withdraw(acc_no, pin, amount)
    return msg


def show_details(acc_no, pin):
    try:
        pin = int(pin)
    except ValueError:
        return "❌ PIN must be a number"

    user = Bank.find_user(acc_no, pin)
    if user:
        return user
    return "❌ No account found"


def update_info(acc_no, pin, name, email, new_pin):
    try:
        pin = int(pin)
    except ValueError:
        return "❌ PIN must be a number"

    success, msg = Bank.update_user(acc_no, pin, name, email, new_pin)
    return msg


def delete_account(acc_no, pin):
    try:
        pin = int(pin)
    except ValueError:
        return "❌ PIN must be a number"

    success, msg = Bank.delete_user(acc_no, pin)
    return msg


# ---------- UI ----------
with gr.Blocks() as app:
    gr.Markdown("# 🏦 Simple Bank App")

    with gr.Tab("Create Account"):
        name = gr.Textbox(label="Name")
        age = gr.Number(label="Age")
        email = gr.Textbox(label="Email")
        pin = gr.Textbox(label="PIN", type="password")
        btn = gr.Button("Create")
        output = gr.Textbox(label="Result")
        btn.click(create_account, [name, age, email, pin], output)

    with gr.Tab("Deposit"):
        acc = gr.Textbox(label="Account Number")
        pin = gr.Textbox(label="PIN", type="password")
        amt = gr.Number(label="Amount")
        btn = gr.Button("Deposit")
        output = gr.Textbox(label="Result")
        btn.click(deposit, [acc, pin, amt], output)

    with gr.Tab("Withdraw"):
        acc = gr.Textbox(label="Account Number")
        pin = gr.Textbox(label="PIN", type="password")
        amt = gr.Number(label="Amount")
        btn = gr.Button("Withdraw")
        output = gr.Textbox(label="Result")
        btn.click(withdraw, [acc, pin, amt], output)

    with gr.Tab("Show Details"):
        acc = gr.Textbox(label="Account Number")
        pin = gr.Textbox(label="PIN", type="password")
        btn = gr.Button("Show")
        output = gr.JSON(label="User Data")
        btn.click(show_details, [acc, pin], output)

    with gr.Tab("Update Info"):
        acc = gr.Textbox(label="Account Number")
        pin = gr.Textbox(label="Current PIN", type="password")
        name = gr.Textbox(label="New Name (optional)")
        email = gr.Textbox(label="New Email (optional)")
        new_pin = gr.Textbox(label="New PIN (optional)")
        btn = gr.Button("Update")
        output = gr.Textbox(label="Result")
        btn.click(update_info, [acc, pin, name, email, new_pin], output)

    with gr.Tab("Delete Account"):
        acc = gr.Textbox(label="Account Number")
        pin = gr.Textbox(label="PIN", type="password")
        btn = gr.Button("Delete")
        output = gr.Textbox(label="Result")
        btn.click(delete_account, [acc, pin], output)

app.launch()
