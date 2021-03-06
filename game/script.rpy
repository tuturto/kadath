# game starts here

define limbaugh = Character('?', color="#6633cc")
define Limbaugh = Character('Limbaugh', color="#6633cc")

define simbali = Character('?', color="#6633cc")
define Simbali = Character('Simbali', color="#6633cc")

define fairies = Character('other fairies', color="#33cccc")

define Chkakuth = Character('Chkakuth', color="#cc6633")

define baker = Character('Baker', color="#3366cc")
define keeper = Character('Keeper', color="#3366cc")
define cutter = Character('Cutter', color="#33cc33")

define black_cat = Character('black cat', color="#336666")
define red_cat = Character('red car', color="#cc3333")

define sprite = Character('?', color="#cccccc")
define Sprite = Character('Sprite', color="#cccccc")

image bg house = "opening_house.png"
image bg book = "book.png"
image bg open_book = "open_book.png"
image bg clearing = "clearing.png"
image bg mushrooms = "mushrooms.png"
image bg limbaugh_img = "limbaugh.png"
image bg pie = "pie.png"
image bg forest_road_bg = "forest_road.png"
image bg meadow_bg = "meadow.png"
image bg stream_bg = "stream.png"
image bg simbali_bg = "simbali.png"
image bg fairy_town_bg = "town.png"
image bg trial_bg = "trial.png"
image bg white_pearls_bg = "white_pearls.png"
image bg high_grass_bg = "high_grass.png"
image bg hive_bg = "hive.png"
image bg central_hive_bg = "central_hive.png"
image bg king_beetle_bg = "king_beetle.png"
image bg prison_bg = "prison.png"
image bg village_bg = "village.png"
image bg outside_village_bg = "outside_village.png"

image bg dragon_nest_bg = "dragon_nest.png"
image bg dragon_faceoff_bg = "dragon_faceoff.png"

image bg unicorn_bg = "unicorn.png"

image bg cats_marketplace = "cats_at_marketplace.png"

define dreamer = None
define he = None
define him = None
define himself = None
define his = None
define He = None
define Him = None
define His = None

define met_limbaugh = False
define ate_pie_with_limbaugh = False
define visited_clearing = False
define white_pearls = False
define black_pearls = False
define delivered_bread = False
define stayed_in_inn = False

define chose_day = True

define night_mushrooms = False
define dragon_eggs = False
define visited_dragons = False
define visited_unicorns = False
define mediate = False
define solve_alone = False
define divide_meadow = False

define harvest_with_humans = False
define harvest_without_humans = False

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
            jump clearing_night

        "Read just a little bit more":
            jump clearing_morning

label clearing_night:
    $ chose_day = False

    "The child yawned again. The book was really intersting and there were so
    many pages left to look at still. But it would probably be the best to
    stop here and continue some other time. The child had one more look at the
    current page and then closed the book carefully. After placing the book on
    the night table, the child pulled blanket tighter and tried to sleep. Soon
    the room was quiet, save for the sound of sleep."

    "The child woke up in grass. Stars were lit high in the sky and dark trees
    surrounding the grassy clearing. Night was quiet, but full of sounds. All
    the creatures that slept during the day were on the move and taking care
    of their nightly business. The child sat up and looked around."

    sprite "Hello there stranger, are you lost?"

    "The child spun around and saw a translucent being that had been standing
    there silently. It seemed to change the shape all the time and it was
    hard to see the details. But the child concluded that this was some sort
    of human looking spirit."

    Sprite "No need to be afraid dear child. I'm night sprite and completely
    harmless being. I wander between dusk and dawn and look that everything
    is as it should be in the dream world."

    Sprite "I have not seen you before and I know most if not all the beings
    that wander in these parts of the land. What should I call you? Do you
    know a particularly nice name that you would like to have?"

    python:
        dreamer = renpy.input("What do you want to be called?")
        dreamer = dreamer.strip()

        if not dreamer:
            dreamer = "Simon"

    Sprite "Pleasure to meet you [dreamer]."

    "As they shook hands, the child was suddenly alarmed. Both of them had
    same translucent appearance. Before the child could panic more, Sprite
    continued."

    Sprite "Do not be alarmed. We are in a dream and that means that things
    can get a bit strange now and then. But that also means that you can
    be something that you aren't in the waking world. Or you can be the same
    thing that you're in the waking world. The choise is yours."

    menu:
        "I would like to"

        "be a boy":
            python:
                he = "he"
                him = "him"
                his = "his"
                himself = "himself"
                He = "He"
                Him = "Him"
                His = "His"
            
        "be a girl":
            python:
                he = "she"
                him = "her"
                his = "her"
                himself = "herself"
                He = "She"
                Him = "Her"
                His = "Her"

        "not choose":
            python:
                he = "they"
                him = "them"
                his = "their"
                himself = "themself"
                He = "They"
                Him = "Them"
                His = "Their"

    "As soon as [dreamer] had made [his] choice, [he] felt [his] body to turn
    more solid. Looking at [his] hands, [dreamer] still could see through
    them, but at least they were more defined now."

    Sprite "Much better. Since we can be anything in dream, you need to first
    decide what you are, before others can see you properly. Some do that
    instinctively, some need to do it on a more conscious level."

    Sprite "Like I said earlier, I'm night sprite and wander around to see
    that things are generally as they should be. Sort of general handyperson
    you see. You could tag along and I'll show you around. There are plenty
    of things to see during night."

    "[dreamer] thought that this sounded like a good idea and agreed. Who
    knows, how often [he] would have an opportunity to travel around in
    company of such a guide. And so they set to travel in the night. Sprite
    was leading the way and [dreamer] was following right behind."

    "Their journey took them along the road and into the woods. They passed by
    some large mushrooms that were standing by the roadside. Sprite stopped
    and examined them closely."

    Sprite "These mushrooms are favoured resting place for travelers. They
    offer shelter from rain and shade from sun. Sometimes hungry travelers
    have idea to try and eat them. That's why I'm stopping here and checking
    that they have not been eaten too much. Small bites the mushrooms can
    heal, but with bigger ones they need my help."

    Sprite "What do you think you would do? If you were traveling here alone
    and were hungry when arriving to these mushrooms, would you take a bite?"

    menu:
        "Would [dreamer] eat mushroom?"

        "Yes, [he] would":
            jump would_eat_mushroom

        "No, [he] wouldn't":
            jump would_not_eat_mushroom

label would_eat_mushroom:
    Sprite "I can't blame you, the mushrooms look quite tasty. If you feel
    hungry, I have some excellent mushroom pie that a friend of mine made. You
    could have some of it."

    "Night sprite produced piece of pie seemingly out of thin air and handed
    it over to [dreamer], who accepted it. The pie was very delicious and
    [dreamer] guessed that it was probably made with penny buns. [He] ate the
    slice with good appetite."

    $ night_mushrooms = True

    jump forest_road_at_night

label would_not_eat_mushroom:
    Sprite "That's nice of you not to eat these mushrooms. Like I said, they
    can heal small cuts and bites, but bigger portions need my help to heal.
    Seems though that we're in luck this time and nobody hungry has been
    snacking here."

    Sprite "However, if you do get hungry later on during our journey, do let
    me know. I have some excellent mushroom pie that a friend of mine made. We
    could share that."

    jump forest_road_at_night

label forest_road_at_night:
    Sprite "Lets continue our journey, there's still a lot to do and see."

    "[dreamer] and night sprite walked along the road in silence for a while.
    After passing a particularly large oak, night sprite turned and headed
    into forest. [dreamer] had some difficulty following, since [he] wasn't
    accustomed to walking in dark woods."

    "Soon [he] noticed red glow further in the woods. It grew stronger as they
    closed and [dreamer] thought that it must be a campfire. But when they
    arrived to it, [he] realised that it was not a regular campfire."

    scene bg dragon_nest_bg
    with dissolve

    "On the sandy ground there was a small pit, carefully lined with small
    pebbles. Ground around it had been cleaned of leaves and twigs. In the
    pit lay several large eggs that were glowing red. The air around was hot
    and dry."

    Sprite "This is a dragon's nest. Those eggs are hot, so be careful and
    don't touch them. You would just burn yourself."

    Sprite "Dragons are rare and I have been coming here every night to see
    that that the eggs are safe, while parents are out hunting for food. Not
    that many creatures would dare to touch the eggs in the first place. But
    aren't they beautiful?"

    menu:
        "What do you think?"

        "Yes, they are beautiful":
            jump beautiful_eggs

        "I'm sort of scared, should we leave?":
            jump scared_of_eggs

label beautiful_eggs:
    "[dreamer] nodded. [He] hadn't seen anything like this before and the
    sight captivated [him]. Tiny pattern that covered the eggs seemed to
    shift and move, depending on the direction [he] looked at it."

    Sprite "We shouldn't stay here too long though. Dragons don't look kindly
    to other creatures that wander too close to their nest. They know me, but
    you are a stranger to them. Maybe in the future I'll ask them if they
    would permit you to be introduced to them."

    $ dragon_eggs = True

    jump fairy_meadow

label scared_of_eggs:
    "While the eggs looked fascinating, [dreamer] found it hard to concentrate
    onto them. They were dragon eggs and this was a dragon nest. Which meant,
    that somewhere in the darkness there were two large dragons. [dreamer] had
    never met one and [he] intended to keep it that way."

    Sprite "I know, dragons are big and scary. They know me, so I should be
    safe even if they would suddenly return. You are a stranger to them
    though, so they might be angry if they surprised us here. I might be able
    to talk senses to them still, they're fairly intelligent creatures."

    jump fairy_meadow

label fairy_meadow:
    Sprite "But lets continue. Everything is in order here. Our next stop is
    not far and we should arrive there in no time."

    "Like before, night sprite walked first and [dreamer] followed. They
    returned back to road and continue walking down it. While they were
    walking, night sprite told [dreamer] stories of things that had happened
    in the woods."

    "Soon they arrived to a meadow and stood still on the edge of it."

    Sprite "This is domain of fairies and thunder beetles. We should not
    wander too far from the road, as they don't take kindly on large folk
    trampling through their meadow."

    "Night sprite pointed some tiny light that were dancing in the air. And
    asked if [dreamer] could see them."

    Sprite "Those are fairies, they are having a banquet tonight it seems.
    They like to dress in colourful clothes and carry tiny lanters while
    flying around. They're easy to mistake as fireflies, if you don't know
    what you're looking at."

    Sprite "If you listen closely, you can hear a small stream that is flowing
    though the meadow. On the other side of it live thunder beetles. They're
    hard working creatures and have built a big underground kingdom there."

    Sprite "Unfortunately fairies and thunder beetles don't get along with
    each other at all. They are constantly raiding and fighting. To me it
    seems that fairies are worried that thunder beetles will build tunnels
    under their houses and make a surprise attack from there."

    Sprite "Thunder beetles are wary of the fairies, because fairies can fly
    and them can't. The stream is no obstacle to fairies, who can easily fly
    over it and make a surprise attack anytime."

    Sprite "I have been wondering if something should be done about the
    matter, but haven't yet decided anything."

    menu:
        "What do you think?"

        "Let them solve it alone":
            jump meadow_solve_alone

        "Somebody should mediate":
            jump meadow_mediate

        "Meadow could be divided to two":
            jump meadow_divide

label meadow_solve_alone:
    "Night sprite looked at the dancing lights in the meadow again. His face
    was frowned and he was silent for a long time."

    Sprite "You are probably right. This is something that they need to solve
    by themselves. Outsiders meddling witht them would just complicate things
    and make it harder for them to find a solution."

    Sprite "It's just so frustrating to watch them to repeat same mistakes
    over and over again. I think that there is hope still though. There are
    some young fairies and thunder beetles who have grown tired of constant
    fighting and have been secretly been discussing with each other. Maybe
    they can change the course of history."

    Sprite "But lets not spend all night here, worrying about things that we
    can't help right now. There is still one more stop that we need to do
    tonight and night is growing old. Soon the sun will rise and I will need
    to rest until next night."

    $ solve_alone = True

    jump night_village

