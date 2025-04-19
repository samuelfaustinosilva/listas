#!/usr/bin/env python
# coding: utf-8

# ### Definição de Listas: É um objeto representado por uma sequência de outros objetos. Estes objetos são separados por vírgulas e iniciados e terminados por colchetes [ ] 

# #### Criando listas

# In[2]:


lista = [1,2,3]


# In[3]:


lista


# In[4]:


type(lista)


# In[7]:


Lista2 = list((1,2,3))


# In[8]:


Lista2


# In[9]:


Lista3 = list("123")


# In[10]:


Lista3


# In[11]:


Lista4 = []


# In[12]:


Lista4


# In[13]:


len(Lista4)


# In[18]:


len(Lista2)


# In[19]:


for elemento in range(4):
    print(elemento)
    if elemento != 0:
        Lista4.append(elemento)
        print(Lista4)


# In[20]:


Lista4


# ### Acessando os valores da lista

# In[21]:


Lista2[1]


# In[22]:


Lista2 + Lista3


# In[23]:


Lista3*5


# ### Verificar se um objeto pertence a  lista

# In[25]:


"1" in Lista2


# In[26]:


1 in Lista2


# In[27]:


Lista5 = []


# In[28]:


Lista5


# In[29]:


for elemento in range(5):
    Lista5.append(elemento)
    print(Lista5)


# In[31]:


Lista5


# In[32]:


3 in Lista5


# ### Métodos

# In[33]:


Lista5


# In[34]:


Lista5.pop()


# In[35]:


Lista5


# In[36]:


Lista5.pop(1)


# In[37]:


Lista5


# In[38]:


Lista5.remove(2)


# In[39]:


Lista5


# In[40]:


Lista6 = [5,8,9,6,3,2,0,1]


# In[41]:


Lista6


# In[42]:


Lista6.sort()


# In[43]:


Lista6


# In[44]:


Lista6.sort(reverse=True)


# In[45]:


Lista6


# In[46]:


Lista6.index(5)


# In[47]:


Lista6.count(5)


# In[ ]:




