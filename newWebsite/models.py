from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GithubOrgMembersInfo(models.Model):
    member_id = models.IntegerField()
    org = models.ForeignKey('GithubUserOrgInfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'github_org_members_info'


class GithubRepoBaseInfo(models.Model):
    repo_name = models.CharField(max_length=255)
    repo_full_name = models.CharField(max_length=255)
    # fork_count = models.IntegerField()
    # star_count = models.IntegerField()
    # subscribe_count = models.IntegerField()
    repo_id = models.IntegerField(primary_key=True)
    # repo_owner = models.ForeignKey('GithubUserOrgInfo', models.DO_NOTHING)
    # owner_type = models.CharField(max_length=100)
    # repo_size = models.IntegerField()
    # language = models.TextField()
    # repo_created_time = models.CharField(max_length=100)
    # repo_description = models.TextField()
    # update_time = models.DateTimeField()
    # repo_update_time = models.CharField(max_length=100)
    # collaborators_count = models.IntegerField()
    # repo_branch_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_repo_base'


class GithubRepoCommitInfo(models.Model):
    commit_file_count = models.IntegerField()
    commit_file_per = models.TextField()
    #commit_user = models.ForeignKey('GithubUserOrgInfo', models.DO_NOTHING)
    #committer_user = models.ForeignKey('GithubUserOrgInfo', models.DO_NOTHING)
    repo = models.ForeignKey(GithubRepoBaseInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'github_repo_commit_info'


class GithubRepoDevelopInfo(models.Model):
    commit_count = models.IntegerField()
    comment_count = models.IntegerField()
    issue_count = models.IntegerField()
    issue_close_open = models.DecimalField(decimal_places=3, max_digits=10)
    develop_long_time = models.DecimalField(decimal_places=3, max_digits=10)
    repo_long_time = models.DecimalField(decimal_places=3, max_digits=10)
    issue_close_time = models.DecimalField(decimal_places=3, max_digits=10)
    issue_comment_count = models.IntegerField()
    pulls_count = models.IntegerField()
    pulls_merged_count = models.IntegerField()
    pulls_member_rate = models.DecimalField(decimal_places=3, max_digits=10)
    repo= models.ForeignKey(GithubRepoBaseInfo, models.DO_NOTHING)
    id = models.IntegerField(primary_key=True)
    code_add_count_perweek = models.TextField()
    code_delete_count_perweek = models.TextField()
    commit_count_perweek_lastyear = models.TextField()
    update_time = models.DateTimeField()
    commit_count_permonth = models.TextField()
    score = models.DecimalField(decimal_places=3,max_digits=6)
    f1 = models.DecimalField(decimal_places=3, max_digits=6)
    f2 = models.DecimalField(decimal_places=3, max_digits=6)
    f3 = models.DecimalField(decimal_places=3, max_digits=6)
    f4 = models.DecimalField(decimal_places=3, max_digits=6)
    f5 = models.DecimalField(decimal_places=3, max_digits=6)
    f6 = models.DecimalField(decimal_places=3, max_digits=6)
    issues_member_rate= models.DecimalField(decimal_places=3, max_digits=10)
    class Meta:
        managed = False
        db_table = 'github_repo_develop_info'
        
class Githubzinfo(models.Model):
    repo = models.ForeignKey(GithubRepoBaseInfo, models.DO_NOTHING)
    zstar = models.DecimalField(decimal_places=3, max_digits=10)
    Zfork = models.DecimalField(decimal_places=3, max_digits=10)
    Zsubscribe = models.DecimalField(decimal_places=3, max_digits=10)
    Zcontributor = models.DecimalField(decimal_places=3, max_digits=10)
    Zcommit_count = models.DecimalField(decimal_places=3, max_digits=10)
    Zissue_count = models.DecimalField(decimal_places=3, max_digits=10)
    Zissue_closeopen = models.DecimalField(decimal_places=3, max_digits=10)
    Zdevelop_long_time = models.DecimalField(decimal_places=3, max_digits=10)
    Zissue_close_time = models.DecimalField(decimal_places=3, max_digits=10)
    Zcomment_count = models.DecimalField(decimal_places=3, max_digits=10)
    Zissue_comment_count = models.DecimalField(decimal_places=3, max_digits=10)
    Zpulls_count = models.DecimalField(decimal_places=3, max_digits=10)
    Zpulls_merged_count = models.DecimalField(decimal_places=3, max_digits=10)
    class Meta:
        managed = False
        db_table = 'github_z'

class GithubRepoDeveloperInfo(models.Model):
    repo = models.ForeignKey(GithubRepoBaseInfo, models.DO_NOTHING)
    user = models.ForeignKey('GithubUserOrgInfo', models.DO_NOTHING)
    user_add_count_perweek = models.TextField()
    user_commit_count = models.IntegerField()
    user_commit_count_perweek = models.TextField()
    user_creat_time = models.CharField(max_length=100)
    user_del_count_perweek = models.TextField()
    user_last_update_time = models.CharField(max_length=100)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'github_repo_developer_info'


class GithubRepoIssueCommentInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    # issue_comment_id = models.IntegerField(primary_key=True)
    # issue_comment_author_association = models.CharField(max_length=100)
    # issue_comment_created_at = models.CharField(max_length=100)
    issue_comment_body = models.TextField()
    issue_comment_updated_at = models.CharField(max_length=50)
    # issue = models.ForeignKey('GithubRepoIssueInfo', models.DO_NOTHING)
    # issue_comment_author = models.ForeignKey('GithubUserOrgInfo', models.DO_NOTHING)
    event_id = models.IntegerField()
    issue_id = models.IntegerField()
    # repo = models.ForeignKey(GithubRepoBaseInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'github_event_issus_comment'


class GithubEventInfo0(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base0'


class GithubEventInfo1(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base1'


class GithubEventInfo2(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base2'


class GithubEventInfo3(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base3'


class GithubEventInfo4(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base4'


class GithubEventInfo5(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base5'


class GithubEventInfo6(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base6'


class GithubEventInfo7(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base7'


class GithubEventInfo8(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base8'


class GithubEventInfo9(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base9'


class GithubEventInfo10(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base10'


class GithubEventInfo11(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base11'


class GithubEventInfo12(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base12'


class GithubEventInfo13(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base13'


class GithubEventInfo14(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base14'


class GithubEventInfo15(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base15'


class GithubEventInfo16(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base16'


class GithubEventInfo17(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base17'


class GithubEventInfo18(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base18'


class GithubEventInfo19(models.Model):
    event_id = models.IntegerField(primary_key=True)
    repo_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'github_event_base19'



class GithubRepoIssueInfo(models.Model):
    # issue_user_type = models.CharField(max_length=100)
    # issue_state = models.IntegerField()
    repo = models.ForeignKey(GithubRepoBaseInfo, models.DO_NOTHING)
    # user = models.ForeignKey('GithubUserOrgInfo', models.DO_NOTHING)
    # issue_close_time = models.CharField(max_length=100, blank=True, null=True)
    # issue_create_time = models.CharField(max_length=100, blank=True, null=True)
    # update_time = models.DateTimeField()
    # issue_comment_count = models.IntegerField()
    issue_id = models.IntegerField(primary_key=True)
    # issue_number = models.IntegerField()
    # issue_update_time = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'github_event_issus'


class GithubRepoMilestonesInfo(models.Model):
    milestones_id = models.IntegerField(primary_key=True)
    milestones_title = models.CharField(max_length=255)
    milestones_state = models.IntegerField()
    milestones_create_time = models.CharField(max_length=100, blank=True, null=True)
    milestones_close_time = models.CharField(max_length=100, blank=True, null=True)
    milestones_update_time = models.CharField(max_length=100, blank=True, null=True)
    update_time = models.DateTimeField()
    milestones_creater = models.ForeignKey('GithubUserOrgInfo', models.DO_NOTHING)
    repo = models.ForeignKey(GithubRepoBaseInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'github_repo_milestones_info'

class GithubUserOrgInfo(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=255)
    avatar_url = models.CharField(max_length=500)
    follows_count = models.IntegerField()
    repos_count = models.IntegerField()
    blog_url = models.CharField(max_length=500, blank=True, null=True)
    email_url = models.CharField(max_length=500, blank=True, null=True)
    belong_org = models.IntegerField(blank=True, null=True)
    org_member_count = models.IntegerField()
    user_create_time = models.CharField(max_length=100)
    update_time = models.DateTimeField()
    user_type = models.CharField(max_length=100)
    user_update_time = models.CharField(max_length=100)
    user_fullname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'github_user_org_info'

class GithubRepoPullsInfo(models.Model):
    pull_id = models.IntegerField(primary_key=True)
    pull_number = models.IntegerField()
    pull_state = models.IntegerField()
    pull_author_association = models.CharField(max_length=100)
    pull_create_time = models.CharField(max_length=100, blank=True, null=True)
    pull_update_time = models.CharField(max_length=100, blank=True, null=True)
    pull_closed_time = models.CharField(max_length=100, blank=True, null=True)
    pull_merged_time = models.CharField(max_length=100, blank=True, null=True)
    pull_is_merged = models.IntegerField()
    update_time = models.DateTimeField()
    user = models.ForeignKey(GithubUserOrgInfo, models.DO_NOTHING)
    repo = models.ForeignKey(GithubRepoBaseInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'github_repo_pulls_info'


