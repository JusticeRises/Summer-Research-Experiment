init:
    #screen size setup
    $ config.screen_width = 800
    $ config.screen_height = 600

    #screen title setup
    $ config.window_title = "Test Experiment"

    #Variables
    $ minutes = 540
    $ bedtime = 1320
    $ checkListDist = 0.03
    $ isNeat = False
    $ addonTime = 0
    $ securityLevel = 3

    $ yIncrement = .5
    $ xMain = .1
    $ xTime = .9

    #Decision Variables
    $ first_sleep_in = False
    $ second_sleep_in = False
    $ pet_type = False
    $ pet_name = False
    $ watch_tv = False
    $ update_phone = False

    $ organize_desk = False
    $ click_popup = False
    $ tax_delivery = False

    $ pirate_movie = False
    $ download_app = False

    $ homework_decision = False
    $ study = False
    $ netflix_password = False

    $ wifi_transfer = False
    $ coffee_break = False
    $ arguing = False

    define introDissolve_1 = Dissolve(2.0)
    define introDissolve_2 = Dissolve(1.0)

    image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0)

    image popup = im.FactorScale("popup.jpg", .75)
    image pet_dog = "pet_dog.png"
    image losing_face = "losing_face.png"

    #Intro Images
    image justice = "swaggin_justice.png"
    image cute_picture = "cute_picture.jpg"
    image intro_image = "introImage.png"
    image intro_bkg = "intro_bkg.png"

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
    image friends_house = "friends_house.png"

    #Security Health Images
    image level_1 = im.FactorScale("level-1.png", .6)
    image level_2 = im.FactorScale("level-2.png", .6)
    image level_3 = im.FactorScale("level-3.png", .6)
    image level_4 = im.FactorScale("level-4.png", .6)
    image level_5 = im.FactorScale("level-5.png", .6)
    image level_6 = im.FactorScale("level-6.png", .6)
    image level_7 = im.FactorScale("level-7.png", .6)

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

    # Security Health Manipulations
    transform levelPlace():
        xanchor 0.5
        yanchor 0.5
        xalign 0.55
        yalign 0.05

    # End Results Manipulations
    transform resultsPlace(xValue, yValue):
        xanchor 0.5
        yanchor 0.5
        xalign (xValue)
        yalign (yValue)

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

        $ minutes_left = 60 - analog_minutes
        $ hours_left = 16 - analog_hours

        if minutes_left == 60:
            $ minutes_left = 0
            $ hours_left += 1

        if minutes <= 1019 and minutes <= 599:
            text ("%d:%02d" % (analog_hours, analog_minutes)) pos (680, 110) color "#e08a2c" size 30 bold True
            text ("%s%d:%02d" % ("Time left: ",hours_left, minutes_left)) pos (665, 140) color "#b76f27" size 12 bold True
        if minutes <= 1019 and minutes >= 600:
            text ("%d:%02d" % (analog_hours, analog_minutes)) pos (675, 110) color "#e08a2c" size 27 bold True
            text ("%s%d:%02d" % ("Time left: ",hours_left, minutes_left)) pos (665, 140) color "#b76f27" size 12 bold True
        if minutes >= 1110:
            text ("%d:%02d" % (analog_hours, analog_minutes)) pos (675, 110) color "#B33A3A" size 27 bold True
            text ("%s%d:%02d" % ("Late: ",hours_left, minutes_left)) pos (680, 140) color "#8C2F2F" size 12 bold True

    screen addonTime_overlay:
        text ("%s %d" % ("+", addonTime)) size 90 pos (250, 225) color "#e4787c" at alpha_dissolve

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
            renpy.hide("img_friends")
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
            if fileTaxes == 1:
                renpy.show("img_fileTaxes", at_list=[placeListItem(spacing)])
                spacing += .05

            if friends == 0:
                renpy.show("img_friends_finished", at_list=[placeListItem(spacing)])
                spacing += .05
            if friends == 3:
                renpy.show("img_friends_working", at_list=[placeListItem(spacing)])
                spacing += .05
            if friends == 1:
                renpy.show("img_friends", at_list=[placeListItem(spacing)])
                spacing += .05

            if homework == 0:
                renpy.show("img_homework_finished", at_list=[placeListItem(spacing)])
                spacing += .05
            if homework == 3:
                renpy.show("img_homework_working", at_list=[placeListItem(spacing)])
                spacing += .05
            if homework == 1:
                renpy.show("img_homework", at_list=[placeListItem(spacing)])
                spacing += .05

            if shopping == 0:
                renpy.show("img_shopping_finished", at_list=[placeListItem(spacing)])
                spacing += .05
            if shopping == 3:
                renpy.show("img_shopping_working", at_list=[placeListItem(spacing)])
                spacing += .05
            if shopping == 1:
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

        def hide_security_level_function(securityValue):
            security_image = "level_%(securityLevel)d" % globals()
            renpy.hide(security_image)
            renpy.with_statement(dissolve, always=True)

        def show_security_level_function(securityValue):
            security_image = "level_%(securityLevel)d" % globals()
            renpy.show(security_image, at_list=[levelPlace])
            renpy.with_statement(dissolve, always=True)

        def increment_show_security(securityValue):
            if securityValue != 7:
                if second_group:
                    hide_security_level_function(securityValue)
                globals()['securityLevel'] += 1
                if second_group:
                    show_security_level_function(securityValue)

        def decrement_show_security(securityValue):
            if securityValue != 1:
                if second_group:
                    hide_security_level_function(securityValue)
                globals()['securityLevel'] -= 1
                if second_group:
                    show_security_level_function(securityValue)


