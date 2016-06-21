init:
    #screen size setup
    $ config.screen_width = 800
    $ config.screen_height = 600

    #screen title setup
    $ config.window_title = "Test Experiment"

    #Variables
    $ minutes = 540
    $ bedtime = 1320
    $ checkListDist = 0.01
    $ isNeat = False
    $ addonTime = 0

    image popup = im.FactorScale("popup.jpg", .75)

    #Clock Images
    image clock = im.FactorScale("clock.png", .5) # Short Clockhand
    image clock_1 = im.FactorScale("clock_1.png", .5) # Long Clockhand
    image clock_2 = im.FactorScale("clock_2.png", .5) # Clockface

    #Checklist Images
    image img_title = im.FactorScale("todoListTitle_bkg.png", .5)
    image img_fileTaxes = im.FactorScale("file_taxes_bkg.png", .5)
    image img_friends = im.FactorScale("hang_friends_bkg.png", .5)
    image img_homework = im.FactorScale("homework_bkg.png", .5)
    image img_shopping = im.FactorScale("shopping_bkg.png", .5)
    image img_hadLunch = im.FactorScale("lunch_bkg.png", .5)
    image img_hadDinner = im.FactorScale("dinner_bkg.png", .5)

    #Checklist Images when Finished
    image img_fileTaxes_finished = im.FactorScale("file_taxes_bkg_finished.png", .5)
    image img_friends_finished = im.FactorScale("hang_friends_bkg_finished.png", .5)
    image img_homework_finished = im.FactorScale("homework_bkg_finished.png", .5)
    image img_shopping_finished = im.FactorScale("shopping_bkg_finished.png", .5)

    #Checklist Images when in progress
    image img_fileTaxes_working = im.FactorScale("file_taxes_bkg_working.png", .5)
    image img_friends_working = im.FactorScale("hang_friends_bkg_working.png", .5)
    image img_homework_working = im.FactorScale("homework_bkg_working.png", .5)
    image img_shopping_working = im.FactorScale("shopping_bkg_working.png", .5)

    #Backgrounds
    image blackBKG = "blackBKG.png"
    image lowPolyRedBKG = "lowPolyRedBKG.png"
    image lowPolyOrangeBKG = "lowPolyOrangeBKG.jpg"

    image room_day = "room.png"
    image room_night = "room_night.png"
    image living_room = "living_room.png"
    image cave = "cave.png"
    image store = "store.png"

    # Clock Manipulations
    transform rotateshort:
        xanchor 0.5
        yanchor 0.2
        xalign 0.5
        yalign 0.1
        rotate (minutes*6)

    transform rotatelong:
        xanchor 0.5
        yanchor 0.2
        xalign 0.5
        yalign 0.1
        rotate (minutes*0.5)

    transform clockPlace:
        xanchor 0.5
        yanchor 0.2
        xalign 0.5
        yalign 0.2

    # Check List Manipulations
    transform placeListItem(yValue):
        xanchor 0.5
        yanchor 0.5
        xalign 0.01
        yalign yValue

    screen clock:
        frame:
            xmaximum 150 # X size of clock graphic
            ymaximum 150 # Y size of clock graphic
            xalign 0.99 # X placement on screen
            yalign 0.02 # Y placement on screen
            add "clock_2" at clockPlace
            add "clock_1" at rotatelong
            add "clock" at rotateshort

    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0

    screen clockDissolve:
        frame at alpha_dissolve:
            xmaximum 150 # X size of clock graphic
            ymaximum 150 # Y size of clock graphic
            xalign 0.99 # X placement on screen
            yalign 0.02 # Y placement on screen
            add "clock_2" at clockPlace
            add "clock_1" at rotatelong
            add "clock" at rotateshort

    screen time_overlay:
        $ analog_minutes = minutes % 60
        $ analog_hours = (minutes / 60) % 24
        text ("%d:%02d" % (analog_hours, analog_minutes)) pos (675, 110)

    screen addonTime_overlay:
        text ("%s %d" % ("+", addonTime)) size 90 pos (250, 225) color "#b20000" at alpha_dissolve

    #Declare todo list tasks
    init python:
        #Declare todo list tasks & their states
        fileTaxes = 1
        friends = 1
        homework = 1
        shopping = 1
        hadLunch = 1
        hadDinner = 1

        #Tracks whether or not the player is tired at the end of the day
        isTired = False
        #tracks whether or not the player slept in
        hasNapped = False

        def hide_menu_function():
            renpy.hide("img_title")
            renpy.hide("img_fileTaxes")
            renpy.hide("img_homework")
            renpy.hide("img_shopping")
            renpy.hide("img_shopping")
            renpy.hide("img_hadLunch")
            renpy.hide("img_hadDinner")

        def create_menu_function(spacing):
            hide_menu_function()

            renpy.show("img_title", at_list=[placeListItem(spacing)])
            spacing += .05

            if fileTaxes == 0:
                renpy.show("img_fileTaxes_finished", at_list=[placeListItem(spacing)])
                spacing += .05
            if fileTaxes == 3:
                renpy.show("img_fileTaxes_working", at_list=[placeListItem(spacing)])
                spacing += .05
            if fileTaxes & fileTaxes != 3 & fileTaxes != 0:
                renpy.show("img_fileTaxes", at_list=[placeListItem(spacing)])
                spacing += .05

            if friends == 0:
                renpy.show("img_friends_finished", at_list=[placeListItem(spacing)])
                spacing += .05
            if friends == 3:
                renpy.show("img_friends_working", at_list=[placeListItem(spacing)])
                spacing += .05
            if friends & friends != 3 & friends != 0:
                renpy.show("img_friends", at_list=[placeListItem(spacing)])
                spacing += .05

            if homework == 0:
                renpy.show("img_homework_finished", at_list=[placeListItem(spacing)])
                spacing += .05
            if homework == 3:
                renpy.show("img_homework_working", at_list=[placeListItem(spacing)])
                spacing += .05
            if homework & homework != 3 & homework != 0:
                renpy.show("img_homework", at_list=[placeListItem(spacing)])
                spacing += .05

            if shopping == 0:
                renpy.show("img_shopping_finished", at_list=[placeListItem(spacing)])
                spacing += .05
            if shopping == 3:
                renpy.show("img_shopping_working", at_list=[placeListItem(spacing)])
                spacing += .05
            if shopping & shopping != 3 & shopping != 0:
                renpy.show("img_shopping", at_list=[placeListItem(spacing)])
                spacing += .05

        def update_clock_function():
            renpy.hide_screen("clock")
            renpy.show_screen("clock")
            renpy.hide_screen("time_overlay")
            renpy.show_screen("time_overlay")

        def addonTime_fadein_function():
            renpy.show_screen("addonTime_overlay")

        def addonTime_fadeout_function():
            renpy.hide_screen("addonTime_overlay")

        def display_adding_time_function():
            addonTime_fadein_function()
            renpy.pause(1.0)
            addonTime_fadeout_function()


