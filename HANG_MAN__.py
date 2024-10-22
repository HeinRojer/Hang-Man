# List of 200 simple English words
words = [
    "apple", "banana", "chair", "dog", "cat", "house", "book","table", "car","pen", "door","cup","shirt", "hat","shoe",
    "bag","bottle","bus","train","phone","key","clock", "tree", "bed", "lamp", "box", "window", "fish", "hand", "water",
    "food", "fork", "spoon", "glass", "coat", "bike", "road", "paper", "pencil","toy", "bird", "flower", "plant", "sun",
    "moon", "star", "rain", "snow", "ball", "face", "hair", "eye", "ear", "mouth", "nose", "leg", "arm", "foot", "head",
    "sky", "cloud", "hill", "river", "beach", "sand", "leaf", "wind", "stone", "tree", "grass", "light", "dark", "hot",
    "cold", "warm", "cool", "sweet", "sour", "bitter", "salt", "butter", "bread", "milk","egg","cheese","cake","juice",
    "meat", "soup", "sauce", "rice", "noodle", "fruit", "vegetable", "sugar", "tea", "coffee", "cookie", "jam", "candy",
    "ice", "cream", "tooth", "tongue", "chin", "cheek", "knee", "elbow", "finger", "thumb", "back", "stomach", "chest",
    "neck", "shoulder", "waist", "bone", "blood", "skin", "heart", "brain", "liver", "lung", "air", "fire", "earth",
    "water", "mountain", "forest", "ocean", "lake", "valley", "desert", "field", "farm", "garden", "village", "city",
    "street", "road", "bridge", "park","shop","school","office", "library", "bank", "hotel", "restaurant", "hospital",
    "market", "store", "building", "room", "kitchen", "bathroom","living","bedroom","roof", "floor", "wall", "ceiling",
    "door", "window", "closet", "mirror", "stair", "elevator", "fence", "gate", "yard", "balcony", "garage", "garden",
    "path", "trail", "bench", "shelf", "pillow", "blanket","basket","clock","radio","television","computer","keyboard",
    "mouse", "screen", "remote", "camera", "printer", "lamp", "fan", "phone", "tablet", "watch", "battery", "plug",
    "wire", "light", "socket"
]
HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''',
    '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
import random
chosen_word = random.choice(words)
print(chosen_word)
place_holder = ""
display = ""
length_word = len(chosen_word)
for i in range (length_word):
    place_holder += "_"
print(place_holder)
game = False
words_store = []
lives = 0# Lives should not exceed 6
lives2=7
# --------------------------------------------------------------------------------------------------------------------
while (not game):

    guess = input("Guess a letter\n").lower()
    display = ""
    for i in chosen_word:
        if i == guess:
            display += guess
            words_store.append(guess)
        elif i in words_store:
            display += i
        else:
            display += "_"
    print(display)
    if "_" not in display:
        game = True
    if guess not in chosen_word:
        lives +=1
        lives2 -=1
        print(HANGMANPICS[lives])
        print(f"You have {lives2} lives left")
        if(lives >= 7):
            game = True
            print("Game Over")