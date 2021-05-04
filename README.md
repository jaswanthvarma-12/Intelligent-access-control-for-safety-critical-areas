# intelligent-access-control-for-safety-critical-areas

## ABSTRACT
In some industries, it is necessary for workers to wear safety helmet and shoes while working. So
to check whether the workers are taking safety precautions or not, we are proposing this system.
We can train our classifier to identify safety helmet and shoes with IBM cloud. There will be video
streaming near the entry of the industries where we can detect the face of a person. If any person
is present, we can take a picture at that moment and send it to IBM cloud to check whether the
person is wearing a helmet or not. If the person is wearing a helmet, we can give him access by
opening the door. Else we can restrict his entry by keeping the door closed. We can even warn the
person to take safety precautions using voice commands.
### CONTENTS
PG. NO
CHAPTER 1: INTRODUCTION 1 <br/>
1.1. PROBLEM STATEMENT 1 <br/>
1.2. OBJECTIVES 1 <br/>
CHAPTER 2: LITERATURE SURVEY 2 <br/>
CHAPTER 3: METHODOLOGY AND DISCUSSION 3 <br/>
3.1. OPEN CV AND HAAR CASCADE 3 <br/>
CHAPTER 4: PROPOSED SYSTEM 4 <br/>
CHAPTER 5: EXPERIMENTAL RESULTS 5 <br/>
5.1. IMAGES IN CLOUD DATABASE <br/>
5.2 FACE RECOGNITION 5 <br/>
REFERENCES 6 <br/>
APPENDIX 7 <br/>
LIST OF FIGURES & TABLES
FIG NO. FIGURE NAME PAGE NO. <br/>
4.1 Image storage in
Cloud database
4 <br/>
4.2 Face recognition
using OpenCV
4 <br/>
TABLE NO. TABLE NAME PAGE NO.
3.1 <br/>
Computer Vision in various fields
and its applications
4 <br/>

## CHAPTER I
INTRODUCTION
Internet of Things (IoT) is a network of physical objects or people called “things” that are
embedded with software, electronics, network, and sensors that allows these objects to collect
and exchange data. IoT makes everything virtually “smart” by improving aspects of our life with
the power of data collection, AI algorithm and networks.
This report is organized as follows: Section 1 gives a brief introduction, describes the problem
statement and states the objective of the tool. In Section 2, the literature survey is presented
followed by Section 3 which deals with the Methodology used in the project. In Section 4, the
result has been presented and the report is concluded in section 5. <br/>
1.1. PROBLEM STATEMENT
In the current world, there are a very few detection algorithms that help in detecting safety requirements
in industry. There is a need to build a recognition tool that can help in analyzing the security
required with ease, without the involvement of physical presence of any supervisor. This tool
provides such an interface between the system and the user, thus making it easier to understand the
processes and files of the system. <br/>
1.2. OBJECTIVES
 Identifying people who are having safety equipment. People need to have proper
safety equipment in some areas of work so as to avoid any fatal accidents.
 Verifying the safety equipment with the trained models of the cloud. By
verifying the safety equipment with the trained model of the cloud, the running
processes can be classified into safe and unsafe processes.

## CHAPTER II
LITERATURE SURVEY <br/>
The Internet of Things is a novel paradigm shift in IT arena. The phrase “Internet of Things” which is also
shortly well-known as IoT is coined from the two words i.e. the first word is “Internet” and the second
word is “Things”. The Internet is a global system of interconnected computer networks that use the
standard Internet protocol suite (TCP/IP) to serve billions of users worldwide. It is a network of networks
that consists of millions of private, public, academic, business, and government networks, of local to global
scope, that are linked by a broad array of electronic, wireless and optical networking technologies [3].
Today more than 100 countries are linked into exchanges of data, news and opinions through Internet.
According to Internet World Statistics, as of December 31, 2011 there was an estimated 2, 267, 233, 742
Internet users worldwide (Accessed data dated on 06/06/2013: from the Universal Resource Location
(http://www.webopedia.com/TERM/I/Internet.html).
This signifies 32.7% of the world’s total population is using Internet. Even Internet is going into space
through Cisco’s Internet Routing in Space (IRIS) program in the coming fourth years (Accessed on
10/05/2012: (http://www.cisco.com/web/strategy/government/space-routing.html). The best definition for
the Internet of Things would be: “An open and comprehensive network of intelligent objects that have the
capacity to auto-organize, share information, data and resources, reacting and acting in face of situations
and changes in the environment”
While coming to the Things that can be any object or person which can be distinguishable by the real
world. Everyday objects include not only electronic devices we encounter and use daily and
technologically advanced products such as equipment and gadgets, but “things” that we do not do normally
think of as electronic at all—such as food, clothing; and furniture; materials, parts and equipment,
merchandise and specialized items; landmarks, monuments and works of art and all the miscellany of
commerce, culture and sophistication [4]. That means here things can be both living things like person,
animals—cow, calf, dog, pigeons, rabbit etc., plants—mango tree, jasmine, banyan and so on and
nonliving things like chair, fridge, tube light, curtain, plate etc. any home appliances or industry apparatus.
So at this point, things are real objects in this physical or material world

## CHAPTER III
METHODOLOGY AND DISCUSSION <br/>
3.1. OpenCV and Haar Cascade <br/>
OpenCV is a cross platform library using which we can develop real-time computer vision
applications. It mainly focuses on image processing, video capture, and analysis including features
like face recognition and object detection.
Computer Vision can be defined as a discipline that explains how to reconstruct, interrupt, and
understand a 3D scene from its 2D images, in terms of the properties of the structure present in the
scene. It deals with modelling and replicating human vision using computer software and
hardware. <br/>
Haar Cascade is an Object Detection Algorithm used to identify faces in an image or a real-time
video. The algorithm uses edge or line detection features proposed by Viola and Jones in their
research paper. <br/>
Table 3.1: Computer Vision in various fields and its applications<br/>

1. Image processing Focuses on image manipulation. <br/>
2. Pattern recognition Explains various techniques to classify patterns. <br/>
3. Photogrammy Concerned with obtaining accurate measurements from images <br/>

## CHAPTER IV
EXPERIMENTAL RESULTS <br/>
4.1. OBJECT STORAGE IN CLOUD DATABASE <br/>
Figure 4.1: Images in the cloud database
4.2. FACE RECOGNITION <br/>
Figure 4.2: Face recognized by the webcam using OpenCV
## REFERENCES 
[5] Aggarwal, R. and Lal Das, M. (2012) RFID Security in the Context of “Internet of Things”. First
International Conference on Security of Internet of Things, Kerala, 17-19 August 2012, 51-56.
http://dx.doi.org/10.1145/2490428.2490435
[6] Biddlecombe, E. (2009) UN Predicts “Internet of Things”. Retrieved July 6.
[7] Butler, D. (2020) Computing: Everything, Everywhere. Nature, 440, 402-405.
http://dx.doi.org/10.1038/440402a
[8] Dodson, S. (2008) The Net Shapes up to Get Physical. Guardian.
[9] Gershenfeld, N., Krikorian, R. and Cohen, D. (2004) The Internet of Things. Scientific American,
291, 76-81. http://dx.doi.org/10.1038/scientificamerican1004-76
[10] Lombreglia, R. (2010) The Internet of Things, Boston Globe. Retrieved October.
[11] Reinhardt, A. (2004) A Machine-to-Machine Internet of Things.
