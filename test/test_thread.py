from unittest import TestCase, main
from siri.agent.thread import Thread

from typing import TYPE_CHECKING



class ThreadTest (TestCase):

    def test_create (self):
        thread = Thread(system_prompt="system_prompt")
        self.assertEqual(
            thread.history,
            {"role": "system", "content": "system_prompt"},
        )

    def test_correct_append (self):
        thread = Thread(system_prompt="system_prompt")
        new_message = {"role": "user", "content": "user_message"}
        
        try:
            thread += new_message
        except Exception as e:
            self.fail(f"Correct usage of thread += raised an exception {e}")

    def test_incorrect_append (self):
        thread = Thread(system_prompt="system_prompt")
        new_message = {"role": "assistant", "content": "assistant_message"}

        try:
            thread += new_message
            self.fail("Thread append of incompatible message failed to raise an exception")
        except:
            pass

if __name__ == "__main__":
    main()

