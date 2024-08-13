# Information-Retrieval-Example
This repository presents an example of an Information Retrieval application, which consists of a command-based joke browser implementation. The dataset used, [Short Jokes](https://www.kaggle.com/datasets/abhinavmoudgil95/short-jokes), contains over 200,000 short jokes on different topics. The authors indicate that, since data is collected by web scraping, inappropriate or offensive jokes are likely to be found.

## Installation
Clone this repository:
```bash
git clone git@github.com:daniel-lima-lopez/Information-Retrieval-Example.git
```

move to installation directory:
```bash
cd Information-Retrieval-Example
```

install [Natural Language Toolkit](https://www.nltk.org/index.html):
```bash
pip install nltk
```

## Method description
Information retrieval is finding material that satisfies an information need. In this case, given a corpus of jokes, the information need is expressed by tokens or querey words and logical operators (AND, OR, NOT). 

To perform this task, it is construted a dictionary of terms, which contains every word in the corpus of jokes. Then, for each term, we have a set, denominated *posting*, that contains the indexes of the jokes where the term appers, this technique is called *inverted index*.

Once all postings are constructed, we can perform queries with terms of interst and logical operators.

## Examples of use
The following examples can be executed in the notebook [examples.ipynb](examples.ipynb).

We can performs simple commands executing [IR.py](IR.py):
```bash
python IR.py
```
and introduce a valid command, considering common terms an logical operations in lower case (and, or, not):
```
Enter a valid command: dog or cat and funny and not smoke

Results:
 - You know what cats don't like? Blow dryers. You know what's funny? Pointing your blow dryer at your cat. Anyway, I lost an eye today.
 - I have a dog named Hot-Dog. Isn't funny? hahahaha....
 - I use my neighbor's outdoor jacuzzi for bubble bath time with my cat. I'd invite him, but my cat's funny about bathing with strangers.
 - What diagnosis did the veterinarian give to the dog with the funny walk? The dog has cerebral pawlsy.
 - No wonder my cigar tastes funny. It's just a really old hot dog.
 - A funny thing to do when someone's dog barks at you is say, "I don't speak dog," and then when they leave the room, speak dog fluently.
 - Bad news, guys. Throwing a cat through a wall doesn't make a funny, cat-shaped hole. Not even close.
 - My 1-year-old thought it was funny to put food in my mouth. It was cute with Skittles. Then she switched to dog food.
 - My Dad's cat had a hernia operation The cat was laying there next to next to me and I asked " What did they sew you up with?" My Dad laughing so hard - as he said "That's not funny!" [Cat Gut]
 - Funny how we say "I drank a *pot* of coffee" instead of "I drank fourteen cups of coffee and chased the cat around the hot tub with a sword"
 - Only funny if you own a dog: I think my dog must have a very cold nose. Every time it walks into a room, all the other dogs sit down.
```

It is posible to perform more complex commands with the `Searcher` class. For example, the command *(computer or laptop) and (sad or amazing)* can be executed by parts with set operations:
```python
from IR import Searcher

test = Searcher() # instantiate the Searcher class
ind1 = test.filter('computer or laptop') # first command
ind2 = test.filter('sad or amazing') # second command
jokes = test.get_jokes(ind1 & ind2) # union of commands

print('Results:')
for ji in jokes:
    print(f' - {ji}')
```
which results in:
```
Results:
 - Why is the Computer D Drive always sad? D:
 - Today was a sad day - we had to pull the plug on my granpa cause I needed the outlet for my laptop
 - Why was the middle aged computer sad? He had a floppy disc.
 - What do you call a computer with an amazing singing voice? A Dell.
 - I should go outside and enjoy the amazing weather but my computer cord isn't long enough.
 - It's amazing how quickly reheated food in the microwave goes cold again when you think you're only going to be on the computer for a moment.
 - What kind of computer is optimized for sad songs? A Dell.
 - What do you call a computer that only plays sad songs? Adele
```