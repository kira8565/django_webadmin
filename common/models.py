from django.contrib.auth.models import User, Group, AbstractBaseUser, \
    AbstractUser
from django.core.urlresolvers import reverse

from django.db import models
from django.utils import timezone
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from common.constants import DICT_NULL_BLANK_TRUE


class BaseModel(models.Model):
    creator = models.ForeignKey(
        User,
        verbose_name=u"数据创建人",
        **DICT_NULL_BLANK_TRUE
    )
    created_at = models.DateTimeField(
        verbose_name=u"数据创建时间",
        default=timezone.now,
        **DICT_NULL_BLANK_TRUE
    )
    updated_at = models.DateTimeField(
        verbose_name=u"数据更新时间",
        default=timezone.now,
        **DICT_NULL_BLANK_TRUE
    )
    deleted_at = models.DateTimeField(
        verbose_name=u"数据删除时间",
        **DICT_NULL_BLANK_TRUE
    )

    class Meta:
        abstract = True
