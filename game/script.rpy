# game starts here

define limbaugh = Character('?', color="#6633cc")
define Limbaugh = Character('Limbaugh', color="#6633cc")

define simbali = Character('?', color="#6633cc")
define Simbali = Character('Simbali', color="#6633cc")

define fairies = Character('other fairies', color="#33cccc")

define Chkakuth = Character('Chkakuth', color="#cc6633")

image bg house = "opening_house.png"
image bg book = "book.png"
image bg open_book = "open_book.png"
image bg clearing = "clearing.png"
image bg mushrooms = "mushrooms.png"
image bg limbaugh_img = "limbaugh.png"
image bg pie = "pie.png"
image bg forest_road = "forest_road.png"

define dreamer = None
define he = None
define him = None
define himself = None
define his = None
define He = None
define Him = None
define His = None

define ate_pie_with_limbaugh = False
define white_pearls = False
define black_pearls = False

label start:
    scene bg house
    with dissolve

    "There was a child, who lived in a house with mother and father. They were
    happy together and while they were not rich, they didn't lack anything
    important."

    scene bg book
    with dissolve

    "In the bookshelf, there was a strange book that the child had never seen
    anyone to read. It was very thick and bound in old leather. While the
    child didn't know its age for sure, the book looked really old."

    "One night, the sleep wouldn't come. The house was completely quiet and
    not even sounds of cars could be heard. The child sat up and listened
    carefully. Not a single sound could be heard. Tiny feet tapped over
    floor and sunk into carpet of the living room. A chair was moved against
    the bookself without a sound."

    "A scraping sound could be heard when the book was removed from the
    bookshelf, followed by the quick patter of feet as the adventurer retreated
    after a succesful raid."

    scene bg open_book
    with dissolve

    "The child was hunched over the book, the blanket was used to provide cover
    while a flashlight provided light needed for reading. The house was
    completely silent and nobody could have guessed that something had
    happened."

    "The book opened and revealed old, ink stained pages. The book was actually
    written by hand and not printed by a printing press. The child found this
    very fascinating. Writing a thick book like this must have taken a very
    long time. The child could not yet read, but just looking those old pages
    filled with strange looking writing was fun."

    "In some pages there were hand drawn pictures. Some of them showed strange
    landscapes, while others depicted fantastical creatures. Page after page
    was turned and each of them was intensively studied. Small eyelids started
    to get heavy as night slumbered slowly forward, but bravely the child kept
    awake and continued through the book."

    menu:
        "Your eyes are really heavy and you feel drowsy. Should you"

        "Put book away and sleep":
            "TODO: description of going to sleep"
            jump clearing_night

        "Read just a little bit more":
            jump clearing_morning

label clearing_night:
    "TODO: clearing at night arc"
    return

label clearing_morning:
    scene bg clearing
    with dissolve

    "The child jolted up. When the drowsiness took over, the book had fallen
    on the grass. It laid there, pages open, with a picture of a road. That
    very same road that started from somewhere behind the child, continued
    all the way to the book and through the open pages and then journeyed
    onward. Around the child grassy clearing was bordered with a gnarled
    looking trees and sun shine didn't reach under the canopy of the trees."

    "The child stood up, look to both directions and wondered what should be
    done and which way would be the correct direction. Of course there was
    also an option of just sitting down and waiting. Maybe somebody would
    soon pass by and tell what this strange place was. There was also the old
    book that could be read while waiting for a person to come."


    menu:
        "What would be the best course of action?"

        "Continue forwards into the forest":
            jump clearing_forward

        "Follow road to other direction":
            jump clearing_backwards

        "Wait here":
            jump clearing_wait

label clearing_backwards:
    "TODO: clearing backwards"
    return

label clearing_wait:
    "TODO: clearing wait"
    return

