css = '''
    <style>
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
    }
    .chat-message.user {
        background-color: #2b3134;
    }
    .chat-message.bot {
        background-color: #475063;
    }
    .chat-message .avatar {
        width: 15%;
    }
    .chat-message .avatar img {
        max-width: 78px;
        max-height: 78px;
        border-radius: 50%;
        object-fit: cover;
    }
    .chat-message .message {
        width: 85%;
        padding: 0 1.5rem;
        color: #fff;
    }
    </style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn.openart.ai/stable_diffusion/575af447d8bec68b334c847aae28df09d4c455d3_2000x2000.webp">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.pinimg.com/736x/3d/91/26/3d9126e00ee953735b1cf2152b4759c7.jpg" style="max-height: 78px; max-width: 78px">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
