import difflib
import random
import time
import tkinter as tk


BEIGE = "#fff8ef"

TEXTS = [
    (
        "In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, "
        "nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort. It had a "
        "perfectly round door like a porthole, painted green, with a shiny yellow brass knob in the exact middle. The door opened on to a "
        "tube-shaped hall like a tunnel: a very comfortable tunnel without smoke, with panelled walls, and floors tiled and carpeted, "
        "provided with polished chairs, and lots and lots of pegs for hats and coats—the hobbit was fond of visitors. The tunnel wound on and on, "
        "going fairly but not quite straight into the side of the hill—The Hill, as all the people for many miles round called it—and many little "
        "round doors opened out of it, first on one side and then on another. No going upstairs for the hobbit: bedrooms, bathrooms, cellars, "
        "pantries (lots of these), wardrobes (he had whole rooms devoted to clothes), kitchens, dining-rooms, all were on the same floor, "
        "and indeed on the same passage."
    ),
    (
        "And we shouldn’t be here at all, if we’d known more about it before we started. But I suppose it’s often that way. The brave things in "
        "the old tales and songs, Mr. Frodo: adventures, as I used to call them. I used to think that they were things the wonderful folk of the "
        "stories went out and looked for, because they wanted them, because they were exciting and life was a bit dull, a kind of a sport, "
        "as you might say. But that’s not the way, as you put it. But I expect they had lots of chances, like us, of turning back, "
        "only they didn’t. And if they had, we shouldn’t know, because they’d have been forgotten. We hear about those as just went on – and not "
        "all to a good end, mind you; at least not to what folk inside a story and not outside it call a good end. You know, coming home, "
        "and finding things all right, though not quite the same – like old Mr. Bilbo. But those aren’t always the best tales to hear, "
        "though they may be the best tales to get landed in! I wonder what sort of a tale we’ve fallen into?"
    ),
    (
        "I would not take this thing, if it lay by the highway. Not were Minas Tirith falling in ruin and I alone could save her, so, "
        "using the weapon of the Dark Lord for her good and my glory. No, I do not wish for such triumphs, Frodo son of Drogo. For myself, "
        "I would see the White Tree flower again in the courts of the kings, and the Silver Crown return, and Minas Tirith in peace: Minas Anor "
        "again as of old, full of light, high and fair, beautiful as a queen among other queens: not a mistress of many slaves, nay, "
        "not even a kind mistress of willing slaves. War must be, while we defend our lives against a destroyer who would devour us "
        "all; but I do not love the bright sword for its sharpness, nor the arrow for its swiftness, nor the warrior for his glory. I love only "
        "that which they defend: the city of the Men of Numenor; and I would have loved her for her memory, her ancientry, her beauty, "
        "and her present wisdom. Not feared, save as men may fear the dignity of a man, old and wise."
    )
]

INSTRUCTIONS = "Copy the text below as quickly and as accurately as you can:"


class TypingTest:

    def __init__(self):
        self.user_is_typing = False
        self.start_time = None
        self.end_time = None

    def start_test(self):
        if not self.user_is_typing:
            self.user_is_typing = True
            self.start_time = time.time()

    def finish_test(self):
        self.end_time = time.time()
        user_input = text_input.get("1.0", "end")
        sample_text = random_text[0]
        time_elapsed = self.end_time - self.start_time
        text_input.destroy()
        words_per_minute = len(user_input.split(" ")) * 60 / time_elapsed
        ratio = difflib.SequenceMatcher(None, sample_text, user_input).ratio()
        accuracy = round(ratio * 100)
        wpm_label = tk.Label(window, font=("Montserrat", 12, "bold"), text=f"You write an average of {words_per_minute:.0f} words per minute.",
                             bg="#ffedda", fg="#2aa1ec")
        wpm_label.grid(column=0, row=4, pady=(15, 5))
        accuracy_label = tk.Label(window, font=("Montserrat", 12, "bold"), text=f"You have an accuracy of {accuracy}%.", bg="#ffedda", fg="#2aa1ec")
        accuracy_label.grid(column=0, row=5, pady=(10, 25))


def get_random_text():
    random_choice = random.choice(TEXTS)
    return random_choice


def press_return(_event):
    typing_test.finish_test()


def press_any_key(_event):
    typing_test.start_test()


typing_test = TypingTest()
random_text = get_random_text()

window = tk.Tk()
window.config(bg="#ffedda")
window.title('Speed Test')

window.bind('<Return>', press_return)
window.bind('<Any-KeyPress>', press_any_key)

title_label = tk.Label(window, justify="center", font=("Montserrat", 18, "bold"), text="Typing Speed Test", bg="#ffedda")
title_label.grid(column=0, row=0, pady=15)

instructions_label = tk.Label(window, font=("Montserrat", 12, "bold"), text=INSTRUCTIONS, bg="#2aa1ec", fg=BEIGE)
instructions_label.grid(column=0, row=1)

sample_text_label = tk.Label(window, font=("Courier", 12), text=random_text, wraplength=650, bg="white", justify="left")
sample_text_label.grid(column=0, row=3, padx=15, pady=15)

hit_return_label = tk.Label(window, font=("Montserrat", 12, "bold"), text="Once you're done, hit 'RETURN'", bg="#ffedda", fg="#2aa1ec")
hit_return_label.grid(column=0, row=2, pady=(5, 0))

text_input = tk.Text(window, width=65, height=18, font=("Courier", 12), wrap="word")
text_input.grid(column=0, row=4, padx=15, pady=15)

window.mainloop()
