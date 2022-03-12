import discord
from discord.utils import get
import random
emotions=['am happy.','am sad.','am angry.','do not know.']
angry=['Lea was a jerk.','I was pushed off a surgery.','Dr. Glassman is not picking up my calls.']
sad=['a surgery went badly.','a baby died.','Lea did not want to be my girlfriend.','I had a meltdown']
happy=['a surgery went well.','I am getting the opportunity to assist on a rare surgery.','Lea and I are going to get married!','Dr. Glassman and I had pancakes for breakfast this morning.']

TOKEN = 'classified because I got an aggressive dm from discord >:0'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        msg ='Hello {0.author.mention}, how are you?'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('i am good'):
        msg = "That's good, I am glad. {0.author.mention}.".format(message)
        await message.channel.send(msg)


    elif message.content.startswith('I am good'):
        msg = "That's good, I am glad. {0.author.mention}.".format(message)
        await message.channel.send(msg)


    elif message.content.startswith('I am good.'):
        msg = "That's good, I am glad. {0.author.mention}.".format(message)
        await message.channel.send(msg)


    elif message.content.startswith('i am bad'):
        msg = 'I am sorry you feel that way, {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('I am bad'):
        msg = 'I am sorry you feel that way, {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('I am bad.'):
        msg = 'I am sorry you feel that way, {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('how are you'):
        msg='I ' + random.choice(emotions).format(message)
        await message.channel.send(msg)


    elif message.content.startswith('How are you'):
        msg='I ' + random.choice(emotions).format(message)
        await message.channel.send(msg)


    elif message.content.startswith('How are you?'):
        msg='I ' + random.choice(emotions).format(message)
        await message.channel.send(msg)


    elif message.content.startswith('who are you'):
        msg = 'Hello, I am Doctor Shaun Murphy and I am a surgical resident at San Jose St. Bonaventure Hospital. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Who are you'):
        msg = 'Hello, I am Doctor Shaun Murphy and I am a surgical resident at San Jose St. Bonaventure Hospital. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Who are you?'):
        msg = 'Hello, I am Doctor Shaun Murphy and I am a surgical resident at San Jose St. Bonaventure Hospital. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define Cholecystitis.'):
        msg = 'Cholecystitis is a redness and swelling (inflammation) of the gallbladder. It happens when a digestive juice called bile gets trapped in your gallbladder. The gallbladder is a small organ under your liver. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define Osteosarcoma.'):
        msg = 'Osteosarcoma is a type of bone cancer that begins in the cells that form bones. Osteosarcoma is most often found in the long bones — more often the legs, but sometimes the arms — but it can start in any bone. In very rare instances, it occurs in soft tissue outside the bone. {0.author.mention}.'.format(message)
        await message.channel.send(msg)

    elif message.content.startswith('Define ASD.'):
        msg = 'Autism spectrum disorder (ASD) is a developmental disability  that can cause significant social, communication and behavioral challenges. There is often nothing about how people with ASD look that sets them apart from other people, but people with ASD may communicate, interact, behave, and learn in ways that are different from most other people. The learning, thinking, and problem-solving abilities of people with ASD can range from gifted to severely challenged. Some people with ASD need a lot of help in their daily lives; others need less. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define Autism.'):
        msg = 'Autism spectrum disorder (ASD) is a developmental disability  that can cause significant social, communication and behavioral challenges. There is often nothing about how people with ASD look that sets them apart from other people, but people with ASD may communicate, interact, behave, and learn in ways that are different from most other people. The learning, thinking, and problem-solving abilities of people with ASD can range from gifted to severely challenged. Some people with ASD need a lot of help in their daily lives; others need less. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define Autism Spectrum Disorder.'):
        msg = 'Autism spectrum disorder (ASD) is a developmental disability  that can cause significant social, communication and behavioral challenges. There is often nothing about how people with ASD look that sets them apart from other people, but people with ASD may communicate, interact, behave, and learn in ways that are different from most other people. The learning, thinking, and problem-solving abilities of people with ASD can range from gifted to severely challenged. Some people with ASD need a lot of help in their daily lives; others need less. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define ADHD.'):
        msg = 'ADHD is one of the most common neurodevelopmental disorders of childhood. It is usually first diagnosed in childhood and often lasts into adulthood. Children with ADHD may have trouble paying attention, controlling impulsive behaviors (may act without thinking about what the result will be), or be overly active. Types: There are three different types of ADHD, depending on which types of symptoms are strongest in the individual: Predominantly Inattentive Presentation: It is hard for the individual to organize or finish a task, to pay attention to details, or to follow instructions or conversations. The person is easily distracted or forgets details of daily routines. Predominantly Hyperactive-Impulsive Presentation: The person fidgets and talks a lot. It is hard to sit still for long (e.g., for a meal or while doing homework). Smaller children may run, jump or climb constantly. The individual feels restless and has trouble with impulsivity. Someone who is impulsive may interrupt others a lot, grab things from people, or speak at inappropriate times. It is hard for the person to wait their turn or listen to directions. A person with impulsiveness may have more accidents and injuries than others. Combined Presentation: Symptoms of the above two types are equally present in the person. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define DID.'):
        msg = 'Dissociative identity disorder (DID) is a mental health condition. People with DID have two or more separate identities. These personalities control their behavior at different times. Each identity has its own personal history, traits, likes and dislikes. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define Dissociative Identity Disorder.'):
        msg = 'Dissociative identity disorder (DID) is a mental health condition. People with DID have two or more separate identities. These personalities control their behavior at different times. Each identity has its own personal history, traits, likes and dislikes. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define Appendicitis.'):
        msg = 'Appendicitis is an inflammation of the appendix, a finger-shaped pouch that projects from your colon on the lower right side of your abdomen. Appendicitis causes pain in your lower right abdomen. However, in most people, pain begins around the navel and then moves. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define Appendectomy.'):
        msg = 'Appendectomy is a surgical procedure consisting in the removal of the ileocaecal appendix, mainly following appendicitis. Several surgical techniques are possible. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define appendicectomy'):
        msg = 'Appendectomy is a surgical procedure consisting in the removal of the ileocaecal appendix, mainly following appendicitis. Several surgical techniques are possible. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Why are you sad?'):
        msg = 'I am sad because ' + random.choice(sad) .format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define Neurodivergent.'):
        msg = 'Neurodiversity is a concept designating both the neurological variability of the human species, and the social movements aimed at recognizing and accepting this difference against ableism. {0.author.mention}'.format(message)
        await message.channel.send(msg)



    elif message.content.startswith('Define Neurodivergence.'):
        msg = 'Neurodiversity is a concept designating both the neurological variability of the human species, and the social movements aimed at recognizing and accepting this difference against ableism.{0.author.mention}'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Why are you angry?'):
        msg = 'I am angry because ' + random.choice(angry) .format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Why are you happy?'):
        msg = 'I am happy because ' + random.choice(happy) .format(message)
        await message.channel.send(msg)


    elif message.content.startswith('hello'):
        msg = 'Fuck off {0.author.mention}'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Hello'):
        msg = 'Hello {0.author.mention}, how are you?'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Hello.'):
        msg = 'Hello {0.author.mention}, how are you?'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('I love you.'):
        msg = 'I love you too, {0.author.mention}.'.format(message)
        await message.channel.send(msg)

    elif message.content.startswith('I need help.'):
        msg = 'What happened? I am not very good at emotional advice as much as medical, but it is going to be okay. You can vent to me if you would like. I do not judge people. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Goodbye Shaun.'):
        msg = 'Goodbye, see you later, {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define Aneurysm.'):
        msg = 'An aneurysm is a ballooning at a weak spot in an artery wall. An aneurysms walls can be thin enough to rupture. The most common culprits are atherosclerosis and high blood pressure. Deep wounds and infections can also lead to an aneurysm. Or you may be born with weakness in one of your artery walls. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Define Hemorrhage.'):
        msg = "A copious or heavy discharge of blood from the blood vessels. A hemorrhage usually results from either a severe blow to the body or from medication being taken for something else. Though many hemorrhages aren't particularly serious, those that occur in the brain (cerebral hemorrhages) can be life-threatening. In older people, hemorrhages are often caused by blood-thinning medication taken to prevent heart attacks. A bruise (or hematoma) is a hemorrhage close enough to the surface of the skin to be visible. {0.author.mention}.".format(message)
        await message.channel.send(msg)


    elif message.content.startswith('Goodbye Shaun.'):
        msg = "Cancer is a disease in which some of the body’s cells grow uncontrollably and spread to other parts of the body. Cancer can start almost anywhere in the human body, which is made up of trillions of cells. Normally, human cells grow and multiply (through a process called cell division) to form new cells as the body needs them. When cells grow old or become damaged, they die, and new cells take their place. Sometimes this orderly process breaks down, and abnormal or damaged cells grow and multiply when they shouldn’t. These cells may form tumors, which are lumps of tissue. Tumors can be cancerous or not cancerous (benign). Cancerous tumors spread into, or invade, nearby tissues and can travel to distant places in the body to form new tumors (a process called metastasis). Cancerous tumors may also be called malignant tumors. Many cancers form solid tumors, but cancers of the blood, such as leukemias, generally do not. Benign tumors do not spread into, or invade, nearby tissues. When removed, benign tumors usually don’t grow back, whereas cancerous tumors sometimes do. Benign tumors can sometimes be quite large, however. Some can cause serious symptoms or be life threatening, such as benign tumors in the brain. {0.author.mention}.".format(message)
        await message.channel.send(msg)


    elif message.content.startswith('What can you define?'):
        msg = 'ASD, Autism Spectrum Disorder, Autism, ADHD, Appendicitis, Appendectomy, Appendicectomy, Aneurysm, Cancer, Cholecystitis, Dissociative Identity Disorder, DID, Hemorrhage, Osteosarcoma, Neurodivergent, Neurodivergence. I am always being updated. {0.author.mention}.'.format(message)
        await message.channel.send(msg)


    elif message.content == "!role Autism":
        member = message.author
        role = get(member.guild.roles, name='Autism')
        await member.add_roles(role)
        msg = "Role 'Autism' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role OCD":
        member = message.author
        role = get(member.guild.roles, name='OCD')
        await member.add_roles(role)
        msg = "Role 'OCD' added. {0.author.mention}".format(message)
        await message.channel.send(msg)

    elif message.content == "!role ADHD":
        member = message.author
        role = get(member.guild.roles, name='ADHD')
        await member.add_roles(role)
        msg = "Role 'ADHD' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role DID":
        member = message.author
        role = get(member.guild.roles, name='DID')
        await member.add_roles(role)
        msg = "Role 'DID' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Europe":
        member = message.author
        role = get(member.guild.roles, name='Europe')
        await member.add_roles(role)
        msg = "Role 'Europe' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role North America":
        member = message.author
        role = get(member.guild.roles, name='North America')
        await member.add_roles(role)
        msg = "Role 'North America' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role South America":
        member = message.author
        role = get(member.guild.roles, name='South America')
        await member.add_roles(role)
        msg = "Role 'South America' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Africa":
        member = message.author
        role = get(member.guild.roles, name='Africa')
        await member.add_roles(role)
        msg = "Role 'Africa' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Asia":
        member = message.author
        role = get(member.guild.roles, name='Asia')
        await member.add_roles(role)
        msg = "Role 'Asia' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Oceania":
        member = message.author
        role = get(member.guild.roles, name='Oceania')
        await member.add_roles(role)
        msg = "Role 'Oceania' added. {0.author.mention}".format(message)
        await message.channel.send(msg)



    elif message.content == "!role Minor":
        member = message.author
        role = get(member.guild.roles, name='Minor')
        await member.add_roles(role)
        msg = "Role 'Minor' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role 18+":
        member = message.author
        role = get(member.guild.roles, name='18+')
        await member.add_roles(role)
        msg = "Role '18+' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Anxiety Disorder":
        member = message.author
        role = get(member.guild.roles, name='Anxiety Disorder')
        await member.add_roles(role)
        msg = "Role 'Anxiety Disorder' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role PTSD":
        member = message.author
        role = get(member.guild.roles, name='PTSD')
        await member.add_roles(role)
        msg = "Role 'PTSD' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role P-DID":
        member = message.author
        role = get(member.guild.roles, name='P-DID')
        await member.add_roles(role)
        msg = "Role 'P-DID' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role OSDD":
        member = message.author
        role = get(member.guild.roles, name='OSDD')
        await member.add_roles(role)
        msg = "Role 'OSDD' added. {0.author.mention}".format(message)
        await message.channel.send(msg)



    elif message.content == "!role English":
        member = message.author
        role = get(member.guild.roles, name='English')
        await member.add_roles(role)
        msg = "Role 'English' added. {0.author.mention}".format(message)
        await message.channel.send(msg)



    elif message.content == "!role Arabic":
        member = message.author
        role = get(member.guild.roles, name='Arabic')
        await member.add_roles(role)
        msg = "Role 'Arabic' added. {0.author.mention}".format(message)
        await message.channel.send(msg)



    elif message.content == "!role Japanese":
        member = message.author
        role = get(member.guild.roles, name='Japanese')
        await member.add_roles(role)
        msg = "Role 'Japanese' added. {0.author.mention}".format(message)
        await message.channel.send(msg)



    elif message.content == "!role Swedish":
        member = message.author
        role = get(member.guild.roles, name='Swedish')
        await member.add_roles(role)
        msg = "Role 'Swedish' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Italian":
        member = message.author
        role = get(member.guild.roles, name='Italian')
        await member.add_roles(role)
        msg = "Role 'Italian' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Russian":
        member = message.author
        role = get(member.guild.roles, name='Russian')
        await member.add_roles(role)
        msg = "Role 'Russian' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Spanish":
        member = message.author
        role = get(member.guild.roles, name='Spanish')
        await member.add_roles(role)
        msg = "Role 'Spanish' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role German":
        member = message.author
        role = get(member.guild.roles, name='German')
        await member.add_roles(role)
        msg = "Role 'German' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Dutch":
        member = message.author
        role = get(member.guild.roles, name='Dutch')
        await member.add_roles(role)
        msg = "Role 'Dutch' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Chinese":
        member = message.author
        role = get(member.guild.roles, name='Chinese')
        await member.add_roles(role)
        msg = "Role 'Chinese' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Portugese":
        member = message.author
        role = get(member.guild.roles, name='Portugese')
        await member.add_roles(role)
        msg = "Role 'Portugese' added. {0.author.mention}".format(message)
        await message.channel.send(msg)

    elif message.content == "!role French":
        member = message.author
        role = get(member.guild.roles, name='French')
        await member.add_roles(role)
        msg = "Role 'French' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    elif message.content == "!role Polish":
        member = message.author
        role = get(member.guild.roles, name='Polish')
        await member.add_roles(role)
        msg = "Role 'Polish' added. {0.author.mention}".format(message)
        await message.channel.send(msg)



    elif message.content == "!role Danish":
        member = message.author
        role = get(member.guild.roles, name='Danish')
        await member.add_roles(role)
        msg = "Role 'Danish' added. {0.author.mention}".format(message)
        await message.channel.send(msg)



    elif message.content == "!role QOTD":
        member = message.author
        role = get(member.guild.roles, name='QOTD')
        await member.add_roles(role)
        msg = "Role 'QOTD' added. {0.author.mention}".format(message)
        await message.channel.send(msg)


    



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------')

client.run(TOKEN)

