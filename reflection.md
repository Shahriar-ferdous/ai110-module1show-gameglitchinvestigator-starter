# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

--- I expected the game to give hints for coorcet guesses but it kept giving me wrong hint. For example if the secret number is lower than my input the hint tells me to go even lower amd vice versa. Also changing the mode of the game let's say to hard has range of number 1-50 but the secret number is sometimes higher than the expected range. Also the new game feature doesn't work when I have guessed a number and I want to start over, the new game button doesn't work to start a new session.
## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

--- I used copilot agent for this project. One of the examples of suggestion that was correct is when AI suggested why the game failed in terms of hints going backward and it was a simple fix. i verified the result by testing out the actual game with inputs and outputs.

One example of AI suggestion that was incorrect is how AI suggested a fix that after succesfully guessing and starting a new game the user can't submit the new number. I verfied it by testing out the actual game and starting a new game after guessing a number.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I decied bug fix through testing the game and trying out different inputs to see all the features are working. One of the test I ran using pytest was the that the hint directions are correct and it showed me how the game logic worked and how to test out features. AI helped me with the new test generation and fixed some errors in the original test file.
## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

--- The secret number kept chaning because when we hit new game button, a new session start. I will explain streamlit rerun to a friend like typing in a box. This keeps running in the background and refreshes the whole page. Session state is like a special storage box that remembers data between these reruns. You can store things like user scores or game secrets. The main change was adding logic to regenerate the secret number whenever the difficulty level changes. Originally, the secret was only set once at the start, so switching from "Normal" (1-100) to "Hard" (1-50) kept the old secret, which could be outside the new range.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I would like to reuse form this project is the prompting technique and how good prompts can give you accurate results. I would probably spend more time understanding the components of the given task a little more and understand how it coordinates with ecah other. I think this project helped me understand how AI can work really well with given context and pipoint the exact point of error.