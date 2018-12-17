# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nm = Character("New Member*Hkljgft", kind=nvl)
define net = Character("Netflix*LukeCage", kind=nvl)
define intel = Character("Intel*DSPN81", kind=nvl)
define micro = Character("Microsoft*Mit2k", kind=nvl)
define splunk = Character("Splunk*Trim", kind=nvl)
define chealth = Character("Collective Health*FaceAnd", kind=nvl)
define amaz = Character("Amazon*Jeff Bezos", kind=nvl)
define tab = Character("Tableau*hellish", kind=nvl)
define gust = Character("Gusto*Itni80", kind=nvl)
define goog = Character("Google*JPpr12", kind=nvl)
define mapr = Character("MapR Technologies*!Lazvgdu", kind=nvl)
define upstart = Character("Upstart*imherenow", kind=nvl)
define emc = Character("EMC*WeAreVenom", kind=nvl)
define exp = Character("Expedia*Meliodas", kind=nvl)
define appl = Character("Apple*Ymxqz02", kind=nvl)
define jac = Character("Jacobs*Poc", kind=nvl)
define visible = [True, True, True]
define done = [False, False, False, False]
# define narrator = nvl_narrator

# define displayName = None


# The game starts here.

label start:

    # 0 = gettinng less work
    # 1 = fit it with cowrkers
    # 2 = stalker mannager
    # 3 = manager comment
    $ cross = 0
    $ companyName = ""
    $ conf = 5
    $ minConf = 2
    show login
    call screen login_screen()
    $ (displayName,companyName) = _return
    define m = Character("[companyName]*[displayName]", kind=nvl, color="#8e1401")
    define cn = Character("[companyName]*Un1dela", kind=nvl)
    define mono = Character(None, what_color="#ffffff")

    define menu = nvl_menu

    # menu:
    #     # $ gui.text_color = #ffffff
    #     "Which company do I work for?"
    #     # $ gui.text_color = #000000
    #
    #     "Google":
    #         $ companyName = "Google"
    #     "Apple":
    #         $ companyName = "Apple"
    #     "Uber":
    #         $ companyName = "Uber"
    #     "Amazon":
    #         $ companyName = "Amazon"
    #     "Microsoft":
    #         $ companyName = "Microsoft"



    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.
    # Intro to problems/choose problems

    # "I've been working in the tech industry for 2 years now."
    #
    # "There are a lot of things I like about the industry, but there are also many things I've been struggling with that are hard to talk about."
    #
    # "I didn't feel comfortable talking about these problems with my manager or co-workers."
    #
    # "I want to appear as a strong-willed individual. I don't want to show my vulnerability."
    #
    # "I don't want to be judged."
    #
    # "I came across this online anonymous chatroom recently, I think it would be a good idea to consult other individuals working in the tech industry. <show image: chatroom for techies>"
    hide login
    jump startMenu

label dialogueUncomfortable():
    hide screen profile_screen
    show dialogue
    with dissolve
    mono "I don't feel comfortable talking about this anymore."
    hide dialogue
    with dissolve
    show screen profile_screen(displayName, companyName, conf)


label main_menu:
    return

label startMenu:
    show lobby
    show screen profile_screen(displayName, companyName, conf)

    if conf <= 3 and True in visible and False in done:
        $ mapped = []
        $ i = 0
        while i < len(visible):
            if visible[i] and not done[i]:
                $ mapped.append(i)
            $ i += 1
        if len(mapped) > 0:
            $ delete = renpy.random.choice(mapped)
            $ visible[delete] = False

    call screen lobby_start_new(visible, done)


label manager:


    show management_chat
    show screen inputtext_screen()
    nvl clear

    m "I feel uncomfortable around my manager. I've been trying everything to transfer to a different team."

    goog "What does your manager do to make you feel uncomfortable? Many companies will allow team transfers as long as you talk to HR about it."

label managerMenu:
    hide screen inputtext_screen
    menu:
        "Talk about what happend this morning":
            jump managerComment
        "I already tried everything":
            jump managerStalker



