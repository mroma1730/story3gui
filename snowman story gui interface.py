import tkinter as tk
import turtle as trtl
import time
import threading


root=tk.Tk()
root.wm_geometry("700x500")
root.wm_title('Snowman Story')

#mainpage
main_page=tk.Frame(root)
main_page.grid(row=0, column=0, sticky="news")

title = tk.Label(main_page, text = "Welcome, please pick your story")
title.pack()

title_1= tk.Label(main_page, text ="We hope you like it, press buttom to proceed")
title_1.pack()

first_story_1 = tk.Frame(root)
first_story_1.grid (row=0, column=0, sticky="news")
main_page.tkraise()


def draw_turtle():
        # draw moon
    trtl.bgcolor("DodgerBlue4")
    trtl.penup()
    trtl.goto(-450,150)
    trtl.pencolor("grey56")
    trtl.pendown()
    trtl.pensize(160)
    trtl.circle(80)

    # draw ground
    trtl.penup()
    trtl.goto(-400, -200)
    trtl.pencolor("honeydew2")
    trtl.pensize(70)
    trtl.pendown()
    trtl.forward(1000)

    #snowman body

    #bottom circle
    trtl.penup()
    trtl.goto(-200,-150)
    trtl.pencolor("white")
    trtl.pendown()
    trtl.pensize(60)
    trtl.circle(30)
    #middle circle
    trtl.goto(-200, -80)
    trtl.pensize(40)
    trtl.circle(20)
    trtl.penup()
    #top circle
    trtl.goto(-200, -25)
    trtl.pendown()
    trtl.pensize(30)
    trtl.circle(15)

    # add details on the snowman like eyes/ mouth/ nose/ buttons

    #nose
    trtl.goto(-195,-10)
    trtl.pencolor("chocolate3")
    trtl.shapesize(0.7)
    trtl.pendown()
    trtl.shape("triangle")
    trtl.fillcolor("chocolate3")
    trtl.clone()

    #righteye
    trtl.penup()
    trtl.shape("classic")
    trtl.pencolor("black")
    trtl.goto(-210,0)
    trtl.pensize(4)
    trtl.pendown()
    trtl.circle(2)
    trtl.fillcolor("black")

    #lefteye
    trtl.penup()
    trtl.goto(-190,0)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(2)
    trtl.fillcolor("black")

    #mouth
    trtl.pensize(2)
    trtl.penup()
    #dot 1
    trtl.goto(-220,-18)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(1)
    trtl.fillcolor("black")
    trtl.penup()
    #dot 2
    trtl.goto(-210,-22)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(1)
    trtl.fillcolor("black")
    trtl.penup()
    #dot 3
    trtl.goto(-200,-26)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(1)
    trtl.fillcolor("black")
    trtl.penup()
    #dot 4
    trtl.goto(-190,-22)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(1)
    trtl.fillcolor("black")
    trtl.penup()
    #dot 5
    trtl.goto(-180,-18)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(1)
    trtl.fillcolor("black")

    #Buttons

    #button 1
    trtl.penup()
    trtl.goto(-200,-50)
    trtl.pendown()
    trtl.pensize(4)
    trtl.circle(2)
    trtl.penup()
    #button 2
    trtl.goto(-200,-70)
    trtl.pendown()
    trtl.pensize(4)
    trtl.circle(2)
    trtl.penup()
    #button 3
    trtl.goto(-200,-90)
    trtl.pendown()
    trtl.pensize(4)
    trtl.circle(2)

    #arms

    #right arm
    trtl.penup()
    trtl.goto(-160,-60)
    trtl.pencolor("saddlebrown")
    trtl.pendown()
    trtl.left(50)
    trtl.forward(60)
    trtl.penup()
    #left arm
    trtl.goto(-240,-60)
    trtl.pencolor("saddle brown")
    trtl.pendown()
    trtl.left(70)
    trtl.forward(60)
    trtl.fillcolor("saddle brown")
    time.sleep(5)

# Functional Programming
def show_text(lines, l):
    # this function will be responsible for showing the lines
    for line in lines:
        l.config(text=line)
        root.update()
        time.sleep(2)  # Adjust sleep duration as needed

