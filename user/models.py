from django.utils import timezone
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, UserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _



# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, nickname, last_name, first_name, address, phone_number, division, password=None ):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not nickname:
            raise ValueError(_('Users must have an email nickname'))

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
            last_name = last_name,
            first_name = first_name,
            address = address,
            phone_number = phone_number,
            division = division,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password,**extra_fields):
        """
        주어진 이메일, 닉네임, 비밀번호 등 개인정보로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여한다. 
        """
        user = self.create_user(
            email=email,
            password=password,
            nickname=nickname,
            **extra_fields
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    MANAGER = '매니저'
    LODGE = '업소'
    DIVISION = (
        (MANAGER, 'Manager'),
        (LODGE, 'Lodge'),
    )

    id = models.AutoField(primary_key=True,  help_text='Unique ID for this particular users across user')
    email = models.EmailField(
        verbose_name=_('Email address'),
        max_length=255,
        unique=True,
    )
    nickname = models.CharField(
        verbose_name=_('Nickname'),
        max_length=30,
        unique=True
    )
    first_name = models.CharField(
        verbose_name=_('First Name'),
        max_length=10,
        unique=False
    )
    last_name = models.CharField(
        verbose_name=_('Last Name'),
        max_length=10,
        unique=False
    )
    address = models.CharField(
        verbose_name=_('Address'),
        max_length=100,
        default=True,
        unique = True
    )
    phone_number = models.CharField(
        verbose_name=_('Phone Number'),
        max_length=30,
        default=True
    )
    division = models.CharField(
        max_length = 10,
        choices = DIVISION,
        default=True,
        help_text = '매니저/업소 중 분류를 입력하세요'
    )
    is_active = models.BooleanField(
        verbose_name=_('Is active'),
        default=True
    )
    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now,
    )
    # 이 필드는 레거시 시스템 호환을 위해 추가할 수도 있다.
    salt = models.CharField(
        verbose_name=_('Salt'),
        max_length=10,
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'last_name', 'first_name', 'address', 'phone_number', 'division']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return self.nickname

    def get_full_name(self):        
        return self.nickname

    def get_short_name(self):
        return self.nickname

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser

    get_full_name.short_description = _('Full name')