label managerComment:
    show screen inputtext_screen
    m "Today while we were eating lunch in the break room, he said to me \"May I ask you a question? Are your breasts real? Because, wow!\""

    micro "Yeah, talk about the horrible threat of retaliation when men have their careers destroyed by lying women. Poor you. Lol."

    micro "Keep in mind all these cases have yet to reach court. There was a Canadian tv host with 6 women accusing him"

    micro "turns out he kept emails and text messages for last 15-20 years. All accusations were easily dismissed as there were proof the women were willing. His career was still destroyed."

    micro "I also don’t hear you talk about women who sexually harass men. In most states the law doesn’t even consider it as a legal possibility."

    chealth "I don't think your manager meant it offensively. Seems like a light-hearted joke. Don't take it personally."

    $ conf -= 4
    $ done[3] = True

    jump managerCommentMenu

label managerCommentMenu:
    hide screen inputtext_screen
    menu:
        "Talk about how it keeps happening" if conf >= minConf:
            jump managerStalker
        "{s}Talk about how it keeps happening{/s}" if conf < minConf:
            call dialogueUncomfortable from _call_dialogueUncomfortable
            jump managerCommentMenu
        "Leave this chat":
            hide management_chat
            jump dialogueManagerCommentBad

label dialogueManagerCommentBad:
    hide screen profile_screen
    show dialogue
    with dissolve
    nvl clear
    mono "If I can't even get some sympathy here, how will I be able to gain support if I bring the issue to higher ups?"
    mono "Most of the people here won't even consider this as sexual harrasment."
    mono "I can still remember the way my manager looked at me when he made that comment."
    mono "I never wanted to ruin anyone's career, but that doesn't mean I want mine to be ruined."
    hide dialogue
    with dissolve
    show screen profile_screen(displayName, companyName, conf)
    jump startMenu


label managerStalker:
    show screen inputtext_screen


    m "My manager has been constantly harassing me. There has been multiple offenses."

    cn "[companyName] as a mature company takes such issue very seriously. Hope you brought the case to HR and skip."

    m "I took it to skip, he was transferred for a few months then came back again..."

    m "He blocked my transfer to a different team (different location), things escalated from there, he didn’t directly say anything to me after that but magically appeared everywhere I went"

    m "which is quite odd considering that hadn’t happened before. He made friends with the guy that lived in the same complex as me and started showing up “bumping” into me in the lobby."

    m "I consulted a lawyer, who told me that given the lack of evidence I didn’t have much of a legal avenue-his first proposition was when we were alone, though I could get restraining order"

    m "which would make it very awkward work wise."

    cn "Something is fishy with your story - a manager at [companyName] can’t block a transfer - you don’t even have to tell them until you accept."

    cn "If you got a really bad review, with 0 rewards, you are unable to transfer without VP approval, but that’s company policy, not your manager’s."

    cn "Also, if something like this was reported to HR, I guarantee they’d take action."
label managerStalkerMenu:
    hide screen inputtext_screen
    menu:
        "Back yourself up!" if conf >= minConf:
            jump manager2

        "{s}Back yourself up!{/s}" if conf < minConf:
            call dialogueUncomfortable from _call_dialogueUncomfortable_1
            jump managerStalkerMenu

        "Leave this chat":
            $ conf -= 4
            $ done[2] = True
            hide management_chat
            jump dialogueManagerStalkerBad
label dialogueManagerStalkerBad:
    hide screen profile_screen
    show dialogue
    with dissolve
    nvl clear
    mono "No one believes me."
    mono "I have no reason to make up these stories."
    mono "My manager is someone who has the power and ability to influence other higher ups."
    mono "Is it so hard to believe that these higher ups can guarentee which team I get placed into regardless of written rules?"
    mono "This is exactly why HR turned away from the situation."
    hide dialogue
    with dissolve
    show screen profile_screen(displayName, companyName, conf)
    jump startMenu

