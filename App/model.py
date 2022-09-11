from dataclasses import dataclass
from datetime import datetime, timedelta

class Model:
    pass

class User:
    pass

class FlashCardFolder:
    pass

@dataclass
class FlashCard:
    """
    dataclass the define a flashcard

    a flashcard has:
        the name of the folder containing the card

        front text
        optional front image path
        back text
        an optional back image path
        create_date - a datetime object???? may be a string later?  uncertain - best might be a unix timestamp?
        last_study_date - another datetime or other object?
        next_study_due - another datetime
        streak - an integer that helps set the next_study_due
    """

    folder: str
    front_text: str
    back_text: str

    streak: int

    create_date: datetime
    last_study_date: datetime
    next_study_due: datetime


    # optional image paths
    front_image_path: str = None
    back_image_path: str = None

    def reset_streak(self):
        self.streak = 0

    def mark_card_remembered(self):
        # add one more time to the streak
        self.streak += 1

        """
        there are other ways to do spaced repetition, but for now...
        
        
        set the next study due date to "streak" days from now.
        """
        self.last_study_date = datetime.utcnow()
        self.next_study_due = self.last_study_date + timedelta(days=self.streak)

    def unit_test(self) -> bool:
        # test that this works, also don't mutate the actual object

        print('testing the Flashcard Class')
        try:
            initial_streak = self.streak
            initial_last_study_date = self.last_study_date
            initial_next_study_date = self.next_study_due

            self.mark_card_remembered()
            assert self.streak == initial_streak + 1
            assert self.next_study_due == self.last_study_date + timedelta(days=self.streak)
            self.streak = initial_streak
            self.last_study_date = initial_last_study_date
            self.next_study_due = initial_next_study_date
            # cool it worked
            return True
        except AssertionError:
            return False


