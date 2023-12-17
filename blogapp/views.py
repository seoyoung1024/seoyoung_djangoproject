from django.shortcuts import render, redirect, get_object_or_404
from .models import Write, Comment
from .forms import WriteForm, CommentForm
# Create your views here.

def index(request):
    all_write = Write.objects.all()
    return render(request, 'index.html', {'all_write': all_write})

def create(request): 
  if request.method == "POST":
    create_form = WriteForm(request.POST)
    if create_form.is_valid():
      create_form.save()
      return redirect('index') #글 쓰고 인덱스로 감
  else:
    create_form = WriteForm()

  return render(request,'create.html',{'create_form':create_form})

def detail(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    comments = Comment.objects.filter(write=my_write)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.write = my_write
            new_comment.save()
            return redirect('detail', write_id=write_id)
    else:
        comment_form = CommentForm()

    return render(request, 'detail.html', {'my_write': my_write, 'comments': comments, 'comment_form': comment_form})


def delete_comment(request, write_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('detail', write_id=write_id)


def update(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)

    if request.method == "POST":
        update_form = WriteForm(request.POST, instance=my_write)
        if update_form.is_valid():
            update_form.save()
            return redirect('index')
    else:
        update_form = WriteForm(instance=my_write)

    return render(request, 'update.html', {'update_form': update_form})

def delete(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    my_write.delete()
    return redirect('index')

def write_detail(request, write_id):
    write = get_object_or_404(Write, id=write_id)
    comments = Comment.objects.filter(write=write)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.write = write
            new_comment.save()
            return redirect('write_detail', write_id=write_id)
    else:
        comment_form = CommentForm()

    return render(request, 'write_detail.html', {'write': write, 'comments': comments, 'comment_form': comment_form})