label clearing_forward:

    "The child pondered and thought and pondered some more. Waiting would be
    the easiest choice and the book would keep company. But waiting felt wrong.
    The whole new world was there waiting to be explored. All the new places
    and people waited to be discovered. If everyone just sat down and waited,
    nothing would happen at all. And if nothing would happen at all, the world
    would be very boring place."

    "The child stood up and picked up the book, closing the pages. The book
    couldn't stay here, it had to be returned on the bookshelf. Otherwise
    mother and father would know that it was taken from there and that
    probably wouldn't be a good thing."

    "The road continue into the forest and sun light soon disappeared behind
    canopy of the trees. The forest was quiet, but not completely silent.
    One could hear small creatures rustling in underbush and fluttering of
    winged creatures up in the trees. It seemed though, that they were trying
    to stay away from sight of this new traveller who was stranger in these
    lands."

    scene bg mushrooms
    with dissolve

    "After a while of walking, it was time to stop and rest. The child sat
    under some large mushrooms that were growing next to the road. All that
    walking had resulted into a hunger, but how would one go about solving
    that? Big mushrooms could probably be eaten, but what if they were
    poisonous? One shouldn't eat strange mushrooms, that much have been taught
    to the child."

    limbaugh "Well, well, what do we have here? Who is sitting here all alone
    under some old and worm eaten mushrooms?"

    scene bg limbaugh_img
    with dissolve

    "The child looked up. A strange creature was standing couple steps away
    from the mushrooms. How it had managed to sneak there without being
    noticed was a mystery unto itself. The creature had long legs like a crane,
    long beak and its body was covered in rags and dozens of small bags. Bright
    and wise eyes blinked from under bushy eye brows."

    limbaugh "I think, that you are a stranger in these lands. I haven't seen
    like you before and your garb is not familiar either. Hold on a second
    and let me to introduce myself properly."

    "The creature bowed deep and made a fancy looking flourish with its hat.
    Then it stood straight again and continued."

    Limbaugh "I'm called Limbaugh. That is of course not my real name, but I
    never tell my real name to strangers. And you would do well, if you would
    keep yours secret too. Knowing real name of something grants one certain
    power of that thing. I know, you should pick yourself a new name. A name
    that you will be known around these parts."

    python:
        dreamer = renpy.input("What should I call you?")
        dreamer = dreamer.strip()

        if not dreamer:
            dreamer = "Simon"

    Limbaugh "It is my pleasure to meet you [dreamer]."

    Limbaugh "If you forgive me, I'm not entirely sure how should I address
    you. I haven't met anyone like you before, therefore, I don't know the
    proper salutations and such. Would you be kind and tell me, how should
    one address you?"

    menu:
        "I would like to be addressed as"

        "He":
            python:
                he = "he"
                him = "him"
                his = "his"
                himself = "himself"
                He = "He"
                Him = "Him"
                His = "His"
            
        "She":
            python:
                he = "she"
                him = "her"
                his = "her"
                himself = "herself"
                He = "She"
                Him = "Her"
                His = "Her"

        "They":
            python:
                he = "they"
                him = "them"
                his = "their"
                himself = "themself"
                He = "They"
                Him = "Them"
                His = "Their"

    Limbaugh "Very well, I shall do so [dreamer]. Thank you for your patience
    with this old bird."

    Limbaugh "Now that we have been properly introduced, I can continue. Like
    I said, I'm called Limbaugh. I live here and there, currently more here
    than there, as you can see. I wander quite a bit and sell small trinkets to
    whoever I happen to encounter. I may not be rich, but I'm free as a bird."

    "Limbaugh chuckled a little bit. He apparently found the pun clever and
    quite funny. Then he straightened his face."

    Limbaugh "You seemed hungry to me when I saw you sitting under the
    mushrooms. It looked like you were almost ready to take a bite from them.
    I would advice against doing that however, these mushrooms aren't
    particularly tasty."

    scene bg pie
    with dissolve   

    Limbaugh "All is not lost though, I have remains of a very delicious
    mushroom pie in one of my bags. Would you like to share it with me
    before I have to continue onward?"

    menu:
        "What should I do about the pie?"

        "Eat the pie with Limbaugh":
            jump eat_pie_with_limbaugh

        "Politely refuse":
            jump do_not_eat_pie_with_limbaugh

