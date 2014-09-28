# game starts here

define limbaugh = Character('?', color="#6633cc")
define Limbaugh = Character('Limbaugh', color="#6633cc")

image bg house = "opening_house.png"
image bg book = "book.png"
image bg open_book = "open_book.png"
image bg clearing = "clearing.png"

define dreamer = None
define he = None
define him = None
define his = None
define He = None
define Him = None
define His = None

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

    jump clearing_forward

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
                He = "He"
                Him = "Him"
                His = "His"
            
        "She":
            python:
                he = "she"
                him = "her"
                his = "hers"
                He = "She"
                Him = "Her"
                His = "Hers"

        "They":
            python:
                he = "they"
                him = "them"
                his = "their"
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
    "foo"

label walk_without_rest:
    "bar"