label meadow_mediate:
    "Night sprite nodded in agreement. His face was sad and suddenly he looked
    much older and frailer than before."

    Sprite "I want to believe that there would be a peaceful solution to this.
    But sometimes it's really hard to keep believing when no progress is being
    made at all. But if you too think that mediating is the answer, maybe I'm
    not wrong after all. We'll see.."

    Sprite "But the time for that is not now. Soon perhaps, but not now. Next
    we'll continue our journey and visit one more place before it's time for
    me to rest until next dusk."

    $ mediate = True

    jump night_village

label meadow_divide:
    Sprite "I have thought of simply dividing the meadow in two, probably
    along the stream. One side would be for fairies and another side would be
    for thunder beetles. Neither would have no business at all on the other
    side."

    Sprite "That is almost the current situation anyway. Somebody would be
    needed to guard the stream though and that somebody would have to be
    neutral, trusted by both sides. Or at least equally hated by both sides."

    Sprite "This is such a sad state of affairs. The meadow is big enough
    for both of the sides, yet they constantly fight over it. I'm not very
    hopeful currently."

    Sprite "We need to continue our journey now. Night is getting old and dawn
    is drawing close. Soon I have to retire and rest until the next dusk.
    There's still one more place to visit tonight."

    $ divide_meadow = True

    jump night_village

label night_village:
    "Night sprite and [dreamer] once again continued their journey. The mood
    was much somber now and the cheerfulness seemed to be gone. As they walked
    in silence, [dreamer] was thinking of fairies and thunder beetles and
    their constant quarrel."

    Sprite "Are you thinking of what we talked at the meadow?"

    Sprite "It's sad, but maybe you should forget it for a moment."

    Sprite "Our last stop will be at a friendly village that lies on the other
    side of the forest. It will be a much happier place to visit and it might
    cheer you up again. In any case, we're not going to solve the trouble in
    fairy meadow tonight, so better not to worry about it all the time."

    "As they talked, the forest had started to grow thin and soon they were
    walking between fields. Night was silent and moon had risen. Fields around
    them were bathed in silvery light and [dreamer] thought how beautiful
    everything looked like."

    "A little further away was the village night sprite had been talking
    about. As they entered it, the streets were quiet and nobody was walking
    on them. [dreamer] and night sprite walked through them, until they
    arrived to the market place."

    scene bg cats_marketplace

    "Market place was full of cats of all kinds. They were sitting on the
    benches and under the trees. Some of them were perched on window sills of
    nearby houses and many were sitting on the ground. One, particularly
    dignified looking black cat, was sitting on the edge of the fountain. As
    they approached, it spoke."

    black_cat "Welcome night sprite, we were already waiting for you."

    Sprite "Greetings to you Black Cat, I'm sorry if I have kept you waiting
    for long. I met a stranger on my way and have been traveling with [him]."

    "[dreamer] greeted Black Cat shyly, not quite sure how to address it or
    how to behave in general in this strange situation."

    black_cat "We have gathered here for a specific purpose. As you know, the
    harvesting season is soon upon us and it's time to celebrate that. While
    the villagers are having their celebration, we'll have ours. But first
    we need to decide where to celebrate this year."

    black_cat "There are two options left. We can stay with the humans and
    secretly celebrate with them. Or we can move to some secluded place and
    have a proper celebration there. Both have their advantages and
    disadvantages. We shouldn't forget that all that grain that they have
    collected will attract mice. But staying with humans means that we can't
    have a big celebration."

    "Other cats started taking turns in talking, weighting in their opinions.
    Some of them were worried that mice might eat lots of grains if they were
    away. Others thought that the mice wouldn't have time to eat that much and
    it would be nice to be able celebrate somewhere where humans weren't in
    the way."

    "The meeting continued for a while, but no consensus could be reached.
    Eventually Black Cat who had been sitting quietly and listening to others
    stood up and spoke."

    black_cat "I don't think we can reach the conclusion without outside help.
    Both ways have their merits. Why don't we ask the night sprite what he
    thinks?"

    Sprite "I have my opinion and that is that you should ask [dreamer]. [He]
    is impartial for sure and doesn't have preference or a favourite cat.
    What do you say [dreamer], where cats should have their harvest party?"

    menu:
        "Where should cats celebrate?"

        "Secretly among humans":
            jump cats_with_humans

        "Away from humans":
            jump cats_without_humans

label cats_with_humans:
    black_cat "It's decided then. This year we will celebrate among the humans
    and keep a close eye on the mice. They won't suspect anything and the
    harvest will be kept safe."

    black_cat "I'm sure the humans will welcome you to take part into their
    celebration. Some of us will drop by to greet you, but mostly we'll stay
    out of the sight."

    black_cat "Now that the important matter has been decided, we'll start
    arranging practical details. There's plenty to do and not much time."

    "Cats started doing practical arrangements. They agreed who would be in
    charge of arranging food and who would make sure that the harvest was
    being guarded even while the celebration was going on. It seemed to
    [dreamer] that the meeting was going to continue forever and [he] yawned."

    $ harvest_with_humans = True

    jump end_of_meeting

label cats_without_humans:
    black_cat "Right, that's decided then. This year we'll celebrate in a
    secret location. Mice won't be destroying the harvest in one night and we
    have deserved our special occasion."

    black_cat "Now that the important matter has been decided, we'll start
    arranging practical details. There's plenty to do and not much time."

    "Cats started doing practical arrangements. It seemed to [dreamer] that
    the meeting was going to continue forever and [he] yawned."

    $ harvest_without_humans = True

    jump end_of_meeting

label end_of_meeting:
    Sprite "The meeting will continue for a while still, but I don't think
    there will be anything important anymore. They're just going through the
    practical arrangements, not that they aren't important too, but nothing
    that will be particular interest to us."

    Sprite "I think you did well there. The night is starting to turn into
    dawn and it's time for me to retire into shadows. If you happen to wander
    around these parts again, I would like to meet you again."

    Sprite "But you should rest too while you have chance. You could take a
    short nap under that tree over there."

    "[dreamer] nodded, [his] eyelids were heavy as lead and it sounded like
    a great idea to have a short nap. [He] wished night sprite a safe journey
    and then curled under the tree. Soon [he] was fast asleep, while the cats
    were still discussing details of the celebration."

    jump end_of_day_one

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

    scene bg mushrooms
    with dissolve

    $ met_limbaugh = True

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

    jump forest_road

label forest_road:
    scene bg forest_road_bg
    with dissolve

    "Soon the forest was quiet again. One could still hear rustling and
    flapping of small creatures here and there, but that was all. [dreamer]
    looked around and then stood up. [He] started walking the road again,
    wondering how long it would take [him] to arrive that friendly village
    Limbaugh had mentioned."

    if ate_pie_with_limbaugh:
        "Walking was easy. The road was even and there were no big hills or
        other obstacles in the way. The mushroom pie had driven the hunger away
        and [he] was on a cheerful mood. [dreamer] was starting to get tired
        though and yawned couple of times. Warm weather and silent forest
        didn't help at all either. [He] was determined to make to that village
        before the dark and pressed onwards."

    if not ate_pie_with_limbaugh:
        "Walking was easy. The road was even and there were no big hills or
        other obstacles in the way. [dreamer] was starting to get hungry and
        wished that [he] had eaten the pie with Limbaugh. On top of that
        [dreamer] was starting to get tired Warm weather and silent forest
        didn't help at all either. [He] was determined to make to that village
        before the dark and pressed onwards."

    scene bg meadow_bg
    with dissolve

    "Eventually [dreamer] arrived to a clearing. The road continue straight and
    just barely edged the clearing. [He] could hear sound of a small stream
    coming from somewhere near, although it was nowhere to be seen. The ground
    was covered in tall grass and flowers of all colours. [dreamer] thought
    that the stream couldn't be far away and was probably just hidden by
    flowers."

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
    scene bg limbaugh_img
    with dissolve

    "Limbaugh shrugged when [dreamer] said [he] would rather not share a pie
    with him. Limbaugh rearranged some of his many bags and then looked at
    [dreamer] again."

    Limbaugh "I don't mind that you didn't want to eat the pie with me. In
    some ways it's actually very sensible to decline in these parts of the
    world. One should be wary of the strangers after all. But if you don't
    mind, we could still sit here for a bit before I have to continue my
    journey."

    Limbaugh "I see that you're carrying a dream book with you. That makes
    traveling here safer. As long as you keep the book with you, there is
    not very much that you need to be afraid of. But if you were to lose the
    book, the situation would be different. So, keep a close eye on the book
    and never let go of it."

    Limbaugh "But now I must continue my journey. I'm on my way to meet
    Baron Inningsborough and his seven cats and shouldn't be late.
    If you continue this road for a while still, you'll arrive to a friendly
    village where you can get more food and place to sleep."

    "[dreamer] watched as Limbaugh stood up, collected his bags and after
    counting them twice, started walking. Curiously, he didn't follow the
    road, but continued directly into shadowy woods."

    jump forest_road

label drowsy_clearing:
    "[dreamer] stepped from the road and started walking into the clearing.
    Tall flowers soon surrounded [him] from every direction. Sun was shining
    warmly and butterflies were flying amidst the flowers. [He] could hear
    buzzing of the bees too. The air was very sweet from the scent on
    colourful flowers and [dreamer] stopped couple of times to smell them."

    scene bg stream_bg
    with dissolve

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

    $ visited_clearing = True

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
    butterflies that were flying amidst them. Sound of the stream could be
    heard somewhere not too far away and it sounded almost like distant
    chatter of people. [He] strirred and tried to listen to more closely. It
    was not just [his] imagination, the stream did sound like people
    chattering."

    scene bg simbali_bg
    with dissolve

    "Now [dreamer] was struggling in order to hear better. Sounds were so close
    that [he] could almost understand what they were talking. Suddenly
    [dreamer] woke up and stood to a sitting position, looking around and
    realised that [he] was surrounded with small, winged creatures that were
    the source of chattering [he] had heard in [his] dream."

    simbali "Hey, big folk! What are you doing here, snoring like an old bear?
    We can barely hear our own thoughts and I'm sure all the birds of the
    forest have gone deaf and are not going to sing in a while."

    "Tiny winged creatures were sitting on flowers and in grass. Some were
    flying around and all of them were chattering busily with each other. It
    seemed that most of their talking was to comment loud snoring of the
    stranger or [his] unfashionable and dull clothes. [dreamer] tried to follow
    them all with [his] eyes, but soon gave up and focused only on the one what
    had been talking to [him]."

    jump fairy_folk_in_clearing

label stay_awake_in_clearing:
    "Despite feeling drowsy, [dreamer] thought that it would be best to stay
    awake. Short naps had the bad habit of turning into long sleep and [he]
    did want to get to the village before it would be dark. However, [he]
    decided that it wouldn't do any harm to lie on the grass for a moment and
    watch the clouds as they sailed across the sky."

    "Some of the butterflies that were flying above [him] looked sort of odd.
    It was almost if they had tiny arms and legs and were wearing clothes.
    [dreamer] focused [his] attention more closely to them and sat up to see
    them better. What [he] saw, took [him] completely by surprise."

    scene bg simbali_bg
    with dissolve  

    "Tiny winged creatures were sitting on flowers and in grass. Some were
    flying around and all of them were chattering busily with each other. It
    seemed that most of their talking was to comment loud stomping of the
    stranger or [his] unfashionable and dull clothes. [dreamer] tried to follow
    them all with [his] eyes, but soon gave up and focused only on the one that
    was closest to [him]."

    simbali "Hey, big folk! What are you doing here, stomping around like an
    old bear? We can barely hear our own thoughts and I'm sure all the birds of
    the forest have gone deaf and are not going to sing in a while."

    jump fairy_folk_in_clearing

label fairy_folk_in_clearing:

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

    scene bg fairy_town_bg
    with dissolve

    "Soon they landed on a large clearing. [dreamer] realized that even if the
    clearing looked large, in reality it was relatively small. Everything just
    looked so much larger from [his] current point of view. Colourful houses
    were surrounding the clearing. Some of them were on the ground, while
    others were hanging from the flowers and grass."

    Simbali "This is our town. As you can see, if you had wandered here you
    could have easily stepped on our houses without noticing them at all. This
    is also where we will decide a proper judgement for you. You may sit down
    in the shade over there as we have our meeting."

    scene bg trial_bg
    with dissolve

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

    "[dreamer] didn't really have any options. Simbali had cast a spell on
    [him] and [he] was in captivity in their town. Escaping seemed impossible,
    so [dreamer] agreed to perform the task."

    scene bg white_pearls_bg
    with dissolve

    Simbali "Good, I knew that you would be reasonable. The task is rather
    simple. We need you to retrieve a bag of pearls that was stolen from us by
    a group of thunder beetles. They have a hive on the other side of the
    river and we know its location. But because the hive is underground, we
    can't enter it and retrieve the pearls by ourselves."

    Simbali "A butterfly will take you near the hive and wait you there. The
    excact details on how you will get the pearls is up to you, but I would
    advice you to avoid the beetles as much as possible. They are vicious folk
    and your story will surely be at end if they catch you."

    scene bg high_grass_bg
    with dissolve

    "A butterfly was summoned and after a brief flight [dreamer] found herself
    standing in the long grass. The butterfly was resting on a large hosta and
    watching [him] as [he] slowly started walking to the direction where the
    hive was supposed to be. [He] had to proceed carefully, as there were
    thorny bushes all around and thorned vines covered the ground here and
    there."

    "[dreamer] was full of doubts. [He] certainly was not a fighter and didn't
    really have an idea how to approach the problem. This was something
    entirely different than raiding [his] parents' cookie jar in the night.
    [He] felt a little sting of home sickness in [his] chest and wondered what
    mother and father were doing anyway and if they had already noticed that
    [he] had disappeared somewhere."

    scene bg hive_bg
    with dissolve

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

    scene bg central_hive_bg
    with dissolve

    "Eventually [dreamer] arrived to an opening that let into a big cavern.
    [He] could see large beetles sleeping here and there in the cavern, with
    few of them wandering about the cavern. They were large, dark coloured and
    generally menacing looking. In the middle of the cavern [he] could see
    a bag of pearls on a big table."

    "[dreamer] started to think what would be the best way to get the pearls.
    [He] could sneak in and try to steal them. That might work since most of
    the beetles seemed to be asleep. [He] could also just charge in and try to
    scare them away. Third option was the scariest one, just walk in and ask
    if [he] could take the pearls and return them to the fairies."

    menu:
        "How should [dreamer] try to solve the problem?"

        "Sneak in and steal the pearls":
            jump steal_pearls

        "Charge in and try to scare beetles":
            jump charge_hive

        "Walk in and ask to have the pearls":
            jump negotiate_with_beetles

label steal_pearls:
    "Stealing pearls would be a difficult task. While they were not actively
    being guarded, there still were beetles in the room and some of them were
    moving about. [dreamer] stood in the shadows and observed. [he] tried to
    find patterns beetles might be following and memorize them. It seemed that
    to [him] that it would be possible to sneak in and use some of the
    sleeping beetles as a cover."

    "When the moving beetles were the furtherst away, [dreamer] snuck into
    the room. [he] quietly tiptoed next to the closest sleeping beetle and
    hid behind it. [he] lay there, holding [his] breath and listened
    another beetle that passed on the other side of the sleeper."

    "When path was clear, [dreamer] started crawling. [he] moved from a
    sleeping beetle to another and lay in waiting while any of the other
    beetles was near by. Slowly [he] was making towards the center of the room
    where pearls shimmered."

    "Last leg would be the most dangerous. There were not much cover, save
    for the rock table where the pearls were. [dreamer] waited until all the
    moving beetles were on the other side and then quickly scurried next to
    the table. [He] didn't dare to look over the edge of it, in fear that   
    the beetles would see [him]. Instead of that [dreamer] blidly groped for
    pearls."

    "After second or two that felt long as years, [dreamer] felt smooth
    surface of the pearls on [his] fingertips. Slowly [he] started pulling
    them towards the edge. Then, suddenly [he] felt cold chitinous arm and
    [dreamer] was pulled up. A large beetle stood on the other side of the
    table and it had caught [him]!"

    "No matter how much [he] kicked, hit and screamer, the beetle wouldn't
    put him back down. More bettles gathered and they were chittering with each
    other, probably negotiation what should be done with the intruder."

    "Soon [dreamer] was being carried deeper into the hive. They went
    downwards for a considerable time, until they reached a pit that was
    covered with a grate. Into that pit [dreamer] was thrown and grate was
    closed again. [dreamer] was now prisoner of the beetles."

    jump hive_prison

label charge_hive:
    "[dreamer] gathered [his] courage for a moment. It probably would work if
    [he] charged in screaming as loud as [he] could. That should confuse the
    beetles and maybe even drive some of them away. In any case, they
    wouldn't be able to react fast enough and [dreamer] could snatch the
    pearls and ran away again."

    "[dreamer] took few deep breaths and then started running, while screaming
    as hard and loud as [he] could. First his plan seemed to work. Beetles
    were unsure what this new thing was that was running inside of their hive,
    screaming like a banshee. But quickly they started moving and taking
    defensive positions."

    "Some of the beetles guarded pathways that lead deeper into hive, while
    others were escorted into safety. They were much quicker that [dreamer]
    had anticipated and soon blocked all the exits from the room. Then group
    of beetles formed a loose ring around [him] and started advancing.
    [dreamer] tried to escape, but it was already too late."

    "Unceremoniously, [dreamer] was picked up by one of the largest beetles.
    No matter how much [he] kicked, hit and screamer, the beetle wouldn't
    put him back down. Beetles were chittering with each other, probably
    negotiation what should be done with the intruder."

    "Soon [dreamer] was being carried deeper into the hive. They went
    downwards for a considerable time, until they reached a pit that was
    covered with a grate. Into that pit [dreamer] was thrown and grate was
    closed again. [dreamer] was now prisoner of the beetles."

    jump hive_prison

label hive_prison:
    scene bg prison_bg
    with dissolve

    "[dreamer] dusted off [his] clothes, stood up and looked around. [He] was
    in a small, but rather deep pit. Grate covered the pit high above [his]
    head and was well beyond [his] reach. The floor was bare and featureless.
    Walls of the pit were almost vertical and definitely too steep to even
    think of scaling them without any tools. [dreamer] sighed, [his] situation
    looked hopeless."

    "For a while [dreamer] kept searching [his] prison, in hope of finding
    a way out, but eventually [he] had to conclude that such thing didn't
    exist. [dreamer] sighed, sat down and stared at the grate high above.
    There was no way to reach it and it was the only way out."

    "Then [he] remember the book. The beetles hadn't taken it away from [him].
    Not that it would do much good, but at least [he] could pass some time
    reading it, while waiting what the beetles would do next. [dreamer] opened
    the book and started looking through it. While the light of fungi was dim,
    it was enough so [he] could look at the pictures."

    "[dreamer] rubbed [his] eyes, while [he] turned to another page. The
    pictures alone were fascinating, but [he] wished that [he] could read the
    text too. The dim light didn't make reading easy and [he] was getting
    tired too. [dreamer] yawned as [he] turned to the next page. Soon [he]
    fell asleep, the book open on [his] lap."

    jump end_of_day_one

label negotiate_with_beetles:
    "[dreamer] was hesitant, but [he] thought this would be the best course of
    action. [His] throat was try and [his] hands were trembling as [he] stepped
    into the cavern. After [dreamer] had taken couple of steps, the beetles
    spotted [him]. As [he] walked towards them [dreamer] heard chittering and
    clattering as more and more beetles were woken and alarmed."

    scene bg king_beetle_bg
    with dissolve

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
    demand that we hand over the pearls. They are spoils of war, rightfully
    ours by the might of the thunder beetles. If those fairies want them back,
    they can come and get them by themselves!"

    "Chkakuth's speech raised an approving storm of beetle chittering.
    Eventually it died down and [dreamer] could continue. This seemed like a
    crucial moment, fail here and [his] mission would fail."

    menu:
        "How should [dreamer] approach this?"

        "Offer trading the pearls for something":
            jump offer_trade

        "Ask if the beetles would rather have peace":
            jump offer_peace

label offer_trade:
    "[dreamer] cleared [his] throat and asked if the beetles could trade the
    pearls for something. [He] explained that while [he] didn't know fairies
    that well, they probably would have something that the beetles could use.
    They would just have to name it and [dreamer] would try to convince the
    fairies to trade the pearls for it."

    Chkakuth "The fairies have a similar bag of pearls as this one is. The
    difference is that those pearls are black, while these are white. We are
    willing to trade our bag to theirs."

    Chkakuth "Black pearls are our most beloved treasure and they have been
    in our possession for countless generations. Fairies have tried to stole
    them from us multiple times and only very recently have succeed doing so.
    Luckily, our surprise raid managed to capture their white pearls soon
    after."

    Chkakuth "Take these pearls and go. Do not try to double cross us, since
    our reach is long and our hathred is strong. You will be escorted to the
    surface."

    $ white_pearls = True

    jump return_surface

label offer_peace:
    "[dreamer] cleared [his] throat and asked if the beetles would rather live
    in peace with the fairies. It seemed to [him] that there would be enough
    space for both of them on the meadow, because fairies lived on top of it
    and the beetles lived underneath. Maybe some compromises would have to be
    done here and there, but [he] was sure that they could work it all out in
    the end."

    Chkakuth "We have been in war with the fairies as long as we can remember.
    They try to drive us away from the meadow and we are trying to do the same.
    We can't just simply say that 'lets forget all this and be friends.' It
    does not work that way."

    "[dreamer] noticed that some of the beetles weren't as enthuastic as before
    and even Chkakuth seemed tired. [He] offered to help with the negotiations.
    They could start slowly and first cease fighting and then try and find out
    a way that everybody could continue living at the meadow."

    "Chkakuth was silent for a very long time. [dreamer] was already getting
    worried that [his] plan wouldn't work after all, but then Chkakuth spoke
    and broke the silence."

    Chkakuth "Very well, we accept your offer. But don't take us as fools that
    you can trick. At the first sign of treachery the agreement is broken and
    we will return to war with fairies. Until then, you have the word of the
    thunder beetles that we won't be attacking the fairies."

    Chkakuth "You may take the pearls that the fairies sent you to retrieve.
    But in return we would like our pearls to be returned to us. They are like
    these, but instead of being white, they are all black. Fairies will know
    what I talk about if you ask them. They took those pearls from us in force.
    A guard will escort you back to the surface."

    $ white_pearls = True

    jump return_surface

label return_surface:
    "Chkakuth turned and slowly walked away. Other beetles started scattering
    to different directions. Lighter coloured beetle handed [dreamer] the bag
    of pearls and started escorting [him] towards the surface. This new beetle
    spoke very little and soon [dreamer] gave up trying to ask more question."

    "After ascending in silence for a while, [dreamer] started notice how light
    was changing. Pale glow of fungi was slowly replaced with the warn sun
    shine and [his] spirits rose as [he] could see the blue sky above [his]
    head again. [dreamer] turned to thank the beetle, but it had already
    retreated back into the hive."

    "[dreamer] retraced [his] steps back to the butterfly, who was more than
    happy to take off and leave the vicinity of the hive. [He] was clutching
    the bag of pearls during the whole flight, worried that they would drop
    and get lost in the tall grass."

    jump fairy_town

label fairy_town:
    scene bg fairy_town_bg
    with dissolve

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
    an alarm had been sounded. If [dreamer] had not been so crafty and
    stealthy, [he] surely would have been caught. But in the end [he] had
    snuck out of the hive and now [he] was here with the pearls."

    "Fairies were listening to [his] story silently. In particularly exciting
    parts somebody might let out a small gasp, but other than that all the
    fairies were silent. They clearly admired how skillful and clever [dreamer]
    was. Only Simbali seemed to be unaffected by the story, [dreamer] was
    wondering if the fairy guessed that [he] wasn't telling the truth."

    "When the story was over, everyone were silent for a while and started at
    Simbali. Eventually the fairy spoke with a steady voice that didn't reveal
    an emotion."

    $ black_pearls = False

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

    $ black_pearls = True

    jump leaving_town