# The game starts here.
label start:

    $ save_name = "Introduction"
    $ renpy.clear_game_runtime()

    $ decision_set = [ ]

    scene blackBKG

    centered "Welcome."

    "..."
    "...zzz..."
    "zzz... hmph."

    scene room_day with fade

    "You slowly begin to open your eyes and consciousness begins to ease its way back into your life."
    "Everything comes flooding back."
    "Your academic career."
    "Your friends."
    "Your slightly grungy apartment complex."
    "You turn on your side and look at the small clock by your bedside table:"

    show screen clockDissolve
    show screen time_overlay

    "9:00am on a Sunday."

    "As the first rays of light begin to pierce through your mildly opaque window blinds, you realize you have a choice to make."
    "This is a choice that every phenomenal writer, great entrepreneur, brilliant scientist, and commonplace college student has had to decide."

    menu:
        "Will you go back to bed for a few more minutes?"

        "Yes":
            $ addonTime = 30
            $ minutes += addonTime
            hide screen clockDissolve
            $ update_clock_function()
            $ display_adding_time_function()
            "I don’t even blame you. "
            "Getting the extra rest now means you’ll be more prepared to tackle the day."
            "You rest for another thirty minutes and then you wake up feeling absolutely amazing."

        "No":
            $ addonTime = 2
            $ minutes += addonTime
            hide screen clockDissolve
            $ update_clock_function()
            $ display_adding_time_function()
            "Sweet."
            "You decide there isn’t a moment to lose and chose to go ahead and tackle the day."

    "You peel your sheets off of your body and draw your knees up to your chest as you begin the mental preparation to start your day."
    "As you run through mental facts, motivational speeches, and Marvin Gaye songs, your eyes burst open to a piercing alarm."
    "As your eyes begin to dart around the room looking for the source of the noise, they land on a small object resting on your desk across the room: your phone."
    "With every pulse of the rhythm of the alarm, your tension begins to grow, but at the same time all you want to do is sleep."
    "You know that the alarm will simply switch off within the next five minutes if you just ignore it."

    menu:
        "Do you get up, dooming yourself to the day? Or do you just let it ring for a moment longer while you get some rest?"

        "Get up":
            $ addonTime = 2
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
        "Sleep in some more":
            $ addonTime = 60
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "You decide the alarm can wait and will switch off eventually anyways."
            "As you drift back off to sleep, your thoughts begin to wander to how your perpetual laziness may cause you to never leave your bed again."
            "You wake an hour later with a throbbing headache and regrets."
            "You might as well start your day and figure out what the alarm was about."

    "You take your legs and groggily begin to swing them off of the bed and take a few steps towards your desk."
    "You almost trip over a couple of your textbooks and dirty laundry scattered across the floor, but you make it."
    "As you begin to reach towards your phone, memories of why you set the alarm in the first place start surfacing."
    "All traces of exhaustion immediately leave your bones."
    "My gosh, today is the day."
    "You’ve been dreading this for weeks."
    "You know how sometimes you seem to overcommit yourself?"
    "Remember how you want to please everyone and still meet your own adult-ish life obligations?"
    "Yeah. Well, you did that again."
    "You mentally berate yourself for doing this to yourself (for the thousandth time)."
    "You take a deep breath and begin to steel yourself to look at the todo list you’ve wrapped yourself in this time."
    "You begin scanning the list on your phone line by line:"

    ###################################
    #Begin Menu Slide in for first time
    ###################################
    show img_title at placeListItem(checkListDist) with moveinleft
    $ checkListDist += .05

    "Today's TODO List:"

    show img_fileTaxes at placeListItem(checkListDist) with moveinleft
    $ checkListDist += .05

    "File your taxes"

    show img_friends at placeListItem(checkListDist) with moveinleft
    $ checkListDist += .05

    "Hang out with your friends"

    show img_homework at placeListItem(checkListDist) with moveinleft
    $ checkListDist += .05

    "Do your homework before tomorrow's class"

    show img_shopping at placeListItem(checkListDist) with moveinleft
    $ checkListDist += .05

    "And go shopping for some groceries before tomorrow"

    #reset checkListDist for next time the menu is spawned
    $ checkListDist = .01

    ###################################
    #End Menu Slide In
    ###################################

    "You sigh and set your phone down."

    "Well, first things first, you have to get ready for the day cause there ain’t no way you are presenting yourself to the world in your current state (*cough* gross *cough*)."

    "As you begin your day-to-day regimen of absolute beautification, you see your cute little pet looking up at you in hunger across the room."

    "But as the narrator, I honestly cannot remember what it is and my script is a little smudged, so you are going to have to remind me."

    $ pet_type = renpy.input("What type of pet is it again?")

    if pet_type == "":
        $ pet_type="rock"

    "Ah yes! A %(pet_type)s! That's what the script I'm not totally making up said."

    $ pet_name = renpy.input("What’s, er, its name again?")

    "%(pet_name)s? Okay. Fine. It's your life... I guess."

    "Good. Good. Glad we have that straightened out."

    "You certainly have a taste in… exotic pets."

    "Anyways, you feed cute little %(pet_name)s and make sure to give 'it' the care it deserves."

    "As you put the last finishing touches on your perfect, god-like body, you cook yourself some breakfast and ease yourself into your favorite kitchen chair."

    "As you munch on your breakfast, you see the tv across from you."

    #Ask for favorite show maybe?

    menu:
        "Flick the tv on to your favorite show?"

        "Yes":
            $ addonTime = 35
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "You enjoy your favorite episode of {i}Little House on the Prairie{/i} (it chokes you up every time)."
            "While it helped you relax, it did nothing to help you get your chores done for today."
            "In fact, you actually lost an extra ten minutes because you were so engrossed in the show, you didn't notice the time passing."
            "Tough luck, brah."
        "No":
            $ addonTime = 25
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "Deciding not to watch tv in the morning is a struggle for you, but you bite the bullet and toss the remote across the room so it won't be a temptation."
            "You finish your breakfast in a reasonable time frame."
            "Not too shabby at all."

    "You silently congratulate yourself for making it through the morning, pat yourself on the back, and encourage yourself the the rest of the day that lays ahead of you."

    "You pull back out your phone and are about to decide what to do first when you see a notification telling you that you have an update pending for your snazzy phone (It’s a robotFruit 8.2 SE)."

    "It doesn’t seem to be a major update and your phone is working fine the way it is currently."

    menu:
        "Do you spend the extra few minutes updating your phone or do you want to hurry up and get to your list?"

        "Yes":
            $ addonTime = 15
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "All about them updates, huh?"
            "You sit there twiddling your thumbs for an extra 15 minutes as you wait for your robotFruit 8.2 SE to restart, download, and restart again."
            "Nothing really looks different."
            "You decide to stop procrastinating and get on with your work."
            "Time to make some decisions."
            #Ask to lock phone with combination?
        "No":
            $ addonTime = 2
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "You chose not to waste your time on an update today."
            "I mean, you’re a busy person and it’s not like there’s anything important in there since your phone is already working fine, right?"
            "NBD. You just get on with your work. Time to make some decisions."

    "Warning: Tough choices be ahead."

    #TODOlist Spawner
    #$ create_menu_function(checkListDist)

    $ seen_set = [ ]