# The game starts here.
label start:

    scene black
    with Pause(1)

    "Hey, uh, quick question:"

    menu:
        "Are you in the first or second experimental group for this game?"

        "First":
            $ second_group = False

        "Second":
            $ second_group = True

    "Appreciate it."
    $ player_major = renpy.input("Secondly, what's your major/background?")
    "Nice!"
    "%(player_major)s? Pretty rad."
    "I just had to do some quick housekeeping really quick is all to set up for all the fun you are about to have."

    scene intro_bkg with dissolve

    play movie "street_day_animated.ogv"
    show movie with dissolve

    "AH welcome."

    "You are probably wondering what the heck you got yourself into by signing away your first born on that form that "
    show justice
    extend "this handsome devil gave you a few minutes ago."

    hide justice

    "Well tsk tsk."
    "Someone is a jolly big eager beaver over here."

    "But I like your gumption."

    "That means you’ll be perfect for our little… "
    extend "research experiment."

    "No no! Don’t go away."

    "It’s harmless. I promise. "
    extend "(hope)"

    "You see, you are one of the first people in line to try out this new area of research and so, honestly, we have no idea what could happen."

    "I would personally say one of three things could happen:"

    "1. You’ll help us prove our hypothesis (huzzah!)"
    "2. You’ll help us disprove it (works too, I guess.)"
    "3. Or you’ll turn into Tom Cruise."

    "Really, all bets are up in the air at the moment as to what'll happen."
    "So, uh, let’s keep our figures crossed for the third option for both our sakes, shall we?"

    "What research are you helping in, you ask?"
    "Meh. "
    "It’s not important (especially now that you’ve signed our forms)."
    "All will be revealed in due time."

    "You are about to embark on a crazy adventure full on adventure, intrigue, and a little romantic subplot."

    "Okay, actually, I’m lying."
    "It’s actually an extremely bland story where you get to go through a day in the life of a college student on a Sunday afternoon trying to get his/her (who knows?) todo list done."

    "GET PUMPED!"

    "It’s a time management game, so use your time efficiently, effectively, and some other word that starts with an \“e\”."

    #Begin instructions

    "The whole purpose is to try and get your list of todo items done before 6:30pm, if possible."

    "Don't worry, if you are super slow and miss the deadline, you will still get to finish the game."

    "But if that happens, I will show you a super sad face at the end and no one wants to see that."

    "However, if you win, you will be considered an super-neo-awesome time manager and I will love you forever."

    "When playing through the game, time will be marked both analog and digitally (for the analog-impaired) in the top right hand corner of the screen like this."

    show screen clockDissolve
    show screen time_overlay

    "As you make decisions, the clock will increase accordingly and one of these:"

    $ addonTime = 30
    $ minutes += addonTime
    hide screen clockDissolve
    show screen clockDissolve
    $ renpy.hide_screen("time_overlay")
    $ renpy.show_screen("time_overlay")
    $ display_adding_time_function()

    "will happen."

    "It's super pretty isn't it?"

    "(Say yes cause I spent probably too much time on that one feature.)"

    "Heck, cause I’m feeling so generous (and for visual balance – hey artists are cool, okay?), I’ll even give you a handy dandy todo list in the top left side of the screen."

    $ create_menu_function(checkListDist)

    "You are, oh, so welcome."

    $ hide_menu_function()
    hide screen clockDissolve
    $ renpy.hide_screen("time_overlay")
    $ minutes -= 30

    if second_group:
        "Oh and one more thing."

        $ show_security_level_function(securityLevel)

        "As you make decisions, your security “health” will go up and down as reflected by that cute little flower over there."

        $ increment_show_security(securityLevel)
        $ renpy.pause(0.75)
        $ decrement_show_security(securityLevel)

        "Yup. And remember, this flower is only a rental, so don’t go killing it on me. I want to be able to return it by the end of this thing."

    "So go! \n"
    "Make wise or stupid decisions!"

    "The only important thing is that you try and answer as wise or as stupid as you would if you were actually in these situations in a real life situation."

    menu:
        "Can you promise me you'll do that?"

        "Yes":
            "Swag. "
            extend "You’re pretty cool."
            "You know that?"
            "Also did you watch {i}Downton Abbey{/i} last night??"
            "haha oh boy was that a big mess!!"
            "ahh ha ha this is like a conversation ha ha this is so personable"
            "Oh man."
            "This will be a fun go around."
            "Let’s hurry up and get this party started!"

        "No":
            "Alr- wait. What? No??"
            "You see? Now that was a test and you utterly failed it."
            "I've never had anyone fail this early on before."
            "Heck, I don't even know what to do now."
            "The script doesn't cover this kind of thing."
            "Well, I can’t let you proceed until you answer correctly while still being truthful."
            "What are trying to do, anyways?"
            "Wreck Justice’s end results?"
            "Not cool."
            "Justice will be hearing about this."
            "I know. We'll just try again and pretend none of this ever happend."

            menu:
                "Can you promise me you'll follow the story truthfully?"

                "Yes":
                    "Swag. "
                    extend "You’re pretty cool."
                    "You know that?"
                    "Also did you watch {i}Downton Abbey{/i} last night??"
                    "haha oh boy was that a big mess!!"
                    "ahh ha ha this is like a conversation ha ha this is so personable"
                    "Oh man."
                    "This will be a fun go around."
                    "Let’s hurry up and get this party started!"

                "No":
                    "Oh come on!"
                    "Why are you even taking this right now if you didn’t plan on answering truthfully?!"
                    "Now quite playing games and answer correctly!"

                    menu:
                        "Yes":
                            "Swag. "
                            extend "You’re pretty cool."
                            "You know that?"
                            "Also did you watch {i}Downton Abbey{/i} last night??"
                            "haha oh boy was that a big mess!!"
                            "ahh ha ha this is like a conversation ha ha this is so personable"
                            "Oh man."
                            "This will be a fun go around."
                            "Let’s hurry up and get this party started!"
                        "No":
                            "Stop it!"
                            "Now answer correctly, gosh darn it!"

                            menu:
                                "Yes":
                                    "Swag. "
                                    extend "You’re pretty cool."
                                    "You know that?"
                                    "Also did you watch {i}Downton Abbey{/i} last night??"
                                    "haha oh boy was that a big mess!!"
                                    "ahh ha ha this is like a conversation ha ha this is so personable"
                                    "Oh man."
                                    "This will be a fun go around."
                                    "Let’s hurry up and get this party started!"
                                "No":
                                    "Here."
                                    "How about this."
                                    "You do me a solid and then I give you one as well."
                                    show cute_picture at truecenter
                                    "Here is a super cute picture I found on the internet."
                                    "May it appease your vehement spirit towards this experiment and cause you to finally get on board with what we are selling."

                                    hide cute_picture

                                    menu:
                                        "So whaddya say?"

                                        "Yes":
                                            "HUZZAH!"
                                            "UPWARDS AND ONWARDS WE GO!"
                                            "But seriously, thanks for finally helping a brotha out."
                                            "Oh man am I pumped to get this thing started."
                                            "Shall we?"
                                        "No":
                                            "Fine."
                                            "You know what?"
                                            "I'm going to rig it."

                                            menu:
                                                "You will answer yes."

                                                "Yes":
                                                    "HUZZAH!"
                                                    "UPWARDS AND ONWARDS WE GO!"
                                                    "But seriously, thanks for finally helping a brotha out."
                                                    "Oh man am I pumped to get this thing started."
                                                    "Shall we?"
                                                "Yes":
                                                    "HUZZAH!"
                                                    "UPWARDS AND ONWARDS WE GO!"
                                                    "But seriously, thanks for finally helping a brotha out."
                                                    "Oh man am I pumped to get this thing started."
                                                    "Shall we?"

    "Here we goooooooo!"
    "Weird."
    "That didn’t work."
    "I hope it isn’t one of those delayed things."

    "I’ll just do a forc-"

    scene black with dissolve

    show intro_image with introDissolve_1

    hide intro_image with introDissolve_2

