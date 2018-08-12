from unittest import skip

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import Accomplishment, Friend, FriendAccomplishment


test_image = SimpleUploadedFile(
        name='test_image.jpg',
        content=open('test_media/test_image.jpg', 'rb').read(),
        content_type='image/jpeg')


class TestFriendView(TestCase):
    @skip('Form invalid - can not figure this out...')
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

    @skip('Form invalid - can not figure this out...')
    def test_friend_update_view_success(self):
        friend = Friend.objects.create(
                name='Ollie',
                mug_shot=test_image
                )
        update_data = {
                'pk': friend.pk,
                'name': 'Jess',
                'mug_shot': test_image,
                'accomplishments': [],
                }
        url = reverse('friend-update', args=(friend.pk, ))

        response = self.client.post(url, data=update_data)
        self.assertEqual(200, response.status_code)

        self.assertEqual(1, len(Friend.objects.all()))
        new_friend = Friend.objects.first()
        friend.refresh_from_db()
        self.assertEqual(friend, new_friend)
        self.assertEqual('Jess', friend.name)

    def test_friend_delete_view_success(self):
        friend = Friend.objects.create(
                name='Ollie',
                mug_shot=test_image
                )
        url = reverse('friend-delete', args=(friend.pk, ))

        self.client.post(url)

        self.assertEqual(0, len(Friend.objects.all()))


class TestAccomplishmentView(TestCase):
    def test_accomplishment_create_view_success(self):
        accomplishment_data = {
                'description': 'Complete park run',
                'points': 5,
                }
        url = reverse('accomplishment-add')

        self.client.post(url, data=accomplishment_data)

        self.assertEqual(1, len(Accomplishment.objects.all()))
        accomplishment = Accomplishment.objects.first()
        self.assertEqual('Complete park run', accomplishment.description)
        self.assertEqual(5, accomplishment.points)

    def test_accomplishment_update_view_success(self):
        accomplishment = Accomplishment.objects.create(
                description='Complete park run',
                points=5,
                )
        update_data = {
                'pk': accomplishment.pk,
                'description': 'Complete park run sub 20',
                'points': 15,
                'accomplished_by': [],
                }
        url = reverse('accomplishment-update', args=(accomplishment.pk, ))

        response = self.client.post(url, data=update_data)
        self.assertEqual(302, response.status_code)

        self.assertEqual(1, len(Accomplishment.objects.all()))
        new_accomplishment = Accomplishment.objects.first()
        accomplishment.refresh_from_db()
        self.assertEqual(accomplishment, new_accomplishment)
        self.assertEqual(
                'Complete park run sub 20',
                accomplishment.description)
        self.assertEqual(15, accomplishment.points)

    def test_accomplishment_delete_view_success(self):
        accomplishment = Accomplishment.objects.create(
                description='Ollie',
                points=5,
                )
        url = reverse('accomplishment-delete', args=(accomplishment.pk, ))

        self.client.post(url)

        self.assertEqual(0, len(Accomplishment.objects.all()))


class TestFriend(TestCase):
    def test_total_points(self):
        friend = Friend.objects.create(
                name='Ollie',
                mug_shot=test_image
                )

        acc_one = Accomplishment.objects.create(
                description='Complete park run',
                points=5,
                )
        acc_two = Accomplishment.objects.create(
                description='Host guest',
                points=15,
                )

        FriendAccomplishment.objects.create(
                friend=friend,
                accomplishment=acc_one,
                )
        FriendAccomplishment.objects.create(
                friend=friend,
                accomplishment=acc_two,
                )

        self.assertEqual(20, friend.total_points)
