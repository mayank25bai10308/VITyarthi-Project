import datetime
import time
import sys

class EngineeringQuizApp:
    """
    A simple command-line quiz application for first-year engineering fundamentals.
    The class structure ensures modularity (Data, Logic, Storage/Reporting) 
    and adherence to professional coding practices.
    """
    def __init__(self):
        # --- 1. DATA STORAGE MODULE (The Question Bank) ---
        self.question_bank = [
            {
                "question": "Q1: In basic electrical engineering, what does 'R' represent in Ohm's Law (V=IR)?",
                "options": ["1. Reactance", "2. Resistance", "3. Reluctance", "4. Radiance"],
                "answer": 2
            },
            {
                "question": "Q2: Which principle of Engineering Mechanics states that the sum of forces and moments about any point is zero for a body in equilibrium?",
                "options": ["1. D'Alembert's Principle", "2. Bernoulli's Principle", "3. Lami's Theorem", "4. Newton's Third Law"],
                "answer": 1
            },
            {
                "question": "Q3: In C programming, which of the following is used to dynamically allocate memory?",
                "options": ["1. new()", "2. malloc()", "3. create()", "4. allocate()"],
                "answer": 2
            },
            {
                "question": "Q4: A material is said to be ductile if it exhibits which of the following characteristics?",
                "options": ["1. High hardness", "2. High resistance to fracture after the yield point", "3. Ability to be drawn into wires", "4. High stiffness"],
                "answer": 3
            },
            {
                "question": "Q5: In Engineering Graphics, what is the view showing an object as it would appear to the eye (in 3D), without projection lines?",
                "options": ["1. Orthographic View", "2. Isometric View", "3. Perspective View", "4. Sectional View"],
                "answer": 3
            }
        ]
        self.score = 0
        self.total_questions = len(self.question_bank)
        self.LOG_FILE = "engineering_quiz_history.txt"
        self.USER_ID = "ENGG_" + datetime.datetime.now().strftime("%y%m%d%H%M") # Mock ID for logging

    # --- 2. LOGIC MODULE (Input Validation & Grading) ---
    def get_user_choice(self):
        """ Handles user input with robust error checking (NFR: Robustness/Error Handling). """
        while True:
            try:
                user_input = input("\nEnter choice (1-4, or 'q' to quit): ").lower()
                
                if user_input == 'q':
                    print("\nExiting quiz. Goodbye!")
                    sys.exit(0)

                user_choice = int(user_input)

                if 1 <= user_choice <= 4:
                    return user_choice
                else:
                    print("❌ Please enter a number between 1 and 4.")
            except ValueError:
                print("❌ Invalid input. Please enter a number or 'q'.")

    def provide_remarks(self):
        """ Generates performance feedback based on the final score. """
        percentage = (self.score / self.total_questions) * 100
        
        if percentage >= 80:
            return "✅ Excellent Performance! Your fundamentals are strong and ready for advanced topics. Keep building on this knowledge."
        elif percentage >= 60:
            return "👍 Good Effort. You have a solid grasp of the core concepts, but review the basics of Engineering Mechanics and C-Programming."
        else:
            return "⚠️ Needs Serious Revision. Focus on revisiting foundational concepts like Ohm's Law and material properties. Consistent study is key to success."

    # --- 3. REPORTING MODULE (Persistence NFR) ---
    def save_result(self):
        """ Saves the final score and remarks to a history file. """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        remarks = self.provide_remarks()
        
        log_entry = (
            f"[{timestamp}] User ID: {self.USER_ID}\n"
            f"Score: {self.score}/{self.total_questions} ({int((self.score / self.total_questions) * 100)}%)\n"
            f"Remarks: {remarks}\n"
            f"----------------------------------------\n"
        )
        
        try:
            with open(self.LOG_FILE, "a") as file:
                file.write(log_entry)
            print(f"💾 Result logged successfully to '{self.LOG_FILE}'")
        except Exception as e:
            print(f"Error saving file: {e}")

    def run_quiz(self):
        """ Executes the main quiz loop. """
        print("\n" + "="*50)
        print(f"   ⚙️  FIRST YEAR ENGINEERING FUNDAMENTALS QUIZ  ⚙️")
        print(f"   [User Session: {self.USER_ID}]")
        print("="*50 + "\n")

        for index, q in enumerate(self.question_bank, 1):
            print(f"--- Question {index} of {self.total_questions} ---")
            print(f"{q['question']}")
            
            for option in q['options']:
                print(f"   {option}")
            
            user_choice = self.get_user_choice()

            if user_choice == q['answer']:
                print("✅ Correct!\n")
                self.score += 1
            else:
                correct_option_text = q['options'][q['answer']-1]
                print(f"❌ Wrong! The correct answer was: {correct_option_text}\n")
            
            time.sleep(0.5)

        # Final Results Display
        print("="*50)
        print("🏁 QUIZ COMPLETED!")
        print(f"🏆 Final Score: {self.score} / {self.total_questions}")
        print("Final Assessment:")
        print(self.provide_remarks())
        print("="*50)

        self.save_result()

if __name__ == "__main__":
    app = EngineeringQuizApp()
    app.run_quiz()