#story1
def story_1():
    first_story_1.tkraise()
    animation_thread = threading.Thread(target=draw_turtle)
    animation_thread.start()

    # story 1
    lines = [
        "Embers wept from the heart of the fire's glow, A snowman stood near, feeling life's warmth go. ",
        'Gently, the heat whispered of an end so near, In his icy heart, a faint, unspoken fear.',
        "Once clothed in flesh, not snow so cold and clear, He lived, he laughed, felt love's embrace draw near.",
        ' A human soul, with dreams and days unfurled, A family, friends, a purpose in the world.',
        "He was a coder, lost in lines of code, A vacation's pause on his life's road. One final task, his mind's ",
        "unyielding chain, A project's weight, his last link to the plane."
    ]
    line__1 = tk.Label(first_story_1, text="")
    line__1.pack()

    show_text(lines, line__1)



    first_story_2 = tk.Frame(root)
    first_story_2.grid (row=0, column=0, sticky = "news")
    first_story_1.tkraise()

    def story_1_p2():
        first_story_2.tkraise()
        line__1.pack_forget()
        next__chapter.pack_forget()
        go_back_.pack_forget()

        lines = [
            'Memories haunted of a life once bright, Before the chill, before the endless night.',
            ' His form grew cold, his flesh to frost did turn, In this new shape, an existential burn.',
            'No fear of change, no pain from icy sheath, But terror struck from the emptiness beneath.',
            'Tears frozen on a face no longer his, Mourning a life where he no longer fits.',
            "His purpose bound to a task left undone, In digital realms where he once had run. By the fire's side,",
            " a symbol of his plight, Its warmth now a tale of what he couldn't fight."
        ]
        line_1 = tk.Label(first_story_2, text="")
        line_1.pack()
        show_text(lines, line_1)
        
        def go_back():
            main_page.tkraise()
            line_1.pack_forget()
            nextchapter.pack_forget()
            go_back_.pack_forget()
            trtl.clearscreen()
        
        first_story_3 = tk.Frame(root)
        first_story_3.grid (row=0, column=0, sticky = "news")
        first_story_2.tkraise()
        
        def story_1_p3():
            first_story_3.tkraise()
            line_1.pack_forget()
            
            lines = [
                'What remained for a soul so out of place? A world that no longer recognized his face.',
                "Family, love, all beyond his frozen grasp, A lonely vigil in the fire's cruel clasp.",
                "Could he choose the moment of his decline? Or was he already too far out of time? As the fire's",
                " warmth bade his form to fade, The snowman's essence into night did wade"
            ]

            line1 = tk.Label(first_story_3, text="")
            line1.pack()
            show_text(lines, line1)

            def go_back():
                main_page.tkraise()
                line1.pack_forget()
                go_back_.pack_forget()
                trtl.clearscreen()
        
            go_back_ = tk.Button(first_story_3, text = "Go Back to Main Page", bg="green", fg = "black", command = go_back)
            go_back_.pack(pady = 10)

        nextchapter = tk.Button(first_story_2, text ="Proceed to next section", bg = "green", fg = "black", command =  story_1_p3)
        nextchapter.pack(pady=10) 
        
        go__back_ = tk.Button(first_story_2, text = "Go Back to Main Page", bg="green", fg = "black", command = go_back)
        go__back_.pack(pady = 10)

    next__chapter = tk.Button(first_story_1, text ="Proceed to next section", bg = "green", fg = "black", command =  story_1_p2)
    next__chapter.pack(pady=10) 

    def go_back():
        main_page.tkraise()
        line__1.pack_forget()
        next__chapter.pack_forget()
        go_back_.pack_forget()
        trtl.clearscreen()
    
    go_back_ = tk.Button(first_story_1, text = "Go Back to Main Page", bg="green", fg = "black", command = go_back)
    go_back_.pack(pady = 10)

next1 = tk.Button(main_page, text = "Story one, this is sad", bg = "blue", fg="white", command = story_1)
next1.pack(pady=10)

second_story_1 = tk.Frame(root)
second_story_1.grid (row=0, column=0, sticky="news")
main_page.tkraise()

