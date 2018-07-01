from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

from .models import Friend

test_image = SimpleUploadedFile(
        name='test_image.jpg',
        content=open('test_media/test_image.jpg', 'rb').read(),
        content_type='image/jpeg')


class TestFriendView(TestCase):
    def test_friend_create_view_success(self):
        friend_data = {
                'name': 'Ollie',
                'mug_shot': test_image,
                }
        url = reverse('friend-add')

        self.client.post(url, data=friend_data)

        self.assertEqual(1, len(Friend.objects.all()))
        friend = Friend.objects.first()
        self.assertEqual('Ollie', friend.name)

    def test_friend_delete_view_success(self):
        friend = Friend.objects.create(
                name='Ollie',
                mug_shot=test_image
                )
        url = reverse('friend-delete', args=(friend.pk, ))

        self.client.post(url)

        self.assertEqual(0, len(Friend.objects.all()))
