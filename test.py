from transformers import pipeline

text = '''
It’s hard to top a kick in the nuts.

Especially when the kicker is Linda McMahon, the Connecticut Republican candidate for the U.S. Senate. Pure comedy gold.

Jon Stewart watches the tape and doubles over with laughter. He and fifteen of The Daily Show’s writers, producers, and performers are gathered around a 40-inch flat-screen TV inside the show’s Eleventh Avenue offices early on a Thursday morning in August. Creating a segment for tonight’s Daily Show around this footage, from one of World Wrestling Entertainment’s harmless little skits, would seem to be easy. Maybe they can just run the nut shot repeatedly. Along with another clip of McMahon, the co-founder and former CEO of WWE, chugging a beer and drooling foam down her cheek.

Except that the goal here isn’t simply topping the kick in the nuts—it’s using the scrotum slam in the service of a larger point. Oh, Stewart & Co. enjoy a lowbrow laugh as much as the folks over at South Park; heck, next week they’re publishing a book that includes some excellent masturbation jokes. But Stewart and The Daily Show became America’s sharpest political satirists by aiming at least a little bit higher.

“Slut! Slut! Slut!” The next clip shows McMahon’s daughter entering the wrestling ring to a booming chant from the crowd. Followed by McMahon’s deadly serious face, in a Nightline interview. “Oh my God,” Stewart interjects. “How do you answer that as a politician? ‘Well, you don’t know my daughter’? Or, ‘You know, the use of the term slut was obviously inadvertent’?”

This sets off a spasm of free-associative jokes from the other writers. “Or, ‘You don’t understand—Americans love this shit.’ ”

“What if we ran the clip like Super Mario Brothers, and every time she kicks that guy in the nuts, a gold coin comes out?”

“Was McMahon endorsed by Triple H? Or was it Triple X?”
'''

summarizer = pipeline('summarization')

summarizer(text, max_length=100, min_length=30, do_sample=False)

print(summarizer)