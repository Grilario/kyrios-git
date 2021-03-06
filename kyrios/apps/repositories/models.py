from django.db import models
from django.db.models import Q
from django.conf import settings

from apps.tasks.models import Task

from utils.date import time_to_utc
from git.repo import Repo

REPOSITORY_NAME_MAX_LENGTH = 64
REPOSITORY_NAME_MIN_LENGTH = 3
REPOSITORY_DESCRIPTION_MAX_LENGTH = 256


class RepositoryManager(models.Manager):
    """
        Manager class for running queries on repositories.
    """

    def get_queryset(self):
        return super(RepositoryManager, self).get_queryset()

    def all_repositories(self, user):
        """
            Returns all repositories a user owns.
        """

        return super(RepositoryManager, self).get_queryset().filter(Q(owner_id=user.id))

    def public_repositories(self, user):
        """
            Returns all public repositories a user owns.
        """

        return super(RepositoryManager, self).get_queryset().filter(Q(owner_id=user.id) & Q(private=False))


class Repository(models.Model):
    """
        A one-to-many model for keeping users repositories and it's data.
    """

    name = models.CharField(max_length=REPOSITORY_NAME_MAX_LENGTH)
    description = models.CharField(
        max_length=REPOSITORY_DESCRIPTION_MAX_LENGTH)
    creation_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)

    objects = RepositoryManager()

    def __str__(self):
        return '{0}\'s {1}'.format(self.owner.username, self.name)

    @property
    def accesses(self):
        """
            Property for returning users having access to this repository.
        """

        return RepositoryAccess.objects.filter(repository_id=self.id)

    @property
    def last_update(self):
        """
            Property for viewing latest activity date on repository in "ISO 8601-like" format and 'UTC' timezone.
        """

        last_update = Repo(Repo.get_repository_location(
            self.owner.username, self.name)).get_last_update()
        if last_update is None:
            return time_to_utc(str(self.creation_date))
        else:
            return last_update

    @property
    def get_latest_status(self):
        """
            Property for viewing repository latest commit status message.
        """

        repo = Repo(Repo.get_repository_location(
            self.owner.username, self.name))
        return repo.get_latest_status()


class RepositoryAccess(models.Model):
    """
        A one-to-many model for keeping users that have access to a repository.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} has access to {1}'.format(self.user.username, self.repository.name)

class RepositoryTask(models.Model):
    """
        A one-to-many model for keeping stars of a repository.
    """

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    postOnProfile = models.BooleanField(default=False)

    def __str__(self):
        return '{0}\'s posted an task {1}'.format(self.task.title, self.repository.name)


# Send signals for operations needed after repository object is saved.
from .signals import *
