import pyautogui
import random
import time

# Bing search URL
bing_url = "https://www.bing.com/search?q=Daily+&qs=n&form=QBRE&sp=-1&ghc=1&lq=0&pq=daily+&sc=11-6&sk=&cvid=FDECBED5D84E4E14AC88473392CAFFB6&ghsh=0&ghacc=0&ghpl="

# List of search queries
search_queries = [
    "computer science news",
    "data science",
    "machine learning tutorials",
    "latest technology trends",
    "daily tech news",
    "Formula 1 standings",
    "current weather",
    "the verge tech news",
    "stock market updates",
    "best programming languages 2023",
    "AI applications in healthcare",
    "newest smartphones",
    "web development frameworks",
    "cybersecurity tips",
    "NASA space exploration",
    "innovative startups",
    "Python programming tutorials",
    "big data analytics",
    "self-driving cars",
    "augmented reality applications",
    "virtual reality gaming",
    "future of renewable energy",
    "blockchain technology",
    "latest gadgets reviews",
    "cloud computing solutions",
    "3D printing advancements",
    "upcoming video games",
    "internet of things (IoT) devices",
    "scientific breakthroughs",
    "computer hardware updates",
    "cryptocurrency market analysis",
    "innovations in robotics",
    "tech industry events 2023",
    "coding bootcamps reviews",
    "software development tools",
    "space exploration missions",
    "data privacy concerns",
    "programming language comparisons",
    "quantum computing developments",
    "top tech podcasts",
    "coding challenges",
    "tech conferences schedule",
    "latest cybersecurity threats",
    "mobile app development trends",
    "future of e-commerce",
    "computer vision applications",
    "deep learning frameworks",
    "ethical hacking tutorials",
    "wearable technology innovations",
    "best online learning platforms",
    "technology in education",
    "smart home devices reviews",
    "latest in bioinformatics",
    "edge computing applications",
    "open-source software projects",
    "latest in UX/UI design",
    "tech giants acquisitions",
    "emerging trends in IT",
    "health tech innovations",
    "robotic process automation (RPA)",
    "latest in quantum physics",
    "AR/VR in education",
    "smart city initiatives",
    "technology in agriculture",
    "innovations in renewable energy",
    "cybersecurity certifications",
    "coding for beginners",
    "future of 5G technology",
    "latest in space technology",
    "programming language popularity",
    "best coding practices",
    "tech and environment sustainability",
    "ethical AI developments",
    "developer communities online",
    "latest in electric vehicles",
    "tech for social impact",
    "advancements in nanotechnology",
    "future of internet security",
    "coding interview preparation",
    "latest trends in app design",
    "challenges in quantum computing",
    "tech solutions for climate change",
    "voice assistants technology",
    "technology and mental health",
    "smart farming innovations",
    "latest in biohacking",
    "tech innovations in sports",
    "coding for artificial intelligence",
    "future of internet of things",
    "latest in clean energy",
    "advancements in computer graphics",
    "cybersecurity for small businesses",
    "best practices in software testing",
    "coding for blockchain",
    "latest in autonomous vehicles",
    "space tourism developments",
    "programming for robotics",
    "innovations in biometrics",
    "latest trends in data visualization",
    "tech for disaster management",
    "coding for quantum computing",
    "future of cryptocurrency",
    "latest in virtual reality healthcare",
    "innovations in medical technology",
    "coding for edge computing",
    "tech solutions for wildlife conservation",
    "coding for AI ethics",
    "latest trends in user experience",
    "drones technology advancements",
    "latest in 6G technology",
    "coding for space exploration",
    "future of smart cities",
    "latest trends in cloud computing",
    "programming for biotechnology",
    "innovations in smart textiles",
    "coding for sustainable development",
    "latest in brain-computer interfaces",
    "genetic engineering breakthroughs",
    "coding for smart transportation",
    "future of augmented reality",
    "latest trends in quantum cryptography",
    "programming for sustainability",
    "innovations in regenerative medicine",
    "coding for personalized medicine",
    "latest in autonomous drones",
    "tech for inclusive design",
    "coding for green technology",
    "future of neurotechnology",
    "latest trends in swarm robotics",
    "programming for sustainable agriculture",
    "innovations in bioelectronic medicine",
    "coding for future of work",
    "latest in neuroprosthetics",
    "tech for ethical AI",
    "coding for space colonization",
    "future of human-computer interaction",
    "latest trends in ecological monitoring",
    "programming for social innovation",
    "innovations in quantum communication",
    "coding for sustainable energy",
    "latest in eco-friendly technology",
    "tech for digital twins",
    "coding for ethical hacking",
    "future of human augmentation",
    "latest trends in cognitive computing",
    "programming for environmental conservation",
    "innovations in sustainable architecture",
    "coding for smart grids",
    "latest in green energy technology",
    "tech for smart homes",
    "coding for eco-friendly transportation",
    "future of smart clothing",
    "latest trends in sustainable development",
    "programming for smart agriculture",
    "innovations in environmental monitoring",
    "coding for circular economy",
    "latest in renewable energy technology",
    "tech for sustainable transportation",
    "coding for sustainable cities",
    "future of sustainable fashion",
    "latest trends in green building technology",
    "programming for eco-friendly products",
    "innovations in sustainable living",
    "coding for sustainable tourism",
    "latest in eco-friendly packaging",
    "tech for sustainable water management",
    "coding for environmental protection",
    "future of sustainable mobility",
    "latest trends in sustainable business",
    "programming for eco-friendly innovations",
    "innovations in environmental conservation",
    "coding for sustainable fisheries",
    "latest in eco-friendly materials",
    "tech for sustainable agriculture",
    "coding for environmental education",
    "future of sustainable energy solutions",
    "latest trends in sustainable urban planning",
    "programming for eco-friendly manufacturing",
    "innovations in sustainable transportation",
    "coding for environmental sustainability",
    "latest in eco-friendly technologies",
    "tech for sustainable building design",
    "coding for sustainable energy sources",
    "future of sustainable infrastructure",
    "latest trends in eco-friendly design",
    "programming for environmental responsibility",
    "innovations in sustainable tourism",
    "coding for eco-friendly practices",
    "latest in sustainable energy innovations",
    "tech for sustainable waste management",
    "coding for eco-friendly solutions",
    "future of sustainable construction",
    "latest trends in green technology innovations",
    "programming for eco-friendly initiatives",
    "innovations in sustainable development goals",
    "coding for sustainable urban development",
    "latest in green energy innovations",
    "tech for sustainable resource management",
    "coding for eco-friendly alternatives",
    "future of sustainable technology",
    "latest trends in eco-friendly architecture",
    "programming for sustainable living practices",
    "innovations in sustainable manufacturing",
    "coding for eco-friendly policies",
    "latest in sustainable agriculture technology",
    "tech for sustainable waste disposal",
    "coding"]


# Number of searches to perform
num_searches = 12

# Function to perform a single search
def wait(num: int):
   time.sleep(num)
def perform_search(query):
    pyautogui.click(x= 315, y= 160)  
    pyautogui.hotkey("ctrl", "a")
    wait(0.5)
    pyautogui.typewrite("")

    
    pyautogui.typewrite(query, 0.1)
    pyautogui.press("enter")
    wait(5)  

wait(3)
pyautogui.hotkey("ctrl", "t")
pyautogui.typewrite(bing_url)
wait(1)
pyautogui.press("enter")
wait(1)

for _ in range(num_searches):
    # Choose a random search query
    query = random.choice(search_queries)
    # Perform the search
    perform_search(query)

for _ in range(num_searches):
    pyautogui.hotkey("ctrl", "w")
    wait(0.2)