label choices:

    $ save_name = "Question Menu"
    $ create_menu_function(checkListDist)

    menu:

        set seen_set

        "What would you like to do?"

        "File Taxes" if fileTaxes:
            $ fileTaxes = 3
            $ create_menu_function(checkListDist)
            call taxes from _call_taxes_1
            $ fileTaxes = 0
            jump choices
        "Hang out with Friends" if friends:
            "Have fun with yo friends dawg!"
            $ friends = 3
            $ create_menu_function(checkListDist)
            call friends from _call_friends_1
            $ friends = 0
            $ create_menu_function(checkListDist)
            jump choices
        "Do Homework" if homework:
            $ homework = 3
            $ create_menu_function(checkListDist)
            call homework from _call_homework_1
            $ homework = 0
            $ create_menu_function(checkListDist)
            jump choices
        "Go Shopping" if shopping:
            "What? You think you are some form of responsible adult now? Fine. Go shopping."
            $ shopping = 3
            $ create_menu_function(checkListDist)
            call shopping from _call_shopping_1
            $ shopping = 0
            $ create_menu_function(checkListDist)
            jump choices
        "Go to Bed" if not(fileTaxes) and not(friends) and not(shopping) and not(homework):
            jump ending

label taxes:
    "Wow. Going with the taxes, huh?"
    "..."
    "Brave soul."

    "You decide that the taxes are just too important and better get done today."
    "Being the tech savvy person you are, you do all of your taxes online."
    "What a beautiful world we live in."

    scene living_room with dissolve
    $ create_menu_function(checkListDist)

    "You move over to your living room and sit down at your desk."
    "Blegh. \n"
    extend "This place is a mess."
    "You are defintiely going to organize it. Right?"

    menu:
        "Do you want to organize your desk before you start your taxes?"

        "Sure!":
            $ addonTime = 15
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ isNeat = True
            "Ah a neat freak. \n"
            extend "Good job."
            "While it may have taken a little extra effort up front, doing this will save you time in the long run."
            "Now that you've gotten that out of the way."
        "Who needs neat?":
            $ addonTime = 2
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "You’re right. \n"
            extend "Organization really isn't worth it."
            "Hey! \n"
            extend "I have an idea!"
            "Following your inspiring life choices, I might as well throw this script up in the air and see what comes of it!"
            "Of course, your life would become a garbled mess, but that’s no different from the way it is right now."
            "Whatever. \n"
            extend "You're the one that gets to make decisions -- not me."

    "You go ahead and boot up your old desktop running Windows Vista and watch it whirl to life."
    "You get hard to work."
    "Sweat starts pouring down your neck and you furiously fill out 1040’s, W-2, 1099-G forms."

    "You consider quitting, but you press on."

    scene blackBKG with fade
    "Everything begins to go black as you are consumed by the tax-life."

    scene living_room with fade
    $ create_menu_function(checkListDist)
    "Suddenly a ding noise coming from your desktop breaks you from your dedicated trance that would have made your uncle, who is a monk, incredibly jealous."

    "You welcome the distraction and glance at the intrusion on your screen."

    show popup at truecenter

    "A notification popped up stating that your computer is \"dangerously in danger!\""

    "It reads:"

    "WARNING! You may have critical errors on your PC. \n"
    extend "This wizard will help you improve the performance of your PC by removing critical system errors which may cause frequent application crashes, instability or slow computer speeds."

    "To continue by scanning your computer for critical errors, click \"Next\" below."

    menu:
        "What would you like to do?"
        "PRESS IT BOI!":
            $ addonTime = 2
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "Whew. \n"
            extend "Crisis averted."
            "You followed the prompts and clicked \“next\” when prompted and now it’s back to work!"
            hide popup
            "Feel safe."
        "Cancel out of that crap":
            $ addonTime = 7
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "You feel a little wary about following a prompt for something you do not recognize."
            "It didn’t look like your antivirus software, so you “cancelled” out of it, received five more popups, and then ran your antimalware software to clean it up. It found something called \“Edgar’s Love Trojan.\”"
            "You felt thoroughly creeped out and violated that that was on your computer."
            hide popup
            "It took some time, but you believe removing that trash to be worth it in the long run."

    "Now that that is over with you continue to slave away and knock out the last of the taxes."
    "All you have to do now is get some of these sweat-laden personal documents to your accountant."

    "Your accountant is such a kind guy (so kind)."
    "He gave you several ways that he would accept the sensitive documents from you."
    "Email, \n"
    extend "set up and send through PGP encrypted email, \n"
    extend "or a personal hand-delivered approach (half hour drive there and back)."

    menu:
        "How would you like to give da goods to your accountant?"

        "Email":
            $ addonTime = 20
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "You chose the fastest approach you could think of."
            "You took all the files, dropped them into an email, signed it with a few XOXO’s and then sent it off."
            "Done and done."
        "Encrypted Email":
            $ addonTime = 60
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "\"These are super sensitive documents, right?\" You thought to yourself."
            "I mean, your social security number is littered all over them."
            "So, of course they are sensitive!"
            "You want to take the extra time and precautions to make sure they get to your accountant safe."
            "You take an hour to set up a public and private key and to get the accountant’s credentials as well."
            "You then package all the files together, drop them into the email, put a secret message just for the accountant’s eyes, and then send them off."
            "What was written in that email, you ask?"
            "I have absolutely no clue. You are the one who wrote it."
            "Done and done."
        "Hand-Delivered":
            $ addonTime = 105
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "Meh. \n"
            extend "I can tell you don't really care for that technogarbage trash."
            "However, you still want to get the documents to your account safe and sound without any danger of it falling into the wrong hands."
            "Plus, this way you have an excuse to see that oh so nice accountant again in the flesh."
            "It’s a win win except in the time category."
            "You package all the files together, hop into the car, and drive to see the lov- the accountant. I meant the accountant."
            "It should have been a simple task of driving there, dropping off the goods, and then driving back, but you get stuck in a social situation with the guy."
            "You guys talk for a lot longer than you originally anticipated and you leave with a spring in your step and a song in your heart."
            "But you still wonder what happened to all your time."
            "He’s such a sweet guy though."

    "That’s one thing checked off the list for today."
    "Feel good about yourself."
    "That was grunge work and you know it, so thankfully it is now out of the way."

    jump choices