def draw_snow():
    trtl.bgcolor("light sky blue")

    # draw sun
    trtl.penup()
    trtl.goto(-450,150)
    trtl.pencolor("gold")
    trtl.pendown()
    trtl.pensize(160)
    trtl.circle(80)

    # draw ground
    trtl.penup()
    trtl.goto(-400, -200)
    trtl.pencolor("alice blue")
    trtl.pensize(100)
    trtl.pendown()
    trtl.forward(1000)

    #snowman body

    #bottom circle
    trtl.penup()
    trtl.goto(-200,-150)
    trtl.pencolor("white")
    trtl.pendown()
    trtl.pensize(60)
    trtl.circle(30)
    #middle circle
    trtl.goto(-200, -80)
    trtl.pensize(40)
    trtl.circle(20)
    trtl.penup()
    #top circle
    trtl.goto(-200, -25)
    trtl.pendown()
    trtl.pensize(30)
    trtl.circle(15)

    # add details on the snowman like eyes/ mouth/ nose/ buttons

    #nose
    trtl.goto(-195,-10)
    trtl.pencolor("chocolate3")
    trtl.shapesize(0.7)
    trtl.pendown()
    trtl.shape("triangle")
    trtl.fillcolor("chocolate3")
    trtl.clone()

    #righteye
    trtl.penup()
    trtl.shape("classic")
    trtl.pencolor("black")
    trtl.goto(-210,0)
    trtl.pensize(4)
    trtl.pendown()
    trtl.circle(2)
    trtl.fillcolor("black")

    #lefteye
    trtl.penup()
    trtl.goto(-190,0)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(2)
    trtl.fillcolor("black")

    #mouth
    trtl.pensize(2)
    trtl.penup()
    #dot 1
    trtl.goto(-220,-18)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(1)
    trtl.fillcolor("black")
    trtl.penup()
    #dot 2
    trtl.goto(-210,-22)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(1)
    trtl.fillcolor("black")
    trtl.penup()
    #dot 3
    trtl.goto(-200,-26)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(1)
    trtl.fillcolor("black")
    trtl.penup()
    #dot 4
    trtl.goto(-190,-22)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(1)
    trtl.fillcolor("black")
    trtl.penup()
    #dot 5
    trtl.goto(-180,-18)
    trtl.pencolor("black")
    trtl.pendown()
    trtl.circle(1)
    trtl.fillcolor("black")

    #Buttons

    #button 1
    trtl.penup()
    trtl.goto(-200,-50)
    trtl.pendown()
    trtl.pensize(4)
    trtl.circle(2)
    trtl.penup()
    #button 2
    trtl.goto(-200,-70)
    trtl.pendown()
    trtl.pensize(4)
    trtl.circle(2)
    trtl.penup()
    #button 3
    trtl.goto(-200,-90)
    trtl.pendown()
    trtl.pensize(4)
    trtl.circle(2)

    #arms

    #right arm
    trtl.penup()
    trtl.goto(-160,-60)
    trtl.pencolor("saddlebrown")
    trtl.pendown()
    trtl.left(50)
    trtl.forward(60)
    trtl.penup()
    #left arm
    trtl.goto(-240,-60)
    trtl.pencolor("saddle brown")
    trtl.pendown()
    trtl.left(70)
    trtl.forward(60)
    trtl.fillcolor("saddle brown")

    time.sleep(5)

def story_2():
    second_story_1.tkraise()
    animation_thread = threading.Thread(target=draw_snow)
    animation_thread.start()
    lines = [
        "In a realm where the skies and mountains meet, A god peered down, a world at their feet.",
        " Upon a mountain, under a celestial glow, Lay untouched, a pristine blanket of snow.",
        "“Why do you lay here alone, so serene?” The god inquired, their tone genuinely keen. The snow,",
        "with a voice soft and forlorn, Shared its solitude, from dusk till morn.",
        "“I long for friends, for laughter and play, But as I fall, the people shy away.",
        " The adults hide, the children, though near, Use me in silence, I’m their canvas, I fear.”"
    ]
     
    line_1 = tk.Label(second_story_1, text= "")
    line_1.pack()
    show_text(lines, line_1)
    
    def go_back():
        main_page.tkraise()
        line_1.pack_forget()
        next1.pack_forget()
        go_back_.pack_forget()
        trtl.clearscreen()
    
    second_story_2 =  tk.Frame(root)
    second_story_2.grid(row= 0, column=0, sticky="news")
    second_story_1.tkraise()

    def story_2_p2():
        second_story_2.tkraise()
        line_1.pack_forget()
        next1.pack_forget()
        go_back_.pack_forget()

        lines = [
            "Moved by the snow’s solemn, quiet plea, The god decided to set its spirit free.",
            "“Now, I bestow upon you a magical grace, To turn into a snowman, with a smiling face.",
            "With arms to embrace, and a heart so true, The children will craft you, and play anew.",
            "As a friend, not just snow, you’ll dance and you’ll sing, Until it’s time to depart with the winter’s wing.”",
            "And so, the snow felt a change, a delightful shift, As children’s laughter gave it a lift. ",
            "From snow to snowman, it happily found, The joy of friendship, all around.",
            "No longer alone, on the mountain so high, It danced with the children under the open sky.",
            " And when the time came for winter to end, It knew next year, it would return, a friend."
        ]

        line1 = tk.Label(second_story_2, text = "")
        line1.pack()
        show_text(lines, line1)
        
        def go_back():
            main_page.tkraise()
            line1.pack_forget()
            go__back_.pack_forget()
            trtl.clearscreen()
        
        go__back_ = tk.Button(second_story_2, text = "Go Back to Main Page", bg="green", fg = "black", command = go_back)
        go__back_.pack(pady = 10)
    next1 = tk.Button(second_story_1, text = "Proceed to next section", bg = "green", fg = "black", command = story_2_p2)
    next1.pack(pady=10)
    go_back_ = tk.Button(second_story_1, text = "Go Back to Main Page", bg="green", fg = "black", command = go_back)
    go_back_.pack(pady = 10)