label eat_pie_with_limbaugh:
    $ ate_pie_with_limbaugh = True

    "Limbaugh rummaged through his various bags and soon produced half a pie
    that smelled delicious. He cut it into two and offered the other half
    to [dreamer], while starting to eat his half."

    Limbaugh "Remember, around here things aren't always what they seem to be
    and generally it's a good idea to be careful around strangers. You do have
    a dream book with you though, which is a good thing. Just never lose it and
    things will turn out just fine in the end."

    Limbaugh "My grand-father, may the wind be soft for him, was fond of saying
    that 'Everything will be fine in the end, if something is not fine, then
    it is not the end yet.' I think it's not that simple always, but the old
    man had a good idea there still."

    Limbaugh "But now I must continue my journey. I'm on my way to meet
    Baroness Zhukovsky and shouldn't be late. If you continue this road for
    a while still, you'll arrive to a friendly village where you can get more
    food and place to sleep."

    "[dreamer] watched as Limbaugh stood up, collected his bags and after
    counting them twice, started walking. Curiously, he didn't follow the
    road, but continued directly into shadowy woods."

    scene bg forest_road
    with dissolve

    "Soon the forest was quiet again. One could still hear rustling and flapping
    of small creatures here and there, but that was all. [dreamer] looked around
    and then stood up. [He] started walking the road again, wondering how long
    it would take [him] to arrive that friendly village Limbaugh had mentioned."

    "Walking was easy. The road was even and there were no big hills or other
    obstacles in the way. The mushroom pie had driven the hunger away and [he]
    was on a cheerful mood. [dreamer] was starting to get tired though and
    yawned couple of times. Warm weather and silent forest didn't help at all
    either. [He] was determined to make to that village before the dark and
    pressed onwards."

    "Eventually [dreamer] arrived to a clearing. The road continue straight and
    just barely edged the clearing. [He] could hear sound of a small stream
    coming from somewhere near, although it was nowhere to be seen. The ground
    was covered in tall grass and flowers of all colours. [dreamer] thought that
    the stream couldn't be far away and was probably just hidden by flowers."

    "Sweet scent of flowers was tantalizing and [he] could see some big
    butterflies flying among them. Would a short stop here to rest hurt that
    much? [He] could use some cool water to drink too. [dreamer] didn't know
    how far the village was and if [he] would make it there before dark,
    especially if [he] would rest here for a bit."

    menu:
        "Should [dreamer] take a short rest here?"

        "Yes, rest for a bit":
            jump drowsy_clearing

        "No, keep going":
            jump walk_without_rest

label do_not_eat_pie_with_limbaugh:
    "No pie!!"

    return

label drowsy_clearing:
    "[dreamer] stepped from the road and started walking into the clearing. Tall
    flowers soon surrounded [him] from every direction. Sun was shining warmly
    and butterflies were flying amidst the flowers. [He] could hear buzzing of
    the bees too. The air was very sweet from the scent on colourful flowers
    and [dreamer] stopped couple of times to smell them."

    "As [he] walked further, the sound of stream started getting stronger.
    Eventually [dreamer] arrived on bank of a small stream that was flowing
    merrily between round rocks. [dreamer] sat down by the bank, removed [his]
    shoes and let stream run over [his] sore toes. The water was very cold,
    but [he] found it pleasing after a long walk. [dreamer] closed [his] eyes
    and enjoyed feeling of arm sun shine and cool water."

    "[He] started nodding. Warm and comfortable drowsiness spread over [him]
    and made [his] limbs heavy and eye lids droopy. It would be easy to just
    stretch out in the long grass and take a short nap. [His] head felt heavy
    and [dreamer] wanted nothing more than just nap in the grass and enjoy
    scent of the flowers."

    menu:
        "Should [dreamer] sleep here?"

        "A little sleep wouldn't hurt anyone":
            jump nap_in_clearing

        "Sleeping wouldn't be a good idea":
            jump stay_awake_in_clearing