label manager2:
    show screen inputtext_screen
    m "I wanted the transfer within a few months of joining. The other team manager contacted him, he gave me terrible feedback effectively putting a stop to it."

    m "Things did not go well despite my efforts. I don't know what I have done to invite the unwanted attention"

    cn "It can happen anywhere. I think the sexism most women experience is more subtle. Unless you have incontrovertible evidence, it is officially illegal, and you will get no assistance."

    $ cross = 1
    $ conf -= 2
    $ done[2] = True
    hide screen inputtext_screen
    menu:
        "Back to Discussion Board":
            hide management_chat
            jump dialogueManagerStalkerGood

label dialogueManagerStalkerGood:
    hide screen profile_screen
    show dialogue
    with dissolve
    nvl clear
    mono "They finally stopped attacking me."
    mono "Do I need to provide every little piece of evidence just for people to believe my story?"
    mono "Whether it is now or when I brought it up to HR, seems like people are constantly poking holes in my story."
    mono "Why is there more doubt in the victim than the harasser?"
    hide dialogue
    with dissolve
    show screen profile_screen(displayName, companyName, conf)
    jump startMenu

label coworkers:
    nvl clear
    show culture_chat
    show screen inputtext_screen()

    m "I have been experiencing unconscious bias from my co-workers, and I am not sure how to confront them about it"

    m "For example, I have been told I am where I am because \"I work harder than my peers\" (male counterparts) as if I cannot be naturally \"good\" at software engineering"

    chealth "What a joke. So someone is giving you a literal compliment and you're taking it the wrong way because feminists told you to believe that everyone is unconsciously biased."

    amaz "Some people believe in talent, others don't. Get over yourself."

    tab "I think you are taking it the wrong way, your bias appears to be showing. It's of course entirely possible that others around you are biased that women aren't able to be engineers."

    tab "But that compliment by itself doesn't imply anything to me. It just says you are the hardest worker there."

    gust "Why does everything got to be a thing. If someone told me I work harder than my peers I'd take it as a compliment."

    chealth "Exactly. It's brainwashing. People are being trained to look for oppression in everything."

    gust "Let me guess, if they said you were naturally talented they'd be sexist for implying you don't work hard."

    chealth "Yep lmao"

    goog "Umm I've been told the same thing and I'm a male. :| I don't think this is unconscious bias. They could be just referring to how fast you've grown compared to others."

label coworkerMenu:
    hide screen inputtext_screen
    menu:
        "Back youself up!" if conf >= minConf:
            jump coworker2
        "{s}Back yourself up!{/s}" if conf < minConf:
            call dialogueUncomfortable from _call_dialogueUncomfortable_2
            jump coworkerMenu
        "Leave this chat":
            $ conf -= 2
            $ done[1] = True
            hide culture_chat
            jump dialogueCultureBad

label dialogueCultureBad:
    hide screen profile_screen
    show dialogue
    with dissolve
    nvl clear
    mono "No one seems to understand my point. Am I thinking too much into it?"
    mono "Seems like people enjoy accusing me more than trying to understand my situation..."
    hide dialogue
    with dissolve
    show screen profile_screen(displayName, companyName, conf)
    jump startMenu

label coworker2:
    show screen inputtext_screen
    m "Sure, saying \"I work harder than my peers\" is usually a compliment. But that's not my point.."

    m "I meant the way it was said implied that engineering wasn't something I could be good at naturally"

    m "As if I HAVE to work harder than my peers, because it is a \"man's field\""

    micro "These comments show why American women are avoiding engineering jobs and also unconscious bias she guessed. Bingo, @[displayName], these folks just confirmed your thought"

    emc "Lot of bias against women. Look at the number of anti-diversity trolls from prestigious companies like Amazon, Google, and Microsoft."

    chealth "What does anti diversity mean? No one is against having different genders and races in the workforce."

    chealth "However, we are against have set quotas whereby less qualified people are hired simply because of their gender."

    mapr "@[displayName] Do you work harder than other team members? If not, let them know. Confront them, be bold."

    amaz "I started noticing the unconscious bias when my team added more women... and often the bias comes from other women."

    amaz "I see it mostly in communicating double standards (men are \"assertive\", women are \"demanding\" or \"bossy\") and more strongly from men who have stay-at-home wives."

    upstart "Don't worry about such things. Only losers bring others down to satisfy their own inferiority."

    $ cross = 1

    $ conf += 2

    $ done[1] = True

    hide screen inputtext_screen
    menu:
        "Back to Discussion Board":
            hide culture_chat
            jump dialogueCultureGood