label leaving_town:
    if black_pearls:
        Simbali "You didn't do too badly. I just wish that we wouldn't have to
        hand over those pearls that are in our possession. In the future, you
        would do well to avoid wandering on the meadow again. This time you
        were lucky and managed to avoid the judgement. Next time might not be
        so easy anymore."

    if not black_pearls:
        Simbali "You did well. It was not an easy task to retrieve the pearls
        from the hive of the thunder beetles. However, in the future, you would
        do well to avoid wandering on the meadow again. This time you were
        lucky and managed to avoid the judgement. Next time might not be so
        easy anymore."

    Simbali "You have fulfilled your part of the deal. We will now fulfill our
    part. First you are escorted at the edge of the meadow, where there are no
    fairies or houses to trample on. Then a spell will be cast upon you that
    will return you back to your normal size. After that you are free to go."

    "Simbali turned away and left. [dreamer] was given a butterfly to fly and
    soon enough [he] and few fairies that were escorting [him] were again at
    the edge of the meadow. [dreamer] stepped down and closed [his] eyes as
    one of the fairies started throwing the colourful dust at [him]."

    scene bg meadow_bg
    with dissolve

    "[dreamer] felt the familiar tingle that started from [his] spine and
    spread over the whole body. As [he] opened [his] eyes, fairies were
    nowhere to be seen and [he] was again looking flowers from the above, not
    from the down."

    "[dreamer] looked at the meadow one more time and then turned to continue.
    The friendly village was somewhere in front of [him]. It occurred to [him]
    that it would have been a good idea to ask the fairies if they knew
    anything about it. Although [dreamer] had a feeling that the fairy folk
    didn't often leave the meadow, if ever at all."

    "[dreamer] started following the road once more. Like before, it was easy
    to walk. The woods around [him] didn't look as thick as before and
    occasionally [dreamer] caught glimpse of meadows and small ponds."

    jump arriving_to_village

label walk_without_rest:
    "The clearing looked really inviting and [dreamer] found it hard to walk
    past it. But staying there would have wasted time and [he] wasn't sure
    how far it was until the friendly village Limbaugh has mentioned. No, it
    was best to keep going and avoid wasting time. If [he] wanted, [dreamer]
    could always come back later."

    jump arriving_to_village

label arriving_to_village:
    scene bg village_bg
    with dissolve

    "Eventually the woods started growing thinner and [dreamer] could see
    further than before. [He] could see fields in the distance and thought
    the the village shouldn't be that far anymore. Soon after that the forest
    ended and [dreamer] was walking on a road that was nestled between two
    fields."

    scene bg outside_village_bg
    with dissolve

    "The village wasn't big, but it certainly was friendly looking. People
    were walking around smiling and they greeted each other in warm and open
    manner. On [his] left, [dreamer] saw some cats walk into an alley, while
    from the right [he] could smell delicious freshly baked bread."

    "[dreamer] looked to the sky. The sun had already passed the high point
    and it might be a good idea to find a place to sleep. There was an inn
    nearby, maybe [he] could get a room from there."

    menu:
        "Which direction [dreamer] should go?"

        "Left, sleeping in the inn would be good":
            jump inn

        "Right, freshly baked bread should be delicious":
            jump fresh_bread

label inn:
    "[dreamer] stepped into the inn. As [he] entered through the door, rich
    aroma of various foods and tobacco smoke greeted [him]. The main room
    of the inn had few patrons and a very large man who seemed to be the owner
    of the inn."

    keeper "Hello and welcome to the Spork and Apple, my very own inn. I'm the
    inn keeper and Keeper is also my name. We have excellent food and good
    beds for the weary travelers here. And you look like you could use both of
    them, if you don't mind me saying so."

    "[dreamer] nodded. [He] was both hungry and tired. Then [he] remembered
    that [he] had no money to pay for food and shelter. [dreamer] looked
    embarrassed and didn't know what to say."

    keeper "What's the matter, don't you have money to pay? Hm.. I'm sure we
    can arrange something."

    keeper "Say, what about if you could help here a bit? There's always some
    chores to do. Work for couple of hours and you'll get warm food and dry
    place to sleep over the night."

    "[dreamer] was more than happy to agree. Keeper showed [him] around and
    soon [dreamer] was happily carrying full plates to customers and taking
    the empty ones back to the kitchen. When there were no customers requiring
    [his] attention, [dreamer] kept tables clean by wiping them and generally
    made sure the dining hall was clean."

    "Eventually even the last patron had left the dining hall, but that didn't
    mean that [dreamer] had time to rest. [He] still had to help cleaning up
    the hall for the night and then attend the dishes in the kitchen."

    "Big oaken vats were filled with steaming water and dishes were loaded
    into them. And then they were scrubbed. [dreamer] thought that they would
    never be done. [His] arms hurt and sweat formed on [his] brow."

    "Finally Keeper put the last plate away and announced that the were no
    more dishes left. [dreamer] dried [his] hands and sat down exhausted,
    while keeper set up some food for them to eat."

    "The soup that was served was probably the best tasting food ever
    [dreamer] had eaten. While they were eating, Keeper told stories of the
    many customers that had stayed in the inn. Over the course of years many
    colourful characters had stayed there and Keeper had many good stories
    to tell."

    "Eventually they were done with their late meal and [dreamer] yawned.
    Keeper showed [him] a small, but cozy room where [he] could spend the
    night. The last thing [dreamer] saw before falling asleep were rays of
    moonlight that streamed in from the small window."

    $ stayed_in_inn = True

    jump end_of_day_one

label fresh_bread:
    "[dreamer] opened a wooden door and step into the bakery. Shelves lined
    the room and all kinds of breads, cakes and cookies were piled on them.
    Mouth watering smell of freshly baked goods filled the air. A large and
    friendly looking man put a new batch of bread into the large oven and
    turned around to face [dreamer]."

    baker "Welcome to the bakery. What would you like to have? We have
    everything from simple, yet delicious, breads to most complex cakes."

    "[dreamer] looked all the delicious goods around [him] and [his] mouth
    watered. [He] could almost feel how soft and fluffy one of those breads
    would feel in [his] mouth and how sweet and delicious the small pastries
    would be to eat. But then [dreamer] remembered that [he] didn't have
    any money with [him] and [his] smile died."

    baker "What's the matter? Don't you like bread or cookies?"

    "Sheepishly [dreamer] admitted that [he] didn't have any money with [him].
    Freshly baked bread would have been really great, but [he] just couldn't
    buy any."

    baker "Hm.. Lets not make that into a problem. I have some baked goods
    that needs to be delivered to people. Ordinarily I would do that by
    myself, but if you can help me, I can keep baking here. In return you'll
    get as much bread and pastries as you want to eat."

    "[dreamer] thought that it was a great idea and quickly agreed. Baker gave
    [him] a bread roll to drive away the hunger and then showed [him] the
    goods and explained where to deliver them."

    "[dreamer] started delivering them around the village as soon as [he] had
    finished with the bread roll. There were a basket of bread rolls to old
    mrs. Wiggums. Then there were two loafs of sesame seed bread to mr.
    Stutter. And many more after that. Everytime [dreamer] returned to the
    bakery to pick up more goods to deliver Baker asked if everything was
    going well and tossed [him] a pastry or bread roll to eat."

    "Eventually all the goods had been delivered and [dreamer] could rest for
     a bit. The day was turning into night and sky outside of the bakery
     window looked gloom."

    baker "The day is over and night is coming. I have a spare room over the
    bakery. If you need a place to sleep, you're free to use that. It's not
    a big one, but it's warm and dry place."

    "[dreamer] was more than happy to stay there. [He] thanked Baker and
    climbed narrow stairs up to the room. Furniture was very minimal, just
    bed, small table and chair. In the corner was cabinet, but that was all.
    There wouldn't have been much space for anything else anyway. A candle
    was sitting on the window sill."

    "[dreamer] lit the candle and sat on the bed. [He] wasn't quite ready to
    sleep yet, so [he] took out the book and started leafing through it. Such
    a strange book and somehow it had sucked [him] into an adventure.
    Eventually [dreamer] was getting tired and extinguished the candle.
    Moon had risen and moonlight cast some rays through the window. It was the
    last thing [he] saw before falling into a peaceful sleep."

    $ delivered_bread = True

    jump end_of_day_one

label end_of_day_one:
    "[dreamer] woke up in [his] bed. First rays of the sun were peeking from
    behind curtains. The book lie on the floor where it had fallen when [he]
    fell asleep last night. The house was quiet, but birds were already
    singing outside."

    "[dreamer] got up quickly and picked up the book. [He] would have to
    return it quickly before anyone would it was missing. [He] opened door of
    [his] room and listened. The house was still quiet, it looked like [he]
    had woken up before [his] parents."

    "[dreamer] snuck into the living room and replaced the book. [He] had
    already resolved to borrow the book next night and see if [he] could
    return back to that strange dream world or if it had been just a dream.
    But that would have to wait until the evening."

    jump day_two

label day_two:
    "The house was silent again. [dreamer] had been patiently waiting for this
    late hour. [His] parents were sleeping and now would be [his] chance to
    sneak into living room and take the book again."

    "Just like previous night, [dreamer] silently entered the living room and
    with the help of a chair, retrieved the book. Then [he] sneakily returned
    into [his] room and carefully closed the door behind [him]. In a one quick
    move, the book was open on the bed and [dreamer] hunched over it."

    "[dreamer] waited for a moment, then another and yet another. Then it
    dawned to [him] that while [he] had been able to visit the dream world
    night before, [he] didn't have a clue how that had happened. [dreamer] had
    just assumed that the book had something to do with it and [he] had been
    told about its signifigance. But still [he] didn't know how to return to
    where he had been."

    "[dreamer] turned the pages and tried to think what [he] should do next.
    While [he] was a bit tired, [dreamer] wanted to solve to riddle or at
    least find a clue how the book worked. A little yawn escaped [his] lips,
    but [he] tried to push drowsiness aside. [He] continued examining the
    book and yawned again."

    if chose_day:
        jump clearing_2nd_morning

    if not chose_day:
        jump clearing_2nd_night