label introduction:

    $ save_name = "Introduction"
    $ renpy.clear_game_runtime()

    $ decision_set = [ ]

    scene blackBKG

    "..."
    "...zzz..."
    "zzz... hmph."

    scene room_day with fade

    "You slowly begin to open your eyes and consciousness begins to ease its way back into your life."
    if not(second_group):
        "Everything comes flooding back."
    if second_group:
        "Everything comes flooding back (again)."
    "Your academic career."
    "Your friends."
    "Your slightly grungy apartment complex."
    "You turn on your side and look at the small clock by your bedside table:"

    show screen clockDissolve
    show screen time_overlay
    if second_group:
        $ show_security_level_function(securityLevel)

    "9:00am on a Sunday."

    "As the first rays of light begin to pierce through your mildly opaque window blinds, you realize you have a choice to make."
    "This is a choice that every phenomenal writer, great entrepreneur, brilliant scientist, and commonplace college student has had to decide."

    menu:
        "Will you go back to bed for a few more minutes?"

        "Yes (Long)":
            $ first_sleep_in = True

            $ addonTime = 30
            $ minutes += addonTime
            hide screen clockDissolve
            $ update_clock_function()
            $ display_adding_time_function()

            "I don’t even blame you. "
            "Getting the extra rest now means you’ll be more prepared to tackle the day."
            "You rest for another thirty minutes and then you wake up feeling absolutely amazing."

        "No (Short)":
            $ first_sleep_in = False

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

        "Get up (Short)":
            $ second_sleep_in = False

            $ addonTime = 2
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
        "Sleep in some more (Long)":
            $ second_sleep_in = True

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
    $ checkListDist = .03

    ###################################
    #End Menu Slide In
    ###################################

    "You sigh and set your phone down."

    "Well, first things first, you have to get ready for the day cause there ain’t no way you are presenting yourself to the world in your current state (*cough* gross *cough*)."

    "As you begin your day-to-day regimen of absolute beautification, you see your cute little pet looking up at you in hunger across the room."

    "But as the narrator, I honestly cannot remember what it is and my script is a little smudged, so you are going to have to remind me."

    $ pet_type = renpy.input("What type of pet is it again?")

    if pet_type != "":
        if pet_type == "dog" or pet_type == "Dog":
            "Ah yes! A %(pet_type)s! That's what the script I'm not totally making up said."
            "You know?"
            "I am so so thankful you chose a dog."
            "I was going to make a graphic for every possible animal that someone could have as a pet."
            "HOWEVER, I spent ages on this one of a dog and I never was able to create the rest."
            "Well, why don't I just show you?"
            show pet_dog with dissolve
            "Isn't she a beaut?"
            "I may have gone a little bit overboard, but no matter!"
            "Man. I love this dog."
        if pet_type != "dog" and pet_type != "Dog":
            "Ah yes!"
            "A do- wait."
            "You didn't chose a dog?"
            "But everyone chooses dogs for pets!"
            "It's like... the most common thing ever!"
            show pet_dog with dissolve
            "What the heck am I supposed to do with this image of your pet {i}dog{/i} that I made??"
            "I spent literally days making this thing and I can't even use it properly?"
            "Man, I knew I should have gone for a %(pet_type)s!"
            "Stupid. Stupid. Stupid."
            "Oh well."
            "Enjoy the rest of my stupid story with your %(pet_type)s."

    if pet_type == "":
        "Way not to choose anything."
        "Fine. I'll just give you something."
        "How about an... umm.... seahorse riding an enchilada?"
        "Yeah, waay to crazy."
        "Just take a dog."
        $ pet_type="dog"
        show pet_dog with dissolve

    $ pet_name = renpy.input("What’s, er, its name again?")

    if pet_name != "":
        "%(pet_name)s? Okay. Fine. It's your life... I guess."

    if pet_name == "":
        "Wow."
        "How the heck do you call your %(pet_type)s without a name?"
        "Ya know what?"
        "For the sake of the story, I'm just gonna call him Steve for now."
        $ pet_name = "Steve"

    "Anyways, you feed cute little %(pet_name)s and make sure to give 'it' the care it deserves."

    hide pet_dog

    "As you put the last finishing touches on your perfect, god-like body, you cook yourself some breakfast and ease yourself into your favorite kitchen chair."

    "As you munch on your breakfast, you see the tv across from you."

    #Ask for favorite show maybe?

    menu:
        "Flick the tv on to your favorite show?"

        "Yes (Long)":
            $ watch_tv = True

            $ addonTime = 35
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "You enjoy your favorite episode of {i}Little House on the Prairie{/i} (it chokes you up every time)."
            "While it helped you relax, it did nothing to help you get your chores done for today."
            "In fact, you actually lost an extra ten minutes because you were so engrossed in the show, you didn't notice the time passing."
            "Tough luck, brah."
        "No (Short)":
            $ watch_tv = False

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


    ###
    # SECURITY QUESTION 1
    ###
    menu:
        "Do you spend the extra few minutes updating your phone or do you want to hurry up and get to your list?"

        "Yes (Long)":
            $ update_phone = True

            $ addonTime = 15
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ increment_show_security(securityLevel)
            "All about them updates, huh?"
            "You sit there twiddling your thumbs for an extra 15 minutes as you wait for your robotFruit 8.2 SE to restart, download, and restart again."
            "Nothing really looks different."
            "You decide to stop procrastinating and get on with your work."
            "Time to make some decisions."
            #Ask to lock phone with combination?
        "No (Short)":
            $ update_phone = False

            $ addonTime = 2
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ decrement_show_security(securityLevel)
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
            jump choices
        "Hang out with Friends" if friends:
            $ friends = 3
            $ create_menu_function(checkListDist)
            call friends from _call_friends_1
            jump choices
        "Do Homework" if homework:
            $ homework = 3
            $ create_menu_function(checkListDist)
            call homework from _call_homework_1
            jump choices
        "Go Shopping" if shopping:
            $ shopping = 3
            $ create_menu_function(checkListDist)
            call shopping from _call_shopping_1
            jump choices
        "Go to Bed" if not(fileTaxes) and not(friends) and not(shopping) and not(homework):
            jump ending
            return

label taxes:
    "Wow. Going with the taxes, huh?"
    "..."
    "Brave soul."

    "You decide that the taxes are just too important and better get done today."
    "Being the tech savvy person you are, you do all of your taxes online."
    "What a beautiful world we live in."

    scene living_room with dissolve
    $ create_menu_function(checkListDist)
    if second_group:
        $ show_security_level_function(securityLevel)

    "You move over to your living room and sit down at your desk."
    "Blegh. \n"
    extend "This place is a mess."
    "You are defintiely going to organize it. Right?"

    menu:
        "Do you want to organize your desk before you start your taxes?"

        "Sure! (Long)":
            $ organize_desk = True

            $ addonTime = 15
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ isNeat = True
            "Ah a neat freak. \n"
            extend "Good job."
            "While it may have taken a little extra effort up front, doing this will save you time in the long run."
            "Now that you've gotten that out of the way."
        "Who needs neat? (Short)":
            $ organize_desk = False

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

    ###
    # SECURITY QUESTION 2
    ###

    scene living_room with fade
    $ create_menu_function(checkListDist)
    if second_group:
        $ show_security_level_function(securityLevel)
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
        "PRESS IT BOI! (Short)":
            $ click_popup = True

            $ addonTime = 5
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ decrement_show_security(securityLevel)
            "Whew. \n"
            extend "Crisis averted."
            "You followed the prompts and clicked \“next\” when prompted and now it’s back to work!"
            hide popup
            "Feel safe."
        "Cancel out of that crap (Long)":
            $ click_popup = False

            $ addonTime = 20
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ increment_show_security(securityLevel)
            "You feel a little wary about following a prompt for something you do not recognize."
            "It didn’t look like your antivirus software, so you “cancelled” out of it, received five more popups, and then ran your antimalware software to clean it up. It found something called \“Edgar’s Love Trojan.\”"
            "You felt thoroughly creeped out and violated that that was on your computer."
            hide popup
            "It took some time, but you believe removing that trash to be worth it in the long run."

    "Now that that is over with you continue to slave away and knock out the last of the taxes."
    "All you have to do now is get some of these sweat-laden personal documents to your accountant."

    "Your accountant is such a kind guy (so kind)."
    "He gave you several ways that he would accept the sensitive documents from you."
    "1. Email \n"
    extend "2. Set up and send through PGP encrypted email \n"
    extend "3. Hand-deliver the sucker (half hour drive there and back)"

    ###
    # SECURITY QUESTION 3
    ###

    menu:
        "How would you like to give da goods to your accountant?"

        "Email (Short)":
            $ tax_delivery = "Email"

            $ addonTime = 20
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ decrement_show_security(securityLevel)
            "You chose the fastest approach you could think of."
            "You took all the files, dropped them into an email, signed it with a few XOXO’s and then sent it off."
            "Done and done."
        "Encrypted Email (Medium)":
            $ tax_delivery = "EEmail"

            $ addonTime = 65
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ increment_show_security(securityLevel)
            "\"These are super sensitive documents, right?\" You thought to yourself."
            "I mean, your social security number is littered all over them."
            "So, of course they are sensitive!"
            "You want to take the extra time and precautions to make sure they get to your accountant safe."
            "You take an hour to set up a public and private key and to get the accountant’s credentials as well."
            "You then package all the files together, drop them into the email, put a secret message just for the accountant’s eyes, and then send them off."
            "What was written in that email, you ask?"
            "I have absolutely no clue. You are the one who wrote it."
            "Done and done."
        "Hand-Delivered (Long)":
            $ tax_delivery = "HDelivered"

            $ addonTime = 135
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ increment_show_security(securityLevel)
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

    $ fileTaxes = 0
    jump choices