next2 = tk.Button(main_page, text = "Story two, this is happy", bg = "pink", fg = "black", command = story_2)
next2.pack(pady=10)

third_story_1 = tk.Frame(root)
third_story_1.grid(row=0, column = 0, sticky = "news")
main_page.tkraise()

def draw_cabin():
    
    trtl.bgcolor("light sky blue")
    #sun
    trtl.penup()
    trtl.pencolor("gold")
    trtl.pensize(50)
    trtl.goto(-150,150)
    trtl.pendown()
    trtl.circle(3)
    trtl.penup()
    #grass
    trtl.goto(-150,-50)
    trtl.pencolor("SpringGreen3")
    trtl.pensize(90)
    trtl.pendown()
    trtl.goto(150,-50)
    trtl.penup()
    #cabinbody
    trtl.goto(-50,-50)
    trtl.pencolor("sienna4")
    trtl.pendown()
    trtl.pensize(40)
    trtl.goto(50,-50)
    trtl.goto(50,50)
    trtl.goto(-50,50)
    trtl.goto(-50,-50)
    trtl.goto(0,0)
    trtl.pensize(90)
    trtl.forward(0.01)
    trtl.penup()
    #cabinroof
    trtl.goto(-50,50)
    trtl.pensize(40)
    trtl.pencolor("sienna2")
    trtl.pendown()
    trtl.goto(-100,50)
    trtl.goto(0,100)
    trtl.goto(100,50)
    trtl.goto(-100,50)
    trtl.goto(25,75)


    time.sleep(5)

def story_3():
    third_story_1.tkraise()
    animation_thread = threading.Thread(target=draw_cabin)
    animation_thread.start()
    
    lines = [
        "Around Christmas time, in a cabin nestled deep, The Goldermans sought refuge, a respite they would keep.",
        " Through the night, the parents spoke, their voices low and hoarse, ",
        "In the children's room, questions lingered with no source.",
        '"Why here, why now?" the boys murmured in the night, Confusion clouded, shrouded in the dim moonlight.',
        " Morning dawned, the children played, innocence in their view, While the parents, heavy-hearted, knew what they must do.",
        "As the day unfurled, and the snow began to fall, The parents' whispered words echoed through the hall. ",
        "With trembling voices, they faced their children's eyes, And with heavy hearts, they uttered their goodbyes.",
        "'We're getting a divorce, the truth finally confessed, A weighty proclamation, leaving hearts distressed. '",
        "Yet in the gentle blanket of snow, life's path took its course, "
    ]
    
    line_1 = tk.Label(third_story_1, text= "")
    line_1.pack()
    show_text(lines, line_1)

    third_story_2 = tk.Frame(root)
    third_story_2.grid(row=0, column = 0, sticky = "news")
    third_story_1.tkraise()

    def story_3_p2():
        third_story_2.tkraise()
        line_1.pack_forget()
        next1.pack_forget()
        go_back_.pack_forget()    

        line1 = tk.Label(third_story_2, text = "Leaving behind echoes of pain (We're getting a divorce.) ")
        line1.pack()

        def go_back():
            main_page.tkraise()
            line1.pack_forget()
            go_back__.pack_forget()
            trtl.clearscreen()
        go_back__ = tk.Button(third_story_2, text = "Main Page", bg = "green", fg = "black", command = go_back)
        go_back__.pack(pady = 10)


    def go_back():
        main_page.tkraise()
        line_1.pack_forget()
        next1.pack_forget()
        go_back_.pack_forget()
        trtl.clearscreen()
    
    next1 = tk.Button(third_story_1, text ="Click to find out what they said!", bg = "purple", fg = "white", command = story_3_p2)
    next1.pack(pady = 10)

    go_back_ = tk.Button(third_story_1, text = "Go Back to Main Page", bg="green", fg = "black", command = go_back)
    go_back_.pack(pady = 10)

next3 = tk.Button(main_page, text = "Story three, beware, this is random", bg = "red", fg = "white", command = story_3)
next3.pack(pady=10)

root.mainloop()