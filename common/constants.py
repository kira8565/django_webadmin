DEFAULT_DASHBOARD_TITLE = '首页'

MALE = 'male'
FEMALE = 'female'

SEX = (
    (MALE, '男'),
    (FEMALE, '女'),
)

TRUE_FALSE = (
    (True, '是'),
    (False, '否')
)

DICT_NULL_BLANK_TRUE = {
    'null': True,
    'blank': True
}


class ReadStatus(object):
    UNREAD = 0
    READ = 1
    DELETED = 99
    STATUS = (
        (UNREAD, '未读'),
        (READ, '已读'),
        (DELETED, '删除'),
    )


class MailStatus(object):
    UNREAD = 0
    READ = 1
    DRAFT = 2
    TRASH = 3
    DELETED = 99
    STATUS = (
        (UNREAD, '未读'),
        (READ, '已读'),
        (DRAFT, '草稿'),
        (TRASH, '回收站'),
        (DELETED, '删除'),
    )


class UsableStatus(object):
    UNUSABLE = 0
    USABLE = 1
    DELETED = 99
    STATUS = (
        (UNUSABLE, '禁用'),
        (USABLE, '启用'),
        (DELETED, '删除'),
    )


class TaskStatus(object):
    NORMAL = 0
    EXCEPT = 1
    FINISHED = 2
    DELETED = 99
    TASK_STATUS = (
        (NORMAL, '正常(进行中)'),
        (EXCEPT, '异常'),
        (FINISHED, '完成'),
        (DELETED, '删除')
    )