label friends:
    "YES! "
    extend "The most socially invigorating thing on your todo list and you are about to embark on it."

    "Your friends have been planning this for ages."
    "First step on the agenda is to watch the latest and greatest movie in your friend groups absolute favorite movie series: {i}Love Comes Softly{/i}."
    "What can I say? \n"
    "You guys are all just a bunch of suckers for a good 'ol chick flick."
    "If you feel any confusion about that right now, just know that this is your life, not mine."
    "I can’t do anything about it."
    "If you are happy about it then... "
    extend "uh… "
    extend "good for you!"

    "Next you and your friends have a tickets to go spelunking in a cave not too far from where you live."
    "Absolutely stellar!"
    "So let’s get this party started!"

    "Let’s be honest."
    "Your crib is a little too small to chill with the dawgs."
    "So, you guys all opted to meet a few blocks down the road at one of your friend’s house who has a truly immersive 7-Dimensional theater system that allows you to enjoy your movie while being able to literally feel the emotions, smell the love, and experience the movie as if it was your own sad drama filled life."

    scene friends_house with dissolve
    $ create_menu_function(checkListDist)
    if second_group:
        $ show_security_level_function(securityLevel)

    "But when you get there, dreams are crushed and hopes are dashed against the harsh harsh rocks of cheapened reality."
    "Your friends never bought the movie! (Thanks, Obama!)"
    "Knowing you were going to watch this movie was literally the only thing keeping you going throughout the week."
    "You HAVE to watch it."
    "(Wow. You are really sad, aren't you?)"

    "After doing a couple of quick searches you are dismayed to find out that it was a direct-to-DVD (who woulda guessed?) and it was never released digitally."
    "You could go to the store to pick it up, but that would take time you are not sure you want to sacrifice."
    "However, you know they have it because you were able to check online first."
    "You could always pirate it and then buy it later the next time you go to the store."
    "You saw a great site in one of the comments of the trailer on YouTube that states you stream the movie from http://fb.me/7SxplnLq7."
    "That could work too."


    ###
    # SECURITY QUESTION 4
    ###

    menu:
        "What would you like to do?"

        "Drive to the store all willy-nilly (Long)":
            $ pirate_movie = False

            $ addonTime = 60
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ increment_show_security(securityLevel)
            "Driving to the store to pick it up doesn’t sound like a bad idea."
            "A long one, but maybe not so bad after you sit there and think about it for a bit."
            "You head to the store without a hitch and pick it up."
            "This pretty much makes you become, quite literally, the hero of your friend group (and not to mention the most responsible one. Way to!)"

        "Stream it from http://fb.me/7SxplnLq7 (Short)":
            $ pirate_movie = True

            $ addonTime = 5
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ decrement_show_security(securityLevel)
            "Eh. "
            extend "You decide that you can always buy the movie later and decide to just stream it from the website you found."
            "Within seconds, you and your friend’s eyes are dripping from the feels that are oozing out of the theater system."
            "Oh gross."
            "Come on, guys, hold yourself together!"

    $ addonTime = 135
    $ minutes += addonTime
    $ update_clock_function()
    $ display_adding_time_function()

    "You go through 7 tissue boxes. SEVEN."
    "That was some wild ride."

    "You and your friends spend a few minutes thinking about life, love, and love lost."
    "You could spend all day there."

    "HA! "
    extend "Who am I kidding?"
    "You guys are ready to go to the caves!!"
    "What’s a little emotional trauma when it comes to having fun?"

    "Get ready for a few hours of fun, adventure, darkness, and dankness."
    "It’s every kid aged 12-17’s dream!"

    "Everyone piles into your friend’s mom’s minivan."
    "There are punch holes in the ceiling, writing on the chairs, and an unidentifiable sticky substance underneath the cushions."
    "The word I would use to describe it is… "
    extend "quaint."

    scene cave with dissolve
    $ create_menu_function(checkListDist)
    if second_group:
        $ show_security_level_function(securityLevel)

    $ addonTime = 25
    $ minutes += addonTime
    $ update_clock_function()
    $ display_adding_time_function()

    "Luckily, the drive isn’t long, so you make it there in relatively good time."
    "You look upon the entrance to the cave from the window seat of the car."
    "You can immediately tell why the tickets were only $3.75 per head."
    "That entrance is tiiinnny."
    "Plus, the place looks madly abandoned."

    "Oh well."
    "Here we go!"

    "You all pile out of the decrepit minivan and begin to gather your equipment for the adventure."
    "Ropes, helmets with flashlights, and those little gummy fruit snacks shaped like a children’s show cartoon."
    "Yup, you have everything you need for a successful trip into the caves right there."

    "Now that you all are equipped for the adventure and the last tears have dried from the movie, you are all gung-ho to dive into the spelunking experience."
    "Your friends all begin to file into the cave with you bringing up the rear."

    $ addonTime = 20
    $ minutes += addonTime
    $ update_clock_function()
    $ display_adding_time_function()

    "As time passes, you get deeper and deeper into the earth."

    "You all come to a large opening within the earth where you can see half a mile in each direction."
    "Shall we say, it's a..."
    extend "DEEP experience?"
    "hahahahahahahahaha"
    "We have good times together, don't we?"
    "Anyways, one of your friends has the awesome idea for everyone to turn off their lights to see what pure pitch black is like."
    "It's the smallest things that amuse that poor boy."

    "So, in the same manner that all the lights came on, they slowly flicker off."
    "You take your helmet off and set it on a nearby stalagmite that you saw before the lights went off."

    "With all the lights off, your eyes start playing tricks on you and you start hallucinating all sorts of things: "
    extend "Chewbacca riding a sea turtle, "
    extend "a british bulldog with a top hat, "
    extend "and even all the Beatles wearing mustaches."
    "(Well, all except Ringo Starr -- you know why.)"
    "You start giggling to yourself (weirdo) and clearly the rest of your friends are seeing things to judging by their slight reactions to the darkness."

    "You take a step backwards and accidentally knock your helmet over."

    "The clanging can be heard for what feels like an eternity."
    "Your friends quickly grab their helmets and flick them on."
    "No fireflies this time."

    "You all look over the precipice that your helmet continues to fall into."

    #Possibly add sound effect?
    "CHBIKKG! "
    extend "It hit the unseen cave floor miles below where you are."

    "Well dang. "
    extend "Not only do you not have head protection anymore, but you are also missing a light."

    "You quickly pull out your phone, but realize that you deleted your flashlight app ages ago."
    "But wait."
    "What the heck?"
    "Seriously, what?"

    "For some bizarre reason you have data down here."
    "You don't even have data at your parent's house in Florida; Why the heck do you have it down here??"

    "Oh oh oh! I've got it!"
    "It must be the liquid on the stalactites that are boosting the signal or something."
    "Yeah. "
    extend "Uh. "
    extend "Let’s go with that."
    "It sounds science-y enough to be true, right?"

    "Either way, you have data and so you begin to download a new app miles below the earth."
    "What a time to be alive!"

    "However, the app asks for permission to use your microphone, camera, and your media and file storage."
    "It’s not blatantly clear why it needs those permissions, but you need the app if you don’t want to slow down the rest of your friends in the cave."

    ###
    # SECURITY QUESTION 5
    ###

    menu:
        "So, what do you do?"

        "Go ahead and download the app (Short)":
            $ download_app = True

            $ addonTime = 2
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ decrement_show_security(securityLevel)
            "Yeah, who cares about those permission needs anyways?"
            "Certianly not you, that's who!"
            "You’ll delete the app the second you get back up on solid ground, so what harm is there?"
            $ addonTime = 120
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "You find yourself having a blast throughout the rest of the caving adventure and actually find that you are able to see more things that you ever where able to before because of the versatility of having a light on your phone instead of your head."

        "Rely on your friends to get you through the rest of the trip (Long)":
            $ download_app = False

            $ addonTime = 145
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ increment_show_security(securityLevel)
            "It’s slow going, but decide to go ahead and trust your friends to guide you through the rest of the caves."
            "It actually becomes pretty fun after a while having everyone cater to you and look out for your best interest."

    "Before you know it, you find yourself climbing upwards instead of down."
    "Eventually you see a faint trace of light in the distance."

    "And just like that you all one by one squeeze out of a little crevice in the earth that leads back above ground."
    "Not too shabby. \n"
    extend "Not too shabby at all."


    $ addonTime = 35
    $ minutes += addonTime
    $ update_clock_function()
    $ display_adding_time_function()
    "You head back to your house after that grand adventure."
    "There was a little traffic this time, but it was no big deal."

    "It was a grand time over all and you glad you set aside the time to do it, even with it being one of the more time-costly things on your list."

    $ friends = 0
    jump choices