label dialogueCultureGood:
    hide screen profile_screen
    show dialogue
    with dissolve
    nvl clear
    mono "I'm not the only one who felt this way. I need to be bolder at work and let myself be heard!"
    mono "I'm glad there are people out there who are supportive."
    mono "Those few words really made a difference."
    hide dialogue
    with dissolve
    show screen profile_screen(displayName, companyName, conf)
    jump startMenu
label work:
    nvl clear

    show projects_chat
    show screen inputtext_screen()

    m "Have you ever felt like you were given less significant work or your contributions were treated as less important due to your gender?"

    micro "How did you arrive at this conclusion? Why do you choose to adopt the victim mentality instead of attempting to get an actual answer? Did you even try talking to your manager?"

    nm "Remember you got in just because you are a woman."

    net "@Hkljgft You're a loser."

    nm "It is the truth. Women have a lower bar in hiring committee. Do you deny that?"

    nm "I am a new grad and I know a lot of my batch mates getting calls from FANG and getting into FANG just because they are female."

    nm "I know for a fact a lot of guys are wayyyyy smarter than them but still couldn’t clear the interviews."

    nm "yea keep hiring women. If @[displayName] can express herself saying she is not being treated well because of her gender so can I."

    net "You’re a new grad, so you know nothing. I’ve never seen a woman get an easy interview in 10 years of experience interviewing candidates."

    net "You should really STFU and take accountability for your own inability to succeed instead of taking things out on women who have actually worked hard to get hired."

    nm "@Luke Cage looks like everybody hires/promotes of actual talent (you included) why is @[displayName] having problems."

    nm "If someone was hired because of talent he/she will be promoted or given a good project because of talent."

    nm "Nobody should complain and put the blame on gender then"

    nm "Let everyone take accountability for their “inability”"

    nm "@[displayName] sorry for being rude. But if that’s really the case you should just look for another job"

    intel "Without a doubt there is strong preference for hiring women in tech as long as they aren’t a complete moron."

    intel "Speaking as a manager, that’s what HR tells you to do, that’s what your management tells you to do. It’s virtually impossible to hire a white male externally."

    intel "The question of whether that is in shareholders interest is a different question."

    net "@DSPN81 Speaking as a black man and a manager, that’s simply not true. I don’t care what color or gender a candidate is. If they can code, that’s who I hire."

    net "I source my own candidates. I’ve never been a “diversity hire”."

    net "We’re encouraged to avoid ONLY hiring people with backgrounds exactly like ours."

    net "That means that instead of hiring the usual classmates and colleagues that all reflect pools of our individual bias, we reach out and search based on skills and experience."

    net "I’ve never been told to not hire a qualified white male for being white in my professional career. Stop spreading misinformation."

    net "you should apply to work at Netflix, our culture filters those toxic managers out and promptly lets them if they somehow make it through."

    micro "@Luke Cage just because it is not true for you, doesn’t mean it is not true for the Intel manager."

    net "It’s not prevalent on an institutionalized and systemic level....the way racism and sexism are."

    net "Implying that giving non whites and non males a chance by encouraging people to look outside their personal networks is “racist” against whites or “sexist” against men is a giant false equivalence."

    intel "@Luke Cage - that’s great, but not my experience. It’s prevalent and institutionalized at my company."

    intel "When I first became a manager I questioned whether that was a wise policy and the response was, “Welcome to being a manager.” Wish it was like how you describe in your experience."

    intel "Do you think that perhaps as a minority HR or management censors their speech around you?"

    # intel "We are also the company whose CEO supposedly slept with our Chief Diversity Officer who was given a $300M budget to go increase our workforce diversity"
    #
    # intel "and are getting sued for firing a bunch of old (white, male) employees two years ago, so could be a one-off f’d up culture and mores."
