import sqlite3 as sq


class SQLighter:

    def __init__(self, database_file):
        self.connection = sq.connect(database_file)
        self.cursor = self.connection.cursor()

    def insert_eng_words(self, eng_word, transcription, translation):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO 'eng_words' (word_on_eng, transcription, translation) VALUES (?, ?, ?)",
                (eng_word, transcription, translation)
            )

        self.connection.commit()