label clearing_2nd_morning:
    "Frustrated, [dreamer] threw [himself] on [his] back. But instead of
    finding the familiar bed, [he] discovered soft and green grass. And the
    ceiling above [him] wasn't there anymore either. Instead of it, [dreamer]
    was staring at the blue sky. [dreamer] quickly got back up and realized
    that [he] must have fallen asleep at somepoint and was now in the dream
    world."

    "[dreamer] got up and took the book that was lying on the grass. [He]
    brushed it clean and then looked around. The clearing looked just like the
    previous time [he] had been here. Same green grass, same old road, same
    trees around the clearing."

    "[dreamer] started walking. If everything was like before, not far ahead
    there would be a group of big mushrooms where [he] could take a break
    before continuing. If [he] were lucky, maybe that old bird would be there
    too. Last time he had offered [dreamer] some pie and having something to
    eat didn't sound the worst option to [him]."

    "Soon [he] arrived at the mushrooms, but something was wrong. Last time
    [dreamer] had been here, the mushrooms had been on the right side of the
    road. Now they were on the left side. [He] stopped and stared at the
    mushrooms. Could it be that [he] was mistaken and they had always been on
    the left side? Or were these different mushrooms and [he] was walking to
    a wrong direction?"

    "[dreamer] decided to sit down and think what to do next. [He] didn't want
    to risk walking to a wrong direction accidentally. Mushrooms did look like
    what [he] remembered them looking, but they definitely were on the wrong
    side of the road."

    Limbaugh "Hello there traveler. [dreamer], if my old mind isn't playing
    tricks on me. How are you on this beautiful day?"

    "[dreamer] looked up and saw the familiar bird. It was Limbaugh, who [he]
    had met last time on a trip to dream world. Like last time, the old bird
    had managed to walk up to [him] without making sound or attracting [his]
    attention. Nevertheless, [dreamer] was more than happy to see a familiar
    face."

    menu:
        "What will [dreamer] answer?"

        "I'm fine, how about you?":
            Limbaugh "Radiant, just radiant. Thank you for asking. The day is
            beautiful and I'm feeling well. A bit of warm sunshine is always
            good for these old bones."

        "I'm confused about these mushrooms":
            Limbaugh "You should remember that we're in the dream world and
            not everything is like in the waking world. Sometimes things are
            almost, but not quite like before. So don't worry that the
            mushrooms seem to be on the wrong side of the road."

            Limbaugh "Visitors of the dream world soon learn how to deal with
            landscape that changes slightly from time to time. Giving
            directions can be somewhat problematic if you rely on things on
            being exactly at any given spot, but the general layout of things
            is usually the same."

    if ate_pie_with_limbaugh:
        Limbaugh "I have some cup cakes in my backpack. I remember that you
        liked my mushroom pie, so perhaps you would like these too. They
        aren't warm anymore, far from it, but they still should be tasty."

        "[dreamer] was more that happy to agree. [He] still remember how good
        the pie had been and [his] stomach was empty. Limbaugh was rummaging
        through his various bags, while muttering that the cup cakes should
        be somewhere there. Then he let out load exclamation and produced
        few large cup cakes."

        Limbaugh "As I said, I baked these by myself. The recipe is from earl
        of eastern marches, lord Malfodor. The story goes that he and duke
        of sandy hills were playing cards one night. The earl won, but duke
        didn't want to give up the lands that he had placed as a bet. Instead,
        he managed to convince the earl to accept the recipe as a substitute."

        Limbaugh "I don't know how true the story is. The old lord Malfodor is
        known to spun a yarn now and then. But the recipe is good and the
        resulting cup cakes are really great."

        "[dreamer] nodded as he was savouring the tasty cup cake. [He] could
        taste at least strawberries, rasberries and blueberries. There
        probably were some other berries there too, but [dreamer] couldn't be
        sure which ones they were. In any case, cup cakes were delicious."

        "Soon cup cakes were gone and [dreamer] was wiping [his] mouth clean
        as Limbaugh arranged his many bags in order again. The food had hit
        the spot and [dreamer] wasn't hungry anymore."

    Limbaugh "I trust you found your way to the friendly village last time you
    were visiting here. If you fancy, you could go there again and see if the
    landscape is still the same as the last time. That makes it fun to travel
    in the dream world, you can never be quite sure what you'll find. Even if
    you have visited that part before."

    Limbaugh "I remember this one time when I was on my way to see the young
    prince of Grokkington and his court. Sure, I could find the young prince
    no problem, but his court was entirely different matter. Instead of a
    large and impressive castle, there was a village of huts with straw roofs.
    Whole court was living in the huts."

    Limbaugh "The chancellor Grubarik tried to look all mighty and important.
    He had chosen the second biggest hut as the biggest one had been given to
    the prince. But it's not so easy to look impressive with huts and straw
    and all that stuff. Poor chap, really."

    Limbaugh "Young prince on the other hand wasn't bothered at all. He spent
    his time lounging in a hammock instead of posturing and posing. He even
    said that the court should consider setting up hammocks in the castle and
    use them instead of thrones and stone benches."

    "Limbaugh was laughing heartily and [dreamer] was soon too. But soon it
    was time for Limbaugh to continue his journey. He picked up his numerous
    bags and heading straight through the forest after wishing [dreamer] a
    safe journey."

    "[dreamer] looked around, stood up and picked the book with [him]. Then
    [he] turned to continue [his] journey. The village wasn't too far away,
    if everything was more or less like during [his] previous visit. But there
    was only one way to find out for sure and that was to walk there and see
    with [his] own eyes."

    jump before_clearing_2nd

label before_clearing_2nd:
    "[dreamer] was in a good mood. The forest didn't feel as dark as last time
    [he] had been there. Probably just because [he] now knew what was supposed
    to be ahead. There were small birds singing somewhere in the woods.
    [dreamer] didn't see them, but [he] could hear them easily."

    "After walking a while, [dreamer] arrived at the edge of a familiar
    clearing. It looked like [he] remembered it from the last time. Lots of
    high grass that was dotted with various flower of all colours. There were
    butterflies and bees flying around."

    if visited_clearing:
        jump visit_clearing_again

    "Like last time, [dreamer] decided that while the clearing looked really
    inviting, it would be better to continue [his] journey. The village wasn't
    that far anymore and [he] was looking forward arriving there. Last time
    everybody had been really nice and helpful."

    jump forest_again

label visit_clearing_again:
    "[dreamer] stepped on the edge of the clearing. [He] didn't want to enter
    deeper uninvited this time. Last time had taught [him] enough about the
    fairy folk and their suspicions towards big folk. If [he] waited for a
    bit on the edge, the fairy folk should spot [him] and hopefully invite
    to visit the meadow."

    "Sure enough, [dreamer] didn't have to wait for long until [he] saw what
    looked like small butterflies circle around [him]. They were the fairy
    folk that had arrived to look who was standing in the edge of their
    domain."

    fairies "Oh, hey! It's that big brute again. Why are you standing on the
    edge of our domain? Are you lost or just slow?"

    "Fairies were flying around laughing. They were making fun of [dreamer],
    but [he] didn't particularly care. Last time it had felt annoying, but
    this time [dreamer] knew better and didn't take it too seriously. [He]
    extended [his] arms and asked if the fairy folk could take him into their
    village again."

    fairies "You, in our village? All the houses would be trampled down by
    those gigantic feet of yours. And our beautiful flower would be completely
    flat after you sat on them. No, we cannot let this happen."

    "One of the fairies then flew around [dreamer] and threw some sparkling
    dust over [him]. Immediately [dreamer] felt the familiar tingle and
    everything around [him] seemed to grow huge. Soon, the high grass of
    meadow had transformed into a forest and flowers towered high above of
    [him]."

    fairies "That is much better. You still look like big folk and can't fly
    by yourself, but at least you aren't going to trample our beautiful houses
    or step on our precious flowers. Come, we'll take you to the village.
    Big things are on the move and Simbali might want to talk with you."

    "A monarch butterfly was summoned and soon [dreamer] was flying through
    the air. This time felt different than before. There was certain urgency
    in the beating of the wings and the butterfly was flying very straight,
    instead of the usual wandering. Soon [dreamer] could see the village in
    front of [him]."

    if white_pearls:
        if black_pearls:
            jump prep_after_peace_offering
        jump prep_after_no_peace_offering

    jump prep_after_jail

label prep_after_peace_offering:
    "As the monarch landed, [dreamer] could see that something was wrong. Lot
    of fairy folk was running around and they were carrying spears and other
    weapons that [dreamer] hadn't seen last time [he] was visiting the village.
    Fairies faces were stern and [dreamer] didn't hear the usual joking and
    laughter that was so characteristic to them."

    "[dreamer] spotted Simbali at the center of the village square and ran to
    him. He was clad in light armour and carried a spear in his hand. A short
    sword was by his side and he was giving orders to other fairies."

    Simbali "You have arrived during tumultuous times. The elders of the fairy
    folk has decided that we should go and try to regain control of the pearls
    that were given away. Preparations are already underway and our forces are
    being gathered."

    "[dreamer] wasn't very happy to hear about this. [He] had worked hard to
    get the thunder beetles and fairies on the path towards peaceful life. And
    now they were after each other again. In a way [he] could understand that
    fairy folk wanted the pearls back though. [He] had promised them to
    thunder beetles without consulting with fairies first after all."

    Simbali "Elders will be happy to hear that you have arrived. Thunder
    beetles keep changing where their tunnels surface and you would have first
    hand knowledge about the entrance. That could provide us a valuable
    advantage if you would join us."

    "[dreamer] was now faced with a dilemma. Should [he] aid the fairies, or
    should [he] honour the agreement with thunder beetles and try to avoid the
    war somehow. [His] part of the deal had been fulfilled already though, so
    in a way [he] didn't owe anything to the beetles anymore."

    menu:
        "What should [dreamer] do?"

        "Join the attack":
            jump join_war

        "Try to prevent the attack":
            jump prevent_war

label join_war:
    "TODO: write"

label prevent_war:
    "[dreamer] was unsure how to best explain [his] view to Simbali.
    Regardless, [he] decided to try. Initially, [he] spoke in an unsure voice,
    but soon picked up the speed and explained with strong terms how the war
    should be avoided at any cost. When [dreamer] was done, [he] and Simbali
    stood face to face, both being completely silent."

    Simbali "You know, I'm not entirely happy about the situation either. I
    would rather avoid the war. Even if I'm captain of the guard, I don't
    always agree what the elders decide. Maybe this is the first time I'm
    going to do something about it."

    Simbali "I don't think that we can succeed alone though, but we need
    allies. And those allies will have to come from the side of thunder
    beetles. If we want to prevent the war, we must hurry and get to the
    thunder beetles before forces of fairy folk are ready."

    "Simbali barked some order to two fairies that were hurrying past them.
    [dreamer] and Simbali would need a quick way to get to thunder beetles.
    Monarch butterflies wouldn't be fast enough, but Simbali seemed to have
    a plan that would help them. He guided [dreamer] through the crowd towards
    the edge of the clearing where two other fairies had already hurried."

    Simbali "We're going to take fastest possible way to travel there and that
    is by using dragonfly. They're fast, but quite temperament and require
    a skilled rider. And my personal mount is the fastest of them all. As soon
    as we get into the air, nobody can catch us anymore."

    "At the edge of the clearing, under shade of some large leaves were few
    dragonflies waiting. They eyed fairies and [dreamer] suspiciously, but
    Simbali soon calmed down one of them and started saddling it with the help
    of two other fairies. Soon they were ready and Simbali climbed onto the
    dragonfly and extended his hand for [dreamer]."

    Simbali "Climb up and sit behind of me. The dragonfly is strong enough to
    carry us both and we don't have time to teach you how to steer one by
    yourself. Be sure to hold on tight, since the ride might be a little bit
    rough."

    "[dreamer] climbed behind of Simbali and wrapped [his] arms around the
    fairy. Simbali's wings were partly blocking [his] view, but [dreamer]
    could still see how two other fairies ran further away as the dragonfly
    took off and started quickly ascending."

    "The ride was breath taking. Simbali kept the dragonfly low and had to
    constantly dodge long grass and flowers. When [dreamer] dared to take a
    quick peek to side, [he] could only see green blur whizzing past in a
    dizzying speed and decided that keeping [his] eyes closed was much better
    idea."

    "After a rough ride, [dreamer] felt that the dragonfly was descending
    rapidly and opened [his] eyes. At the same time Simbali motioned with his
    hand and pointed to quickly approaching ground."

    Simbali "I'll set down over there. We are close to the location where you
    said their tunnels start. Unfortunately I don't dare to leave the
    dragonfly here alone, so I'll have to send it away. If we fail to reason
    with thunder beetles, we don't have any means of escape. And even if we
    manage to reason with them, we are in for a long walk back."

    "[dreamer] nodded. The whole mission was desperate last chance effort and
    [he] realised how slim their chances for success were. But it was also
    reassuring that [he] wasn't on it alone, but had Simbali there to help.
    Hopefully together they would be able to convince the thunder beetles to
    help them."

    "After the landing Simbali removed their few items from the back of the
    dragonfly and set it free after taking of the harness and saddle. In the
    meantime, [dreamer] was keeping watch, while nervously glancing around.
    [He] had been here before, but it didn't make facing the thunder beetles
    any easier. On the contrary, since now [he] knew how large and fearsome
    they actually were."

    "Simbali hoisted the gear in a small bag and turned towards [dreamer]. He
    didn't watch how dragonfly was getting smaller and smaller as it raced
    away. Simbali didn't want to waste time on sentiments. They had things to
    do and it was best to get going."

    Simbali "You have been here before. Lead the way. Lets try and stay out of
    sight as long as possible. No point alarming them before we have an idea
    what the situation is. I'll follow right behind of you."

    "[dreamer] and Simbali started creeping through the high grass and other
    vegetation. Even when they tried to be as quiet as possible, [dreamer]
    thought that they must sound like two cargo trains going through forest.
    However; the truth was that they were very silent and probably could have
    sneaked past anything."

    "After dodging brambles and branches for a while, the two adventurers
    arrived to a clearing that [dreamer] recognized well. On the center of it,
    there was an entrance into tunnels of thunder beetles. Unlike last time,
    the entrance was being guarded by two ferocious looking thunder beetles.
    Sneaking past them would be difficult, if not impossible."

    Simbali "This looks like a tricky situation. I think we might be able to
    sneak past them though. But I'll leave the decision to you."

    menu:
        "How should they proceed?"

        "Sneak past the guards":
            jump sneak_past

        "Walk openly to clearing":
            jump open_approach

        "Wait for a while":
            jump wait_and_see

