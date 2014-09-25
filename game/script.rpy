# game starts here

define limbaugh = Character('?', color="#6633cc")
define Limbaugh = Character('Limbaugh', color="#6633cc")

image bg house = "opening_house.png"
image bg book = "book.png"

init python:
    menu = nvl_menu
    config.nvl_paged_rollback = True

label start:
    scene bg house

    "There was a child, who lived in a house with mother and father. They were
    happy together and while they were not rich, they didn't lack anything
    important."

    scene bg book

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

    "After a while of walking, it was time to stop and rest. The child sat under
    some large mushrooms that were growing next to the road. All that walking
    had resulted into a hunger, but how would one go about solving that? Big
    mushrooms could probably be eaten, but what if they were poisonous? One
    shouldn't eat strange mushrooms, that much have been taught to the child."

    limbaugh "foo"
