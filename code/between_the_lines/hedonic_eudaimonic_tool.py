import random

class SelfReflectionTool:
    def __init__(self):
        self.hedonic_score = 0
        self.eudaimonic_score = 0
        self.hedonic_questions = [
            "Did this task allow you to take it easy?",
            "Did you engage in this task to experience enjoyment?",
            "Did this task help you relax?",
            "Was the main intention behind this task to indulge in a pleasurable activity?",
            "Was the purpose of this task to enjoy a leisurely activity?",
            "Did you engage in this task to escape from stress or negative emotions?",
            "Did you do this task to have fun or feel good in the moment?"
        ]
        self.eudaimonic_questions = [
            "Did this task involve developing a skill, learning something new, or gaining insights?",
            "Did you consider this task a step toward achieving your long-term aspirations?",
            "Did you engage in this task to achieve personal growth or development?",
            "Did you strive for excellence or work towards a personal ideal through this task?",
            "Was the primary reason for this task to further your journey toward self-improvement?",
            "Did you feel a sense of accomplishment or personal fulfillment from completing this task?",
            "Did this task contribute to your overall sense of purpose and meaning in life?"
        ]
        self.all_questions = self.shuffle_mixed_questions()

    def shuffle_mixed_questions(self):
        mixed_questions = self.hedonic_questions + self.eudaimonic_questions
        random.shuffle(mixed_questions)
        return mixed_questions

    def ask_question(self, question):
        response = int(input(question + " (1-7): "))
        return response

    def collect_scores(self, question_list):
        scores = []
        for question in question_list:
            scores.append(self.ask_question(question))
        return sum(scores) / len(scores)

    def run(self):
        print("Welcome! We're here to help you reflect on your recent activities.")
        print("As you respond to a series of questions, we will classify the task based on your responses.")
        print("Think about each question and rate your response on a scale of 1 to 7, where 1 means 'not at all' and 7 means 'very much'.")
        print("Let's begin!\n")
        
        self.hedonic_score = self.collect_scores(self.all_questions[:7])
        self.eudaimonic_score = self.collect_scores(self.all_questions[7:])

        if self.hedonic_score > self.eudaimonic_score:
            print("Based on your responses, the task is driven by hedonic motives.")
        elif self.eudaimonic_score > self.hedonic_score:
            print("Based on your responses, the task is driven by eudaimonic motives.")
        else:
            print("Based on your responses, the task has an equal balance of hedonic and eudaimonic motives.")

def main():
    tool = SelfReflectionTool()
    tool.run()

if __name__ == "__main__":
    main()