label nap_in_clearing:
    "Grass felt soft and comfortable as [dreamer] stretched [himself] across
    the ground. [He] watched the clouds drifting on the sky, but then [his] eye
    lids felt too heavy and [he] had to close them. Very soon [dreamer] was in
    a deep sleep as flowers and butterflies were guarding [him]."

    "[dreamer] was dreaming of sweet smelling flowers of all colours and big
    butterflies that were flying amidst them. Sound of the stream could be heard
    somewhere not too far away and it sounded almost like distant chatter of
    people. [He] strirred and tried to listen to more closely. It was not just
    [his] imagination, the stream did sound like people chattering."

    "Now [dreamer] was struggling in order to hear better. Sounds were so close
    that [he] could almost understand what they were talking. Suddenly [dreamer]
    woke up and stood to a sitting position, looking around and realised that
    [he] was surrounded with small, winged creatures that were the source of
    chattering [he] had heard in [his] dream."

    jump fairy_folk_in_clearing

label stay_awake_in_clearing:
    "Staying awake"

label fairy_folk_in_clearing:
    simbali "Hey, big folk! What are you doing here, snoring like an old bear?
    We can barely hear our own thoughts and I'm sure all the birds of the forest
    have gone deaf and are not going to sing in a while."

    "Tiny winged creatures were sitting on flowers and in grass. Some were
    flying around and all of them were chattering busily with each other. It
    seemed that most of their talking was to comment loud snoring of the
    stranger or [his] unfashionable and dull clothes. [dreamer] tried to follow
    them all with [his] eyes, but soon gave up and focused only on the one what
    had been talking to [him]."

    simbali "This clearing is home of the fairy folk and we don't like when
    big folk come stomping and crushing here. You are loud and impolite and
    troublesome in general. Big folk can travel on their hard and boring road,
    but the clearing and flowers are domain of fairy folk."

    Simbali "I'm known as Simbali and I'm captain of the guard. And you are
    here without our permission. Be glad that you didn't stomp over any houses
    with your big feets as you trampled through the meadow. You are to come
    with us, so a due justice can be administered."

    fairies "[He] will trample our homes and crush all the beautiful flowers!"

    Simbali "That is true, we can't let you cause any havoc in our beautiful
    meadow. I'll arrange this."

    "Simbali started flying around [dreamer] and threw multicoloured dust at
    [him] while singing a strange melody. First, nothing seemed to happen, but
    then [dreamer] felt small tingling. The tingling started from [his] spine
    and spread up and down from there. Flowers and grass around [him] seemed
    to grow and soon they were high above [his] head."

    "[dreamer] kept shrinking and shrinking, until [he] was the same size as
    the fairies. Other fairies giggled as they flew around confused [dreamer].
    From [his] new vantage point, high grass looked like tall trees and
    butterflies were like big birds."

    Simbali "That's much better. Now you can come with use without fear of
    crushing a house or trampling down an innocent fairy. But walking back to
    our town would take too long now. We need to get you a ride."

    "Upon Simbali's request, a large monarch butterfly landed nearby. [dreamer]
    climbed on its back off they went. [He] was holding very tightly and barely
    dared to peek down. The butterfly followed fairies, as they left the stream
    and headed deeper into the meadow."

    "Soon they landed on a large clearing. [dreamer] realized that even if the
    clearing looked large, in reality it was relatively small. Everything just
    looked so much larger from [his] current point of view. Colourful houses
    were surrounding the clearing. Some of them were on the ground, while others
    were hanging from the flowers and grass."

    Simbali "This is our town. As you can see, if you had wandered here you
    could have easily stepped on our houses without noticing them at all. This
    is also where we will decide a proper judgement for you. You may sit down
    in the shade over there as we have our meeting."

    "[dreamer] sat down on a small twig and watched as fairies gathered in the
    clearing. [He] couldn't hear clearly what the fairies were talking, but
    clearly they were quite agitated. Time passed and the sun was rising
    higher. At some point a fairy bought [him] something to eat. Eventually
    fairies seemed to reach a conclusion and they parted to different
    directions. [dreamer] stood up as Simbali walked towards [him]."

    Simbali "We have come to a conclusion and will give you an opportunity
    to redeem yourself. Not long time ago, a treasure was stolen from us and
    we wish to get it back. While we know where it is, we can't retrieve it by
    ourselves. This is where you come into the picture. If you can retrieve the
    treasure and return it to us, we will let you go."

    Simbali "However, if you choose not to perform this task or fail trying it,
    you will be imprisoned until we decide otherwise."

    "[dreamer] didn't really have any options. Simbali had cast a spell on [him]
    and [he] was in captivity in their town. Escaping seemed impossible, so
    [dreamer] agreed to perform the task."

    Simbali "Good, I knew that you would be reasonable. The task is rather
    simple. We need you to retrieve a bag of pearls that was stolen from us by
    a group of thunder beetles. They have a hive on the other side of the
    river and we know its location. But because the hive is underground, we
    can't enter it and retrieve the pearls by ourselves."

    Simbali "A butterfly will take you near the hive and wait you there. The
    excact details on how you will get the pearls is up to you, but I would
    advice you to avoid the beetles as much as possible. They are vicious folk
    and your story will surely be at end if they catch you."

    "A butterfly was summoned and after a brief flight [dreamer] found herself
    standing in the long grass. The butterfly was resting on a large hosta and
    watching [him] as [he] slowly started walking to the direction where the
    hive was supposed to be."

    "[dreamer] was full of doubts. [He] certainly was not a fighter and didn't
    really have an idea how to approach the problem. This was something entirely
    different than raiding [his] parents' cookie jar in the night. [He] felt a
    little sting of home sickness in [his] chest and wondered what mother and
    father were doing anyway and if they had already noticed that [he] had
    disappeared somewhere."

    "Soon [he] arrived to what had to be the hive. There was a large mound of
    soil that had a hole on the side. Wide stairs lead down under the earth.
    [dreamer] could see that there had been lot of traffic going in and coming
    out, but currently there were no movement to see."

    "After gathering [his] courage for a bit, [dreamer] snuck to the stairs and
    looked down. Spiraling stairs were illuminated by luminuous fungi that was
    growing on the walls and ceiling. Heavy hanging air smelled like damp
    ground and moist roots."

    "[dreamer] started descending the stairs, stopping now and then to listen.
    As [he] proceeded deeper and deeper under the ground, the sun light was
    replaced with pale glow of the fungi. [He] heard faint chittering in the
    distance that grew stronger further [he] progressed."

    "Eventually [dreamer] arrived to an opening that let into a big cavern. [He]
    could see large beetles sleeping here and there in the cavern, with few of
    them wandering about the cavern. They were large, dark coloured and
    generally menacing looking. In the middle of the cavern [he] could see
    a bag of pearls on a big table."

    "[dreamer] started to think what would be the best way to get the pearls.
    [He] could sneak in and try to steal them. That might work since most of the
    beetles seemed to be asleep. [He] could also just charge in and try to scare
    them away. Third option was the scariest one, just walk in and ask if [he]
    could take the pearls and return them to the fairies."

    menu:
        "How should [dreamer] try to solve the problem?"

        "Sneak in and steal the pearls":
            jump steal_pearls

        "Charge in and try to scare beetles":
            jump charge_hive

        "Walk in and ask to have the pearls":
            jump negotiate_with_beetles

label steal_pearls:
    "stealing"

label charge_hive:
    "Charge!"

label negotiate_with_beetles:
    "[dreamer] was hesitant, but [he] thought this would be the best course of
    action. [His] throat was try and [his] hands were trembling as [he] stepped
    into the cavern. After [dreamer] had taken couple of steps, the beetles
    spotted [him]. As [he] walked towards them [dreamer] heard chittering and
    clattering as more and more beetles were woken and alarmed."

    "Large beetles were surrounding [him] now. [dreamer] hoped that [he] hadn't
    done a mistake when [he] decided to try and reason with them. A large and
    differently coloured beetle slowly walked on front of [him]. It towered far
    above [dreamer] and could easily crush [him] any moment. [dreamer] tried to
    speak, but [his] throat was completely dry."

    Chkakuth "I am king Chkakuth, leader of the thunder beetles and ruler of
    this hive. Who are you and why have you intruded into our tunnels?"

    "[dreamer] had to tried twice, before [he] could answer. With a trembling
    voice [he] explained that [he] had been sent by the fairies to retrieve the
    pearls that had been taken from them and asked if the beetles would be so
    kind and give them to [him]."

    "[His] explanation raised a roar of chittering from the beetles. For a
    moment [dreamer] feared that [his] life would end at this very instant, but
    then the king Chkakuth silenced the beetles."

    Chkakuth "You are either very brave or very stupid to walk in here and
    demand that we hand over the pearls. They are spoils of war, rightfully ours
    by the might of the thunder beetles. If those fairies want them back, they
    can come and get them by themselves!"

    "Chkakuth's speech raised an approving storm of beetle chittering.
    Eventually it died down and [dreamer] could continue. This seemed like a
    crucial moment, fail here and [his] mission would fail."

    menu:
        "How should [dreamer] approach this?"

        "Ask if the beetles could trade the pearls for something":
            jump offer_trade

        "Ask if the beetles would rather have peace":
            jump offer_peace

