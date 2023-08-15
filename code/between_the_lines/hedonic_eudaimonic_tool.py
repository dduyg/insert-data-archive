class SelfReflectionTool:
    def __init__(self):
        self.hedonic_score = 0
        self.eudaimonic_score = 0
        self.hedonic_questions = [
            "Did you engage in this task primarily for immediate pleasure?",
            "Was the main goal of this task to experience enjoyment?",
            "Did you do this task to have fun or feel good in the moment?"
        ]
        self.eudaimonic_questions = [
            "Did you feel a sense of purpose while doing this task?",
            "Did you engage in this task to achieve personal growth or development?",
            "Did you do this task to contribute to your long-term well-being?"
        ]

    def ask_question(self, question):
        response = input(question + " (yes/no): ")
        return response.lower() == 'yes'

    def collect_scores(self, question_list):
        score = 0
        for question in question_list:
            if self.ask_question(question):
                score += 1
        return score

    def run(self):
        print("Welcome to the Self-Reflection Tool!")
        self.hedonic_score = self.collect_scores(self.hedonic_questions)
        self.eudaimonic_score = self.collect_scores(self.eudaimonic_questions)

        if self.hedonic_score > self.eudaimonic_score:
            print("The task is hedonic.")
        elif self.eudaimonic_score > self.hedonic_score:
            print("The task is eudaimonic.")
        else:
            print("The task has balanced motives.")

def main():
    tool = SelfReflectionTool()
    tool.run()

if __name__ == "__main__":
    main()
