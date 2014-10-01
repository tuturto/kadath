# game starts here

define limbaugh = Character('?', color="#6633cc")
define Limbaugh = Character('Limbaugh', color="#6633cc")

define simbali = Character('?', color="#6633cc")
define Simbali = Character('Simbali', color="#6633cc")

define fairies = Character('other fairies', color="#33cccc")

image bg house = "opening_house.png"
image bg book = "book.png"
image bg open_book = "open_book.png"
image bg clearing = "clearing.png"
image bg mushrooms = "mushrooms.png"

define dreamer = None
define he = None
define him = None
define himself = None
define his = None
define He = None
define Him = None
define His = None

define ate_pie_with_limbaugh = False

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
                his = "hers"
                himself = "herself"
                He = "She"
                Him = "Her"
                His = "Hers"

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
    with your big feets as you trampled through the meadow."

label walk_without_rest:
    "bar"