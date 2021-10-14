#!/usr/bin/env python
# coding: utf-8

# In[8]:


from random import randint
import copy

story='''one day my friend {} and i decide to go to the {} for game {} .
        we really wanted to see the {} play the game{} .
        so we {} our {} down to the and bought some {}s.
        we got into the game and got some fun .
        we ate some {} and drank some {} .
        we had a great time we plan to a head next  year!'''
#a=("ha","ff","h")
#print(story.format('a','b','f'))




adjective=list(map(str,input().split(" ")))
city=list(map(str,input().split(" ")))
noun=list(map(str,input().split(" ")))
action_noun=list(map(str,input().split(" ")))
sport=list(map(str,input().split(" ")))
place=list(map(str,input().split(" ")))
    
def get_word(type):
    words=type
    cnt=len(words)-1
    index=randint(0,cnt)
    return type[index]




def create_story():
    return story.format(get_word(adjective),
                       get_word(city),
                       get_word(sport),
                       get_word(place),
                       get_word(sport),
                       get_word(noun),
                       get_word(noun),
                       get_word(noun),
                       get_word(noun),
                       get_word(noun))
print("story1:")
print(create_story())


print("story2:")
print(create_story())


# In[ ]:






# In[ ]:


adjective=["greed","abressive","rich","grubby"]
city=["chicago","India","america"]
noun=["people","map","music","food","water",'packed','food','icecream']
action_noun=["walk","fall","jump"]
sport=["dress","play","puck","cricket"]
place=['desert','ground','land']


# In[ ]:




