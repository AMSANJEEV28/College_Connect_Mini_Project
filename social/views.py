# social/views.py
from django.shortcuts import render, redirect
from .models import Group
from .forms import GroupCreationForm, GroupSearchForm, GroupJoinForm

def create_group(request):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.creator = request.user
            group.save()
            group.members.add(request.user)
            return redirect('group_detail', group_id=group.group_id)
    else:
        form = GroupCreationForm()
    return render(request, 'create_group.html', {'form': form})

# social/views.py
# ...

def search_group(request):
    user_groups = []
    
    if request.user.is_authenticated:
        user_groups = request.user.group_members.all()

    search_results = []

    if request.method == 'POST':
        form = GroupSearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']

            # Check the value of search_query
            print("Search Query:", search_query)

            # Filter by group_id directly
            groups = Group.objects.filter(group_id__exact=search_query)

            # Check the groups returned by the query
            print("Groups:", groups)

            # Check the user_groups
            print("User Groups:", user_groups)

            # Check if the user is a member of any groups in the search results
            for group in groups:
                already_member = group in user_groups
                search_results.append((group, already_member))

            # Check the search_results
            print("Search Results:", search_results)

    else:
        form = GroupSearchForm()

    return render(request, 'search_group.html', {'form': form, 'search_results': search_results, 'user_groups': user_groups})
    user_groups = []
    
    if request.user.is_authenticated:
        user_groups = request.user.group_members.all()

    search_results = []

    if request.method == 'POST':
        form = GroupSearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']

            # Check the value of search_query
            print("Search Query:", search_query)

            # Filter by group_id directly
            groups = Group.objects.filter(group_id__exact=search_query)

            # Check the groups returned by the query
            print("Groups:", groups)

            # Check the user_groups
            print("User Groups:", user_groups)

            # Check if the user is a member of any groups in the search results
            for group in groups:
                already_member = group in user_groups
                search_results.append((group, already_member))

            # Check the search_results
            print("Search Results:", search_results)

    else:
        form = GroupSearchForm()

    return render(request, 'search_group.html', {'form': form, 'search_results': search_results, 'user_groups': user_groups})

def join_group(request, group_id):
    group = Group.objects.get(group_id=group_id)
    group.members.add(request.user)
    return redirect('group_detail', group_id=group.group_id)

def group_detail(request, group_id):
    group = Group.objects.get(group_id=group_id)
    user_groups = request.user.group_members.all()
    return render(request, 'group_detail.html', {'group': group, 'user_groups': user_groups})

def feeds_view(request):
    # Your view logic here
    return render(request, 'feeds.html')