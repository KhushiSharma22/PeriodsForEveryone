import discord
import os
import random
from keep_alive import keep_alive
from replit import db
import re

def update_facts(new_fact):
  if "facts" in db.keys():
    facts = db["facts"]
    facts.append(new_fact)
    db["facts"] = facts
  else:
    db["facts"] = [new_fact] 

client = discord.Client()

fact_list = ["You could have as little as 150 or as many as 450 periods in your life","You’re born with all your eggs"," The age at which women start their period is becoming younger and younger","Pregnancy and periods can go hand in hand","Some periods aren’t true periods","A missed period doesn’t always mean you’re pregnant","You don’t need to have a period whilst on the pill","You lose a smaller amount of blood each month than you’d expect","Heavy periods could mean you have a hormone imbalance","Your brain can be affected by your period","A female spend nearly 10 years of her life on her period","Your period can affect how you sound and smell","Cramps that get more painful can be a sign of something serious","Period tracking apps help you stay on top of your cycle","Your periods may get worse during perimenopause","It's okay to skip your period","Women who live together sometimes do get their periods at the same time, but it may just be a coincidence.","On an average, a woman loses about 60 milliliters, or 2.7 ounces of blood during each period (That's almost two shot glasses)","Studies have shown that sleeping with a night light can help regulate your cycle","A girl's first period usually occurs between the ages of 10 and 14","If a girl does not have her period at age 16, this is called primary amenorrhea.","Having a hot shower eases cramps and makes you feel so much better.","Men also have periods. The main difference is they don't bleed but mood swings, cravings and all other things are there.","In 1946, Walt Disney created a 10-minute animated film called, 'The Story of Menstruation0'.","Your menstrual cycle is your 5th vital sign","Menstrual Cycle and Period are different things.","It's estimated that over 30% of women begin taking hormonal birth control to help with period pain.","Period symptoms are 'common' not 'normal'.","Calories don't count on your period.","Avoiding caffeine during your period is a good idea."]

options = fact_list
if "facts" in db.keys():
  options = options + db["facts"]

