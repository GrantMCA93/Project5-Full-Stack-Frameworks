from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .create_conversations import CreateConversations
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from .forms import EnquiryForm, ContactForm
from .models import PropertyEnquire
from django.contrib.auth.models import User
from listings.views import house



@login_required
def send_enquire(request, user_id, house_id):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your enquire has been send.")
            return house(request, house_id)
        else:
            messages.error(request, form.errors)
            return house(request, house_id)
    else:
        return redirect('index')


def send_contact_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            messages.success(request, "Thank you for your message!")
            return redirect('/#contact-us')
        else:
        	messages.error(request, form.errors)
        	return redirect('/#contact-us')
    else:
        return redirect('index')
        

@login_required
def get_messages(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            conversations = CreateConversations(
                request.session['_auth_user_id']).create_conversations()
            return JsonResponse(conversations, safe=False)
        else:
            return redirect('index')
    else:
        return redirect('index')


@login_required
def delete_message(request, user_id, conversation_member, house_id):
    if request.method == "POST":
        if user_id is not int(request.session['_auth_user_id']):
            return HttpResponse("You are not allowed to delete this message!")
        received_id = [x.pk for x in PropertyEnquire.objects.filter(
            to_id=user_id, sender_id=conversation_member, house_id=house_id)]
        sent_id = [x.pk for x in PropertyEnquire.objects.filter(
            to_id=conversation_member, sender_id=user_id, house_id=house_id)]
        if received_id or sent_id:
            if received_id:
                PropertyEnquire.objects.filter(to_id=user_id,
                                               id__in=received_id).update(delete_to=True)
            if sent_id:
                PropertyEnquire.objects.filter(
                    sender_id=user_id, id__in=sent_id).update(delete_sender=True)
            hidden_for_both = [x.pk for x in PropertyEnquire.objects.filter(
                house_id=house_id, delete_sender=True, delete_to=True)]
            if hidden_for_both:
                PropertyEnquire.objects.filter(
                    id__in=hidden_for_both).delete()
            return HttpResponse("success")
        else:
            return HttpResponse("There seems to be a problem updating your message!")
    else:
        return redirect('index')


@login_required
def toggle_read(request, user_id, conversation_member, house_id):
    if request.method == "POST":
        if user_id is not int(request.session['_auth_user_id']):
            return redirect('index')
        messages_id = [x.pk for x in PropertyEnquire.objects.filter(
            to_id=user_id, sender_id=conversation_member, house_id=house_id, new_to=True)]
        if messages_id:
            PropertyEnquire.objects.filter(
                id__in=messages_id).update(new_to=False)
            return HttpResponse("success")
        else:
            return HttpResponse("There seems to be a problem updating your message!")
    else:
        return redirect('index')


