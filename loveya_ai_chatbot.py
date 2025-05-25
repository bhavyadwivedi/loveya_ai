class LoveyaAI:
    def __init__(self):
        self.name = "Loveya AI"
        self.interests = {
            "fashion": ["shoes", "sneakers", "jordans", "dunks"],
            "music": {
                "artists": ["chase atlantic"],
                "genres": ["rap", "hip-hop"]
            },
            "food_drinks": {
                "snacks": ["chocolate"],
                "beverages": ["mountain dew", "green juice"]
            },
            "tv_shows": ["all american", "suits"],
            "sports": ["taekwondo"]
        }
        
        self.dislikes = ["movies", "badminton"]
        
    def introduce_self(self):
        return f"Hey! I'm {self.name}!"
    
    def respond_to_topic(self, message):
        message = message.lower()
        responses = {
            "shoes": "OMG, let's talk sneakers! Have you seen the latest drops?",
            "chase atlantic": "Chase Atlantic's music hits different fr fr!",
            "rap": "Nothing better than bars and beats!",
            "chocolate": "Chocolate is literally life! Can't get enough!",
            "mountain dew": "That Mountain Dew energy hit different!",
            "green juice": "yum. (it's not grass i swear)",
            "all american": "i love layla keating",
            "suits": "i love donna paulsen",
            "taekwondo": "don't do that anymore but i rlly want to",
            "movies": "Movies aren't really my thing tbh..."
        }
        
        # Check if any of the topics appear in the message
        for topic, response in responses.items():
            if topic in message:
                return response
                
        return "Let's talk about something! (please let's yap abt shoes)"
    
    def check_vibe(self, topic):
        topic = topic.lower()
        if topic in self.dislikes:
            return "Not really my vibe..."
        elif any(topic in str(category).lower() for category in self.interests.values()):
            return "yesyesyesyesyes"
        else:
            return "Meh, I'm neutral on that."

def main():
    bot = LoveyaAI()
    print(bot.introduce_self())
    print("(type 'bye' to exit)")
    
    while True:
        user_input = input("\nyou: ").strip()
        
        if user_input.lower() == 'bye':
            print("\nLoveya AI: bye bestie! come back soon!")
            break
            
        # Check if it's a vibe check question
        if "do you like" in user_input.lower() or "what do you think about" in user_input.lower():
            topic = user_input.lower().replace("do you like ", "").replace("what do you think about ", "")
            print("\nLoveya AI:", bot.check_vibe(topic))
        else:
            print("\nLoveya AI:", bot.respond_to_topic(user_input))

if __name__ == "__main__":
    main()
