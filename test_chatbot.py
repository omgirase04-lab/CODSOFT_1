"""Unit tests for the expanded CodBot chatbot."""

import unittest
from chatbot import RuleBasedChatbot


class TestRuleBasedChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = RuleBasedChatbot()

    def test_greeting(self):
        response = self.bot.get_response("Hello there").lower()
        self.assertTrue(any(word in response for word in ["hello", "hey", "hi", "what would you like"]))

    def test_name(self):
        self.assertIn("CodBot", self.bot.get_response("What is your name?"))

    def test_help(self):
        self.assertIn("Try asking", self.bot.get_response("help"))

    def test_empty_message(self):
        self.assertIn("type a message", self.bot.get_response("   ").lower())

    def test_unknown_message_fallback(self):
        self.assertIn("rule-based chatbot", self.bot.get_response("Explain quantum gravity"))

    def test_thanks(self):
        self.assertTrue(any(word in self.bot.get_response("Thanks!").lower() for word in ["welcome", "anytime"]))

    def test_python_explanation(self):
        self.assertIn("programming language", self.bot.get_response("What is Python?"))

    def test_ai_explanation(self):
        self.assertIn("Artificial intelligence", self.bot.get_response("Explain AI"))

    def test_machine_learning(self):
        self.assertIn("Machine learning", self.bot.get_response("What is machine learning?"))

    def test_joke(self):
        self.assertTrue(self.bot.get_response("Tell me a joke"))

    def test_motivation(self):
        response = self.bot.get_response("Motivate me").lower()
        self.assertTrue(any(word in response for word in ["progress", "efforts", "consistency"]))

    def test_goodbye(self):
        self.assertIn("Goodbye", self.bot.get_response("bye"))

    def test_variable_explanation(self):
        self.assertIn("variable", self.bot.get_response("What is a variable?").lower())


if __name__ == "__main__":
    unittest.main()