label sneak_past:
    "[dreamer] decided that it would be best to sneak past the guards. Trying
    to explain their mission to them would just take too long and they didn't
    have time to waste. Forces of fairie folk might be on their way any moment
    now. [He] and Simbali had a quick discussion over the plan and they
    decided to try and crawl in the cover of underbush as close as possible
    and then sneak past when thunder beetles were looking different direction."

    "[dreamer] and Simbali started crawling towards the entrace trying to hide
    behind the underbush. There was a small ditch running at the edge of the
    clearing and that they chose to use as an avenue of approach. Moving was
    slow and every tiny sound they made sounded like rumbling truck to
    [dreamer]. Eventually they made to the point where the ditch was closest
    to the entrance and stopped."

    "This was the most dangerous step. The beetles were slowly patrolling
    around and [dreamer] would have to time their move perfectly. They waited
    for a time that felt like an eternity and then when all the beetles were
    facing away, quickly started towards the entrace, while trying to make
    as little sound as possible."

    "Just as everything was looking good and [dreamer] thought they would
    miraculously succeed, they saw two thunder beetles emerge from the shadows
    of the entrance. Maybe they had been hiding there or maybe they were
    replacement guards sent to relieve the current ones. Either way, it made
    no difference to them at this point."

    "[dreamer] and Simbali were quickly surrounded by the thunder beetles who
    then started escorting them down the tunnels. While this was the direction
    [dreamer] and Simbali wanted to go, they would have much preferred to be
    able to sneak in without being noticed."

    jump before_thunder_beetles

label open_approach:
    "[dreamer] thought that there was little point in hiding. The thunder
    beetles would see them eventually anyway. So it would be a good idea to
    openly walk on the clearing and show that they didn't mean harm."

    "They quickly went over their plan just one more time and then Simbali
    took his sword and left it on the ground. No point on walking to the
    thunder beetles while openly carrying arms. Then they took a deep breath
    and stepped on the clearing."

    "As soon as [dreamer] stepped on the clearing, the thunder beetles noticed
    [him]. Simbali was following right behind of [him]. The beetles ran
    towards them and quickly surrounded the two adventurers, who tried their
    best to remain calm. As soon as they had been surrounded, one large
    beetle stepped in front of them. [dreamer] reasoned that this one must be
    some sort of leader."

    "The large thunder beetle stepped in the front of [dreamer] and stared down
    at [him] without speaking. [dreamer] had never felt so small, but bravely
    [he] stared back at the beetle. After a silence that seemed to go forever,
    the beetle turned away and ordered [dreamer] and Simbali to be escorted
    down the tunnels."

    "While they descented, [dreamer] found [himself] wondering if they had
    made a good choice. Now they were prisoners of the thunder beetles and
    escaping would be almost impossible. But other hand, [he] thought that open
    approach was best way to convince the thunder beetles that they meant no
    harm."

    jump before_thunder_beetles

label wait_and_see:
    "[dreamer] decided that they should wait for a bit and see how the
    situation develops. With a bit of luck, the thunder beetles would move
    further away from the tunnels and it would be easier to slip past them
    unnoticed. They didn't have too much time, but hurrying in a wrong spot
    would cost them time that they couldn't afford."

    "Simbali and [dreamer] were talking with hushed voices as they waited and
    watched the thunder beetle guards. The beetles weren't moving far from the
    tunnel opening and were keenly watching around them. [dreamer] was already
    starting to wonder if they would have to wait forever, because they had
    waited so long without anything happening."

    "As [dreamer] and Simbali were looking at the clearing, they heard a stern
    voice behind them. As they turned, they saw three beetles that had sneaked
    behind them and had spears pointed at them. Running at this point would
    have been futile, there was nothing else to do, but to raise the hands and
    hope for the best."

    "Angry looking beetles surrounded them and started escorting Simbali and
    [dreamer] towards the entrance and then down the tunnel. While this was
    where [dreamer] and Simbali wanted to get, they would have preferred to
    arrive without angry guards that had sharp spears."

    jump before_thunder_beetles

label before_thunder_beetles:
    "After descending deep into the tunnels of the thunder beetles, [dreamer]
    and Simbali arrived in a large chamber. Dozens and dozens of thunder
    beetles were lined by the walls and more were arriving all the time. This
    had to be some sort of assembly hall concluded [dreamer] as [he] looked
    around."

    "A large thunder beetle stands in the middle of other beetles. His
    commanding presence indicated him to be a leader of all these beetles.
    After observing the adventurers for a while, he finally spoke."

    Chkakuth "I am king Chkakuth, leader of the thunder beetles and you have
    entered in our domain without a permission."

    "TODO: write"

    "interrogation, explanation"

    menu:
        "What should [dreamer] do?"

        "Try to convince beetles":
            jump convince_beetles

        "Let Simbali help":
            jump simbali_convinces

label convince_beetles:
    "try convince, fail"

    "Simbali steps in, offers pearls"
    
    "TODO: write"

    jump beetle_plan

label simbali_convinces:
    "simbali offers pearls"

    "TODO: write"

    jump beetle_plan

label beetle_plan:
    "beetles hide, dreamer and simbali stay behind"
    "fairies arrive, questioning"
    "king beetle arrives with pearls"
    "negotiation"

    "TODO: write"





label prep_after_no_peace_offering:
    "TODO: write"

    menu:
        "What should [dreamer] do?"

        "Join the attack":
            jump join_war_2

        "Try to prevent the attack":
            jump prevent_war_2

label join_war_2:
    "TODO: write"

label prevent_war_2:
    "TODO: write"

label prep_after_jail:
    "TODO: write"

    jump join_war_3

label join_war_3:
    "TODO: write"

label forest_again:
    "TODO: write"

label clearing_2nd_night:
    Sprite "Hello there"

    "[dreamer] looked up. [He] was sitting on a familiar clearing and night
    sprite was standing close by. The moon and stars were shining high above
    them. [dreamer] must have fallen asleep at some point, although [he]
    couldn't guess when."

    Sprite "I see you decided to come and visit here again. Fancy a stroll
    through the night like last time?"

    "[dreamer] jumped up and picked up the book. [He] wouldn't want to miss
    another chance to see secrets of the dream world. [He] was wondering where
    they would head this time as the night sprite started walking along the
    road."

    if dragon_eggs:
        jump dragon_nest

    jump unicorn_spring

label unicorn_spring:
    Sprite "I was thinking that we could go and see if some of my old friends
    would be around. They come and go unannounced and it's always a bit of
    question of a luck if I can catch up with them. But the night air has
    that certain feeling in it, so I'm very hopeful they'll be around."

    "Night sprite started walking along the road. But instead of heading to
    the direction of the village, he was walking to the opposite direction."

    Sprite "We need to make a bit of detour on our way to the village, but
    it's not that far. There's a spring nearby and my friends often stay
    there when they come to this area."

    "[dreamer] was wondering what kind of friends night sprite was talking
    this time. Surely it wouldn't be yet another dragon nest. No matter what
    night sprite would say, [dreamer] would be hesitant to meet such
    creatures."

    scene bg unicorn_bg
    with dissolve

    "Soon they stepped from the road and continued through the woods. After
    reaching a small stream, night sprite started following it to the
    upstream. Suddenly, they stepped into a small clearing, where a stream
    connected to a small pond. And on the opposite side of the clearing were
    two unicorns."

    "[dreamer] had never seen anything so beautiful in [his] whole life. One
    of the unicorns raised his head and looked at the travelers, while the
    other continued eating the grass that covered the clearing. They had pearl
    white coat that glimmered in the moonlight."

    Sprite "Beautiful, aren't they? Unicorns travel over wide distances and
    don't tend to stay in one place for long. However, they tend to get
    attached to a special locations and like visiting them when they are
    around the area. This spring is one of such places."

    "Now both unicorns crossed the clearing and came very close. [dreamer]
    could see that their hooves weren't like horses had, but cloven. Their
    tail resembled more of a lion tail than of horse tail. But they moved
    very graciously and [dreamer] felt unfamiliar longing and sadness in [his]
    chest as [he] watched them."

    "[He] reached out and carefully stroked mane of the unicorn that was
    closest to [him]. [dreamer] was surprised to find that the mane felt like
    silken strands and not coarse at all. [He] started into intelligent eyes
    of the unicorn as [he] continue stroking the mane."

    Sprite "We should continue. The night is young, but there's still plenty
    of things to do."

    "Longingly [dreamer] said good bye to unicorns and then they turned back
    and started their journey back to the road. [dreamer] found it hard to
    later remember how long they had spent in the clearing. It felt like an
    eternity and split second at the same time."

    $ visited_unicorns = True

    jump fairy_meadow_again

label dragon_nest:
    Sprite "I already checked the mushrooms on the way here, so we don't have
    to visit there. Instead, we'll head directly to the dragon nest. I have a
    feeling that there's something really great there tonight. Lets see if my
    feeling is right."

    "Like last time, they walked along the road until the arrived to the large
    oak and then turned into the woods. Night sprite was walking more
    carefully than last time and avoiding making too much noise. Soon
    [dreamer] started to see the familiar red glow, the nest was near."

    "Night sprite had now stopped and was looking at the direction of the
    nest. He motioned [dreamer] to come closer and started talking in a low
    voice."

    Sprite "I was right. Look very closely and tell me what you see there."

    "[dreamer] trained [his] eyes and stared at the direction of the nest. At
    first [he] didn't notice anything strange, but then [he] realised that the
    glow was larger than before and slowly moving. After staring for another
    moment [he] realised that there were two dragons at the nest."

    Sprite "Correct, both dragons are at the nest. They probably caught their
    food early and have already returned to the nest. They seem pretty calm
    even. Do you think you would want to come there with me and introduce
    yourself?"

    menu:
        "Will [dreamer] go and see the dragons?"

        "yes":
            jump visit_dragons

        "no":
            jump admire_dragons

label visit_dragons:
    "[dreamer] swallowed. [His] throat was dry of fear, but after short
    hesitation [he] nodded. Not very often [he] would be able to meet real
    dragons."

    "Night sprite nodded and told [dreamer] to follow him. As they walked
    towards the dragons, dreamer was wondering if this was such a good idea
    after all. Those dragons looked larger and larger they got and night
    sprite had said that they didn't like unexpected visitors."

    "The dragons looked up. They had obviously sensed their presence. Night
    sprite started talking on a soothing voice and they continued towards the
    dragons slower than before."

    "Eventually they entered the glow of the nest and [dreamer] was staring
    two dragons from very close distance. They were much larger than [he] had
    guessed from the distance, but at the same time dragons were were elegant
    and sleek looking."

    scene bg dragon_faceoff_bg
    with dissolve

    "The dragons eyed them suspiciously and one of them leaned down to have a
    closer look. [dreamer] felt hot and sulfuric breath of it as it stared
    [him] from the touching distance. Without thinking, [dreamer] raised [his]
    hand and touched the bony beak of the dragon. They stared at each other
    and then dragon raised his head again."

    Sprite "You are either really brave or really stupid, perhaps even both.
    Stronger warriors than you have lost limbs from trying that. But it's
    clear that they accept you and we shouldn't have anything to worry about
    right now."

    "They stayed for a bit still, admiring the dragons who pretty much ignored
    them now and discussing in a low voice. Eventually it was time to leave
    and they slowly walked away. [dreamer] didn't really know what to think
    about the dragons and [he] was confused. They walked back to the road in
    silence and started following it again."

    $ visited_dragons = True

    jump fairy_meadow_again

