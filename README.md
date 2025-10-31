Guide to clone our repo. 
Clone the repository using the code below in your terminal 
The owner of the repository should send an invitation to the rest of the team. Once the invitation is accepted, every team member should clone the repository to their local machine:
   git clone (https://github.com/MatteoGuardamagna4/textutils-team13)
   ```
   This will create a local copy of the shared project on your computer.
Environment of our team: environment.yml.
On your terminal, enter this:
micromamba create -f environment.yml -y.
micromamba activate textutils.
With this, now you will have the same environment as the host of the repository.
Run test.
In the terminal, First do pip install -e and than  enter pytest and this will check if there is any error in the functions.
Project does:
In our main branch, you can find these functions:
*word_counts – counts the words in the input → Example: "Hello world" → 2
*average_word_length – gives the average word length → Example: "I love Python" → 4.0
*count_vowels – counts vowels (a, e, i, o, u) → Example: "Education" → 5
*unique_words – returns unique words alphabetically → Example: "red red blue" → ['blue', 'red']
*sentence_count – counts sentences → Example: "Hi! How are you?" → 2
*slugify – makes a lowercase, hyphenated string → Example: "Hello World!" → "hello-world" 