label workMenu:
    # show screen my_menu("back yourself up", "Leave this chat", work2, startMenu)
    hide screen inputtext_screen
    menu:
        "Clarify what you mean!" if conf >= minConf:
            jump work2
        "{s}Clarify what you mean!{/s}" if conf < minConf:
            call dialogueUncomfortable() from _call_dialogueUncomfortable_3
            jump workMenu
        "Leave this chat":
            $ conf -= 2
            $ done[0] = True
            hide projects_chat
            jump dialogueProjectsBad

label dialogueProjectsBad:
    hide screen profile_screen
    show dialogue
    with dissolve
    nvl clear
    mono "This is really going off topic."
    mono "I don't think this Hkljgft person has ever considered the possibility that there could be bias at work??"
    mono "My whole point is trying to point out that there is bias when it comes to assigning projects."
    mono "But instead I get attacked for being a bad engineer?"
    hide dialogue
    with dissolve
    show screen profile_screen(displayName, companyName, conf)
    jump startMenu


label work2:
    show screen inputtext_screen
    m "My question isn't even about hiring, rather it is about getting work/projects that are significant and being treated as a valuable asset to the team."

    m "Many times I am excluded in meetings that I'm supposed to be in, and I almost never get a chance to speak during meetings since they're always talking over me"

    m "I've taken it up with my manager and the tech leads have noticed it as well and brought it up with business group, but they don't seem to change."

    exp "Something I do is actively search and find significant things to do even outside of my current team. Though prepare to be labeled aggressive."

    appl "Amazing responses above. Ask a question, get told you are incompetent & that there are no problems to address?"

    appl "@[displayName] could be male, the question could get a response from men who feel they are treated differently, and the question wasn't even about hiring."

    appl "It's possible for hiring to be just fine (or favorable) and then for the actual experience to be less than favorable at work."

    appl "@[displayName] I haven't seen this on my team, I would say that the women have more significant work on average but not because of gender"

    jac "Absolutely brown women in tech are not there because anyone respects our capability or our knowledge and we certaily will not be allowed to do anything of importance"

    jac "unless we scream loudly while wavering our degrees from ivy leagues and vast experience compared to the straight white guys with high school educations who have been given the keys to the kingdom"

    jac "Yes I have been given far less significant work, but it has given me time to work on my doctorate and other things that matter to me :)"

    $ cross = 1
    $ done[0] = True
    $ conf += 2
    hide screen inputtext_screen
    menu:
        "Back to Discussion Board":
            hide projects_chat
            jump dialogueProjectsGood

label dialogueProjectsGood:
    hide screen profile_screen
    show dialogue
    with dissolve
    nvl clear
    mono "I'm glad I wasn't the only who felt this way. I was really starting to doubt myself."
    mono "I never thought I was the top engineer on the team, but I always had some confidence in my coding skills."
    mono "After being attacked so much here, I was really starting to feel like maybe I am the one who is unworthy of getting important work."
    hide dialogue
    with dissolve
    show screen profile_screen(displayName, companyName, conf)
    jump startMenu


    # This ends the game.

label ending():
    hide screen profile_screen
    hide screen inputtext_screen
    show dialogue
    with dissolve
    mono "Regardless of whether it is in person or online, I will still get accused and attacked."
    mono "These comments are hurtful and can really be traumatiizng."
    mono "I don't see how discrimination can get better if people won't even believe in the victims."
    mono "It just became so much harder to defend myself and talk about my problems the moment I started getting negative responses."
    return
