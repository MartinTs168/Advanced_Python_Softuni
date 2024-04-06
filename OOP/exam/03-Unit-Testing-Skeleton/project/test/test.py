import unittest
from project.social_media import SocialMedia


class TestSocialMedia(unittest.TestCase):
    def setUp(self):
        self.sc = SocialMedia("MTS", "Twitter", 100, "game")
        self.sc_with_post = SocialMedia("Ddio", "Twitter", 100, "game")
        self.sc_with_post._posts = [{'content': "D2", 'likes': 2, 'comments': []}]

    def test_init(self):
        self.assertEqual("MTS", self.sc._username)
        self.assertEqual("Twitter", self.sc._platform)
        self.assertEqual(100, self.sc.followers)
        self.assertEqual("game", self.sc._content_type)
        self.assertEqual([], self.sc._posts)

    def test_validate_platform_with_incorrect(self):
        with self.assertRaises(ValueError) as ve:
            self.sc._validate_and_set_platform("ABB")

        self.assertEqual(f"Platform should be one of {['Instagram', 'YouTube', 'Twitter']}", str(ve.exception))

    def test_with_negative_followers(self):
        with self.assertRaises(ValueError) as ve:
            self.sc.followers = -1

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_create_post(self):
        actual = self.sc.create_post("D2")
        self.assertEqual(f"New {self.sc._content_type} post created by {self.sc._username} on {self.sc._platform}.",
                         actual)
        self.assertEqual([{'content': "D2", 'likes': 0, 'comments': []}], self.sc._posts)

    def test_like_post_with_invalid_index(self):
        actual = self.sc.like_post(100)
        self.assertEqual("Invalid post index.", actual)

    def test_like_post(self):
        actual = self.sc_with_post.like_post(0)
        self.assertEqual(f"Post liked by {self.sc_with_post._username}.", actual)
        self.assertEqual(self.sc_with_post._posts[0]['likes'], 3)

    def test_like_with_max_likes(self):
        self.sc_with_post._posts[0]['likes'] = 10
        actual = self.sc_with_post.like_post(0)
        self.assertEqual("Post has reached the maximum number of likes.", actual)

    def test_comment_on_post_with_valid_comment(self):
        actual = self.sc_with_post.comment_on_post(0, "I do not like judge")
        self.assertEqual([{'user': self.sc_with_post._username, 'comment': "I do not like judge"}], self.sc_with_post._posts[0]['comments'])
        self.assertEqual(f"Comment added by {self.sc_with_post._username} on the post.", actual)

    def test_comment_with_invalid_comment(self):
        actual = self.sc_with_post.comment_on_post(0, "I")
        self.assertEqual("Comment should be more than 10 characters.", actual)


if __name__ == '__main__':
    unittest.main()