label homework:
    "Ah slave work. \n"
    extend "Er, I mean homework."

    "A necessary suffering to the college student’s life."
    "Unfortunately, you chose to have that suffering start right now."

    scene room_day with fade
    $ create_menu_function(checkListDist)
    if second_group:
        $ show_security_level_function(securityLevel)

    $ addonTime = 2
    $ minutes += addonTime
    $ update_clock_function()
    $ display_adding_time_function()

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
    extend "1. Pirate it \n"
    extend "2. Skip the homework and get a poor grade \n"
    extend "3. Keep searching"

    ###
    # SECURITY QUESTION 6
    ###

    menu:
        "What would you like to do?"

        "Pirate it (Medium)":
            $ homework_decision = "Pirate"

            $ addonTime = 20
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ decrement_show_security(securityLevel)
            "Ah sailing the high seas, are we?"
            "Well it looks like it worked out for you."
            "You found a site called freeepubsformoms.com and were able to get the textbook you needed."
            "Your mom would be incredibly proud!"

        "Skip it (Short)":
            $ homework_decision = "Skip"

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

        "Keep searching (Long)":
            $ homework_decision = "Search"

            $ addonTime = 90
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ increment_show_security(securityLevel)
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

        "Sure. Why not? (Long)":
            $ study = True

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

            ###
            # SECURITY QUESTION 7
            ###

            menu:
                "How do you want to send him your username and password?"

                "Text (Short)":
                    $ netflix_password = "Text"

                    $ addonTime = 5
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    $ decrement_show_security(securityLevel)
                    "You send him a hurried text."
                    "Quickly, you type out your username and password and click send."
                    "You don’t want to get distracted any more than you have to since you are kinda in the flow at the moment."

                "Email (Short)":
                    $ netflix_password = "Email"

                    $ addonTime = 15
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    $ decrement_show_security(securityLevel)
                    "Since it’s your brother, you decide you should at least give him the curtesy of sending him an email back with the info he needs."
                    "Plus, this way you won't get sucked into a conversation with him when you really just need to get back to work."
                    "You write the email as fast as you can, giving him your credentials, and then press send."
                    "You don’t want to get distracted any more than you have to since you are kinda in the flow at the moment."

                "Encrypted Email (Long)":
                    $ netflix_password = "EEmail"

                    $ addonTime = 60
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    $ increment_show_security(securityLevel)
                    "You decide and encrypted email is the way to go."
                    "Your information is important and you don’t want the Chinese to somehow get access to your precious Netflix account."
                    "They'd probably wreck all of the hours you’ve spent rating movies for better recommendations!"
                    "Honestly, you have nothing against dubbed movies, you’d just rather not have it plastered all over your feed."
                    "So you take the time to set up a public and private key and get your brother to do the same."
                    "It takes time and your brother got a little annoyed at you over the whole thing, but once you sent you username and password you know it was the safest option available."

                "Phone Call (Medium)":
                    $ netflix_password = "Call"

                    $ addonTime = 45
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    $ decrement_show_security(securityLevel)
                    "You decide just to call him up and give him the information over the phone."
                    "Hey, it’s your brother and you haven’t talked in a while so it only makes sense to do it this way."
                    "It really was a nice break from all of your hard work."
                    "Sure, you may have used a little more time this way, but you got to catch up with him and hear all about his recent crush on Rory Gilmore."
                    "Yup. It was something special."

                "Encrypted Call (Long)":
                    $ netflix_password = "ECall"

                    $ addonTime = 90
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    $ increment_show_security(securityLevel)
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

        "I'd rather not. What's a \"study\" anyways? (Short)":
            $ study = False

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

            ###
            # SECURITY QUESTION 7
            ###

            menu:
                "How do you want to send him your username and password?"

                "Text (Short)":
                    $ netflix_password = "Text"

                    $ addonTime = 5
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    $ decrement_show_security(securityLevel)
                    "You send him a hurried text."
                    "Quickly, you type out your username and password and click send."
                    "You don’t want to get distracted any more than you have to since you are kinda in the flow at the moment."

                "Email (Short)":
                    $ netflix_password = "Email"

                    $ addonTime = 15
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    $ decrement_show_security(securityLevel)
                    "Since it’s your brother, you decide you should at least give him the curtesy of sending him an email back with the info he needs."
                    "Plus, this way you won't get sucked into a conversation with him when you really just need to get back to work."
                    "You write the email as fast as you can, giving him your credentials, and then press send."
                    "You don’t want to get distracted any more than you have to since you are kinda in the flow at the moment."

                "Encrypted Email (Long)":
                    $ netflix_password = "EEmail"

                    $ addonTime = 60
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    $ increment_show_security(securityLevel)
                    "You decide and encrypted email is the way to go."
                    "Your information is important and you don’t want the Chinese to somehow get access to your precious Netflix account."
                    "They'd probably wreck all of the hours you’ve spent rating movies for better recommendations!"
                    "Honestly, you have nothing against dubbed movies, you’d just rather not have it plastered all over your feed."
                    "So you take the time to set up a public and private key and get your brother to do the same."
                    "It takes time and your brother got a little annoyed at you over the whole thing, but once you sent you username and password you know it was the safest option available."

                "Phone Call (Medium)":
                    $ netflix_password = "Call"

                    $ addonTime = 45
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    $ decrement_show_security(securityLevel)
                    "You decide just to call him up and give him the information over the phone."
                    "Hey, it’s your brother and you haven’t talked in a while so it only makes sense to do it this way."
                    "It really was a nice break from all of your hard work."
                    "Sure, you may have used a little more time this way, but you got to catch up with him and hear all about his recent crush on Rory Gilmore."
                    "Yup. It was something special."

                "Encrypted Call (Long)":
                    $ netflix_password = "ECall"

                    $ addonTime = 90
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    $ increment_show_security(securityLevel)
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
    if second_group:
        $ show_security_level_function(securityLevel)

    "When you get there, you dutifully peruse the pastries and exotic cheeses, gather the necessary ingredients for the strawberry lobster soufflé you’ve been dying to try, and moved towards the checkout counter."
    "You inch closer and closer in your line, until… "
    extend "shoot!"
    "You forgot that you bought that really expensive Smurf’s TV tray from ebay a few weeks ago and don’t have any money in your checking account!"

    "You pull out your phone to quickly make a transfer from savings into checking, but you don’t have data in this area."
    "One bad thing after another, huh?"
    "What a day."

    "Wait!"
    "Before you quit and all hope is lost, you notice that the store has a free unprotected WiFi hotspot!"
    "However, there is a slight snag."
    "When you navigate to your bank's webpage, out of the corner of your eye you notice a lack of a green padlock in the corner of the url."
    "You could still easily connect to it to make the transfer and be on your way."

    ###
    # SECURITY QUESTION 8
    ###

    menu:
        "What would you like to do?"

        "Transfer the money through the store's wifi (Short)":
            $ wifi_transfer = True

            $ addonTime = 7
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ decrement_show_security(securityLevel)
            "Definitely the quickest and most efficient option."
            "Who even knows what that little green thing in the url means anyways?"
            "You use your formidable intellect to determine that you would like to save time, money, and gas by just moving money over into your bank account."
            "Nice one!"
            "You continue to cruise through the checkout counter without skipping a beat and are soon out of the store before you know it with all the goat cheese your arms could carry."

        "Head back home, get some cash, come back to the store, and check out again (Long)":
            $ wifi_transfer = False

            $ addonTime = 100
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            $ increment_show_security(securityLevel)
            "You berate yourself as you carefully put all the cartful of goat cheese all back in its respective aisle in the store and climb back into your car to head home."
            "Sometimes you wonder why you go through so much trouble in order to be secure even when it would have just been a short transaction."
            "After the long drive back home, you grab the extra cash you store in the cookie jar in your kitchen, make a mental note to get cookies while at the store, and then head back out."
            "You are able to check out this time without too much trouble, but man, did you wish you hadn’t forgotten about your empty checking account earlier!"

    "You feel a little drained after that whole ordeal and actually feel a little exhausted."

    menu:
        "Would you like to head to the local coffee shop and snag some caffeine and crumpets?"

        "Heck yes! Pure caffeine is the foundation of America! (Long)":
            $ coffee_break = True
            $ arguing = False

            $ addonTime = 45
            $ minutes += addonTime
            $ update_clock_function()
            $ display_adding_time_function()
            "Coffee it is!"
            "You spend a little time heading over to your favorite StarDollars (hey, copyright infringement fees are expensive) and fill up on all sorts of caffeinated delights."
            "This will keep you going for the rest of the day for sure!"
            "You find yourself chanting \“Power to the People\” over and over again while you fist pump the air as you walk out of the coffee shop ready to finish your day."

        "I’m not really much of a coffee person. I’d rather not. (None)":

            menu:
                "But, but, but, are you sure??"

                "YES! Stop trying to force this on me!":
                    $ coffee_break = False
                    $ arguing = True

                    "Okay. :("
                    "Woah. \n"
                    extend "Now that I think about it, is this our first fight?"
                    "We need to recover from this right away."
                    "You know, I know a great psychiatrist that can help us push through this."
                    extend "TOGETHER!"

                    "Our relationship was formed on rock and roll and he can help us get back to those roots."
                    "I'm certain of it."

                    menu:
                        "Now just let me sign us up really quick..."

                        "NO!":
                            "Whaat?? Are you sure? I think we need this."
                            "The fact that you are rejecting this makes me believe we need it all the more."
                            "That's it. I'm calling Dr. Langeskov."
                            "He'll know what to do."
                            "...."
                            "uhhuh."
                            "hmm"
                            "yes?"
                            "okay."
                            "..."
                            "will do."
                            "thanks, Doc"
                            "You always know how to cheer me up."
                            "hahahaha no you hang up!"
                            "HANG UP GOSH DARN IT!"
                            "haha okay, bye!"
                            "*click*"
                            "Yup, that was the Doc alright."
                            "He wants us to tell a story together for some reason."
                            "Thank goodness that I have this script right here with every move you are going to make during the course of the rest of the day."
                            "We can totally live through it together!"
                            "I'll dictate and you listen/ help when needed while our love grows fonder."
                            "This is all for you now. \n"
                            extend "No one else."
                            "Let's get back into it, shall we?"

                        "You, my good sir, are a relationship wizard.":
                            "Wait. \n"
                            extend "You really think so?"
                            "Honest to goodness?"
                            "I think I'm going to cry."
                            "Yup. \n"
                            extend "Here it comes"
                            ":''''''''''''')"
                            "Those are tears of joy right there."
                            "I'm going to build you the best story ever from now on!"
                            "And you have my word on that (as well as my prewritten script!"
                            "*sniff* Just know I'm always here for you if you ever need me."

                    "So, I guess you decide caffeine really isn’t needed."
                    "You have so much moxxy that you are certain that you can get the rest of your list done on your current energy reserves."
                    "You feel proud that you know yourself and your limits so well. \n"
                    extend "(Wow, I think that was the most serious line in this whole game.)"

                "You're right! Coffee is now my favorite thing. Let's go! (Long)":
                    $ coffee_break = True
                    $ arguing = False

                    $ addonTime = 45
                    $ minutes += addonTime
                    $ update_clock_function()
                    $ display_adding_time_function()
                    "Coffee it is!"
                    "You spend a little time heading over to your favorite StarDollars (hey, copyright infringement fees are expensive) and fill up on all sorts of caffeinated delights."
                    "This will keep you going for the rest of the day for sure!"
                    "You find yourself chanting \“Power to the People\” over and over again while you fist pump the air as you walk out of the coffee shop ready to finish your day."


    "Mhmmmmm congrat on getting all that shopping done."
    "Now to make that totes delish, mhhhmmm, lobster soufflé of the strawberry variety (If you know what I mean.;) )"
    "But first you have to finish the rest of your chores, yo!"
    "No slackin' off just yet."

    $ shopping = 0
    jump choices