label friends:
    "Friends"

label homework:
    "Ah slave work. \n"
    extend "Er, I mean homework."

    "A necessary suffering to the college student’s life."
    "Unfortunately, you chose to have that suffering start right now."

    scene room_day with fade
    $ create_menu_function(checkListDist)

    "You head back to your room where you remember from this morning that you, oh so carefully, stored your books there on the floor."
    "As you walk around the room and pick up the scattered textbooks and papers all around, you begin to develop a sinking feeling in the pit of your stomach."

    "Where is it? \n"
    extend "Where is the book you need for your homework??"
    "You could have sworn that you haphazardly put it here with all the others."

    "Panic starts to seep in and your searching begins to become more and more frantic."

    "You need this book to complete the assignment due tomorrow!"
    "You can’t complete it without it!"

    "It’s at times like these that you wish you were in the same courses as your friends, but instead you chose the lonely route that is having an obscure major."

    "The way I see it, you have three options: \n"
    extend "1. Pirate it (20 min) \n"
    extend "2. Skip the homework and get a poor grade (2 min) \n"
    extend "3. Keep searching (1 hr 30 min)"

    menu:
        "What would you like to do?"

        "Pirate it (20 min)":
            $ addonTime = 20
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "Ah sailing the high seas, are we?"
            "Well it looks like it worked out for you."
            "You found a site called freeepubsformoms.com and were able to get the textbook you needed."
            "Your mom would be incredibly proud!"

        "Skip it (2 min)":
            $ addonTime = 2
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "Meh. \n"
            extend "You're right."
            "Who needs homework anyways?"
            "You’ve been doing fine in the class up until this point."
            "What’s one missing assignment?"
            "Just do as all a favor and find that book later, okay?"
            "We wouldn’t want you making this decision all the time now."

            menu:
                "Do you promise me you'll find it later? Pretty Please?"

                "Eh sure.":
                    "OH THANK YOU THANK YOU THANK YOU."
                    "Now doesn't that feel nice?"
                    "Do you feel the power of positive change coursing through your veins?"
                    "(I think I may be falling in love.)"
                    "(No. Control yourself.)"
                    "(You can't have another experience like in Switzerland.)"
                    "Ahem. I mean. Good job young chap."
                    "I'm proud of you."
                    "Now get back to work since you skimping out on your education!"
                "Nope. Sorry.":
                    "..."
                    "......."
                    "Excuse me?"
                    "I slave over a hot stove all day for you and this is the thanks I get??"
                    "I'm ashamed of your upbringing."
                    "I don't know if I can ever look at you the same way again."
                    "But I guess that has no bearing on your story, so I'll try and not let it impact anything (loser)."
                    "NOW GET BACK TO WORK YOU LAZY BUM!"
                    "Sorry. \n"
                    extend "I don't know what came over me there."
                    "Ahem. I mean back to the story."

            $ homework = 0
            jump choices

        "Keep searching (1 hr 30 min)":
            $ addonTime = 90
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "You chose the hard and laborious path of continuing the search."
            "Throughout it, you find things you never even knew you owned!"

            #Start ebay music
            play music "ebay_song.mp3"
            "Did you always have two pets?"
            "I mean, look.. "
            extend "at all… "
            extend "this stuff…"
            "Somebody has been shopping."
            "How do you even live with yourself?"
            "This is just... excessive."
            "BRB. I'm gonna call {i}American Hoarders Hotline{/i} really quick."
            "........"
            "............."
            "........"
            "Yeah, they say you are a lost cause."
            "I guess we'll just have to move on regardless!"
            stop music
            #End ebay music

            "Okay enough of that."
            "I know you are craving the envigorating plot that is yet to come."
            "Here it is:"
            "You spent a good deal of time, but you finally found it."
            "(And your room isn’t a pigsty anymore! What a responsible semi-adult.)"
            "Boom."
            "You're welcome."

    menu:
        "Now that all of that is taken care of, did you perchance want to study before you start your homework?"

        "Sure. Why not?":
            $ addonTime = 40
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "Swag. \n"
            "You lose an extra 45 minutes to studying, but that will undeniably help you when it comes time to actually do the homework."
            "Here we go."
            "The first assignment."
            "You. "
            extend "Can. "
            extend "Do this."

            "You begin to psych yourself up by playing some {i}\“In the Air Tonight\”{/i} by Phil Collins."
            "The beat moves in rhythm with your pencil and you get into your flow."
            "It’s incredible."
            "It feels like you are flying."

            "Suddenly you get an email from you brother and right before the big drop in the song too."
            "Long story short, he found out the latest season of {i}Gilmore Girls{/i} is on Netflix and would really like to borrow your account so he can watch it this weekend."
            "You’re fine with letting him use your account, there’s just the problem with getting him your credentials so that he can log in."

            menu:
                "How do you want to send him your username and password?"

                "Text":
                    $ addonTime = 5
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    "You send him a hurried text."
                    "Quickly, you type out your username and password and click send."
                    "You don’t want to get distracted any more than you have to since you are kinda in the flow at the moment."

                "Email":
                    $ addonTime = 15
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    "Since it’s your brother, you decide you should at least give him the curtesy of sending him an email back with the info he needs."
                    "Plus, this way you won't get sucked into a conversation with him when you really just need to get back to work."
                    "You write the email as fast as you can, giving him your credentials, and then press send."
                    "You don’t want to get distracted any more than you have to since you are kinda in the flow at the moment."

                "Encrypted Email":
                    $ addonTime = 60
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    "You decide and encrypted email is the way to go."
                    "Your information is important and you don’t want the Chinese to somehow get access to your precious Netflix account."
                    "They'd probably wreck all of the hours you’ve spent rating movies for better recommendations!"
                    "Honestly, you have nothing against dubbed movies, you’d just rather not have it plastered all over your feed."
                    "So you take the time to set up a public and private key and get your brother to do the same."
                    "It takes time and your brother got a little annoyed at you over the whole thing, but once you sent you username and password you know it was the safest option available."

                "Phone Call":
                    $ addonTime = 45
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    "You decide just to call him up and give him the information over the phone."
                    "Hey, it’s your brother and you haven’t talked in a while so it only makes sense to do it this way."
                    "It really was a nice break from all of your hard work."
                    "Sure, you may have used a little more time this way, but you got to catch up with him and hear all about his recent crush on Rory Gilmore."
                    "Yup. It was something special."

                "Encrypted Call":
                    $ addonTime = 90
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    "You decide not to compromise sociability or security and decide to download an app that encrypts your phone calls over wifi."
                    "You have to wait a little for your brother to download the app and to get into a wifi zone, but it works."
                    "Sure, you may have used a little more time this way to set it all up securely and to talk with your brother, but you got to catch up with him and hear all about his recent crush on Rory Gilmore."
                    "Plus, the audio only cut out once or twice on you."
                    "Yup. It was something special."

            "Now that that distraction is out of the way, you pump back on the music and you take out the homework like it was nothing."
            $ addonTime = 30
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "Thanks to that extra studying and you got everything done much faster than you originally anticipated."

            $ homework = 0
            jump choices

        "I'd rather not. What's a \"study\" anyways?":
            $ addonTime = 2
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "Yeah, I didn't really pinpoint you as the extracurriculur-\"I play in the band after school\"-studious type."
            "You've paid attention in class though so you feel like you can do it."
            "You've got this."
            "Here we go."
            "The first assignment."
            "You. "
            extend "Can. "
            extend "Do this."

            "Suddenly, get an email from you brother."
            ". It caught you off guard and actually disrupted your daydreaming fantasies long enough for you to glance over at your computer and read the email."
            "Long story short, he found out the latest season of {i}Gilmore Girls{/i} is on Netflix and would really like to borrow your account so he can watch it this weekend."
            "You’re fine with letting him use your account, there’s just the problem with getting him your credentials so that he can log in."

            menu:
                "How do you want to send him your username and password?"

                "Text":
                    $ addonTime = 5
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    "You send him a hurried text."
                    "Quickly, you type out your username and password and click send."
                    "You don’t want to get distracted any more than you have to since you are kinda in the flow at the moment."

                "Email":
                    $ addonTime = 15
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    "Since it’s your brother, you decide you should at least give him the curtesy of sending him an email back with the info he needs."
                    "Plus, this way you won't get sucked into a conversation with him when you really just need to get back to work."
                    "You write the email as fast as you can, giving him your credentials, and then press send."
                    "You don’t want to get distracted any more than you have to since you are kinda in the flow at the moment."

                "Encrypted Email":
                    $ addonTime = 60
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    "You decide and encrypted email is the way to go."
                    "Your information is important and you don’t want the Chinese to somehow get access to your precious Netflix account."
                    "They'd probably wreck all of the hours you’ve spent rating movies for better recommendations!"
                    "Honestly, you have nothing against dubbed movies, you’d just rather not have it plastered all over your feed."
                    "So you take the time to set up a public and private key and get your brother to do the same."
                    "It takes time and your brother got a little annoyed at you over the whole thing, but once you sent you username and password you know it was the safest option available."

                "Phone Call":
                    $ addonTime = 45
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    "You decide just to call him up and give him the information over the phone."
                    "Hey, it’s your brother and you haven’t talked in a while so it only makes sense to do it this way."
                    "It really was a nice break from all of your hard work."
                    "Sure, you may have used a little more time this way, but you got to catch up with him and hear all about his recent crush on Rory Gilmore."
                    "Yup. It was something special."

                "Encrypted Call":
                    $ addonTime = 90
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    "You decide not to compromise sociability or security and decide to download an app that encrypts your phone calls over wifi."
                    "You have to wait a little for your brother to download the app and to get into a wifi zone, but it works."
                    "Sure, you may have used a little more time this way to set it all up securely and to talk with your brother, but you got to catch up with him and hear all about his recent crush on Rory Gilmore."
                    "Plus, the audio only cut out once or twice on you."
                    "Yup. It was something special."


            "Now that that distraction is out of the way, you try your hardest to get back into your work."
            $ addonTime = 120
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "It’s slow-going and there are a few more distractions, but you eventually get all the work done."
            "It feels good to finally have that out of the way."

            $ homework = 0
            jump choices