label admire_dragons:
    "[dreamer] looked at the looming shapes in the distance and decided that
    [he] was already close enough. While the dragons looked beautiful, they
    were also quite scary looking in the darkness. [dreamer] forced [his]
    breath to normal, but still [he] was on the edge."

    Sprite "Aren't they beautiful? There aren't many left and they are very
    reclusive to begin with. Having a chance to see two of them together and
    a real nest is very rare thing indeed."

    Sprite "Dragons live really long time, but they don't often lay eggs. And
    eggs take several years before they will hatch. I think that dragons are
    not really from this world and they don't see things in the same way as we
    do. 10 years is for them like a morning is for us."

    Sprite "They don't build towns or cities, but I'm sure they're
    intelligent. They rarely communicate with anything else than other
    dragons. So, very mysterious and enigmatic creatures that nobody has been
    able to really figure out."

    "They stood in silence again. Dampness was creeping through shoes and
    [dreamer] shivered. Night sprite noticed that and turned back towards the
    road."

    Sprite "It's time for us to continue our journey. There's many places to
    go and many things to do. And the night is short enough without us
    standing here all night. Not that I don't like admiring the dragons. We
    can always come back some other night of course."

    "They starting walking through the forest. While they walked, [dreamer]
    and night sprite were conversing in a low voice. After arriving back to
    the road, they started following it again."

    jump fairy_meadow_again

label fairy_meadow_again:
    "After a while, [dreamer] and night sprite arrived to the meadow again.
    Like before they stood on the edge of the meadow and looked across it
    towards the lights of fairy village."

    if solve_alone:
        jump fairy_meadow_solve_alone

    Sprite "I think tonight we'll venture further into the meadow and see what
    can be done about the war between fairies and thunder beetles. I know some
    magic that allows us to shrink to a smaller size. That should ensure that
    we don't accidentally trample over their houses."

    Sprite "I have sent a word earlier letting them know that we'll arrive
    tonight. No reason to drop by unannounced, especially when the matter is
    as important as it's now. Our rides should arrive soon, better get ready."

    "Night sprite closed his eyed and muttered some intonation. Immediately
    everything around them seemed to grow enermous as they shrunk to size of
    fairies. [dreamer] looked around and admired how the world looked so
    different from their new perspective. Little twigs that [he] wouldn't have
    normally noticed were suddenly size of large logs."

    "As [dreamer] was exploring their surroundings, two large moths landed
    near them. Night sprite indicated that they should climb on them and off
    they went. The flight through night meadow was breath taking. [dreamer]
    could rather feel than see how they were weaving through the long grass
    and flowers. Soon lights of the fairy village were right in front of them
    and they landed on a clearing."

    if mediate:
        jump fairy_meadow_mediate

    if divide_meadow:
        jump fairy_meadow_divided

label fairy_meadow_mediate:
    "A fairy stepped out from the crowd that had gathered on the clearing and
    greeted them."

    Simbali "I'm Simbali, captain of the guard and will be representing
    fairies in the matter at hand."

    "While Simbali was greeting the night sprite and [dreamer], crowd parted
    and few thunder beetles emerged. They were large, burly and serious
    looking creatures."

    Chkakuth "I am Chkakuth and I am king of the thunder beetles. I have come
    here as night sprite summonned us."

    "[dreamer] sensed that the atmosphere was tensed and everyone present was
    ready for action. [He] started seriously thinking if this was a good idea
    to begin with and if they would survive through the meeting without a
    fight."

    Sprite "this is [dreamer]. I have bought [him] here to act as mediator.
    [He] is not affliated with either side and we all can trust [him]. Shall
    we move into the grand hall then?"

    "Simbali and Chkakuth hesitated and then turned towards a large building.
    [dreamer] and night sprite followed them with some other fairies and
    thunder beetles. Night sprite explained that they would be there to
    observe and act as secretaries."

    "The grand hall had a table set up in the middle and negotiators sat
    around it. Secretaries were positioned a little distance away from it,
    close enough to hear what was being talked, but far away enough so that
    they wouldn't disturb the negotiations."

    "Start of the negotiations was really tense. Both parties were very
    decided on what they wanted and were not willing to compromise at all.
    Night sprite was doing his best to guide the negotiations and from time
    [dreamer] did [his] best to help too. On the background, the scribes
    were busily writing down everything that was being said."

    "As time passed, [dreamer] was getting more and more agitated with the
    negotiatiors. They were arguing over insignificant details and complaining
    how they had to do all the hard work, while the other party just reaped
    the benefits. At this rate the negotiations would take years and the only
    result would be heaps and heaps of paper."

    "[dreamer] suddenly stood up and slammed both of [his] palms on the table.
    The room was completely silent, most of those present even forgot to
    breath for a moment. All eyes were on [him] and [dreamer] was starting to
    feel hesitant. Then [he] noticed night sprite giving a slight nod and got
    [his] courage back."

    "[dreamer] started explaining how they were getting nowhere by fighting
    and arguing about petty little things. In the beginning, [his] voice was
    shaky, but as [he] continue, it grew stedier. [dreamer] explained that it
    really didn't matter how many butterflies fairies were allowed to have or
    how long tunnels thunder beetles could dig."

    "Simbali and Chkakuth glanced each other sheepishly as [dreamer] said that
    so far the negotiations had been closer to an argument on a school yard
    than to group of adults trying to find a solution that everybody could
    agree. Eventually [dreamer] ran out of steam, looked around flustered and
    then slumped back to [his] chair."

    Simbali "I think [dreamer] is correct and I apologize on the behalf of the
    fairies. I hope we can start the discussion again, with fresh minds and
    find a solution that works for all of us."

    Chkakuth "Thunder beetles are not without fault either. We're ready to
    try and find a solution that helps us to live in peace. The meadow is
    large and there is enough space for all of us. Especially when we
    remember that thunder beetles prefer to live underground while fairy folk
    love to see sun, moon and stars."

    "The negotiations resumed with much different agenda. They still weren't
    particularly easy, but this time both parties were trying to find a
    solution that would work for everyone, instead of trying to win and
    outsmart their opponent."

    "Eventually there was a decision to continue negotiations at a later time.
    There were still some open issues, but the big picture was starting to
    be clear for everyone. Chkakuth and Simbali thanked night sprite and
    [dreamer] for their help and hoped they would join them in the future too.
    They waved them good bye as [dreamer] and night sprite took off on a
    night moths."

    "Night sprite was on a good mood as they reached the edge of the meadow.
    He cast the spell to return them back to normal size and they resumed
    their journey on the road."

    Sprite "You did really well there. I was starting to lose all hope that
    the negotiations would have any chance of succeeding. But you managed to
    get us back on track. There's still a lot to do, but the first steps have
    been taken and they are the most important ones."

    "Stars were twinkling high above their heads as the two travelers were
    walking on the road. [dreamer] was already thinking of the celebration
    that would be waiting them in the village. [He] was starting to get
    hungry and food would really hit the spot."

    jump continue_towards_village

label fairy_meadow_solve_alone:
    Sprite "My heart is heavy, but I guess there's no other way now than to
    leave them to solve their differences by themselves. We wouldn't be able
    to help them when the situation is as tensed as it is now. Maybe in the
    future though..."

    "Night sprite sighed heavily and [dreamer] felt night around them like a
    suffocating blanket. [He] didn't know any of the fairies or thunder
    beetles, but still the thought of two warring groups made [him] sad."

    Sprite "Don't worry too much about them. They have been against each other
    for a very long time. Couple more years here or there won't make a
    difference in the large scale. Of course for the individuals even a single
    day might be a crucial difference. But that's how it always is."

    Sprite "Even if we leave them to their own devises, we should check back
    from time to time and see if there's anything we can do to nudge them to
    a more peaceful direction. Forcing a peace isn't an option, so we must
    be patient and calm."

    Sprite "Lets continue further on, there's a certain celebration that is
    waiting and I wouldn't want to miss that. Harvest has been good and there
    is much reason to celebrate tonight."

    "Night sprite started walking down the road and [dreamer] followed him.
    For a while they walked in a silence, but soon their spirits started to
    rise and mood was merrier again. [dreamer] was already looking forward the
    harvest celebration."

    jump continue_towards_village

label fairy_meadow_divided:
    "A fairy stepped out from the crowd that had gathered on the clearing and
    greeted them."

    Simbali "I'm Simbali, captain of the guard and will be representing
    fairies in the matter at hand."

    "While Simbali was greeting the night sprite and [dreamer], crowd parted
    and few thunder beetles emerged. They were large, burly and serious
    looking creatures."

    Chkakuth "I am Chkakuth and I am king of the thunder beetles. I have come
    here as night sprite summonned us."

    Sprite "Right, lets get down to business and get this over with as soon
    as we can."

    "Simbali and few other fairies showed way to a large building, while night
    sprite, [dreamer] and few thunder beetles followed. Inside the building
    was a large hall with table in the middle. As soon as everyone had been
    seated, night sprite continued in a stern voice:"

    Sprite "As you all know, fairy folk and thunder beetles have been in war
    for a very long time. Numerous attemps have been made to solve the
    situation, but nothing has been worked so far. Thus, instead of solving
    the situation, we are going to limit the damages as much as possible."

    Sprite "The meadow will be divided in two and an area will be placed in
    the middle where none of you will have any business being on. Both sides
    are free to guard their side in the way they see fit. The middle ground
    will be guarded by sentries that are neutral."

    "Fairies and thunder beetles started to protest. They feared that the
    sentries wouldn't be neutral or could be surprised by their enemies. The
    exact location of division was an important matter too and both sides
    wanted to grab as much land as possible."

    "[dreamer] felt sorry for everyone. In a way [he] understood what was
    going on and why thunder beetles and fairies tried to protect their
    domains. But on the other hand [he] couldn't fathom why they couldn't just
    make peace and find a way to live together. The meadow surely should be
    big enough."

    Sprite "The meadow will be divided where the stream flows. In the coming
    weeks thunder beetles and fairy folk will move to their own sides. After
    passage of 4 weeks everything should be ready. At that point a group of
    water sprites will move in and settle in the stream and on its banks.
    They will act as sentries and make sure that our agreements are
    respected."

    Sprite "We are doing this while hoping that the future will be different.
    Now the most important thing is to stop the fighting and give everyone
    time to calm down. After some time, we will revisit this decision and
    see if we can try again to live in peace and among each other. But until
    then, the meadow shall be a divided domain."

    "As the meeting ended, thunder beetles gathered their items and started
    their journey through the meadow. Night sprite and [dreamer] watched
    their departing in silence and then starting making preparations for
    their own departure."

    "The flight back to the edge of meadow was somber and [dreamer] felt heavy
    weight on [his] shoulders as they started along the road once again.
    [He] knew that there would be a celebration waiting for them in the
    village and the journey wouldn't take long, but it was hard for [him]
    to feel happy about it."

    jump continue_towards_village

label continue_towards_village:
    "Eventually the woods started to thin and [dreamer] knew that the village
    was really close. After the next bend in the road, they arrived to a
    location where they could see the village nestled in between of all the
    fields. Colourful lanterns had been placed all around it and a bonfire
    had been set on the market square."

    if harvest_with_humans:
        jump celeb_village

    if harvest_without_humans:
        Sprite "Cats have probably started their own celebration too in
        secrecy. If you want, we can join them there. However, if you rather
        would celebrate with the humans, you can go there too. I can't really
        join with you there though."

        menu:
            "Who should we celebrate with?"

            "join villagers":
                jump celeb_village
            "join cats":
                jump celeb_secret_cats
  