label ending:
    scene room_night with dissolve
    $ create_menu_function(checkListDist)
    if second_group:
        $ show_security_level_function(securityLevel)

    "Ah man."
    "What a day."
    "Am I right, or am I right?"

    if minutes <= 1110:
        "But woah!"
        "You did it!"
        "You did everything on your list and all with time to spare!"
        "Looks like I love you forever, huh? ;) ;) ;)"
        "Your following Monday morning was rocking with all that rest you got (and all the stuff you did!)"
        "Congrats!"
        "I knew you could do it."
        "xoxoxo <3"

    if minutes >= 1110:
        "But oooh... "
        "Tough luck"
        "It seems like you took an exorbitant amount of time to get your tasks done today."
        "I didn't want to do this, but you left me with no choice."

        show losing_face

        ":("

        hide losing_face

        "I'm so sorry."
        "That hurt me more than it hurt you. Promise."

        "I don't want to tell you what the consequences were on your following Monday morning for gettng to bed so late, but it wasn't pretty."
        "(for anyone)"
        "But hey! All is not lost."
        "You still did some good today."

    "Now let's see what decisions made up your day:"

    scene black with dissolve

    if first_sleep_in or second_sleep_in:
        if first_sleep_in and not(second_sleep_in):
            show text "You Slept In." at resultsPlace(xMain, yIncrement)
            show text "+30" at resultsPlace(xTime, yIncrement)
            $ yIncrement += .3
        if second_sleep_in and not(first_sleep_in):
            show text "You Slept In."
            show text "+30"
        if first_sleep_in and second_sleep_in:
            show text "You Slept In."
            show text "+60"
    # pet_type
    # pet_name

    if watch_tv:
        show text "You watched Little House on the Prarie"
        show text "+30"
    if update_phone:
        show text "You updated your phone to v1.1"
        show text "+30"

    if not(fileTaxes):
        if organize_desk:
            show text "You organized your messy desk"
            show text "+30"
        if not(click_popup):
            show text "You uninstalled Edgar's Love Trojan from your computer"
            show text "+30"
        if tax_delivery == "Email":
            show text "You delivered your taxes through email"
            show text "+30"
        if tax_delivery == "EEmail":
            show text "You delivered your taxes through an encrypted email"
            show text "+30"
        if tax_delivery == "HDelivery":
            show text "You hand delivered your taxes"
            show text "+30"

    if not(friends):
        if pirate_movie:
            show text "You chose to pirate the movie for your friends"
            show text "+30"
        if not(pirate_movie):
            show text "You chose to buy a copy of the movie for your friends"
            show text "+30"
        if download_app:
            show text "You downloaded the flashlight app"
            show text "+30"
        if not(download_app):
            show text "You had your friends guide you out of the cave"
            show text "+30"

    if not(homework):
        if homework_decision == "Pirate":
            show text "You pirated your textbook"
            show text "+30"
        if homework_decision == "Skip":
            show text "You skipped your homework for the day"
            show text "+30"
        if homework_decision == "Search":
            show text "You found your textbook (and your second pet) and completed your homework"
            show text "+30"
        if study:
            show text "You studied before you homework"
            show text "+30"
        if not(study):
            show text "You didn't study at all before your homework"
            show text "+30"
        if netflix_password == "Text":
            show text "You sent your netflix credentials to your brother through text"
            show text "+30"
        if netflix_password == "Email":
            show text "You sent your netflix credentials to your brother through email"
            show text "+30"
        if netflix_password == "EEmail":
            show text "You sent your netflix credentials to your brother through encrypted email"
            show text "+30"
        if netflix_password == "Call":
            show text "You sent your netflix credentials to your brother through a phone call"
            show text "+30"
        if netflix_password == "ECall":
            show text "You sent your netflix credentials to your brother through an encrypted phone call"
            show text "+30"

    if not(shopping):
        if wifi_transfer:
            show text "You transferred your cash through the wifi hotspot"
            show text "+30"
        if wifi_transfer:
            show text "You picked up some cash from home"
            show text "+30"
        if coffee_break:
            show text "You took a coffee break after shopping"
            show text "+30"
        if arguing:
            show text "You argued with me for awhile"
            show text "+30"

    if not(fileTaxes) and not(friends) and not(shopping) and not(homework):
        show text "You completed your whole checklist!!"

    "Fin."

    "One Second as I record all your data."

    $ file_ = open('/Users/justicejuraschek/Documents/School/Senior Year/Summer Research/Experiment Stuff/Renpy/Time TODO!/game/results/results.txt', 'a')
    $ file_.write("-------------------------------------------" + '\n')

    $ file_.write("---" + player_major + " ---" + '\n')

    $ file_.write("-------------------------------------------" + '\n')

    $ file_.write("Second Group: " + str(second_group) + '\n')

    $ file_.write("Security Level: " + str(securityLevel) + '\n')

    $ file_.write("Finish Time: " + str(minutes) + '\n')

    $ file_.write("----------------Decisions------------------" + '\n')

    $ file_.write("Introduction:------------------------------" + '\n')
    $ file_.write("Updated Phone: " + str(update_phone) + '\n')

    $ file_.write("Filing Taxes:------------------------------" + '\n')
    $ file_.write("Installed Trojan from Popup: " + str(click_popup) + '\n')
    $ file_.write("Delivered Taxes through: " + tax_delivery + '\n')

    $ file_.write("Friends:-----------------------------------" + '\n')
    $ file_.write("Pirated Movie: " + str(pirate_movie) + '\n')
    $ file_.write("Downloaded App: " + str(download_app) + '\n')

    $ file_.write("Homework:----------------------------------" + '\n')
    $ file_.write("Lost Book Decision: " + homework_decision + '\n')
    $ file_.write("Netflix Password Delivery: " + str(netflix_password) + '\n')

    $ file_.write("Shopping:---------------------------------" + '\n')
    $ file_.write("Bank Wifi Transfer: " + str(wifi_transfer) + '\n')

    $ file_.write("Did they argue with me? " + str(arguing) + '\n')

    $ file_.write("-------------------------------------------" + '\n')
    $ file_.write("-------------------------------------------" + '\n')

    $ file_.write('\n')
    $ file_.write('\n')
    $ file_.close()

    "I wrote all your data to a file called \"results.txt\" ."

    $ renpy.full_restart()

    return


return

# The splashscreen is called, if it exists, before the main menu is
# shown the first time. It is not called if the game has restarted.
#
#label splashscreen:
#     scene black
#     show text "Taylor University's Computer Science Department Presents..." with dissolve
#     $ renpy.pause(2.0)
#     hide text with dissolve(1)
#
#     return

init python:
    style.text.color = "#e08a2c"
    style.text.bold = True
    style.text.size = 27
