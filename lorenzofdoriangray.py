#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:12:07 2022

@author: nrm518

Please credit me if you use this elsewhere, but otherwise feel free to go ham!
This was my final project for the first programming class I took in college.

"""
#maybe add plural nouns
#import packages
import numpy as np #For arrays
import matplotlib.pyplot as plt #For plotting
from scipy.integrate import odeint #I want to use ODEint. The internet doesn't want me to. Oh well. 
import plotly.express as px
import plotly.io as pio
pio.renderers.default='browser'


    
#Variables
#time
    #beginning time
tmin = 0
    #ending time
tmax = 20
    #number of steps
nts = 100000
    #as an array
time = np.linspace(tmin, tmax,nts)

#Constants for lorenz
#Don't put negative numbers or imaginary numbers in here, but other than that go crazy.
#Prandtl number (example number from brown webpage: 10)
sigma = 10
#Rayleigh number (example number from brown webpage: 28)
rho = 28
#Some physical property of region (example number from brown webpage: 8/3)
beta = 8/3

#initial conditions array [x initial, y initial, z initial]
#feel free to change these. negatives, whatever are fine here. still no imaginary numbers allowed though.
s_init = [1.,2.,3.]


#inputs to s_init:
    #Dalton: inputs 1., 42000., 2


# Lorenz Eqns Code
#The version I found online didn't use ODEint. I want to use odeint because I feel like it will be
#easier and more accurate and it's right there, y'know?

#function that has the lorenz ODES
def lorenz(s,t):
    #constants are going to be global variables
    #x values are 0th column in s_init
    x = s[0]
    #y vals are 1st column in s_init
    y = s[1]
    #z vals are 2nd column in s_init
    z = s[2]
    
    #deriv = [dx/dt, dy/dt, dz/dt]
    deriv = [sigma*(y-x), x*(rho-z)-y, x*y-beta*z]
    #return the values of the derivatives
    return deriv

#Differential Equation-solving function, my beloved.
def diffeq_solver(s_initial, tmin, tmax, nts, deriv):
    t = np.linspace(tmin,tmax,nts)
    s = odeint(deriv, s_initial, t)
    return t,s 

#Actually calling the functions

#(time, array with 0th column x 1st column y 2nd column z) = the solved differential equation
(t, pos) = diffeq_solver(s_init, tmin, tmax, nts, lorenz)

#cld all be done in one line, but this is much easier to read
x = pos[:,0]
y = pos[:,1]
z = pos[:,2]

#the 3d scatter plot
fig2 = px.scatter_3d(pos, x=0,y=1,z=2)

#mostly plotting just to make sure the equations are doing what they're supposed to, and also to see the approx
#range of stuff
#plotting x, y, and z on graphs, courtesy of:
    #https://medium.com/codex/python-and-physics-lorenz-and-rossler-systems-65735791f5a2
    #Multiple graph plotting
fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize = (15, 5))
ax1.plot(x, y)
#adding the axes titles myself, used help from
# https://matplotlib.org/stable/gallery/pyplots/fig_axes_labels_simple.html
ax1.set_xlabel("X")
ax1.set_ylabel("Y")
ax1.set_title("X & Y")
#plot 2
ax2.plot(x, z)
ax2.set_title("X & Z")
ax2.set_xlabel("X")
ax2.set_ylabel("Z")
#plot 3
ax3.plot(y, z)
ax3.set_title("Y & Z")
ax3.set_xlabel("Y")
ax3.set_ylabel("Z")
plt.show()
print(len(x))


fig2 = px.scatter_3d(pos, x=0,y=1,z=2 )
fig2.show()

#For my sentence structure, I'm going to take the first sentence of a picture of dorian gray
#at least for the proof of concept.
#The sentence is as follows:
"""The studio was filled with the rich odour of roses, and when the light summer wind 
stirred amidst the trees of the garden, there came through
the open door the heavy scent of the lilac, or the more delicate perfume
of the pink-flowering thorn. """
#Broken down, the sentence is as follows

#article + noun1 + verb (past tense) + prep + art2 + adj1 + noun2 + prep +plnoun1 + ,
# + coord conjunct + when acting as conjunct + art3 + adj2 + noun3 + noun4
#this is tiring. for proof of concept i'm just going to do the first clause. 
#i might base it off of little red riding hood for full story, but also I'm going to have both
#because I like the Picture of Dorian Gray and the first few paragraphs have some really fun imagery

""" Little red riding hood story as written down by me from memory
Once upon a time there was a little girl named Little Red Riding Hood. 
One day her mother sent her to her grandmother's house with a basket full of goodies to deliver.
Along the way, a big bad wolf spotted Little Red Riding Hood and her basket, so he went ahead to her
grandmother's house and ate the grandma.
When Little Red Riding Hood got there, she thought the wolf was her grandma.
When the wolf revealed himself and tried to eat her, she ran away home.
"""

#importing my arrays from the file word_arrays
#found how to do this here: 
    #https://stackoverflow.com/questions/42314934/python-importing-an-array-from-a-different-file
from word_arrays import nouns, articles, ptverbs, adjectives, conjunctions, prepz, adverbs

#most of the word banks have 100 words apiece. They take up too much space so they get their own file


#function that turns numbers into strings and then splits them up so each
#digit is its own little string in an array.


# Split string using for loop
#source: https://www.includehelp.com/python/split-a-string-into-array-of-characters.aspx
# function to split string
def split_str(s):
  return [ch for ch in s]

#function that has you input a number, and which digit of that number you would like to return
#output is the digit of that number returned.
#input the actual digit you want. the function will correct for the fact that it's an array
def assign_d_ig(number, digit):
    snum = str(number)
    digs = split_str(snum)
    if digs[0] =='-':
        digit +=1
    #https://stackoverflow.com/questions/11251709/check-if-item-is-in-an-array-list
    if ('.' in digs and (digit ==2) and( number <10.00)):
        wanted = digs[2]
    elif ('.' in digs and( digit ==3) and( abs(100)>number >=abs(10.00))):
        digit = 4
        wanted = digs[4]
    elif ('.' in digs and( digit ==4) and(abs(1000)> number >=abs(100.00))):
        digit = 5
        wanted = digs[5]
    elif ('.' in digs and( digit ==5) and(abs(10000)> number >=abs(1000.00))):
        digit = 6
        wanted = digs[6]
    elif ('.' in digs and( digit ==6) and(abs(100000)> number >=abs(10000.00))):
        digit = 7
        wanted = digs[7]
    elif ('.' in digs and( digit ==7) and(abs(1000000)> number >=abs(100000.00))):
        digit = 8
        wanted = digs[8]
    elif ('.' in digs and( digit ==8) and(abs(10000000)> number >=abs(1000000.00))):
        wanted = digs[9]
    elif ('.' in digs and( digit ==9) and(abs(100000000)> number >=abs(10000000.00))):
        digit = 10
        wanted = digs[10]
    elif ('.' in digs and( digit ==10) and(abs(1000000000)> number >=abs(10000000.00))):
        digit = 11
        wanted = digs[11]
    elif ('.' in digs and( digit ==11) and(abs(10000000000)> number >=abs(100000000.00))):
        digit = 12
        wanted = digs[12]
    else:
        wanted = digs[digit-1]
    return int(wanted)

#function that finds what position a decimal is in
#relies on split_str
#input must be a float

def wheredecimal (num):
    narray = split_str(str(num))
    n = 0
    while True:
        dig = narray[n]

        if str(dig) == '.':
            break
        n +=1
    return n

#new version of assign_dig that should eliminate having a limit for how large the numbers can be
def assign_dig(number, digit):
    snum = str(number)
    digs = split_str(snum)
    if digs[0] =='-':
        digit +=1
    deci = wheredecimal(number)
    if digit == deci:
        wanted = digs[digit+1]
    else:
        wanted = digs[digit]
    return int(wanted)

        
#testing assign_dig
testboy = assign_dig(1003., 2)
print("This is a test of assign_dig:"+ str(assign_dig(1003., 4)))

#Assigning words to coords
#functions section of assigning words to coords
#i'm gonna make her a function since i'll be using her a lot (origianlly was just the for loop.
#delted the for loop so adding this note for context)
def artfunc(artnum, artarray):
    #for loop that assigns the article to correspond with the pre assigned number in the array 

    for ti, i in enumerate(artarray):
        if i[0] == artnum:
            art = i[2]
            break
    return art

#art func also works for conjunctions!


#testing if she (artfunc) works
testart = artfunc(testboy, articles)
print("This is a test of artfunc:" + testart)

#what if i make it more general

#function that takes a word from a 3-columned array (one of my word banks) where the first 2 columns
#are digits 1-9, and the last column is a word. pos (part of speech) is the array to find the words in.
def gimme_word(digit1, digit2, pos):
    #for loop that assigns the article to correspond with the pre assigned number in the array 
    if digit2 == 0:
        digit2 =9
    for ti, i in enumerate(pos):
        
        if i[0] == digit1 and i[1] == digit2:
            word = i[2]
            break
    return word
#testing if gimme_word works
testnoun = gimme_word(0,9,nouns)
print("this is a test of gimme_word:" + testnoun)

#articles (need 2)
    #first article corresponds to the 2nd digit of x's 101st term
    #make x's 100th term into a string and then splits it up
art1num= assign_dig(x[100],2)

art1 = artfunc(art1num, articles)

#article 2
art2num = assign_dig(x[99], 2)

art2 = artfunc(art2num, articles)

#article 3
art3num = assign_dig(x[800], 1)

art3 = artfunc(art3num, articles)

#article 4
print(x[731])
art4num = assign_dig(x[731], 4)

art4 = artfunc(art4num, articles)
#article 5
art5num = assign_dig(x[99], 3)

art5 = artfunc(art5num, articles)
#art6
art6num= assign_dig(x[106],2)

art6 = artfunc(art6num, articles)

#article 7
art7num = assign_dig(x[997], 2)

art7 = artfunc(art7num, articles)

#article 8
art8num = assign_dig(x[808], 1)

art8 = artfunc(art8num, articles)

#article 9
art9num = assign_dig(x[739], 4)

art9 = artfunc(art9num, articles)
#article 10
art10num = assign_dig(x[5], 3)

art10 = artfunc(art10num, articles)

#nouns: (need 4)

#noun 1
n1d1 = assign_dig(y[90], 3)
n1d2 = assign_dig(y[91], 5)

noun1 = gimme_word(n1d1, n1d2, nouns)

#noun2
n2d1 = assign_dig(y[35], 2)
print(y[300])
n2d2 = assign_dig(y[300], 1)

noun2 = gimme_word(n2d1, n2d2, nouns)

#noun3

n3d1 = assign_dig(y[420], 8)
n3d2 = assign_dig(y[14], 2)
print(n3d2)
noun3 = gimme_word(n3d1, n3d2, nouns)

#noun4
n4d1 = assign_dig(y[900], 9)
n4d2 = assign_dig(y[600], 8)

noun4 = gimme_word(n4d1, n4d2, nouns)

#noun 5
n5d1 = assign_dig(y[90], 2)
n5d2 = assign_dig(y[91], 3)

noun5 = gimme_word(n5d1, n5d2, nouns)

#noun6
n6d1 = assign_dig(y[35], 4)
n6d2 = assign_dig(y[300], 5)

noun6 = gimme_word(n6d1, n6d2, nouns)

#noun7

n7d1 = assign_dig(y[420], 0)
n7d2 = assign_dig(y[14], 0)

noun7 = gimme_word(n7d1, n7d2, nouns)

#noun8
n8d1 = assign_dig(y[900], 8)
n8d2 = assign_dig(y[600], 7)

noun8 = gimme_word(n8d1, n8d2, nouns)

#noun 9
n9d1 = assign_dig(y[909], 2)
n9d2 = assign_dig(y[919], 3)

noun9 = gimme_word(n9d1, n9d2, nouns)

#noun10
n10d1 = assign_dig(y[350], 4)
n10d2 = assign_dig(y[310], 5)

noun10 = gimme_word(n10d1, n10d2, nouns)

#noun11

n11d1 = assign_dig(y[411], 0)
n11d2 = assign_dig(y[141], 0)

noun11 = gimme_word(n11d1, n11d2, nouns)

#noun12
n12d1 = assign_dig(y[912], 8)
n12d2 = assign_dig(y[612], 7)

noun12 = gimme_word(n12d1, n12d2, nouns)

#verbs (need 1)
#i have been working on this for like. 4 hours straight
v1d1 = assign_dig(z[69], 0)
v1d2 = assign_dig(z[500], 1)

verb1 = gimme_word(v1d1, v1d2, ptverbs)
#verb2
v2d1 = assign_dig(z[96], 3)
v2d2 = assign_dig(z[24], 0)

verb2 = gimme_word(v2d1, v2d2, ptverbs)
#verb3
v3d1 = assign_dig(z[96], 4)
v3d2 = assign_dig(z[24], 1)

verb3 = gimme_word(v3d1, v3d2, ptverbs)

#prepositions (2)

#prep 1
p1d1 = assign_dig(y[700], 7)
p1d2 = assign_dig(z[78], 8)

prep1 = gimme_word(p1d1, p1d2, prepz)

#prep2
p2d1 = assign_dig(y[88], 9)
p2d2 = assign_dig(z[54], 1)

prep2 = gimme_word(p2d1, p2d2, prepz)
#prep3
p3d1 = assign_dig(y[808], 7)
p3d2 = assign_dig(z[584], 2)

prep3 = gimme_word(p3d1, p3d2, prepz)
#prep4
p4d1 = assign_dig(y[678], 9)
p4d2 = assign_dig(z[543], 2)

prep4 = gimme_word(p4d1, p4d2, prepz)
#prep5
p5d1 = assign_dig(y[80], 3)
p5d2 = assign_dig(z[90], 1)

prep5 = gimme_word(p5d1, p5d2, prepz)
prep2 = gimme_word(p2d1, p2d2, prepz)
#prep6
p6d1 = assign_dig(y[808], 6)
p6d2 = assign_dig(z[584], 1)

prep6 = gimme_word(p6d1, p6d2, prepz)
#prep7
p7d1 = assign_dig(y[678], 8)
p7d2 = assign_dig(z[544], 1)

prep7 = gimme_word(p7d1, p7d2, prepz)
#prep8
p8d1 = assign_dig(y[801], 3)
p8d2 = assign_dig(z[901], 1)

prep8 = gimme_word(p8d1, p8d2, prepz)

#adjectives 

#adj1
adj1d1 = assign_dig(x[933], 4)
adj1d2 = assign_dig(y[890], 5)

adj1 = gimme_word(adj1d1, adj1d2, adjectives)
#adj2
adj2d1 = assign_dig(x[330], 7)
adj2d2 = assign_dig(y[720], 5)

adj2 = gimme_word(adj2d1, adj2d2, adjectives)

#adj3
adj3d1 = assign_dig(x[933], 3)
adj3d2 = assign_dig(y[890], 4)

adj3 = gimme_word(adj3d1, adj3d2, adjectives)
#adj4
adj4d1 = assign_dig(x[330], 6)
adj4d2 = assign_dig(y[720], 4)

adj4 = gimme_word(adj4d1, adj4d2, adjectives)

#adj5
adj5d1 = assign_dig(x[933], 2)
adj5d2 = assign_dig(y[890], 3)

adj5 = gimme_word(adj5d1, adj5d2, adjectives)
#adj6
adj6d1 = assign_dig(x[330], 5)
adj6d2 = assign_dig(y[720], 3)

adj6 = gimme_word(adj6d1, adj6d2, adjectives)

#conjunctions

con1d1 = assign_dig(z[300], 2)
con1d2 = assign_dig(z[470], 0)

conj1 = artfunc(con1d1, conjunctions)
#conjunction2
con2d1 =assign_dig(z[470], 1)


conj2 = artfunc(con2d1, conjunctions)

#adverbs

#adverb1
adv1d1 = assign_dig(y[812], 0)
adv1d2 = assign_dig(y[931], 1)

adv1 = gimme_word(adv1d1, adv1d2, adverbs)

#adverb2
adv2d1 = assign_dig(y[812], 1)
adv2d2 = assign_dig(y[931], 2)

adv2 = gimme_word(adv1d1, adv1d2, adverbs)

print(noun1)
#Forming the sentence:
    #clause 1
    #art1 + noun1 + verb (past tense) + prep + art2 + adj1 + noun2 + prep2 +noun4
    #  + conj1 + prep3 + art3 +adj2 + noun5 +noun6 + verb2 + prep4 + art4 + noun7 + prep5 + art5 +noun8
    # + ", " + adv1 + verb3 + prep6 + art6 +adj3 +noun9 + art7 + adj4 +noun10 + prep7 + art8 + noun10
    # + ", " + conj2 + art9 + adv2 + adj5 + noun11 + prep8 +art10 + adj6 + noun12 + "."
"""The studio was filled with the rich odour of roses, and when the light summer wind 
stirred amidst the trees of the garden, there came through
the open door the heavy scent of the lilac, or the more delicate perfume
of the pink-flowering thorn. """
#feel free to add extra stuff and change up the sentence as you will! feel free to play with this


print(art1)

print(art1 + noun1 + verb1 + prep1 + art2 + adj1 + noun2 + prep2 + noun4 + ', '
      + conj1 + prep3 + art3 +adj2 + noun5 +noun6 + verb2 + prep4 + art4 + noun7 + prep5 + art5 +noun8
      + ", " + adv1 + verb3 + prep6 + art6 +adj3 +noun9 + art7 + adj4 +noun10 + prep7 + art8 + noun10
      + ", " + conj2 + art9 + adv2 + adj5 + noun11 + prep8 +art10 + adj6 + noun12 + ".")



#sentence structure

#sources for actually understanding things:
    #https://www.cfm.brown.edu/people/dobrush/am34/Mathematica/ch3/lorenz.html Explained how the equations 
    #actually work. 
    #The Picture of Dorian Gray by Oscar Wilde (accessed via the Gutenberg Project's PDF)
    #
    #sources that helped with grammar
        #http://partofspeech.org/what-part-of-speech-is-when/ 
        
#i'm letting my friends give me inputs for the functions. here are their requests and the outputs:
"""
    Gabe's input: 3, 17, 98.5
    Output:the grandpa finished on the friendly chaos along woman , 
    and near that lucky princess coyote fought but that lilac but this field
    
    Emily's input: 12, 23, 67
    Output: a staff set from a winged cookie across doily , but before 
    Dr.pretty curtain rod table sat beneath Dr.pond by Dr.studio 
    New Output after bug fix in numassign:
    Dr.summer stole by Dr.mulched spring aboard studio , or beneath Dr.learned woman 
    laptop knighted from Mr.program by a cellphone , gently sat near some many-eyed 
    winter Mr.spikey knight beside Dr.knight , and a gently mulched grandpa after 
    the balanced program .
    
    Discord Rando named Canuck: 42 2814 5887
    output: some shoe wolfed down for Dr.pretty number off wheel , as amid Ms.malformed 
    wolf wheel bloomed beneath Mrs.dog to that manor , too laughed beneath 
    Ms.wet shoe the drunken window below Ms.window , so Mrs.too fat president between that fast frog .
    
    Discord Rando named Llull: 5, 14, 124
    output: that garden stole minus that ugly chaos among knoll , 
    and but a bad lily man pat with some cocktail beside that wolf , 
    abnormally flowered beside that funny scream Mrs.winged corset but a corset ,
    and Mrs.abnormally many-eyed prince except the gentle finale .
    
    Discord Rando named carpet wizard: 18, 358, 8384
    output: Mx.page crouched onto Mx.quiet wolf by bridge , 
    or except that large page frog trained at some tower near Mx.president ,
    sloppily finished off the thin corset some harsh president despite that president , 
    but Ms.sloppily annoying spring for the magical lilac .
    
    Discord Rando named vm70: pi, 47, and 70
    output: the queen punched off the preppy prince like knoll , 
    but below Mr.indescribbable staff finale knighted before Ms.railing near the building , 
    neatly bloomed except the wet cup Mr.appreciated balcony off Mr.balcony , 
    and Mrs.neatly rough person near the maniac cellphone .
    
    Discord Rando named Gareef: 420, 69, 1337
    *output: Ms.couch ripped around Ms.bulbous porch swing but finale , 
    therefore unlike Mr.willowy grandpa cup trained through a president except Ms.queen , 
    ultimately bumbled round Mx.beautiful coyote the ugly queen toward Mr.queen , 
    when a ultimately eccentric shrubbery regarding Mr.light queen .
    
    John: 414.56 3.1415 2006.01
    output: the finale punched next the haunted chaos off bumblebee ,
    and on a small finale odour sprawled beside the wolf up to the summer , 
    officiallly finished on the put-together king the wet finale among a finale , 
    and that officiallly put-together rose near Mr.chivalrous lilac .
    
    Bears from yellowstone magic discord: 23277 273 4663
    *output:the ur mom heard from Mx.wet summer up to cellphone ,
    because round that final window finale swaggered unlike this woman after a window , 
    wonkily lounged before a busy rose that busy ur mom beneath that ur mom , 
    so this wonkily beautiful ur mom before Dr.mottled window .
    
    discord rando from ysm named echo: 917, 1226, 37394
    output: some painting walked below some emo grandpa against program ,
    so below this balanced tree woman typed but Mx.pond above this winter ,
    sleepily chuckled aboard some maniac tree some aromatic woman across this woman , 
    but Mx.sleepily annoying club against that slow winter .
    
    Peaches: 3, 9, 6
    *output: the cone was filled beside the electric chaos below shoe ,
    so round that pretty finale lily glared via the knoll in the couch , 
    even bloomed like the maniac lily some aromatic cherry blossom across that cherry blossom ,
    but that even green grandpa like the easygoing class .
    
    Sample output:10, 28, 8/3
        a window ate like a lucky cookie at balcony , 
        because along Dr.large grass shoelace left on a dress below a knoll ,
        slowly crouched from a drunken wind Ms.light cat except Dr.cat ,
        so the slowly drunken page onto the mulched painting .
    
    Sam: 7, 43, 7/3
    output:that log pondered in that light princess in doily ,
    as regarding this pretty night log mulched next the painting between that volleyball ,
    knavishly bloomed for that lonesome laptop the friendly log for this log , 
    or that knavishly rich fall by the scary log .
    
    Class generated:
    a bridge placed beside a horrific flower below arrangement ,
    or along that fat king corset drank about Dr.ur mom as a coyote , s
    loppily brushed on Mr.many-legged king Mrs.large pack beside that pack , 
    and Dr.sloppily electric couch except the bumbling lilac .
    
    Cindy: 2 2 2
    output:the building painted since the bumbling flower at staff , 
    because out that giant king manor rode toward the odour by the couch , 
    nearly heard in the bulbous cocktail a painted arrangement beneath that arrangement , 
    so the nearly bulbous knoll beside the delicious child .
    
    input: 10.0001, 28.1, 8/3
    *output:a pond sat via a unknowable cookie in number , 
    because among Dr.lucky grass volleyball knighted by Mr.class beneath a rose , 
    neatly crouched concerning a drunken window Ms.tough mouse for Dr.mouse , 
    so a neatly unknowable fall per the aromatic chaos .
    
    
"""

    
    
    
    
    
    
    
#
    
    
