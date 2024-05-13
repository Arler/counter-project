from django.shortcuts import render, redirect
from .models import File
from .forms import FileForm, WordForm

# Create your views here.
def counter_view(request):
	if request.method == 'POST':
		if 'count' in request.POST:
			wordform = WordForm(request.POST)
			if wordform.is_valid():
				word = wordform.cleaned_data['word']
				if File.objects.exists():
					context = {
						'fileform': FileForm,
						'wordform': WordForm,
						'counted_word': count(word)
					}
					return render(request, template_name='count.html', context=context)
				else:
					return redirect('/')
		elif 'delete' in request.POST:
			File.objects.first().delete()
			return redirect('/')
		else:
			fileform = FileForm(request.POST, request.FILES)
			if fileform.is_valid():
				fileform.save()
				return redirect('/')
	else:
		context = {
			'fileform': FileForm,
			'wordform': WordForm,
		}

		return render(request, template_name='count.html', context=context)


def count(user_word):
	file = File.objects.first()
	counted_words = {}
	with open(file.file.path, 'r') as f:
		list_str_f = []
		for string in f.readlines():
			for word in string.rstrip('\n').split():
				list_str_f.append(word)
		for word in list_str_f:
			if word.isalpha() and word in counted_words.keys():
				counted_words[word] += 1
			elif word.isalpha() and word not in counted_words.keys():
				counted_words[word] = 1
	return counted_words[user_word]