label shopping:
    "Everyone needs food right?"
    "You looked in your cupboards earlier and notice a strange lack of anything edible after you ate the last of your food for breakfast."
    "To remedy this, you decide to head to the store to do some much needed shoppin’."

    scene store with dissolve
    $ create_menu_function(checkListDist)

    "When you get there, you dutifully peruse the pastries and exotic cheeses, gather the necessary ingredients for the strawberry lobster soufflé you’ve been dying to try, and moved towards the checkout counter."
    "You inch closer and closer in your line, until… "
    extend "shoot!"
    "You forgot that you bought that really expensive Smurf’s TV tray from ebay a few weeks ago and don’t have any money in your checking account!"

    "You pull out your phone to quickly make a transfer from savings into checking, but you don’t have data in this area."
    "One bad thing after another, huh?"
    "What a day."

    "Wait!"
    "Before you quit and all hope is lost, you notice that the store has a free unprotected WiFi hotspot!"
    "You could easily connect to it to make the transfer and be on your way."

    menu:
        "What would you like to do?"

        "Transfer the money through the store's wifi":
            $ addonTime = 7
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "Definitely the quickest and most efficient option."
            "You use your formidable intellect to determine that you would like to save time, money, and gas by just moving money over into your bank account."
            "Nice one!"
            "You continue to cruise through the checkout counter without skipping a beat and are soon out of the store before you know it with all the goat cheese your arms could carry."

        "Head back home, get some cash, come back to the store, and check out again":
            $ addonTime = 100
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "You berate yourself as you carefully put all the cartful of goat cheese all back in its respective aisle in the store and climb back into your car to head home."
            "Sometimes you wonder why you go through so much trouble in order to be secure even when it would have just been a short transaction."
            "After the long drive back home, you grab the extra cash you store in the cookie jar in your kitchen, make a mental note to get cookies while at the store, and then head back out."
            "You are able to check out this time without too much trouble, but man, did you wish you hadn’t forgotten about your empty checking account earlier!"

    "You feel a little drained after that whole ordeal and actually feel a little exhausted."

label ending:
    scene room_night with dissolve
    $ create_menu_function(checkListDist)

    "ending"

# The splashscreen is called, if it exists, before the main menu is
# shown the first time. It is not called if the game has restarted.

# We'll comment it out for now.
#
# label splashscreen:
#     scene black
#     show text "Taylor University's Computer Science Department Presents..." with dissolve
#     $ renpy.pause(1.0)
#     hide text with dissolve
#
#     return

    return

init python:
    style.text.color = "#e08a2c"
    style.text.bold = True
    style.text.size = 27
