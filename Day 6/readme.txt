Basically just dit Reeborg excercises on the website. so going to look for another excercise to do for this day

### **Project Overview: Word Scrambler Game**

The Word Scrambler Game is a fun project where the program takes a word, scrambles the letters, and prompts the user to guess the original word. You can add features like tracking the number of attempts or providing hints if the user struggles.

### **How to Start**

1. **Step 1: Plan the Workflow**
   - **Input:** The program should prompt the user for a word (or you could use a predefined list of words and randomly select one).
   - **Process:** Scramble the word by shuffling its letters.
   - **Output:** Display the scrambled word and ask the user to guess the original word.
   - **Additional Features:** Track the number of attempts and provide hints after a certain number of wrong guesses.

2. **Step 2: Break Down the Tasks**
   - **Input Handling:** Get the word from the user or select a word from a list.
   - **Scramble Logic:** Implement a function to shuffle the letters in the word.
   - **User Interaction:** Display the scrambled word and prompt for guesses.
   - **Validation:** Check if the user’s guess is correct and provide feedback.
   - **Looping:** Allow multiple attempts and possibly loop the game for multiple rounds.

3. **Step 3: Write the Functions**
   - **Separation of Concerns:** Write separate functions for different tasks, like `get_word()`, `scramble_word(word)`, `get_user_guess()`, and `check_guess()`.
   - **Keep It Simple First:** Start with the basic functionality of scrambling and guessing before adding more features like tracking attempts or providing hints.

### **Best Practices to Follow**

1. **Modular Design:** 
   - Break down the project into smaller functions. Each function should have a single responsibility. For instance, one function scrambles the word, another checks the user's guess, etc. This makes your code easier to understand, test, and maintain.

2. **Documentation and Comments:** 
   - Write docstrings for each function to describe what it does, its inputs, and its outputs. Comment on tricky parts of the code to explain your thought process.

3. **Input Validation:** 
   - Ensure that your program handles unexpected input gracefully. For example, check that the word input by the user isn’t empty and that the guess has the correct number of letters.

4. **Testing:** 
   - Test each function individually before integrating them. You can use simple print statements or, if you're feeling adventurous, write basic unit tests to verify the functionality.

5. **Iterative Development:** 
   - Start with the simplest version of your game. Once that works, add complexity like tracking the number of attempts or providing hints. This approach prevents you from getting overwhelmed and allows you to debug more effectively.

6. **User Experience:** 
   - Think about the user experience—how will the user interact with your program? Is the output clear? Are the instructions easy to follow? Consider how you would like to play the game and design accordingly.

### **Additional Tips**

- **Refactor Often:** As you add new features, revisit your code to ensure it's clean and efficient. Refactor repetitive code into reusable functions.
- **Practice Debugging:** If something doesn’t work as expected, try to debug systematically. Use print statements or Python’s built-in debugger (`pdb`) to trace the issue.
- **Experiment:** Don’t be afraid to try different approaches to solving the problem. This will help you understand Python’s capabilities better.

By following these steps and best practices, you'll not only build the Word Scrambler Game but also develop good coding habits that will benefit you in future projects.








### **Step-by-Step Guide for Building the Word Scrambler Game**

#### **Step 1: Plan and Set Up**
1. **Understand the Problem:**
   - Clearly define what the program should do: scramble a word and let the user guess it.
   - Identify the main tasks: word input, scrambling, user interaction, and validation.

2. **Set Up Your Environment:**
   - Open your preferred Python editor or IDE.
   - Create a new Python file (e.g., `word_scrambler.py`).

3. **Outline the Program Structure:**
   - Decide on the functions you'll need, such as `scramble_word()`, `get_user_guess()`, and `check_guess()`.
   - Plan the main loop that will run the game.

#### **Step 2: Write the Basic Functions**
1. **Function 1: Scramble Word**
   - **Goal:** Write a function that takes a word as input and returns a scrambled version.
   - **Hint:** Use Python’s randomization tools to shuffle the letters in the word.

2. **Test Scrambling:**
   - Print the scrambled word to ensure your function works correctly.
   - Test with different words to verify the scrambling is sufficiently random.

3. **Function 2: Get User Guess**
   - **Goal:** Create a function that prompts the user to guess the original word.
   - **Hint:** Use a `input()` function to capture user input.

4. **Test User Interaction:**
   - Run the program to ensure it asks the user for a guess and captures it correctly.

#### **Step 3: Implement the Game Logic**
1. **Function 3: Check the Guess**
   - **Goal:** Write a function to compare the user’s guess with the original word.
   - **Hint:** Use conditional statements to provide feedback (correct/incorrect).

2. **Integrate Basic Functions:**
   - Combine the functions in a simple loop where the word is scrambled, and the user tries to guess it.
   - Add a condition to end the loop when the correct word is guessed.

3. **Test the Basic Game:**
   - Run the full game flow to ensure it works as expected. Make sure the word scrambles, user can guess, and the program correctly identifies if the guess is right.

#### **Step 4: Add Enhancements**
1. **Track Attempts:**
   - **Goal:** Implement a counter to track the number of attempts the user takes to guess the word.
   - **Hint:** Initialize a counter variable and increment it each time the user makes a guess.

2. **Provide Hints (Optional):**
   - **Goal:** Offer hints after a certain number of wrong attempts.
   - **Hint:** You could reveal the first letter of the word or inform the user how many letters are correct.

3. **Loop the Game:**
   - **Goal:** Allow the user to play multiple rounds by asking if they want to play again after each round.
   - **Hint:** Use a while loop that continues until the user chooses to quit.

#### **Step 5: Final Testing and Polishing**
1. **Test All Features:**
   - Run the game multiple times to ensure all features (scrambling, guessing, attempts, hints) work together smoothly.
   - Test edge cases, like entering a blank guess or non-alphabetic characters.

2. **Refactor Code:**
   - Review your code for any repetitive sections or long functions. Break them down into smaller, more manageable pieces if necessary.
   - Ensure your code is clean, well-organized, and easy to read.

3. **Add Comments and Documentation:**
   - Write docstrings for each function explaining what it does.
   - Add comments where needed to explain complex or important parts of the code.

4. **Polish User Interaction:**
   - Refine the prompts and feedback to make the game user-friendly.
   - Ensure the output is clear and intuitive.

#### **Step 6: Reflect and Learn**
1. **Review Your Work:**
   - Look back at the steps you took. Consider what worked well and what challenges you faced.
   - Identify areas where you could improve or add additional features in the future.

2. **Experiment Further:**
   - If you have extra time, try adding new features, such as different difficulty levels or a time limit.
   - Consider how you might refactor the code to handle more complex cases or scale the game.

By following these steps, you'll systematically build your Word Scrambler Game, gaining valuable experience in structuring a small project and learning when to focus on different aspects of the development process.