label celeb_village:
    Sprite "They started celebrating as the sun went down and will continue
    until morning. You have plenty of time still to join the villagers and
    enjoy the festivities. The cats will be there too, but they will be
    keeping their distance I would assume."

    Sprite "I won't be joining the villagers, they don't really know me after
    all. While they have an idea that something like me exists, I have
    deliberately kept my distance and let them to take care of their own
    matters. But I'll be somewhere nearby, in case you need me."

    "[dreamer] continued towards the village as the night sprite disappeared
    in the shadows. [He] could hear the laughter and merry-making already even
    at this distance. Delicious smell of food lingered in the air and [he]
    started walking faster."

    "Soon [he] entered the market square, which was packed full of people.
    Tables have been carried outside and placed all around it. A large bonfire
    was in the middle and several smaller ones had been lit on the edge of the
    market square. Smell of roasted meat was in the air and mixed with fresh
    bread, exotic spices and other food items."

    if harvest_with_humans:
        "As [dreamer] walked in the market square, two cats emerged from a
        side alley. They stopped briefly and watched [him]. Then they nodded
        and went on their way as [dreamer] raised [his] hand in a greeting."

    baker "Hello there. I think I haven't seen you around here before. I'm
    Baker and welcome you to join our harvest festival."

    "A large and friendly looking man had spotted [dreamer] and was talking to
    [him]. [dreamer] replied and explained that [he] was just passing by, when
    the sound of the festival had caught [his] attention."

    baker "No worries at all. We in the dream land have gotten used to all
    kinds of people passing by. It would be a strange week when we didn't
    see any new faces."

    baker "Here, have a seat and take something to eat. Would you like som
    sesame seed bread? I baked it by myself just for the occasion. It's a
    special recipe that has been handed down for generations in our family."

    "[dreamer] sat down and took some of the bread that Baker offered. It
    was fluffy and tasted very good. A bowl full of steaming meat stew was
    brought to her and [he] started eating it with a good appetite. While
    [dreamer] was eating, Baker was telling stories about the village and
    its inhabitants. He knew people of the village very well and had many
    funny stories to tell."

    if harvest_with_humans:
        "As [dreamer] was eating, a red cat jumped on the bench next to [him]
        and butted its head against [his] side. [dreamer] reached at it and
        scratched the cat behind ear. It started purring immediately. After
        staying there for a moment, the cat jumped off the bench and
        disappeared somewhere."

        baker "That's Molly, she's old Jameson's cat. Usually she's quite
        a bit more shy and don't like strangers at all, but she seems to
        have taken liking to you."

    "A bit later a woman joined their company and brought some mead with her.
    She introduced herself as Cutter, the local carpenter, who had made all
    the chairs and the tables on the market square. She was cheerful person
    and [dreamer] immediately liked her friendly manners."

    cutter "And then there was this time when I was making a new garden
    benches for the Mr. and Mrs. Sandhurst. I had cut all the parts and was
    doing fitting, so benches had been assembled, but had not been properly
    joined yet. So, Mrs. Sandhurst comes to visit and decides to test sit
    one of the benches while I'm inside. I head a loud crash and when I ran
    outside, she's lying there in the middle of the all the bench parts."

    "[dreamer] and Baker were laughing with tears in their eyes. Cutter was
    good at telling stories and this one she apparently had told many times.
    Cutter sipped her mead and asked Baker to tell a story. She didn't have to
    ask twice and soon Baker was in the middle of the story about how he was
    supposed to bake two dozen saffron rolls, but used dried chili instead of
    saffron."

    "Eventually the celebration started to quiet down and people started
    heading their homes to sleep. [dreamer] enjoyed last heat of the embers
    that were still left of the bonfire and then left the market square. [He]
    headed to outside of the village to wait for night sprite."

    if harvest_with_humans:
        "On [his] way out of the village [dreamer] passed a group of three
        cats who were lying under a tree. One of the cats looked up as [he]
        passed and lazily yawned. [dreamer] waved to them as [he] walked
        past them and out of the village."

    jump decision

label celeb_secret_cats:
    Sprite "The cats sent me a message earlier telling where their celebration
    is being held. We don't need to enter the village, but head into one of
    those barns over there, outside of the village. The cats have gathered
    there, as villagers aren't going there tonight."

    "[dreamer] looked the direction night sprite was pointing and saw a barn
    not far away from them. The doors were closed and it was completely dark.
    [He] wouldn't have been able to guess that there was a celebration going
    on inside it, if [he] hadn't been told so."

    "They stepped from the road and started walking towards the barn. Field
    was bare as the harvest had been gathered recently. [dreamer] found
    [himself] wondering what kind of celebration the cats would be having.
    [He] hadn't really thought it before. Hopefully something that [he] could
    participate."

    "As they stepped in the front of the barn, night sprite pointed out a
    small crack on the wall that was partly hidden by a haybale. The sneaked
    through it and then they were inside of the barn. Some bales had been
    arranged to block out the light from showing through the crack and
    [dreamer] had to walk around them."

    black_cat "Well, well, look who have arrived. Welcome to the harvest
    celebration of the cats."

    "The black cat bowed to them and gestured them to step further in.
    [dreamer] saw that bales had been pushed to the sides of the barn, so that
    they would block all the light from escaping outside. In the middle, there
    was clear space that was surrounded by steps and tables made of bales.
    And everywhere [he] looked, [dreamer] saw cats of all colours and sizes."

    "On the tables there were all kinds of foods and drinks. Night sprite took
    some bread and offered it to [dreamer] who took it and tasted it. The
    bread was very fresh, it couldn't have been baked longer than an hour ot
    two ago."

    black_cat "Every cat brings a little bit food or drink to the celebration.
    That way we have enough to eat and nobody has to bring too much. Many
    people give cats something nice to eat during the harvest celebration and
    it all ends here."

    "Another cat walked to greet them. This one was red with stripes and thick
    fur. It nodded to night sprite and looked [dreamer] from head to toe and
    back."

    red_cat "I remember you from the meeting some nights ago. You were in the
    village as we were discussing whether to have harvest celebration among
    the villagers or all by ourselves. I must admit that it's really nice to
    be here for a change, haven't had a harvest celebration without villagers
    in a while."

    "[dreamer] nodded. That was all [he] could do, since [his] mouth was full
    of delicious bread and speaking with mouth full would have been impolite.
    This seemed to amuse the red cat, who chuckled a bit."

    red_cat "I'll be heading back with my friends. It was nice meeting you
    again. If you want to have a chat later, I'm free."

    black_cat "I'll do the same thing as well. Enjoy your stay here. We don't
    have any formal program, so feel free to mingle with others, eat some
    food and generally just have a good time."

    "[dreamer] nodded again. Then [he] finally managed to finish the bread and
    thanked the two cats best [he] could. Night sprite seemed to be having
    fun and [dreamer] shot a stern glance at him."

    Sprite "Just having a bit of fun, no worries. Don't worry too much, but
    have another bite. Those pies look positively delicious."

    "Night sprite and [dreamer] each took small pies and then headed to a
    group of cats to see what they were talking about. Soon [dreamer] found
    [himself] in the middle of a debate whether the cat was created when the
    lion sneezed or not."

    "Eventually the celebration started to wind down. Cats started
    disappearing one by one. [dreamer] yawned, [he] had been up all night and
    was getting really tired."

    Sprite "Lets go, I know this nice stone nearby where we can sit for a bit
    and watch as the sun gets ready to get up."

    "[dreamer] agreed and they slipped outside. It was still dark, but the sky
    wasn't as deep blue as when they entered the barn. The field was covered
    in morning dew and [dreamer] soon found [his] feet wet. Night sprite lead
    them to a small pile of stones that was at the edge of the field."

    jump decision

label decision:
    "[dreamer] sat on a stone and watched as the sky was slowly starting to
    grow lighter. It wouldn't take long before the dawn and [he] would have
    to return back to waking world."

    Sprite "Another night is over and a new day will start again. Soon it
    will be time for me to hide away and let the dream world to run its own
    course. It would be nice, if I could have an eye on the world during the
    day too, but it's not really possible for me."

    Sprite "You on the other hand, would not have a problem walking here
    during the day time. And as far as I have seen, you have sensible ideas
    about the world. What do you think? Would you want to help me to look
    after the dream world? We could meet during dusk and dawn to see how
    things are currently going."

    "[dreamer] was pondering. On the one hand, it sounded like a really
    exciting arrangement, but on the other hand the responsibility was
    concerning [him]. Would [he] be able to do all the correct decisions when
    the night sprite weren't there to guide [him]?"

    menu:
        "What will [dreamer] decide?"

        "Help the night sprite":
            jump night_end_help

        "Decline to help":
            jump night_end_no_help

label night_end_help:
    Sprite "That is great, I'm glad to hear that you're willing to help me.
    I shall send a word around that you are helping me in governing the dream
    world. Next time you come to visit the dream world, I'll be waiting for
    you in that same clearing we originally met."

    Sprite "But now I must go, before the day really breaks. Take care
    [dreamer] and have safe journeys."

    "[dreamer] started helping night sprite with his duties and soon got quite
    good at them. [He] was respected for all the hard work and devotion [he]
    put into the task."

    if night_mushrooms:
        "There were some trouble with mushrooms now and then, but nothing too
        major. It seemed that visitors of dream world were more likely to take
        a bite from large mushrooms than before. The reason for this was never
        discovered and since it wasn't a big problem, was never really
        investigated that much."

    if visited_dragons:
        "[dreamer] was held in very high regard because somehow [he] had been
        able to befriend the mighty dragons. Nobody knew how this was
        possible and it hadn't ever happened before. Nevertheless, [dreamer]
        knew dragons and that was something to respect."

    if visited_unicorns:
        "There were rumours that when moon was full and stars bright,
        [dreamer] often met with unicorns in the woods. Nobody had actually
        seen this happen, as unicorns were very rare animals, but people still
        whispered about it."

    if mediate:
        "The old strife between thunder beetles and fairy folk was finally
        solved thanks to the help of [dreamer] and night sprite. It wasn't an
        easy task and it wasn't done quickly, but in the end it happened.
        [dreamer] got nickname 'the soothsayer', because of [his] great skills
        in negotiation."

    if solve_alone:
        "The old strife between thunder beetles and fairy folk was not solved
        properly. They tried arranging their own negotiations from time to
        time, but without too much of success. [dreamer] and night sprite kept
        close eye on both groups though and patiently waited for time when
        they could step in and guide them to peace."

    if divide_meadow:
        "The old strife between thunder beetles and fairy folk was solved with
        force. The meadow was divided between them and sentries were placed
        on the border to guard it. Even while fighting between the inhabitants
        of the meadow ceased, the solution was far from the optimal."

    "[dreamer] liked [his] new duties and tried [his] best to be good at them.
    Eventually [he] decided to stay completely in the dream world and moved in
    to a small house at the edge of the village. Villagers liked this
    arrangement and made sure [dreamer] always had fresh food and warm clothes
    at [his] disposal."

    return

label night_end_no_help:
    Sprite "I understand that you're wary of the responsibility. I hope that
    you still will visit us from time to time and drop by to have a chat.
    There are always new things to see and experience in the dream world."

    Sprite "But now I must go, before the day really breaks. Take care
    [dreamer] and have safe journeys."

    "[dreamer] watched as the night sprite disappeared into shadows and then
    turned to watch the sunrise. Soon it would be time for [him] to wake up,
    but there was still a little bit of time to enjoy the rays of sun."

    jump closing_the_book

label closing_the_book:
    "As time passed, [dreamer] started visiting the dream world less often.
    [He] had grown up and was busy in the waking world. [dreamer] graduated,
    moved into [his] own apartment and started working. One day [he] met the
    just perfect person and eventually a wedding was held."

    "[dreamer] had pretty much forgotten the old book and the adventures [he]
    had in the dream world. Sometimes [he] almost remembered them when [his]
    children were telling stories about the adventures they had while
    sleeping, but usually [dreamer] just pushed the memories aside."

    return