def factsFunction():
  return random.choice(options)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.lower().startswith('hey') or message.content.lower().startswith('hello') or message.content.lower().startswith('hi'):
    await message.channel.send(message.author.mention)
    await message.channel.send('''
    Heyy!!
Thanks for joining the server!😊
Use the command -help to get started.''')

  if message.content.lower().startswith('-help'):
    await message.channel.send('''
    Use -fact command to get yourself aware about menstruation with some interesting facts.

You can also add your own period facts to my list with -new "New Fact" command.

If you have any questions related to menstruation, drop them here and I will try my level best to answer all your questions.😊
    ''')

  if message.content.lower().startswith('-fact'):
    await message.channel.send(factsFunction())

  msg = message.content
  if msg.startswith('-new'):
    f = msg.split("-new ",1)[1]
    update_facts(f)
    await message.channel.send("New Fact Added!")
    print(options)

  if re.search('cramps',message.content.lower()):
    await message.channel.send('''
    Menstrual cramps are throbbing, aching cramps you get in your lower belly just before and during your period. They’re some of the most common, annoying parts of your period.

If you have mild menstrual cramps, take aspirin or another pain reliever, such as acetaminophen, ibuprofen,or naproxen. For best relief, take these medications as soon as bleeding or cramping starts.
    
Heat can also help. Place a heating pad or hot water bottle on your lower back or tummy. A warm bath may also provide some relief.
    
Avoid foods with caffeine and salt.
    
Massage your lower back and abdomen.

To read more about period cramps, visit this link- https://www.healthpartners.com/blog/13-ways-to-stop-period-pain/''')  

  if re.search('menstrual bleeding',message.content.lower()):
    await message.channel.send('''
    Menstrual bleeding is the result of the uterus shedding its lining.
Each month, a woman’s body prepares itself for pregnancy, but if no pregnancy occurs, the uterus will shed its lining and the woman's period will commence. Menstrual blood leaves the uterus through the cervix and then it is released from the body through the vagina.''')

  if re.search('menstrual blood',message.content.lower()):
    await message.channel.send('''
    Menstrual blood is not just blood; it’s also made up of tissue.
Menstrual blood consists of blood as well as extra tissue from the uterine lining. It also can contain the remnants of the egg that traveled down the fallopian tube into the uterus during ovulation and wasn’t fertilized.''')

  if re.search('menorrhagia',message.content.lower()):
    await message.channel.send('''
    Menorrhagia is the medical term for menstrual periods with abnormally heavy or prolonged bleeding. Although heavy menstrual bleeding is a common concern, most women don't experience blood loss severe enough to be defined as menorrhagia.
To read more about Menorrhagia go to this link- https://www.mayoclinic.org/diseases-conditions/menorrhagia/diagnosis-treatment/drc-20352834''')

  if re.search('sync',message.content.lower()):
    await message.channel.send('''
    Women and girls who live together may get their periods at the same time.
While it’s true that women who live together may indeed get their periods at the same time, the scientific evidence supporting the theory that living together causes menstrual synchrony remains unclear. 
The concept arose in 1971 when then University of Chicago psychologist Martha McClintock published a paper with her theory that women’s bodies react to the pheromones of other women around them, and it causes a synchronization of menstruation. 
She did a follow-up study that supported her theory in 1998. However, others have tested McClintock’s theory and the scientific results remain divided. Women who live together sometimes do get their periods at the same time, but it may just be a coincidence.''')

  if re.search('exercise',message.content.lower()):
    await message.channel.send('''
    The physical and mental benefits of exercise don’t stop just because you have your period. In fact, sticking with a routine can actually help ease some of the common complaints that accompany menstruation.
Avoiding exercise isn’t going to save energy or make you feel better. Instead of ceasing all activity during your period, use this week as an opportunity to try some new workouts. 
To know about the benefits of exercising during your period visit this link- https://www.healthline.com/health/exercise-during-period
''')
  
  if re.search('get pregnant',message.content.lower()):
    await message.channel.send('''
    It is very unlikely, but still possible to get pregnant while on your period. For conception to occur during your period, it most likely means that you have either an extremely short menstrual cycle or a long period that closely connects your ovulation stage with the onset of menstruation. An egg only stays in your fallopian tube waiting to be fertilized for about 24 hours, so if sperm is present during that time (and keep in mind that sperm can live for 3 to 4 days), you could get pregnant.   
''')

  if re.search('pms',message.content.lower()):
    await message.channel.send('''
    Premenstrual syndrome (PMS) is a combination of emotional, physical, and psychological disturbances that occur after a woman's ovulation, typically ending with the onset of her menstrual flow. 
The most common mood-related symptoms are irritability, depression, crying, oversensitivity, and mood swings. The most common physical symptoms are fatigue, bloating, breast tenderness (mastalgia), acne flare-ups, and appetite changes with food cravings.
To know more about PMS visit this link- https://www.medicinenet.com/premenstrual_syndrome/article.htm
''')

  if re.search('menstrual cycle',message.content.lower()):
    await message.channel.send('''
    The female reproductive system involves the uterus, ovaries, fallopian tubes and vagina. The female hormones, estrogen and progesterone produced by the ovaries, rise and fall during the month and cause the menstrual cycle.
A menstrual cycle is the time from the first day you start bleeding (also called day 1) of one period to the day before the next period. The average menstrual cycle is 28 days long. However, a cycle can range anywhere from 21 to 35 days.
''')

  if re.search('first period',message.content.lower()):
    await message.channel.send('''
    The first time a girl gets her menstrual period is called menarche and it starts at an average of 12 years. A girl can begin menstruating anytime between the ages of 10 and 16 years once all the parts of a girl's reproductive system have matured and are working together.
To know more visit this link- https://www.healthline.com/health/first-period
''')

  if re.search('late period',message.content.lower()) or re.search('irregular period',message.content.lower()) or re.search('missed period',message.content.lower()):
    await message.channel.send('''
    Missed or late periods happen for many reasons other than pregnancy. Common causes can range from hormonal imbalances to serious medical conditions.

There are also two times in a woman’s life when it’s totally normal for her period to be irregular: when it first begins, and when menopause starts. As your body goes through the transition, your normal cycle can become irregular.

Most women who haven’t reached menopause usually have a period every 28 days. However, a healthy menstrual cycle can range from every 21 to 35 days. If your period doesn’t fall within these ranges, it could be because of one of the following reasons.
1. Stress
2. Low body weight
3. Obesity
4. Polycystic ovary syndrome (PCOS)
5. Birth control
6. Chronic diseases
7. Early peri-menopause
8. Thyroid issues 
''')

  if re.search('early peri-menopause',message.content.lower()):
    await message.channel.send('''
    Most women begin menopause between ages 45 to 55. Women who develop symptoms around age 40 or earlier are considered to have early peri-menopause. This means your egg supply is winding down, and the result will be missed periods and eventually the end of menstruation.
''')

  if re.search('birth control',message.content.lower()):
    await message.channel.send('''
    You may experience a change in your cycle when you go on or off birth control. Birth control pills contain the hormones estrogen and progestin, which prevent your ovaries from releasing eggs. It can take up to six months for your cycle to become consistent again after stopping the pill. Other types of contraceptives that are implanted or injected can cause missed periods as well.
''')

  if re.search('pcos',message.content.lower()) or re.search('polycystic ovary syndrome',message.content.lower()) or re.search('pcod',message.content.lower()):
    await message.channel.send('''
    Polycystic ovary syndrome (PCOS) is a condition that affects a woman’s hormone levels.

Women with PCOS produce higher-than-normal amounts of male hormones. This hormone imbalance causes them to skip menstrual periods and makes it harder for them to get pregnant.

PCOS also causes hair growth on the face and body, and baldness. And it can contribute to long-term health problems like diabetes and heart disease.

Birth control pills and diabetes drugs can help fix the hormone imbalance and improve symptoms.
To read more about PCOS visit this link- https://www.healthline.com/health/polycystic-ovary-disease
''')

  if re.search('menopause',message.content.lower()):
    await message.channel.send('''
    Menopause is the natural cessation, or stopping, of a woman's menstrual cycle, and marks the end of fertility. Most women experience menopause by the age of 52, but pelvic or ovarian damage may cause sudden menopause earlier in life. Genetics or underlying conditions may also lead to early onset of menopause.
''')

  if re.search('menarche',message.content.lower()):
    await message.channel.send('''
    Menarche is the first menstrual cycle, or first menstrual bleeding, in female humans. From both social and medical perspectives, it is often considered the central event of female puberty, as it signals the possibility of fertility.
''')

  if re.search('menstrual cup',message.content.lower()):
    await message.channel.send('''
    A menstrual cup is a type of reusable feminine hygiene product. It’s a small, flexible funnel-shaped cup made of rubber or silicone that you insert into your vagina to catch and collect period fluid.
Cups can hold more blood than other methods, leading many women to use them as an eco-friendly alternative to tampons. And depending on your flow, you can wear a cup for up to 12 hours.
To learn more about menstrual cups visit- https://www.healthline.com/health/womens-health/menstrual-cup
''')

keep_alive()     

client.run(os.getenv('TOKEN'))