label offer_trade:
    "offer trade"

label offer_peace:
    "[dreamer] cleared [his] throat and asked if the beetles would rather live
    in peace with the fairies. It seemed to [him] that there would be enough
    space for both of them on the meadow, because fairies lived on top of it and
    the beetles lived underneath. Maybe some compromises would have to be done
    here and there, but [he] was sure that they could work it all out in the
    end."

    Chkakuth "We have been in war with the fairies as long as we can remember.
    They try to drive us away from the meadow and we are trying to do the same.
    We can't just simply say that 'lets forget all this and be friends.' It
    does not work that way."

    "[dreamer] noticed that some of the beetles weren't as enthuastic as before
    and even Chkakuth seemed tired. [He] offered to help with the negotiations.
    They could start slowly and first cease fighting and then try and find out
    a way that everybody could continue living at the meadow."

    "Chkakuth was silent for a very long time. [dreamer] was already getting
    worried that [his] plan wouldn't work after all, but then Chkakuth spoke and
    broke the silence."

    Chkakuth "Very well, we accept your offer. But don't take us as fools that
    you can trick. At the first sign of treachery the agreement is broken and
    we will return to war with fairies. Until then, you have the word of the
    thunder beetles that we won't be attacking the fairies."

    Chkakuth "You may take the pearls that the fairies sent you to retrieve. But
    in return we would like our pearls to be returned to us. They are like
    these, but instead of being white, they are all black. Fairies will know
    what I talk about if you ask them. They took those pearls from us in force.
    A guard will escort you back to the surface."

    "Chkakuth turned and slowly walked away. Other beetles started scattering
    to different directions. Lighter coloured beetle handed [dreamer] the bag
    of pearls and started escorting [him] towards the surface. This new beetle
    spoke very little and soon [dreamer] gave up trying to ask more question."

    "After ascending in silence for a while, [dreamer] started notice how light
    was changing. Pale glow of fungi was slowly replaced with the warn sun shine
    and [his] spirits rose as [he] could see the blue sky above [his] head
    again. [dreamer] turned to thank the beetle, but it had already retreated
    back into the hive."

    "[dreamer] retraced [his] steps back to the butterfly, who was more than
    happy to take off and leave the vicinity of the hive. [He] was clutching the
    bag of pearls during the whole flight, worried that they would drop and get
    lost in the tall grass."

    $ white_pearls = True

    jump fairy_town

label fairy_town:
    "Back in the fairy town, there was a huge gathering of fairies waiting for
    [him]. Loud murmuring rose from the crowd as the butterfly landed and
    [dreamer] stepped down, holding the bag of pearls."

    Simbali "I have to admit, you are more resourceful than you look like. How
    did you manage to get the pearls back?"

    menu:
        "What should [dreamer] say?"

        "Tell about the trade and peace offering":
            jump tell_peace_offering

        "Lie that you snuck in and stole them":
            jump lie_about_sneaking_in

