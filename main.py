import tkinter as tk
import random
import math

COMMON_WORDS = ['although', 'set', 'their', 'were', 'him', 'she', 'part', 'per', 'ago', 'story', 'natural', 'public',
                'technology', 'american', 'until', 'team', 'plan', 'why', 'been', 'important', 'space', 'national',
                'want',
                'particular', 'ever', 'issues', 'an', 'country', 'head', 'their', 'bad', 'certain', 'instead',
                'certain',
                'having', 'share', 'called', 'an', 'system', 'power', 'love', 'called', 'where', 'this', 'usually',
                'almost',
                'almost', 'become', 'short', 'could', 'high', 'game', 'right', 'insurance', 'find', 'center', 'big',
                'may',
                'control', 'person', 'love', '', 'been', 'world', 'add', 'all', 'someone', 'process', 'until', 'what',
                'common',
                'major', 'could', 'I', 'next', 'their', 'whole', 'age', 'making', 'internet', 'far', 'comes', 'next',
                'could',
                'person', 'small', 'been', 'rather', 'team', 'having', 'it', 'per', 'might', 'those', 'again', 'media',
                'above',
                'women', 'services', 'kind', 'car', 'either', 'find', 'one', 'city', 'child', 'seems', 'if', 'but',
                'years',
                'support', 'management', 'major', 'services', 'good', 'at', 'may', 'taking', 'market', 'good', 'now',
                'we',
                'great', 'site', 'which', 'even', 'least', 'close', 'space', 'told', 'means', 'months', 'means',
                'insurance',
                'health', 'against', 'team', 'quite', 'during', 'might', 'example', 'major', 'against', 'from', 'car',
                'well',
                'day', 'believe', 'we', 'my']
FONT = "Times New Roman"
counter = 0
user_typed_words = []


def check_typing_speed():
    correct_spelled_words = ""
    for _ in range(len(user_typed_words)):
        if user_typed_words[_] == COMMON_WORDS[_]:
            correct_spelled_words += user_typed_words[_]
    speed = len(correct_spelled_words) / 5
    score_field = tk.Label(frame, borderwidth=15, text=f"Your typing speed is: {math.ceil(speed)} WPM", relief=tk.FLAT,
                           font=("Arial", 20, "bold"), width=30, bg="white", fg="#579BB1")
    score_field.grid(row=2, column=1)


def space_pressed(event):
    if typing_field.get():
        written_text = typing_field.get().split()[0]
        user_typed_words.append(written_text)
        canvas.itemconfig(text_words, text=print_text())
        typing_field.delete(0, "end")
        typing_field.focus()


def start_timer(seconds):
    if seconds > 0:
        global timer_update
        seconds -= 1
        if seconds < 10:
            timer_data = f"00:0{seconds}"
        else:
            timer_data = f"00:{seconds}"
        canvas.itemconfig(timer_text, text=timer_data)
        timer_update=window.after(1000, start_timer, seconds)
    if seconds == 0:
        check_typing_speed()


def start_test(user_wrote):
    if user_wrote:
        start_timer(60)
    else:
        user_wrote = len(typing_field.get()) > 0
        window.after(10, start_test, user_wrote)


def restart_test():
    global typing_field
    global counter,user_typed_words
    user_typed_words = []
    counter=0
    random.shuffle(COMMON_WORDS)
    window.after_cancel(timer_update)
    typing_field.delete(0, "end")
    canvas.itemconfig(timer_text,text="01:00")
    canvas.itemconfig(text_words,text=print_text())
    typing_field = tk.Entry(frame, borderwidth=15, relief=tk.FLAT,
                            font=("Arial", 20, "bold"), width=30, bg="white", fg="#579BB1")
    typing_field.grid(row=2, column=1)
    typing_field.focus()
    start_test(user_wrote=False)


def print_text():
    global counter
    common_words_copy = COMMON_WORDS[counter:counter + 63]

    order_words = ""
    for _ in range(63):
        order_words += common_words_copy[_]
        if (_ + 1) % 7 == 0:
            order_words += "\n"
        else:
            order_words += " "
    counter += 1
    return order_words


window = tk.Tk()
window.geometry("980x630")
window.title("Typing Speed Test")
window.config(bg="#579BB1", pady=10, padx=20)

random.shuffle(COMMON_WORDS)
text = print_text()
canvas = tk.Canvas(window, width=950, height=400, bg='#579BB1', highlightthickness=0)
label_title = tk.Label(window, text="Typing Speed Test", bg="#579BB1", fg="#FFE9B1", font=(FONT, 30,))
label_title.grid(row=0, columnspan=2)
timer_text = canvas.create_text(870, 20, text="01:00", fill="#5FD068", font=(FONT, 24, "bold"),tags="timer_text")
text_words = canvas.create_text(500, 230, text=text, fill="white", font=("Courier", 22, "bold"))
canvas.grid(column=1, row=1)
frame = tk.Frame(window, borderwidth=5, relief=tk.SUNKEN)
frame.grid(row=2, column=1)
typing_field = tk.Entry(frame, borderwidth=15, relief=tk.FLAT,
                        font=("Arial", 20, "bold"), width=30, bg="white", fg="#579BB1")
typing_field.grid(row=2, column=1)
typing_field.focus()

start_test(user_wrote=False)

restart_button = tk.Button(window, text="Restart", fg='#5FD068', bg="#579BB1", borderwidth=10,
                           font=("Arial", 20, "bold"), command=restart_test)
restart_button.place(x=770, y=452)

window.bind("<space>", space_pressed)
window.mainloop()
