style vbox_spacing:
    xalign 0.5
    yalign 0.6
    spacing 80


default displayName = "anonymous"
screen my_menu(choice1,choice2,dest1,dest2):
    hbox:
        xpos 740
        ypos 968
        textbutton choice1 action Jump(dest1)
        textbutton choice2 action Jump(dest2)
screen profile_screen(displayName,companyName, conf):
    textbutton "{b}Log out{/b}" action Jump("ending") xpos 60 ypos 40

    vbox:
        xalign .130
        ypos 273
        text displayName size 30 color "#8e1401"
        text companyName size 20 color "#545454"

screen inputtext_screen():
    imagebutton:
        xpos 745
        ypos 968
        idle "text_input.png"
        hover "text_input.png"

screen login_screen():
    $ company = None
    vbox:
        style "vbox_spacing"
        text "Login" size 40 xalign .5

        hbox:
            spacing 80
            text "Display Name"
            input value VariableInputValue("displayName", returnable=True)

        hbox:
            spacing 80
            text "Company Name"
            vbox:
                textbutton "Uber" action Return((displayName, "Uber"))
                textbutton "Microsoft" action Return((displayName,"Microsoft"))
                textbutton "Google" action Return((displayName,"Google"))
                textbutton "LinkedIn" action Return((displayName,"LinkedIn"))
                textbutton "Apple" action Return((displayName,"Apple"))

screen lobby_start_new(visible, done):
    default selected = False
    default hover = None
    $ startingX = 840
    $ i = 0
    vbox:
        imagebutton:
            xpos 733
            ypos 163
            xsize 1005
            ysize 106
            if selected:
                idle "start_new_button_hover.png"
            else:
                idle "start_new_button_idle.png"
            hover "start_new_button_hover.png"
            action SetScreenVariable("selected", not selected)
        if selected:
            hbox:
                if visible[1] and not done[1]:
                    imagebutton:
                        xpos startingX
                        ypos 200
                        xsize 187
                        ysize 64
                        idle "culture.png"
                        hover "culture_hover.png"
                        action Jump("coworkers")
                        hovered SetScreenVariable("hover","culture")
                        unhovered SetScreenVariable("hover", None)
                else:
                    if done[1]:
                        imagebutton:
                            xpos startingX
                            ypos 200
                            xsize 187
                            ysize 64
                            idle "culture_cross.png"
                            hover "culture_cross.png"
                            action NullAction()
                            hovered SetScreenVariable("hover","culture_done")
                            unhovered SetScreenVariable("hover", None)
                    else:
                        imagebutton:
                            xpos startingX
                            ypos 200
                            xsize 187
                            ysize 64
                            idle "culture_cross.png"
                            hover "culture_cross.png"
                            action NullAction()
                            hovered SetScreenVariable("hover","culture_visible")
                            unhovered SetScreenVariable("hover", None)

                $ i += 1

                if visible[0] and not done[0]:
                    imagebutton:
                        xpos startingX + i*100
                        ypos 200
                        xsize 187
                        ysize 64
                        idle "projects_idle.png"
                        hover "projects_hover.png"
                        action Jump("work")
                        hovered SetScreenVariable("hover","projects")
                        unhovered SetScreenVariable("hover", None)
                else:
                    if done[0]:
                        imagebutton:
                            xpos startingX + i * 100
                            ypos 200
                            xsize 187
                            ysize 64
                            idle "projects_cross.png"
                            hover "projects_cross.png"
                            action NullAction()
                            hovered SetScreenVariable("hover","projects_done")
                            unhovered SetScreenVariable("hover", None)
                    else:
                        imagebutton:
                            xpos startingX + i * 100
                            ypos 200
                            xsize 187
                            ysize 64
                            idle "projects_cross.png"
                            hover "projects_cross.png"
                            action NullAction()
                            hovered SetScreenVariable("hover","projects_visible")
                            unhovered SetScreenVariable("hover", None)

                $ i += 1
                if visible[2] and not done[2] and not done[3]:
                    imagebutton:
                        xpos startingX + i*100
                        ypos 200
                        xsize 235
                        ysize 64
                        idle "management.png"
                        hover "management_hover.png"
                        action Jump("manager")
                        hovered SetScreenVariable("hover","management")
                        unhovered SetScreenVariable("hover", None)
                else:
                    if  done[2] or  done[3]:
                        imagebutton:
                            xpos startingX + i*100
                            ypos 200
                            xsize 235
                            ysize 64
                            idle "management_cross.png"
                            hover "management_cross.png"
                            action NullAction()
                            hovered SetScreenVariable("hover","management_done")
                            unhovered SetScreenVariable("hover", None)
                    else:
                        imagebutton:
                            xpos startingX + i*100
                            ypos 200
                            xsize 235
                            ysize 64
                            idle "management_cross.png"
                            hover "management_cross.png"
                            action NullAction()
                            hovered SetScreenVariable("hover","management_visible")
                            unhovered SetScreenVariable("hover", None)


        if hover == "culture":
            imagebutton:
                xpos 742
                ypos 279
                idle "culture_preview.png"
                hover "culture_preview.png"
        elif hover == "projects":
            imagebutton:
                xpos 742
                ypos 279
                idle "projects_preview.png"
                hover "projects_preview.png"
        elif hover == "management":
            imagebutton:
                xpos 742
                ypos 279
                idle "management_preview.png"
                hover "management_preview.png"
        elif hover == "projects_done":
            text "I already tried bringing this topic up." xpos 1042 ypos 250
        elif hover == "projects_visible":
            text "I don't feel comfortable bringing this up." xpos 1010 ypos 250
        elif hover == "management_done":
            text "I already tried bringing this topic up." xpos 1362 ypos 250
        elif hover == "management_visible":
            text "I don't feel comfortable bringing this up." xpos 1342 ypos 250
        elif hover == "culture_done":
            text "I already tried bringing this topic up." xpos 742 ypos 250
        elif hover == "culture_visible":
            text "I don't feel comfortable bringing this up." xpos 742 ypos 250