label lie_about_sneaking_in:
    "[dreamer] decided that even when [he] had agreed to help to trade
    the pearls between fairies and the beetles, it wouldn't work in the end.
    Now was [his] chance to spin some yarn and make a good impression on
    the fairies. Who knows, maybe [he] could even ask to have one or two
    pearls as a token of friendship."

    "[dreamer] told an impressive story of how [he] had first silently
    sneaked inside the hive and after considerable effort located the pearls.
    There were at least twice as many beetles in [his] story that had been
    in the hive and most of them were awake. Somehow, [he] had still had
    managed to stay in the shadows and patiently sneak to the pearls."

    "[His] story continued as [dreamer] explained that as soon as [he] had
    the pearls in [his] custody, a beetle had noticed the missing pearls and
    an alarm had been sounded. If [dreamer] had not been so crafty and stealthy,
    [he] surely would have been caught. But in the end [he] had snuck out of
    the hive and now [he] was here with the pearls."

    "Fairies were listening to [his] story silently. In particularly exciting
    parts somebody might let out a small gasp, but other than that all the
    fairies were silent. They clearly admired how skillful and clever [dreamer]
    was. Only Simbali seemed to be unaffected by the story, [dreamer] was
    wondering if the fairy guessed that [he] wasn't telling the truth."

    "When the story was over, everyone were silent for a while and started at
    Simbali. Eventually the fairy spoke with a steady voice that didn't reveal
    an emotion."

    Simbali "You have fulfilled your part of the deal. We will now fulfill our
    part. First you are escorted at the edge of the meadow, where there are no
    fairies or houses to trample on. Then a spell will be cast upon you that
    will return you back to your normal size. After that you are free to go."

    Simbali "You did well. It was not an easy task to retrieve the pearls from
    the hive of the thunder beetles. However, in the future, you would do
    well to avoid wandering on the meadow again. This time you were lucky and
    managed to avoid the judgement. Next time might not be so easy anymore."

    $ white_pearls = False

    jump leaving_town

label tell_peace_offering:
    "[dreamer] starts telling how [he] entered the hive and what transpired
    within it. When [he] arrived to the part where deal was made to trade
    the pearls, Simbali's face turned dark. Regardless of that [dreamer]
    continued, until the story had been told."

    Simbali "You were sent to retrieve the pearls and not to trade away our
    treasures. However, fairies keep their word, unlike certain earth digging
    beetles. I will have a squad to deliver the black pearls to the hive. We
    can always get them back later with force."

    Simbali "You have fulfilled your part of the deal. We will now fulfill our
    part. First you are escorted at the edge of the meadow, where there are no
    fairies or houses to trample on. Then a spell will be cast upon you that
    will return you back to your normal size. After that you are free to go."

    Simbali "You didn't do too badly. I just wish that we wouldn't have to hand
    over those pearls that are in our possession. In the future, you would do
    well to avoid wandering on the meadow again. This time you were lucky and
    managed to avoid the judgement. Next time might not be so easy anymore."

    $ white_pearls = True

    jump leaving_town

label leaving_town:
    "Simbali turned away and left. [dreamer] was given a butterfly to fly and
    soon enough [he] and few fairies that were escorting [him] were again at
    the edge of the meadow. [dreamer] stepped down and closed [his] eyes as
    one of the fairies started throwing the colourful dust at [him]."

    "[dreamer] felt the familiar tingle that started from [his] spine and spread
    over the whole body. As [he] opened [his] eyes, fairies were nowhere to be
    seen and [he] was again looking flowers from the above, not from the down."

    "[dreamer] looked at the meadow one more time and then turned to continue.
    The friendly village was somewhere in front of [him]. It occurred to [him]
    that it would have been a good idea to ask the fairies if they knew anything
    about it. Although [dreamer] had a feeling that the fairy folk didn't often
    leave the meadow, if ever at all."

label walk_without_rest:
    "bar"

label arriving_to_village:
    "arrive to village"
