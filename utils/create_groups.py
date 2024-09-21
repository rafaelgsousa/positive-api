def create_groups(group:str, ret=False):
        from django.contrib.auth.models import Group, Permission

        type_permissions = ['view', 'add', 'change', 'delete']
        table = ['albummeeting', 'commentcourse', 'course', 'ebook', 'imagealbummeeting', 'meeting', 'news', 'planner', 'wheeluseranalysis', 'customuser', 'videocourse', 'videomeeting', 'welcome']
        list_perm = []
        if group.lower().strip() in ('free','basic'):
            list_perm = [Permission.objects.get(codename=f'view_{name}').id for name in table if name != 'wheeluseranalysis']
        if group.lower().strip() == 'premium':
            for data in table:
                if data == 'wheeluseranalysis':
                    list_perm.extend([Permission.objects.get(codename=f'{name}_{data}').id for name in type_permissions])
                else:
                    list_perm.extend([Permission.objects.get(codename=f'view_{data}').id])
        if group.lower().strip() == 'master':
            for data in table:
                list_perm.extend([Permission.objects.get(codename=f'{name}_{data}').id for name in type_permissions])
        
        group = Group.objects.create(name=group)
        group.permissions.set(list_perm)
        group.save()

        if ret:
            return group.id    